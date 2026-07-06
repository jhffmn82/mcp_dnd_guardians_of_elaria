# review_gallery.py
# Builds art_review/review.html: a self-contained approval board embedding
# every image in art_review/ as a data URI (base64 stays on disk, never in
# the model's context). PENDING_*.png are flagged for approval; others show
# as already-approved. Rebuild after each generation, then (re)publish the
# Artifact pointing at review.html.
import base64, glob, io, os, html
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RD = os.path.join(ROOT, "art_review")

def data_uri(path, maxpx=900, q=80):
    im = Image.open(path).convert("RGB")
    im.thumbnail((maxpx, maxpx))
    buf = io.BytesIO(); im.save(buf, format="JPEG", quality=q)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

def card(path):
    name = os.path.basename(path)
    pending = name.startswith("PENDING_")
    label = name[len("PENDING_"):] if pending else name
    label = os.path.splitext(label)[0].replace("_", " ")
    status = "Awaiting approval" if pending else "Approved"
    cls = "pending" if pending else "approved"
    return f'''<figure class="card {cls}">
      <img src="{data_uri(path)}" alt="{html.escape(label)}" loading="lazy"/>
      <figcaption>
        <span class="status {cls}">{status}</span>
        <span class="name">{html.escape(label)}</span>
      </figcaption>
    </figure>'''

def build():
    imgs = sorted(glob.glob(os.path.join(RD, "*.png")) + glob.glob(os.path.join(RD, "*.jpg")))
    pend = [p for p in imgs if os.path.basename(p).startswith("PENDING_")]
    done = [p for p in imgs if not os.path.basename(p).startswith("PENDING_")]
    cards = "\n".join(card(p) for p in pend + done)
    n_pend = len(pend)
    head = f'''{n_pend} image{'s' if n_pend != 1 else ''} awaiting your approval''' if n_pend else "All caught up. Nothing pending."
    doc = f'''<style>
  .wrap {{ max-width: 1000px; margin: 0 auto; padding: 2rem 1rem 3rem; font-family: Georgia, 'Iowan Old Style', serif; color: #2a2118; }}
  .wrap * {{ box-sizing: border-box; }}
  .masthead {{ text-align: center; border-bottom: 2px solid #b8860b; padding-bottom: 1rem; margin-bottom: 1.75rem; }}
  .kicker {{ font-size: .72rem; letter-spacing: .28em; text-transform: uppercase; color: #8a6d1f; margin: 0; }}
  .masthead h1 {{ font-size: 1.9rem; font-weight: 600; color: #7a4a12; margin: .25rem 0 .35rem; }}
  .tally {{ font-size: .95rem; color: #6b5d45; font-style: italic; margin: 0; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem; }}
  .card {{ margin: 0; background: #fbf6ea; border: 1px solid #e6dcc4; border-radius: 12px; overflow: hidden; }}
  .card.pending {{ border-color: #b8860b; box-shadow: 0 0 0 2px rgba(184,134,11,.18); }}
  .card img {{ display: block; width: 100%; height: auto; }}
  figcaption {{ display: flex; align-items: center; gap: .6rem; padding: .7rem .85rem; }}
  .status {{ font-size: .64rem; letter-spacing: .12em; text-transform: uppercase; padding: .2rem .5rem; border-radius: 999px; white-space: nowrap; }}
  .status.pending {{ background: #f3e2b8; color: #7a4a12; }}
  .status.approved {{ background: #e3ecdf; color: #3f5a37; }}
  .name {{ font-size: .95rem; color: #40372a; text-transform: capitalize; }}
  @media (prefers-color-scheme: dark) {{
    .wrap {{ color: #e8dfce; }}
    .masthead h1 {{ color: #e0b658; }} .kicker {{ color: #c99f4a; }} .tally {{ color: #b3a179; }}
    .card {{ background: #221c12; border-color: #4a3d22; }}
    .name {{ color: #d8ccb0; }}
  }}
</style>
<div class="wrap">
  <header class="masthead">
    <p class="kicker">The Guardians of Elaria</p>
    <h1>Art Review Board</h1>
    <p class="tally">{head}</p>
  </header>
  <div class="grid">
    {cards if cards else '<p>No images in art_review/ yet.</p>'}
  </div>
</div>'''
    os.makedirs(RD, exist_ok=True)
    out = os.path.join(RD, "review.html")
    open(out, "w", encoding="utf-8").write(doc)
    print("wrote", out, "|", len(pend), "pending,", len(done), "approved")

if __name__ == "__main__":
    build()
