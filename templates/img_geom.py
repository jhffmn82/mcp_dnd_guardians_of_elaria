# -*- coding: utf-8 -*-
"""Usage: python templates/img_geom.py <pdf>
Scan a rendered PDF for the DM's two image complaints:
A) centered images narrower than the text band (side whitespace both sides)
B) images extending past the bottom content margin (BOT ~ 727pt)
US Letter 612x792, text band x=72..540, bottom limit 727."""
import fitz, sys, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
pdf = sys.argv[1] if len(sys.argv) > 1 else "10_Session_8_Underroot.pdf"
doc = fitz.open(pdf)
BAND_L, BAND_R, BOT = 72.0, 540.0, 727.0
band_w = BAND_R - BAND_L
narrow, overflow = [], []
for i, page in enumerate(doc):
    for img in page.get_image_info(xrefs=True):
        r = fitz.Rect(img["bbox"])
        w, h = r.width, r.height
        if w < 40 or h < 40:      # decorations
            continue
        lgap, rgap = r.x0 - BAND_L, BAND_R - r.x1
        if r.y1 > BOT + 2:
            overflow.append((i+1, round(w/72,2), round(h/72,2), round(r.y1-BOT,1)))
        # centered = both gaps big and roughly equal; narrower than 92% of band
        if w < band_w*0.92 and lgap > 35 and rgap > 35 and abs(lgap-rgap) < 40:
            narrow.append((i+1, round(w/72,2), round(h/72,2), round(lgap,0), round(rgap,0)))
print(f"== {pdf}: {doc.page_count} pages ==")
print(f"\nA) NARROW CENTERED (side whitespace), {len(narrow)}:")
for p,w,h,lg,rg in narrow: print(f"   p{p:3} {w}x{h}in  gaps L{lg} R{rg}")
print(f"\nB) BOTTOM OVERFLOW, {len(overflow)}:")
for p,w,h,ov in overflow: print(f"   p{p:3} {w}x{h}in  past bottom by {ov}pt")
