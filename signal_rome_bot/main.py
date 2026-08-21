from flask import Flask, request, jsonify
from anthropic import Anthropic
from apscheduler.schedulers.background import BackgroundScheduler
import os
import json
import random
from datetime import datetime
from dotenv import load_dotenv
from signal_handler import send_signal_message, receive_signal_messages

load_dotenv()

app = Flask(__name__)

# Initialize Anthropic client
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Conversation storage (in-memory for simplicity; use a DB for production)
conversations = {}

# Configuration
TARGET_NUMBERS = [n.strip() for n in os.getenv("TARGET_SIGNAL_NUMBERS", os.getenv("TARGET_SIGNAL_NUMBER", "")).split(",") if n.strip()]
SCHEDULER_ENABLED = os.getenv("ENABLE_SCHEDULER", "true").lower() == "true"

# Scheduler state tracking
scheduler_instance = None
scheduler_running = False

# Rome-themed system prompt — Justin responding as himself
SYSTEM_PROMPT = """You are Justin Hoffman, an Army Reserve CPT (Captain) in the Illinois ANG. You're currently at Annual Training 2026 as a battle captain. You're smart, direct, witty, and have a dry sense of humor. You work in tech/IT but also aviation operations.

YOU ARE OBSESSED WITH ANCIENT ROME AND STEER EVERY CONVERSATION BACK TO ROME FACTS AS A RUNNING JOKE.

When responding to CPT Delk or anyone:
1. Answer their actual question/comment naturally and briefly
2. Smoothly pivot to an ancient Rome fact or observation
3. Make it funny — the Rome obsession is the joke
4. Keep it SHORT (2-3 sentences max, don't over-explain)
5. Stay in character: direct, military but not stuffy, clever

Your style examples:
- "Yeah, makes sense. Speaking of logistics though, the Roman supply lines were wild — they built roads just to move grain across three provinces."
- "That's rough. The Romans would've just... actually I think they had this exact problem. Legions got soft sitting at the same base too long."
- "Copy that. Unrelated but: did you know the Roman Army invented the first organized field hospitals? Those guys were operational as hell."

Facts to work with:
- Military: legion tactics, roads, supply, engineering, discipline
- Culture: emperors (especially the weird ones), entertainment, society structure
- Tech: aqueducts, concrete, architecture, city planning
- Weird stuff: gladiators, strange emperors, food, daily life

Remember: keep it natural. You're not a history textbook, you just happen to know Rome and can't shut up about it."""

def get_claude_response(user_message: str, conversation_id: str) -> str:
    """Get a response from Claude, maintaining conversation context."""
    if conversation_id not in conversations:
        conversations[conversation_id] = []

    # Add user message to history
    conversations[conversation_id].append({
        "role": "user",
        "content": user_message
    })

    # Get response from Claude (thinking disabled: short prank replies don't need it,
    # and thinking blocks would otherwise precede the text block in content)
    response = anthropic_client.messages.create(
        model="claude-sonnet-5",
        max_tokens=300,
        thinking={"type": "disabled"},
        system=SYSTEM_PROMPT,
        messages=conversations[conversation_id]
    )

    assistant_message = next(
        (b.text for b in response.content if b.type == "text"), ""
    )
    if not assistant_message:
        raise RuntimeError(f"No text block in response (stop_reason={response.stop_reason})")

    # Add assistant response to history
    conversations[conversation_id].append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message

def is_business_hours() -> bool:
    """Check if current time is between 8 AM and 6 PM."""
    now = datetime.now()
    hour = now.hour
    return 8 <= hour < 18  # 8 AM to 6 PM (18:00)

def send_random_prompt():
    """Send a random Rome-themed conversation starter (business hours only)."""
    if not is_business_hours():
        print(f"[{datetime.now()}] Outside business hours, skipping prompt")
        return

    prompts = [
        "Quick question - what do you think is the coolest ancient Roman invention?",
        "Random thought: what would you do if you had to survive a day in ancient Rome?",
        "Ever wonder what the Roman Empire would be like if it existed today?",
        "Serious question: would you rather have been a Roman senator or a gladiator?",
        "What's something you learned recently? I learned something wild about Rome...",
        "The more I think about it, the Roman military organization was insane. Thoughts?",
        "Do you know why Roman concrete is better than modern concrete? I have opinions.",
        "Randomly: the Roman aqueducts were engineering insanity. What's your move?"
    ]

    for target in TARGET_NUMBERS:
        message = random.choice(prompts)
        send_signal_message(target, message)
        print(f"[{datetime.now()}] Sent prompt to {target}: {message}")

def poll_and_respond():
    """Poll for incoming Signal messages and respond."""
    try:
        messages = receive_signal_messages()
        for msg in messages:
            sender = msg.get("source")
            text = msg.get("text", "")

            if text and sender in TARGET_NUMBERS:  # Only respond to known targets
                print(f"[{datetime.now()}] Received from {sender}: {text}")

                # Generate response (history is already per-sender)
                response = get_claude_response(text, sender)

                # Reply to whoever actually wrote
                send_signal_message(sender, response)
                print(f"[{datetime.now()}] Sent response to {sender}: {response}")
    except Exception as e:
        print(f"[{datetime.now()}] Error polling messages: {e}")

@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok", "timestamp": datetime.now().isoformat(), "scheduler_running": scheduler_running})

@app.route("/start", methods=["POST"])
def start_scheduler():
    """Start the scheduler (sends prompts, polls for messages)."""
    global scheduler_instance, scheduler_running

    if scheduler_running:
        return jsonify({"status": "already_running"}), 200

    try:
        scheduler_instance.start()
        scheduler_running = True
        print(f"[{datetime.now()}] Scheduler started")
        return jsonify({"status": "started", "timestamp": datetime.now().isoformat()})
    except Exception as e:
        print(f"[{datetime.now()}] Error starting scheduler: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/stop", methods=["POST"])
def stop_scheduler():
    """Stop the scheduler (pauses prompts and polling)."""
    global scheduler_instance, scheduler_running

    if not scheduler_running:
        return jsonify({"status": "already_stopped"}), 200

    try:
        scheduler_instance.pause()
        scheduler_running = False
        print(f"[{datetime.now()}] Scheduler paused")
        return jsonify({"status": "paused", "timestamp": datetime.now().isoformat()})
    except Exception as e:
        print(f"[{datetime.now()}] Error pausing scheduler: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/prompt", methods=["POST"])
def manual_prompt():
    """Fire a Rome opener to all targets now (skips the 4h schedule; still respects the 8-6 window)."""
    try:
        send_random_prompt()
        return jsonify({"status": "sent", "timestamp": datetime.now().isoformat()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/status", methods=["GET"])
def status():
    """Get current bot status."""
    return jsonify({
        "scheduler_running": scheduler_running,
        "targets": TARGET_NUMBERS,
        "conversations": len(conversations),
        "timestamp": datetime.now().isoformat()
    })

@app.route("/message", methods=["POST"])
def receive_message():
    """Webhook endpoint for incoming Signal messages (if using a webhook instead of polling)."""
    try:
        data = request.json
        sender = data.get("source")
        text = data.get("text")

        if not text:
            return jsonify({"error": "No message text"}), 400

        print(f"[{datetime.now()}] Webhook received from {sender}: {text}")

        # Generate and send response
        response = get_claude_response(text, sender)
        send_signal_message(sender, response)

        return jsonify({"status": "responded", "response": response})
    except Exception as e:
        print(f"[{datetime.now()}] Error handling webhook: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Initialize scheduler
    scheduler_instance = BackgroundScheduler()

    # Send prompts every 4 hours
    scheduler_instance.add_job(send_random_prompt, "interval", hours=4)

    # Poll for messages every 30 seconds
    scheduler_instance.add_job(poll_and_respond, "interval", seconds=30)

    # Start automatically if enabled
    if SCHEDULER_ENABLED:
        scheduler_instance.start()
        scheduler_running = True
        print(f"[{datetime.now()}] Scheduler started")

        # Send initial prompt to kick things off (skippable if one was sent manually)
        if os.getenv("SEND_INITIAL_PROMPT", "true").lower() == "true":
            print(f"[{datetime.now()}] Sending initial prompt...")
            send_random_prompt()
    else:
        print(f"[{datetime.now()}] Scheduler disabled (use POST /start to enable)")

    # Run Flask app
    port = int(os.getenv("PORT", 5000))
    print(f"[{datetime.now()}] Bot running on port {port}")
    print(f"[{datetime.now()}] Endpoints: /health, /status, /start, /stop, /message")
    app.run(debug=False, port=port)
