# -*- coding: utf-8 -*-
"""Usage: python templates/img_geom.py <pdf>
Image-geometry QA for the keepsake book (v2, post read-through).
US Letter 612x792pt, text band x=72..540, bottom content limit ~727pt.

Flags:
A) NARROW image regardless of alignment: any content image whose width is under
   ~92% of the text band and which is not a legitimate text-wrap float. A float
   is only legitimate if it hugs the left or right band edge AND has real text
   beside it (see C). Centered, left-shrunk, and right-shrunk plates all flag.
B) BOTTOM OVERFLOW or bottom-margin contact, floats and inline alike.
C) FLOAT WITHOUT TEXT BESIDE IT: an edge-hugging image with no text blocks
   overlapping its vertical span on the open side (the below-the-text and
   shredded-wrap failure modes surface here).
Instruments are triage, not signoff: eyeball every page before shipping.
"""
import fitz, sys, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
pdf = sys.argv[1] if len(sys.argv) > 1 else "10_Session_8_Underroot.pdf"
doc = fitz.open(pdf)
BAND_L, BAND_R, BOT = 72.0, 540.0, 727.0
band_w = BAND_R - BAND_L
narrow, overflow, orphan = [], [], []
for i, page in enumerate(doc):
    words = page.get_text("words")  # x0,y0,x1,y1,word,...
    for img in page.get_image_info(xrefs=True):
        r = fitz.Rect(img["bbox"])
        w, h = r.width, r.height
        if w < 40 or h < 40:
            continue
        lgap, rgap = r.x0 - BAND_L, BAND_R - r.x1
        if r.y1 > BOT + 2:
            overflow.append((i + 1, round(w/72, 2), round(h/72, 2), round(r.y1 - BOT, 1)))
        # side-by-side pair (imgrow / 2-up cards): another image shares the band
        band_mates = [o for o in page.get_image_info() if o["bbox"] != img["bbox"]
                      and fitz.Rect(o["bbox"]).width >= 40
                      and not (fitz.Rect(o["bbox"]).y1 < r.y0 or fitz.Rect(o["bbox"]).y0 > r.y1)]
        if band_mates:
            continue
        if w < band_w * 0.90:
            hugging = lgap < 12 or rgap < 12
            # text beside: words overlapping the image's vertical span on the open side
            beside = [wd for wd in words
                      if wd[3] > r.y0 + 6 and wd[1] < r.y1 - 6
                      and (wd[2] <= r.x0 - 4 if rgap < 12 else wd[0] >= r.x1 + 4)]
            if hugging and len(beside) >= 12:
                pass                      # legitimate float with real wrap text
            elif hugging:
                orphan.append((i + 1, round(w/72, 2), round(h/72, 2), len(beside)))
            else:
                narrow.append((i + 1, round(w/72, 2), round(h/72, 2),
                               round(lgap, 0), round(rgap, 0)))
print(f"== {pdf}: {doc.page_count} pages ==")
print(f"\nA) NARROW (any alignment, not a working float), {len(narrow)}:")
for p, w, h, lg, rg in narrow:
    print(f"   p{p:3} {w}x{h}in  gaps L{lg} R{rg}")
print(f"\nB) BOTTOM OVERFLOW/CONTACT, {len(overflow)}:")
for p, w, h, ov in overflow:
    print(f"   p{p:3} {w}x{h}in  past bottom by {ov}pt")
print(f"\nC) FLOAT WITH NO TEXT BESIDE IT, {len(orphan)}:")
for p, w, h, n in orphan:
    print(f"   p{p:3} {w}x{h}in  words-beside={n}")
