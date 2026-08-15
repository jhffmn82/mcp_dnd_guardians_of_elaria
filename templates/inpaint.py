# inpaint.py
# Repair a REGION of an existing campaign image without regenerating the rest.
# Use when approved art has one localized flaw (a malformed hand, a stray object)
# and a full regeneration would lose the parts that are already right.
#
# Usage:
#   python templates/inpaint.py <src.png> <out.png> <prompt_file> x0 y0 x1 y1 [more rects...]
# Rect coords are FRACTIONS of width/height (0..1), so they read the same at any
# resolution. Everything inside a rect is repainted; everything else is preserved.
#
# Key is read from ~/.openai_key (never stored in the repo), same as genart.py.
import base64
import io
import os
import sys

import requests
from PIL import Image

KEY = open(os.path.expanduser("~/.openai_key")).read().strip()
MODEL = os.environ.get("GENART_MODEL", "gpt-image-2")
QUALITY = os.environ.get("GENART_QUALITY", "high")


def build_mask(size, rects):
    """Opaque = keep, transparent = repaint (the API's convention)."""
    w, h = size
    mask = Image.new("RGBA", (w, h), (255, 255, 255, 255))
    px = mask.load()
    for (x0, y0, x1, y1) in rects:
        for x in range(int(x0 * w), int(x1 * w)):
            for y in range(int(y0 * h), int(y1 * h)):
                px[x, y] = (0, 0, 0, 0)
    return mask


def inpaint(src_path, out_path, prompt, rects, attempts=3):
    import time
    src = Image.open(src_path).convert("RGBA")
    mask = build_mask(src.size, rects)

    src_buf, mask_buf = io.BytesIO(), io.BytesIO()
    src.save(src_buf, format="PNG")
    mask.save(mask_buf, format="PNG")

    headers = {"Authorization": f"Bearer {KEY}"}
    size = "%dx%d" % src.size if src.size[0] != src.size[1] else "1024x1024"
    last = None
    for i in range(attempts):
        try:
            files = [
                ("image", ("src.png", src_buf.getvalue(), "image/png")),
                ("mask", ("mask.png", mask_buf.getvalue(), "image/png")),
            ]
            data = {"model": MODEL, "prompt": prompt, "size": size, "quality": QUALITY}
            resp = requests.post("https://api.openai.com/v1/images/edits",
                                 headers=headers, data=data, files=files, timeout=600)
            j = resp.json()
            if "data" not in j:
                raise SystemExit(f"API error: {j}")
            img = base64.b64decode(j["data"][0]["b64_json"])
            out = Image.open(io.BytesIO(img)).convert("RGB")
            if out.size != src.size:
                out = out.resize(src.size, Image.LANCZOS)
            os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
            out.save(out_path)
            print("saved", out_path, out.size)
            return
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            last = e
            print(f"attempt {i+1} failed ({type(e).__name__}), retrying...")
            time.sleep(5 * (i + 1))
    raise last


if __name__ == "__main__":
    src, out, prompt_file = sys.argv[1], sys.argv[2], sys.argv[3]
    nums = [float(v) for v in sys.argv[4:]]
    rects = [tuple(nums[i:i + 4]) for i in range(0, len(nums), 4)]
    inpaint(src, out, open(prompt_file, encoding="utf-8").read(), rects)
