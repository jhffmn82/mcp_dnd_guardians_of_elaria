# -*- coding: utf-8 -*-
"""Scale specific plates in the Session 7 docx so each fits in the space left on
the preceding page instead of being pushed and stranding a gap.

Each target names a text fragment that FOLLOWS the plate; the script scales the
last real image extent before it (ignoring caption-frame extents, which have a
near-zero height)."""
import re, os, zipfile

base = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base, 's7_unpacked', 'word', 'document.xml')
xml = open(path, encoding='utf-8').read()

MIN_REAL = 200000        # EMU; anything shorter is a caption frame, not a plate

TARGETS = [
    ('The Verdant Plaza, a single jewel of living green', 0.78),
    ('The plaza erupts, Iron Drudges rise', 0.74),
    ('Overclocked Death-Spark', 0.82),      # Rogue Servitor bestiary portrait
]

def scale(xml, fragment, factor):
    i = xml.find(fragment)
    if i == -1:
        return xml, 'FRAGMENT NOT FOUND'
    last = None
    for m in re.finditer(r'<wp:extent cx="(\d+)" cy="(\d+)"/>', xml[:i]):
        if int(m.group(2)) >= MIN_REAL:
            last = m
    if not last:
        return xml, 'no real plate found before fragment'
    cx, cy = int(last.group(1)), int(last.group(2))
    ncx, ncy = int(cx * factor), int(cy * factor)
    head, tail = xml[:last.start()], xml[last.end():]
    xml = head + '<wp:extent cx="%d" cy="%d"/>' % (ncx, ncy) + tail
    # the graphic's own a:ext carries the same numbers inside the same drawing
    win = xml[last.start():last.start() + 4000]
    am = re.search(r'<a:ext cx="%d" cy="%d"/>' % (cx, cy), win)
    if am:
        s, e = last.start() + am.start(), last.start() + am.end()
        xml = xml[:s] + '<a:ext cx="%d" cy="%d"/>' % (ncx, ncy) + xml[e:]
    return xml, '%.2f x %.2f in  ->  %.2f x %.2f in' % (
        cx / 914400, cy / 914400, ncx / 914400, ncy / 914400)

for frag, factor in TARGETS:
    xml, msg = scale(xml, frag, factor)
    print('%-50s %s' % (frag[:48], msg))

open(path, 'w', encoding='utf-8').write(xml)

out = os.path.join(base, 's7_fixed.docx')
if os.path.exists(out):
    os.remove(out)
src = os.path.join(base, 's7_unpacked')
with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(os.path.join(src, '[Content_Types].xml'), '[Content_Types].xml')
    for root, dirs, files in os.walk(src):
        for f in files:
            full = os.path.join(root, f)
            arc = os.path.relpath(full, src).replace(os.sep, '/')
            if arc != '[Content_Types].xml':
                z.write(full, arc)
print('repacked')
