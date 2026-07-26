# patch_stormarc2.py: Storm-Arc deals 1d6 to the target and arcs 2d6 to two others.
import ast, os
os.chdir(r"C:\Users\jhffm\dnd-campaign")
p = "templates/build_compendium.py"
t = open(p, encoding="utf-8").read()

old = '''        "**Storm-Arc.** The drum never stops humming. Whenever you hit a creature with "
        "Boomstick, lightning arcs from the target to up to two other creatures of your choice "
        "within 15 feet of it. Each must make a Dexterity saving throw against your spell save "
        "DC, taking 2d6 Lightning damage on a failed save, or half as much damage on a "
        "successful one.",'''
new = '''        "**Storm-Arc.** The drum never stops humming. Whenever you hit a creature with "
        "Boomstick, the shot crackles: the target takes an extra 1d6 Lightning damage, and "
        "lightning arcs from it to up to two other creatures of your choice within 15 feet of "
        "it. Each arced creature must make a Dexterity saving throw against your spell save "
        "DC, taking 2d6 Lightning damage on a failed save, or half as much damage on a "
        "successful one.",'''
assert old in t, "Storm-Arc not found"
t = t.replace(old, new)

ast.parse(t)
open(p, "w", encoding="utf-8", newline="\n").write(t)
print("Storm-Arc v2 applied")
