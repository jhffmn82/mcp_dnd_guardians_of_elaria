# genart.py
# Generate campaign artwork via the OpenAI images API with character
# reference images for consistency. Key is read from ~/.openai_key
# (never stored in the repo). Usage:
#   python templates/genart.py <out_path> <prompt_file> [ref1 ref2 ...]
# Refs are attached via the edits endpoint so the model matches the
# characters' established designs; no refs -> plain generation.
import base64
import os
import re
import sys
import requests

KEY = open(os.path.expanduser("~/.openai_key")).read().strip()
MODEL = os.environ.get("GENART_MODEL", "gpt-image-2")
SIZE = os.environ.get("GENART_SIZE", "1024x1024")
QUALITY = os.environ.get("GENART_QUALITY", "high")
# set GENART_BACKGROUND=transparent for alpha-channel output (e.g. shirt art)
BACKGROUND = os.environ.get("GENART_BACKGROUND", "")


class RateLimited(Exception):
    """The org's images-per-minute cap, not a real failure. Worth waiting out."""

    def __init__(self, message, retry_after):
        super().__init__(message)
        self.retry_after = retry_after


def generate(out_path, prompt, refs, attempts=3, rate_limit_attempts=8):
    """Retry transient network errors a few times, and rate limits many times.

    Rate limits get their own budget because they are not errors: the cap is
    5 input-images per minute, so a batch of prompts that each carry two or
    three reference images will trip it constantly. Waiting is the whole fix.
    """
    import time
    last = None
    rate_waits = 0
    i = 0
    while i < attempts:
        try:
            return _generate_once(out_path, prompt, refs)
        except RateLimited as e:
            rate_waits += 1
            if rate_waits > rate_limit_attempts:
                raise
            wait = e.retry_after or min(15 * rate_waits, 90)
            print(f"rate limited, waiting {wait}s (wait {rate_waits}/{rate_limit_attempts})...")
            time.sleep(wait)
            continue  # a rate limit does not consume a real attempt
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            last = e
            i += 1
            print(f"attempt {i} failed ({type(e).__name__}), retrying in {5*i}s...")
            time.sleep(5 * i)
    raise last


def _generate_once(out_path, prompt, refs):
    headers = {"Authorization": f"Bearer {KEY}"}
    if refs:
        files = []
        for r in refs:
            mime = "image/webp" if r.lower().endswith(".webp") else "image/png"
            files.append(("image[]", (os.path.basename(r), open(r, "rb"), mime)))
        data = {"model": MODEL, "prompt": prompt, "size": SIZE, "quality": QUALITY}
        if BACKGROUND:
            data["background"] = BACKGROUND
        if MODEL.startswith("gpt-image-1"):
            data["input_fidelity"] = "high"
        resp = requests.post("https://api.openai.com/v1/images/edits",
                             headers=headers, data=data, files=files, timeout=600)
    else:
        payload = {"model": MODEL, "prompt": prompt,
                   "size": SIZE, "quality": QUALITY}
        if BACKGROUND:
            payload["background"] = BACKGROUND
        resp = requests.post("https://api.openai.com/v1/images/generations",
                             headers=headers, json=payload, timeout=600)
    j = resp.json()
    if "data" not in j:
        err = j.get("error") or {}
        if err.get("code") == "rate_limit_exceeded":
            # the message carries "Please try again in 12s"; honour it when present
            m = re.search(r"try again in ([\d.]+)s", err.get("message", ""))
            raise RateLimited(err.get("message", "rate limited"),
                              float(m.group(1)) + 2 if m else None)
        raise SystemExit(f"API error: {j}")
    img = base64.b64decode(j["data"][0]["b64_json"])
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(img)
    print("saved", out_path, len(img), "bytes")


if __name__ == "__main__":
    out = sys.argv[1]
    prompt = open(sys.argv[2], encoding="utf-8").read()
    refs = sys.argv[3:]
    generate(out, prompt, refs)
