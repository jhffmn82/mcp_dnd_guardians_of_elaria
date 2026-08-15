# -*- coding: utf-8 -*-
"""Map every embedded image in the Session 7 docx to the repo asset it came from,
by perceptual similarity (Word recompresses, so hashes do not match).

Prints any embedded image whose best match is NOT in assets/session_07, and any
asset that appears in the doc more than once, which is how a bad swap shows up.
"""
import os, glob, zipfile, shutil, sys
import numpy as np
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
DOCX = r'C:\Users\jhffm\dnd-campaign\sessions\session_07_gearhaven.docx'
ASSETS = r'C:\Users\jhffm\dnd-campaign\assets'
WORK = os.path.join(BASE, 'mapchk')


def sig(path_or_img):
    im = Image.open(path_or_img) if isinstance(path_or_img, str) else path_or_img
    return np.asarray(im.convert('RGB').resize((48, 48)), dtype=np.float32)


def main():
    if os.path.exists(WORK):
        shutil.rmtree(WORK)
    os.makedirs(WORK)
    zipfile.ZipFile(DOCX).extractall(WORK)

    cands = []
    for pat in ('session_07/**/*.png', 'art_refs/*.png', 'monsters/*.png',
                'world/*.png', 'items/*.png', 'scenes/*.png', 'companions/*.png'):
        cands += glob.glob(os.path.join(ASSETS, pat), recursive=True)
    cands += glob.glob(os.path.join(r'C:\Users\jhffm\dnd-campaign\_triage\superseded_art', '*.png'))
    csigs = []
    for c in cands:
        try:
            csigs.append((c, sig(c)))
        except Exception:
            pass

    mdir = os.path.join(WORK, 'word', 'media')
    used = {}
    for f in sorted(os.listdir(mdir), key=lambda x: (len(x), x)):
        p = os.path.join(mdir, f)
        try:
            s = sig(p)
        except Exception:
            continue
        best, bestd = None, 1e9
        for c, cs in csigs:
            if cs.shape != s.shape:
                continue
            dv = float(np.abs(cs - s).mean())
            if dv < bestd:
                best, bestd = c, dv
        rel = os.path.relpath(best, r'C:\Users\jhffm\dnd-campaign') if best else '?'
        flag = ''
        if bestd > 12:
            flag = '  <-- NO GOOD MATCH'
        if '_triage' in rel:
            flag += '  <-- RETIRED ART STILL EMBEDDED'
        used.setdefault(rel, []).append(f)
        print('%-16s %-64s d=%5.1f%s' % (f, rel, bestd, flag))

    print('\n--- assets embedded more than once ---')
    for rel, files in used.items():
        if len(files) > 1:
            print('  %s  ->  %s' % (rel, files))


if __name__ == '__main__':
    main()
