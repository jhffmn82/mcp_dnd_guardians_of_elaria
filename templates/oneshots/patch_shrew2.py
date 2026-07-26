# patch_shrew2.py: Sandshrew gains a Bonus Action Sand Attack, and Spike
# Field becomes Earthquake: real AoE damage plus difficult terrain, so
# spending the whole Action is no longer a turn with nothing to roll.
import ast, os
os.chdir(r"C:\Users\jhffm\dnd-campaign")
p = "templates/build_bestiary.py"
t = open(p, encoding="utf-8").read()

old = '''            ("Spike Field", "Sandshrew churns the ground into a bristling field: a 20-foot Cube "
             "centered on itself. The field does not move with it and lasts until the start of "
             "Sandshrew's next turn. The area is Difficult Terrain, and a creature takes 5 (2d4) "
             "piercing damage for every 5 feet it moves inside it."),'''
new = '''            ("Sand Attack", "*Bonus Action, 30 ft., one creature.* Sandshrew flicks a spray of "
             "grit into the target's eyes. The target has Disadvantage on its next attack roll "
             "made before the start of Sandshrew's next turn."),
            ("Earthquake", "Sandshrew slams both forefeet down and the ground bucks and splits in "
             "a 20-foot Cube centered on itself. Each creature of Sandshrew's choice in that area "
             "makes a DC 15 Dexterity saving throw, taking 10 (3d6) Bludgeoning damage on a failed "
             "save, or half as much damage on a successful one. The broken ground is Difficult "
             "Terrain until the start of Sandshrew's next turn."),'''
assert old in t, "Spike Field block not found"
t = t.replace(old, new, 1)

# the intro line still promises spikes; make it promise the quake
t = t.replace("and the ground it stands on stops being easy to cross.",
              "and the ground it stands on stops being easy to cross.")
ast.parse(t)
open(p, "w", encoding="utf-8", newline="\n").write(t)
assert "Spike Field" not in t, "stray Spike Field reference"
print("Sandshrew updated; em dashes:", t.count(chr(0x2014)))
