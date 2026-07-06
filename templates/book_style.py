# book_style.py
# Shared publication framework for The Guardians of Elaria chronicle.
# Encodes the Session 8 house style: US Letter, parchment-gold read-aloud
# boxes, lavender DM boxes, goldenrod/sienna headings, star dividers,
# gray italic captions, and a centered star page footer.
# Build scripts import build_doc() and feed it a list of content blocks.

import io
import os
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Twips
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# House palette (from Session_8_Gearhaven_v2)
INK = "222222"          # body text
GOLD_FILL = "FBF6EA"    # read-aloud box fill
GOLD_EDGE = "B8860B"    # read-aloud left rule + H1 color
PURPLE_FILL = "F4F0FA"  # DM box fill
PURPLE_EDGE = "5B2A86"  # DM box left rule (Ursa purple)
STAT_FILL = "FCF6F6"    # statblock fill
STAT_EDGE = "8B2020"    # statblock left rule (deep crimson)
H2_COLOR = "A0522D"     # sienna
H3_COLOR = "1F4D78"     # deep blue
CAPTION_GRAY = "888888"
ACCENTS = {"lilly": "1F6FB8", "stabby": "A32B2B", "ursa": "5B2A86",
           "ghostbloom": "1F7A78", "gold": GOLD_EDGE}

BODY_FONT = "Georgia"
BODY_SIZE = Pt(10.5)

def _set_font(run, size=None, bold=None, italic=None, color=None, font=BODY_FONT):
    run.font.name = font
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn('w:rFonts'))
    if rfonts is None:
        rfonts = OxmlElement('w:rFonts'); rpr.append(rfonts)
    for a in ('w:ascii', 'w:hAnsi', 'w:cs'):
        rfonts.set(qn(a), font)
    if size: run.font.size = size
    if bold is not None: run.font.bold = bold
    if italic is not None: run.font.italic = italic
    run.font.color.rgb = RGBColor.from_string(color or INK)

def _shade(paragraph, fill, edge):
    """Left rule + shading, matching the S8 box construction."""
    ppr = paragraph._p.get_or_add_pPr()
    pbdr = OxmlElement('w:pBdr')
    left = OxmlElement('w:left')
    left.set(qn('w:val'), 'single'); left.set(qn('w:sz'), '18')
    left.set(qn('w:space'), '12'); left.set(qn('w:color'), edge)
    pbdr.append(left); ppr.append(pbdr)
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill)
    ppr.append(shd)
    paragraph.paragraph_format.left_indent = Twips(340)
    paragraph.paragraph_format.right_indent = Twips(340)
    paragraph.paragraph_format.space_before = Twips(30)
    paragraph.paragraph_format.space_after = Twips(70)

def _rich(par, text, base_color=INK, base_size=BODY_SIZE, base_bold=False, base_italic=False):
    """Minimal inline markup: **bold**, *italic*, and {color:name}...{/} accents."""
    import re
    pos = 0
    tokens = re.split(r'(\*\*.*?\*\*|\*.*?\*|\{color:\w+\}.*?\{/\})', text)
    for tok in tokens:
        if not tok: continue
        if tok.startswith('**') and tok.endswith('**'):
            r = par.add_run(tok[2:-2]); _set_font(r, base_size, True, base_italic, base_color)
        elif tok.startswith('{color:'):
            import re as _re
            m = _re.match(r'\{color:(\w+)\}(.*)\{/\}', tok, _re.S)
            r = par.add_run(m.group(2)); _set_font(r, base_size, True, base_italic, ACCENTS.get(m.group(1), base_color))
        elif tok.startswith('*') and tok.endswith('*') and len(tok) > 2:
            r = par.add_run(tok[1:-1]); _set_font(r, base_size, base_bold, True, base_color)
        else:
            r = par.add_run(tok); _set_font(r, base_size, base_bold, base_italic, base_color)

def _footer_stars(section):
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p.add_run("✦ "); _set_font(r1, Pt(9), color=CAPTION_GRAY)
    fld1 = OxmlElement('w:fldChar'); fld1.set(qn('w:fldCharType'), 'begin')
    instr = OxmlElement('w:instrText'); instr.set(qn('xml:space'), 'preserve'); instr.text = ' PAGE '
    fld2 = OxmlElement('w:fldChar'); fld2.set(qn('w:fldCharType'), 'end')
    rf = p.add_run(); _set_font(rf, Pt(9), color=CAPTION_GRAY)
    rf._element.append(fld1)
    rm = p.add_run(); _set_font(rm, Pt(9), color=CAPTION_GRAY)
    rm._element.append(instr)
    re_ = p.add_run(); _set_font(re_, Pt(9), color=CAPTION_GRAY)
    re_._element.append(fld2)
    r2 = p.add_run(" ✦"); _set_font(r2, Pt(9), color=CAPTION_GRAY)

def _image_png_bytes(path, max_w_px=1600):
    """Return PNG bytes for any raster (webp converted, large images downscaled)."""
    from PIL import Image
    im = Image.open(path)
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGB")
    if im.width > max_w_px:
        im = im.resize((max_w_px, int(im.height * max_w_px / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="PNG", optimize=True)
    return buf.getvalue(), im.width, im.height

def build_doc(blocks, out_path):
    doc = Document()
    # US Letter, S8 margins
    sec = doc.sections[0]
    sec.page_width = Twips(12240); sec.page_height = Twips(15840)
    sec.left_margin = Twips(1440); sec.right_margin = Twips(1440)
    sec.top_margin = Twips(1080); sec.bottom_margin = Twips(1080)
    _footer_stars(sec)

    st_normal = doc.styles['Normal']
    st_normal.font.name = BODY_FONT
    st_normal.font.size = BODY_SIZE
    st_normal.font.color.rgb = RGBColor.from_string(INK)

    for blk in blocks:
        kind = blk[0]

        if kind == "titlepage":
            # (titlepage, kicker, title, subtitle, note)
            _, kicker, title, subtitle, note = blk
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(60)
            r = p.add_run("✦  ✦  ✦"); _set_font(r, Pt(16), color=GOLD_EDGE)
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(18)
            r = p.add_run(kicker); _set_font(r, Pt(15), True, color=INK)
            r.font.name = BODY_FONT
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(title); _set_font(r, Pt(30), True, color=GOLD_EDGE)
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(subtitle); _set_font(r, Pt(17), True, color=H2_COLOR)
            if note:
                p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(16)
                r = p.add_run(note); _set_font(r, Pt(9.5), italic=True, color=CAPTION_GRAY)

        elif kind == "h1":
            p = doc.add_paragraph()
            if len(blk) > 2 and blk[2].get("pagebreak"):
                p.paragraph_format.page_break_before = True
            p.paragraph_format.space_before = Pt(18); p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(blk[1]); _set_font(r, Pt(16), True, color=GOLD_EDGE)

        elif kind == "h2":
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(14); p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(blk[1]); _set_font(r, Pt(13), True, color=H2_COLOR)

        elif kind == "gold":
            p = doc.add_paragraph(); _shade(p, GOLD_FILL, GOLD_EDGE)
            _rich(p, blk[1])

        elif kind == "dm":
            p = doc.add_paragraph(); _shade(p, PURPLE_FILL, PURPLE_EDGE)
            _rich(p, "▶ " + blk[1], base_size=Pt(9.5))

        elif kind == "stat":
            # (stat, title, [lines])
            p = doc.add_paragraph(); _shade(p, STAT_FILL, STAT_EDGE)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(blk[1]); _set_font(r, Pt(11), True, color=STAT_EDGE)
            for line in blk[2]:
                p = doc.add_paragraph(); _shade(p, STAT_FILL, STAT_EDGE)
                _rich(p, line, base_size=Pt(9))

        elif kind == "body":
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(6)
            _rich(p, blk[1])

        elif kind == "bridge":
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(10)
            _rich(p, blk[1], base_italic=True)

        elif kind == "hero":
            # (hero, who, line) suggested PC voice, accent colored
            _, who, line = blk
            p = doc.add_paragraph(); _shade(p, GOLD_FILL, GOLD_EDGE)
            r = p.add_run(who + ": "); _set_font(r, BODY_SIZE, True, color=ACCENTS.get(who.split(' ')[0].lower(), INK))
            _rich(p, "“" + line + "”", base_italic=True)

        elif kind == "divider":
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(10)
            r = p.add_run("✦ ✦ ✦"); _set_font(r, Pt(12), color=GOLD_EDGE)

        elif kind == "img":
            # (img, path, caption, width_inches)
            _, path, caption, w = blk
            data, pw, ph = _image_png_bytes(path)
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.keep_with_next = bool(caption)
            p.paragraph_format.space_before = Pt(8)
            run = p.add_run()
            run.add_picture(io.BytesIO(data), width=Inches(w))
            if caption:
                cp = doc.add_paragraph(); cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                cp.paragraph_format.space_after = Pt(9)
                r = cp.add_run(caption); _set_font(r, Pt(9), italic=True, color=CAPTION_GRAY)

        elif kind == "pagebreak":
            p = doc.add_paragraph()
            p.add_run().add_break(WD_BREAK.PAGE)

        else:
            raise ValueError(f"unknown block kind {kind}")

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    doc.save(out_path)
    return out_path
