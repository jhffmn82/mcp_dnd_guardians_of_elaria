# genart.py
# Generate campaign artwork via the OpenAI images API with character
# reference images for consistency. Key is read from ~/.openai_key
# (never stored in the repo). Usage:
#   python templates/genart.py <out_path> <prompt_file> [ref1 ref2 ...]
# Refs are attached via the edits endpoint so the model matches the
# characters' established designs; no refs -> plain generation.
import base64
import os
import sys
import requests

KEY = open(os.path.expanduser("~/.openai_key")).read().strip()
MODEL = os.environ.get("GENART_MODEL", "gpt-image-2")
SIZE = os.environ.get("GENART_SIZE", "1024x1024")
QUALITY = os.environ.get("GENART_QUALITY", "high")


def generate(out_path, prompt, refs):
    headers = {"Authorization": f"Bearer {KEY}"}
    if refs:
        files = []
        for r in refs:
            mime = "image/webp" if r.lower().endswith(".webp") else "image/png"
            files.append(("image[]", (os.path.basename(r), open(r, "rb"), mime)))
        data = {"model": MODEL, "prompt": prompt, "size": SIZE,
                "quality": QUALITY, "input_fidelity": "high"}
        resp = requests.post("https://api.openai.com/v1/images/edits",
                             headers=headers, data=data, files=files, timeout=600)
    else:
        resp = requests.post("https://api.openai.com/v1/images/generations",
                             headers=headers,
                             json={"model": MODEL, "prompt": prompt,
                                   "size": SIZE, "quality": QUALITY},
                             timeout=600)
    j = resp.json()
    if "data" not in j:
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
