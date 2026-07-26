# patch_drop_shroud.py: Dread Shroud is cut from every version of Ghostbloom.
# It duplicated the frightened condition her Spectral Lash rider already
# imposes, at will, on a bonus action (DM call 2026-07-18).
import ast, os, re
os.chdir(r"C:\Users\jhffm\dnd-campaign")

targets = ["templates/build_bestiary.py", "templates/build_sheets.py"]
total = 0
for p in targets:
    t = open(p, encoding="utf-8").read()
    # Each entry is a ("Dread Shroud", "...") tuple spanning several lines,
    # ending at the closing '),' of the tuple. Match non-greedily.
    pat = re.compile(r'[ \t]*\("Dread Shroud",.*?\),\n', re.S)
    t2, n = pat.subn("", t)
    assert n > 0, f"no Dread Shroud entry matched in {p}"
    ast.parse(t2)
    open(p, "w", encoding="utf-8", newline="\n").write(t2)
    print(f"{p}: removed {n}")
    total += n

for p in targets:
    assert "Dread Shroud" not in open(p, encoding="utf-8").read(), f"stray reference in {p}"
print("total removed:", total)
