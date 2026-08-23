# Signal Rome Bot

A Claude-powered bot that messages someone on Signal every ~4 hours with random Rome-themed conversation starters, and responds in character when they reply.

## How it works

1. **Scheduled prompts**: Every 4 hours, sends a random Rome-themed question or comment
2. **Bidirectional**: When the target replies, Claude generates a witty response that steers the conversation back to ancient Rome
3. **In-character**: Uses a system prompt to keep responses playful and Rome-focused
4. **Deployed**: Runs 24/7 on a cloud platform

## Architecture

```
main.py              - Flask web server + scheduler
signal_handler.py    - Wraps signal-cli for sending/receiving
.env                 - Configuration (API keys, phone numbers)
requirements.txt     - Python dependencies
```

## Quick start

1. **Install dependencies**: `pip install -r requirements.txt`
2. **Link Signal account**: `signal-cli -u +YOUR_NUMBER link`
3. **Configure .env**: Copy `.env.example`, add API key and phone numbers
4. **Test locally**: `python main.py`
5. **Deploy**: See DEPLOY.md for Railway/Fly.io/Docker instructions

## Customization

**Change the character**: Edit `SYSTEM_PROMPT` in `main.py`

**Adjust message frequency**: Change `hours=4` in the scheduler job

**Change Rome prompts**: Edit the `prompts` list in `send_random_prompt()`

**Response length**: Adjust `max_tokens` in the Claude API call

## Files

- **main.py** - Core app (Flask, scheduler, Claude API integration)
- **signal_handler.py** - Signal CLI wrapper
- **DEPLOY.md** - Cloud deployment guide
- **requirements.txt** - Dependencies
- **.env.example** - Configuration template
