#!/usr/bin/env python3
"""Build art_review/board.html: every Session 8 plate in reading order, each
tagged with a big letter so the DM can review by saying "redo C, E and J".

Unlike review_gallery.py (which sorts by filename and only shows PENDING_ ones)
this reads an explicit ordered manifest, so the letters match the order the
plates appear in the session and stay stable as plates are added or replaced.

Manifest format, one plate per line, pipe separated:
    letter | status | path relative to repo root | caption
status is one of: pending, approved, missing
"""
import base64
import html
import io
import os

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "art_review", "board_manifest.txt")
OUT = os.path.join(ROOT, "art_review", "board.html")


def data_uri(path, maxpx=1150, q=82):
    # Page weight: ~20 plates at 1150px/82 lands near 6 MB, which the artifact
    # viewer handles. Raising either number risks a board that will not load.
    im = Image.open(path).convert("RGB")
    im.thumbnail((maxpx, maxpx))
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=q)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def card(letter, status, path, caption):
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        status = "missing"
    if status == "missing":
        img = '<div class="miss">not generated yet</div>'
    else:
        img = '<img src="%s" alt="%s" loading="lazy"/>' % (
            data_uri(full), html.escape(caption))
    return """<figure class="card {st}">
  <div class="letter">{L}</div>
  {img}
  <figcaption><span class="badge {st}">{stlabel}</span>{cap}</figcaption>
</figure>""".format(L=html.escape(letter), img=img, st=status,
                    stlabel={"pending": "needs review", "approved": "approved",
                             "missing": "not made"}[status],
                    cap=html.escape(caption))


def build():
    rows = []
    with io.open(MANIFEST, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split("|")]
            if len(parts) == 4:
                rows.append(parts)

    cards = "\n".join(card(*r) for r in rows)
    counts = {}
    for r in rows:
        st = r[1] if os.path.exists(os.path.join(ROOT, r[2])) else "missing"
        counts[st] = counts.get(st, 0) + 1
    summary = " &bull; ".join("%d %s" % (v, k) for k, v in sorted(counts.items()))

    doc = """<title>Session 8 Art Board</title>
<style>
  :root {
    --bg:#f6f1e7; --card:#fffdf8; --ink:#2b2622; --muted:#7a6f60;
    --line:#e0d5c2; --accent:#8a6d3b;
    --pend:#b06a1f; --pendbg:#fdf0df; --appr:#3f7a48; --apprbg:#e9f4ea;
    --miss:#8a3b3b; --missbg:#f7e8e8;
  }
  @media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
    --bg:#15130f; --card:#211d18; --ink:#efe7da; --muted:#a8998a;
    --line:#3a332a; --accent:#d3b276;
    --pend:#e2a25c; --pendbg:#3a2a14; --appr:#8fd39c; --apprbg:#17301c;
    --miss:#e08a8a; --missbg:#3a1c1c;
  }}
  :root[data-theme="dark"] {
    --bg:#15130f; --card:#211d18; --ink:#efe7da; --muted:#a8998a;
    --line:#3a332a; --accent:#d3b276;
    --pend:#e2a25c; --pendbg:#3a2a14; --appr:#8fd39c; --apprbg:#17301c;
    --miss:#e08a8a; --missbg:#3a1c1c;
  }
  body { background:var(--bg); color:var(--ink); margin:0; padding:28px 20px 60px;
         font-family:"Iowan Old Style","Palatino Linotype",Georgia,serif; }
  header { max-width:1100px; margin:0 auto 26px; }
  h1 { font-size:1.7rem; margin:0 0 6px; letter-spacing:.01em; }
  .sub { color:var(--muted); font-size:.95rem; margin:0; }
  .grid { max-width:1100px; margin:0 auto; display:grid; gap:26px;
          grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); }
  .card { margin:0; background:var(--card); border:1px solid var(--line);
          border-radius:10px; overflow:hidden; position:relative; }
  .letter { position:absolute; top:10px; left:10px; z-index:2;
            width:40px; height:40px; border-radius:8px; background:var(--accent);
            color:#fff; font-size:1.35rem; font-weight:700; display:flex;
            align-items:center; justify-content:center;
            box-shadow:0 2px 8px rgba(0,0,0,.35); font-family:system-ui,sans-serif; }
  .card img { display:block; width:100%; height:auto; }
  .miss { padding:70px 12px; text-align:center; color:var(--muted);
          font-style:italic; background:repeating-linear-gradient(45deg,
          transparent,transparent 10px,var(--line) 10px,var(--line) 11px); }
  figcaption { padding:12px 14px 15px; font-size:.94rem; line-height:1.45; }
  .badge { display:inline-block; font-family:system-ui,sans-serif; font-size:.68rem;
           letter-spacing:.09em; text-transform:uppercase; padding:3px 8px;
           border-radius:99px; margin-right:8px; vertical-align:1px; }
  .badge.pending { color:var(--pend); background:var(--pendbg); }
  .badge.approved { color:var(--appr); background:var(--apprbg); }
  .badge.missing { color:var(--miss); background:var(--missbg); }
</style>
<header>
  <h1>Session 8: Part One art board</h1>
  <p class="sub">In reading order. Call plates by their letter, for example
  &ldquo;redo C, E and J&rdquo;. @@SUMMARY@@</p>
</header>
<div class="grid">
@@CARDS@@
</div>"""
    # token substitution, not %-formatting: the CSS above is full of percent
    # signs (width:100%) and would break a format string.
    doc = doc.replace("@@SUMMARY@@", summary).replace("@@CARDS@@", cards)

    io.open(OUT, "w", encoding="utf-8").write(doc)
    print("wrote %s | %s" % (OUT, summary))


if __name__ == "__main__":
    build()
