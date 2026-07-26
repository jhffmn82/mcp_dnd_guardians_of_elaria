# patch_gb_art.py: wire the approved level-7 portrait into Ghostbloom's L7
# card only. Her original card keeps its original art.
import ast, os
os.chdir(r"C:\Users\jhffm\dnd-campaign")
p = "templates/build_bestiary.py"
t = open(p, encoding="utf-8").read()

i = t.find('"name": "Ghostbloom, Spectral Blossom (Level 7)"')
assert i > 0, "L7 card not found"
j = t.find('"assets/characters/ghostbloom.png"', i)
assert j > i, "L7 img line not found"
t = t[:j] + '"assets/characters/ghostbloom_l7.png"' + t[j + len('"assets/characters/ghostbloom.png"'):]

# sanity: the ORIGINAL card must still point at the original art
assert '"assets/characters/ghostbloom.png"' in t, "original art reference lost"
ast.parse(t)
open(p, "w", encoding="utf-8", newline="\n").write(t)
print("L7 portrait wired; em dashes:", t.count(chr(0x2014)))
