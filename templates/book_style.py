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

def _image_png_bytes(path, max_w_px=1200):
    """Return compressed JPEG bytes for any raster (webp converted, large images
    downscaled). JPEG keeps the illustrated docx/PDF a sane size; the art is
    opaque painterly work, so no alpha is lost."""
    from PIL import Image
    im = Image.open(path).convert("RGB")
    if im.width > max_w_px:
        im = im.resize((max_w_px, int(im.height * max_w_px / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=82, optimize=True)
    return buf.getvalue(), im.width, im.height

def _sb_line(doc, label, text, size=Pt(9)):
    p = doc.add_paragraph(); _shade(p, STAT_FILL, STAT_EDGE)
    p.paragraph_format.space_after = Pt(0); p.paragraph_format.space_before = Pt(0)
    r = p.add_run(label + " "); _set_font(r, size, True, color=STAT_EDGE)
    _rich(p, text, base_size=size)

def _sb_rule(doc):
    p = doc.add_paragraph(); _shade(p, STAT_FILL, STAT_EDGE)
    p.paragraph_format.space_after = Pt(1); p.paragraph_format.space_before = Pt(1)
    ppr = p._p.get_or_add_pPr(); pbdr = ppr.find(qn('w:pBdr'))
    bot = OxmlElement('w:bottom')
    bot.set(qn('w:val'), 'single'); bot.set(qn('w:sz'), '4'); bot.set(qn('w:space'), '1'); bot.set(qn('w:color'), STAT_EDGE)
    pbdr.append(bot)

def _mod(score):
    m = (int(score) - 10) // 2
    return f"+{m}" if m >= 0 else str(m)

def _float_right(paragraph, data, w_in):
    """Anchor a picture floated to the right with square text-wrap, so the
    statblock body wraps around it instead of stranding whitespace."""
    from docx.oxml import parse_xml
    run = paragraph.add_run()
    pic = run.add_picture(io.BytesIO(data), width=Inches(w_in))
    cx, cy = pic._inline.extent.cx, pic._inline.extent.cy
    drawing = run._r.find(qn('w:drawing'))
    inline = drawing.find(qn('wp:inline'))
    graphic = inline.find(qn('a:graphic'))
    docpr = inline.find(qn('wp:docPr'))
    anchor = parse_xml(
        '<wp:anchor xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
        'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
        'behindDoc="0" distT="91440" distB="91440" distL="201600" distR="0" simplePos="0" locked="0" '
        'layoutInCell="1" allowOverlap="1" relativeHeight="2">'
        '<wp:simplePos x="0" y="0"/>'
        '<wp:positionH relativeFrom="column"><wp:align>right</wp:align></wp:positionH>'
        '<wp:positionV relativeFrom="paragraph"><wp:posOffset>0</wp:posOffset></wp:positionV>'
        f'<wp:extent cx="{cx}" cy="{cy}"/>'
        '<wp:effectExtent l="0" t="0" r="0" b="0"/>'
        '<wp:wrapSquare wrapText="bothSides"/>'
        f'<wp:docPr id="{docpr.get("id")}" name="{docpr.get("name")}"/>'
        '<wp:cNvGraphicFramePr/>'
        '</wp:anchor>')
    anchor.append(graphic)
    drawing.remove(inline)
    drawing.append(anchor)


def _render_statblock(doc, sb):
    """A 5e-style statblock in the crimson house box, with the creature
    portrait floated to the right and the text wrapping around it. sb keys:
    name, type, ac, hp, speed, abilities {STR..CHA}, optional cr, saves,
    skills, resistances, vulnerabilities, immunities, condition_immunities,
    senses, languages, traits/actions/reactions/legendary [(name,text)], img, img_w."""
    # name header, and float the portrait from this first paragraph so the
    # whole block wraps around it
    p = doc.add_paragraph(); _shade(p, STAT_FILL, STAT_EDGE)
    p.paragraph_format.keep_with_next = True; p.paragraph_format.space_after = Pt(0)
    if sb.get("img"):
        try:
            data, pw, ph = _image_png_bytes(sb["img"])
            w = sb.get("img_w", 2.35)
            if w * (ph / pw) > 2.6:
                w = 2.6 / (ph / pw)
            _float_right(p, data, w)
        except Exception:
            pass
    r = p.add_run(sb["name"]); _set_font(r, Pt(12.5), True, color=STAT_EDGE)
    # type line
    p = doc.add_paragraph(); _shade(p, STAT_FILL, STAT_EDGE)
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(sb["type"]); _set_font(r, Pt(8.5), italic=True, color=INK)
    _sb_rule(doc)
    if sb.get("ac"): _sb_line(doc, "Armor Class", sb["ac"])
    if sb.get("hp"): _sb_line(doc, "Hit Points", sb["hp"])
    if sb.get("speed"): _sb_line(doc, "Speed", sb["speed"])
    _sb_rule(doc)
    # ability scores as a single wrapping line (plays nicely beside the float)
    ab = sb.get("abilities")
    if ab:
        p = doc.add_paragraph(); _shade(p, STAT_FILL, STAT_EDGE)
        p.paragraph_format.space_after = Pt(1)
        for i, name in enumerate(["STR", "DEX", "CON", "INT", "WIS", "CHA"]):
            sc = ab.get(name, 10)
            rr = p.add_run(("   " if i else "") + name + " "); _set_font(rr, Pt(9), True, color=STAT_EDGE)
            rr = p.add_run(f"{sc} ({_mod(sc)})"); _set_font(rr, Pt(9), color=INK)
        _sb_rule(doc)
    for key, label in [("saves", "Saving Throws"), ("skills", "Skills"),
                       ("resistances", "Damage Resistances"), ("vulnerabilities", "Damage Vulnerabilities"),
                       ("immunities", "Damage Immunities"), ("condition_immunities", "Condition Immunities"),
                       ("senses", "Senses"), ("languages", "Languages"), ("cr", "Challenge")]:
        if sb.get(key):
            _sb_line(doc, label, sb[key])
    for section, items in [("Traits", sb.get("traits")), ("Actions", sb.get("actions")),
                           ("Reactions", sb.get("reactions")), ("Legendary Actions", sb.get("legendary"))]:
        if not items:
            continue
        if section != "Traits":
            _sb_rule(doc)
            p = doc.add_paragraph(); _shade(p, STAT_FILL, STAT_EDGE)
            p.paragraph_format.space_after = Pt(1); p.paragraph_format.keep_with_next = True
            r = p.add_run(section); _set_font(r, Pt(10), True, color=STAT_EDGE)
        for nm, txt in items:
            p = doc.add_paragraph(); _shade(p, STAT_FILL, STAT_EDGE)
            p.paragraph_format.space_after = Pt(1)
            if nm:
                r = p.add_run(nm + ". "); _set_font(r, Pt(9), True, italic=True, color=INK)
            _rich(p, txt, base_size=Pt(9))
    # a trailing spacer so the next block clears the floated image if it overhangs
    doc.add_paragraph().paragraph_format.space_after = Pt(0)


def _page_parchment(doc, hexcolor="F9F2E2"):
    """Book-wide parchment page color (exports to PDF via Word)."""
    bg = OxmlElement('w:background')
    bg.set(qn('w:color'), hexcolor)
    doc.element.insert(0, bg)
    settings = doc.settings.element
    if settings.find(qn('w:displayBackgroundShape')) is None:
        el = OxmlElement('w:displayBackgroundShape')
        settings.append(el)


def build_doc(blocks, out_path):
    doc = Document()
    _page_parchment(doc)
    # US Letter, S8 margins
    sec = doc.sections[0]
    sec.page_width = Twips(12240); sec.page_height = Twips(15840)
    sec.left_margin = Twips(1440); sec.right_margin = Twips(1440)
    sec.top_margin = Twips(1080); sec.bottom_margin = Twips(1300)
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
            p.paragraph_format.space_before = Pt(24)
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
            # Content flows continuously; only hard-break before the Appendix
            # (or when a block explicitly asks with hardbreak). Parts are set
            # off by generous space and a keep-with-next rule, not a page break.
            hard = blk[1].strip().lower().startswith("appendix")
            if len(blk) > 2 and blk[2].get("hardbreak"):
                hard = True
            if hard:
                p.paragraph_format.page_break_before = True
            p.paragraph_format.space_before = Pt(20); p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(blk[1]); _set_font(r, Pt(16), True, color=GOLD_EDGE)
            # Chapter-header rule: a thin goldenrod line under every part title,
            # the touch that reads as a 5e-style sourcebook heading.
            _ppr = p._p.get_or_add_pPr()
            _pbdr = OxmlElement('w:pBdr')
            _bot = OxmlElement('w:bottom')
            _bot.set(qn('w:val'), 'single'); _bot.set(qn('w:sz'), '6')
            _bot.set(qn('w:space'), '4'); _bot.set(qn('w:color'), GOLD_EDGE)
            _pbdr.append(_bot); _ppr.append(_pbdr)

        elif kind == "h2":
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(11); p.paragraph_format.space_after = Pt(3)
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

        elif kind == "statblock":
            _render_statblock(doc, blk[1])

        elif kind == "body":
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(4)
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
            # Cap rendered HEIGHT so tall/portrait art cannot eat a whole page
            # and strand whitespace. Landscape art keeps its requested width.
            aspect = ph / pw
            max_h = 4.2
            if w * aspect > max_h:
                w = max_h / aspect
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.keep_with_next = bool(caption)
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run()
            run.add_picture(io.BytesIO(data), width=Inches(w))
            if caption:
                cp = doc.add_paragraph(); cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                cp.paragraph_format.space_after = Pt(7)
                r = cp.add_run(caption); _set_font(r, Pt(9), italic=True, color=CAPTION_GRAY)

        elif kind == "imgrow":
            # (imgrow, [(path, label), (path, label)], width_each) side-by-side
            _, pairs, w = blk
            tbl = doc.add_table(rows=2, cols=len(pairs))
            tbl.autofit = False
            tbl.alignment = 1
            for ci, (path, label) in enumerate(pairs):
                data, pw, ph = _image_png_bytes(path)
                ww = w
                if ww * (ph / pw) > 3.6:
                    ww = 3.6 / (ph / pw)
                c0 = tbl.cell(0, ci); c1 = tbl.cell(1, ci)
                c0.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
                c0.paragraphs[0].add_run().add_picture(io.BytesIO(data), width=Inches(ww))
                c1.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = c1.paragraphs[0].add_run(label)
                _set_font(r, Pt(9), italic=True, color=CAPTION_GRAY)
            doc.add_paragraph().paragraph_format.space_after = Pt(4)

        elif kind == "melody":
            # (melody, text) a sung verse or carol, set like sheet-music epigraph
            for i, line in enumerate(blk[1].split("|")):
                p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(10 if i == 0 else 0)
                p.paragraph_format.space_after = Pt(2)
                txt = line.strip()
                if i == 0:
                    txt = "♪  " + txt
                if i == len(blk[1].split("|")) - 1:
                    txt = txt + "  ♪"
                r = p.add_run(txt.replace("\u266a", "♪"))
                _set_font(r, Pt(12), bold=False, italic=True, color=GOLD_EDGE)
            sp = doc.add_paragraph(); sp.paragraph_format.space_after = Pt(6)

        elif kind == "imgfloat":
            # (imgfloat, path, width_inches[, "left"|"right"]) - image floated
            # into the following text with square wrap; no caption. The text
            # that comes AFTER this block flows around the image.
            _, path, w = blk[0], blk[1], blk[2]
            side = blk[3] if len(blk) > 3 else "right"
            data, pw, ph = _image_png_bytes(path)
            if w * (ph / pw) > 3.4:
                w = 3.4 / (ph / pw)
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(0); p.paragraph_format.space_before = Pt(0)
            _float_right(p, data, w)
            if side == "left":
                # flip the anchor alignment to left
                anch = p._p.findall('.//' + qn('wp:anchor'))
                if anch:
                    al = anch[0].find(qn('wp:positionH') + '/' + qn('wp:align'))
                    if al is None:
                        ph_el = anch[0].find(qn('wp:positionH'))
                        al = ph_el.find(qn('wp:align'))
                    if al is not None:
                        al.text = 'left'

        elif kind == "pagebreak":
            p = doc.add_paragraph()
            p.add_run().add_break(WD_BREAK.PAGE)

        else:
            raise ValueError(f"unknown block kind {kind}")

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    doc.save(out_path)
    return out_path
