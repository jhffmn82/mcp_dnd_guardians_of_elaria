import subprocess
import json
import os
import signal as os_signal
import sys
from typing import List, Dict

def _run_with_tree_kill(cmd: list, timeout: int):
    """Run a command; on timeout, kill the entire process tree (signal-cli
    is a shell wrapper around a JVM child, and killing only the wrapper
    leaves the JVM holding the stdout pipe, deadlocking communicate())."""
    popen_kwargs = dict(stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if sys.platform != "win32":
        popen_kwargs["start_new_session"] = True
    proc = subprocess.Popen(cmd, **popen_kwargs)
    try:
        out, err = proc.communicate(timeout=timeout)
        return proc.returncode, out, err
    except subprocess.TimeoutExpired:
        if sys.platform != "win32":
            try:
                os.killpg(os.getpgid(proc.pid), os_signal.SIGKILL)
            except (ProcessLookupError, PermissionError):
                proc.kill()
        else:
            subprocess.run(["taskkill", "/F", "/T", "/PID", str(proc.pid)],
                           capture_output=True)
        try:
            out, err = proc.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            out, err = "", "process tree kill timed out"
        raise subprocess.TimeoutExpired(cmd, timeout)

SIGNAL_CLI_PATH = os.getenv("SIGNAL_CLI_PATH", "signal-cli")
SIGNAL_ACCOUNT = os.getenv("SIGNAL_ACCOUNT_NUMBER")  # Your Signal number that's sending messages
SIGNAL_CONFIG_DIR = os.getenv("SIGNAL_CONFIG_DIR")  # Optional custom data dir (used in cloud deploys)

def _base_cmd():
    cmd = [SIGNAL_CLI_PATH]
    if SIGNAL_CONFIG_DIR:
        cmd += ["--config", SIGNAL_CONFIG_DIR]
    return cmd

def send_signal_message(phone_number: str, message: str) -> bool:
    """
    Send a Signal message using signal-cli.

    Args:
        phone_number: Recipient's Signal number (e.g., "+1234567890")
        message: Message text to send

    Returns:
        True if successful, False otherwise
    """
    try:
        cmd = _base_cmd() + [
            "-u", SIGNAL_ACCOUNT,
            "send",
            "-m", message,
            phone_number
        ]

        returncode, out, err = _run_with_tree_kill(cmd, timeout=300)

        if returncode != 0:
            print(f"Signal CLI error: {err}")
            return False

        return True
    except subprocess.TimeoutExpired:
        print(f"Signal CLI timeout sending to {phone_number}")
        return False
    except Exception as e:
        print(f"Error sending Signal message: {e}")
        return False

def receive_signal_messages(phone_number: str = None) -> List[Dict]:
    """
    Poll for incoming Signal messages using signal-cli.

    Args:
        phone_number: (Optional) Filter messages from a specific number

    Returns:
        List of received messages with format: {"source": "+1234567890", "text": "message"}
    """
    try:
        # --output=json is a global flag and must precede the subcommand
        cmd = _base_cmd() + [
            "--output=json",
            "-u", SIGNAL_ACCOUNT,
            "receive",
            "--timeout", "5"
        ]

        returncode, out, err = _run_with_tree_kill(cmd, timeout=300)

        if returncode != 0:
            # No messages or error
            print(f"Signal CLI receive error: {err}")
            return []

        messages = []
        for line in out.strip().split('\n'):
            if not line:
                continue
            try:
                # Parse JSON output from signal-cli
                msg_data = json.loads(line)

                # Extract the actual message from the envelope
                if 'envelope' in msg_data:
                    envelope = msg_data['envelope']
                    source = envelope.get('source')

                    if 'dataMessage' in envelope:
                        text = envelope['dataMessage'].get('message', '')
                        if phone_number is None or source == phone_number:
                            messages.append({"source": source, "text": text})
            except json.JSONDecodeError:
                # Ignore lines that aren't valid JSON
                continue

        return messages
    except subprocess.TimeoutExpired:
        print("Signal CLI receive timeout")
        return []
    except Exception as e:
        print(f"Error receiving Signal messages: {e}")
        return []
