# patch_stormarc.py: Arc becomes an always-on rider (Storm-Arc); the Cell's
# charges become two Thunder Wave + two Counter-Bolt per Long Rest.
import ast, os
os.chdir(r"C:\Users\jhffm\dnd-campaign")
p = "templates/build_compendium.py"
t = open(p, encoding="utf-8").read()

old = '''        "**Charged Rounds.** The Storm Cell holds two charged rounds of each kind below, and "
        "you regain all expended rounds when you finish a Long Rest. If a round requires a "
        "saving throw, the DC equals your spell save DC.",
        "**Arc Round.** When you hit a creature with Boomstick, you can expend one Arc Round "
        "to make the shot leap: lightning arcs from the target to up to two other creatures of "
        "your choice within 15 feet of it. Each must make a Dexterity saving throw, taking 2d6 "
        "Lightning damage on a failed save, or half as much damage on a successful one.",'''
new = '''        "**Storm-Arc.** The drum never stops humming. Whenever you hit a creature with "
        "Boomstick, lightning arcs from the target to up to two other creatures of your choice "
        "within 15 feet of it. Each must make a Dexterity saving throw against your spell save "
        "DC, taking 2d6 Lightning damage on a failed save, or half as much damage on a "
        "successful one.",
        "**Charged Rounds.** The Storm Cell holds two Thunder Wave Rounds and two "
        "Counter-Bolts, and you regain all expended rounds when you finish a Long Rest. If a "
        "round requires a saving throw, the DC equals your spell save DC.",'''
assert old in t, "charged rounds block not found"
t = t.replace(old, new)

ast.parse(t)
open(p, "w", encoding="utf-8", newline="\n").write(t)
print("Storm-Arc applied; em dashes:", t.count(chr(0x2014)))
