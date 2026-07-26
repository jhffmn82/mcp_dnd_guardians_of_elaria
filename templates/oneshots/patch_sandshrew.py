# patch_sandshrew.py: the Earth companion is Sandshrew, not Sandslash.
# Spiked Coat (quills it does not have) becomes Sand Veil; portrait wired in.
import ast, os
os.chdir(r"C:\Users\jhffm\dnd-campaign")
p = "templates/build_bestiary.py"
t = open(p, encoding="utf-8").read()

# 1. name + portrait
old = '''        "name": "Sandslash",
        "sub": "Medium beast (Ground), unaligned \\u2726 Earth-rift companion",
        "banner": TEAL,'''
new = '''        "name": "Sandshrew",
        "sub": "Medium beast (Ground), unaligned \\u2726 Earth-rift companion",
        "img": "assets/characters/sandshrew.png", "img_w": 2.4,
        "banner": TEAL,'''
assert old in t, "name block not found"
t = t.replace(old, new, 1)

# 2. Spiked Coat -> Sand Veil
old = '''            ("Spiked Coat", "A creature that hits Sandslash with a melee attack takes 5 piercing "
             "damage from its quills."),'''
new = '''            ("Sand Veil", "Dust curls constantly from its plates. Attack rolls against Sandshrew "
             "made from more than 15 feet away have Disadvantage."),'''
assert old in t, "Spiked Coat not found"
t = t.replace(old, new, 1)

# 3. remaining name references
t = t.replace("Sandslash rolls into the path", "Sandshrew rolls into the path")
t = t.replace("Sandslash churns the ground", "Sandshrew churns the ground")
t = t.replace("start of \\n             \"Sandslash's next turn", "start of \\n             \"Sandshrew's next turn")
t = t.replace("Sandslash's next turn", "Sandshrew's next turn")
t = t.replace("*Reaction, 15 ft.* When an ally it can see is hit by an attack, "
              "Sandslash", "*Reaction, 15 ft.* When an ally it can see is hit by an attack, Sandshrew")
t = t.replace("A creature that hits Sandslash", "A creature that hits Sandshrew")
t = t.replace("*The Underroot's own answer to a charge. Sandslash plants",
              "*The Underroot's own answer to a charge. Sandshrew plants")

assert "Sandslash" not in t, "stray Sandslash reference remains"
ast.parse(t)
open(p, "w", encoding="utf-8", newline="\n").write(t)
print("Sandshrew applied; em dashes:", t.count(chr(0x2014)))
