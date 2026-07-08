# geom_audit.py -- render a docx and report layout offenders per page.
# Usage: python templates/geom_audit.py <docx> [<docx> ...]
# Reports, per page: image-bbox margin violations, blank pages, and
# trailing-whitespace % (target <33% except intentional section-end pages).
# Content band (points): TOP=54, BOT=727; page is US Letter 612x792.
import os, sys
import fitz  # PyMuPDF
sys.path.insert(0, os.path.dirname(__file__))
from render_check import docx_to_pdf

TOP, BOT = 54.0, 727.0
LEFT_LIM, RIGHT_LIM = 70.5, 541.5
BOT_LIM = 728.0


def audit_pdf(pdf):
    doc = fitz.open(pdf)
    rows = []
    for i, page in enumerate(doc):
        pno = i + 1
        text = page.get_text().strip()
        # image bboxes
        margins = []
        max_y = TOP
        for img in page.get_images(full=True):
            xref = img[0]
            for r in page.get_image_rects(xref):
                if r.y1 > BOT_LIM or r.x1 > RIGHT_LIM or r.x0 < LEFT_LIM:
                    margins.append((round(r.x0, 1), round(r.y0, 1),
                                    round(r.x1, 1), round(r.y1, 1)))
                max_y = max(max_y, r.y1)
        # text extent for whitespace
        blocks = page.get_text("blocks")
        for b in blocks:
            # skip the footer page-number line (sits at/below the content band)
            if b[1] >= BOT - 8:
                continue
            max_y = max(max_y, b[3])
        ws = (BOT - min(max_y, BOT)) / (BOT - TOP) * 100
        flag = []
        if len(text) < 15:
            flag.append("BLANK")
        if margins:
            flag.append("MARGIN" + str(margins))
        if ws > 33 and len(text) >= 15:
            flag.append(f"WS{int(ws)}%")
        if flag:
            rows.append((pno, "; ".join(flag)))
    doc.close()
    return rows


if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    for docx in sys.argv[1:]:
        base = os.path.splitext(os.path.basename(docx))[0]
        pdf = os.path.join(os.path.dirname(docx), base + ".pdf")
        docx_to_pdf(docx, pdf)
        rows = audit_pdf(pdf)
        n = fitz.open(pdf).page_count
        print(f"\n== {base} ({n} pages) ==")
        if not rows:
            print("  clean")
        for pno, f in rows:
            print(f"  p{pno}: {f}")
