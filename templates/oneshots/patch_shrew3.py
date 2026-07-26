# patch_shrew3.py: Sandshrew becomes a true wall. Curl and Guard (protect an
# ally) becomes Curl Up (protect himself), since Challenge already pulls the
# attacks onto him. Sand Attack is cut: Challenge occupies the same Bonus
# Action every round, so it would never be used.
import ast, os
os.chdir(r"C:\Users\jhffm\dnd-campaign")
p = "templates/build_bestiary.py"
t = open(p, encoding="utf-8").read()

old_reaction = '''            ("Curl and Guard", "*Reaction, 15 ft.* When an ally it can see is hit by an attack, "
             "Sandshrew rolls into the path and becomes the target instead. It takes the damage, "
             "reduced by 5."),'''
new_reaction = '''            ("Curl Up", "*Reaction.* When Sandshrew is hit by an attack, it tucks behind its "
             "plates. Reduce that attack's damage by 10."),'''
assert old_reaction in t, "Curl and Guard not found"
t = t.replace(old_reaction, new_reaction, 1)

old_sand = '''            ("Sand Attack", "*Bonus Action, 30 ft., one creature.* Sandshrew flicks a spray of "
             "grit into the target's eyes. The target has Disadvantage on its next attack roll "
             "made before the start of Sandshrew's next turn."),
'''
new_sand = '''            ("Challenge", "*Bonus Action.* Sandshrew rears up with a rattling hiss and dares "
             "them to try it. Until the start of its next turn, each enemy within 30 feet that "
             "can see it has Disadvantage on attack rolls against any target other than "
             "Sandshrew."),
'''
assert old_sand in t, "Sand Attack not found"
t = t.replace(old_sand, new_sand, 1)

ast.parse(t)
open(p, "w", encoding="utf-8", newline="\n").write(t)
assert "Sand Attack" not in t and "Curl and Guard" not in t, "stray reference"
print("Sandshrew is a wall now; em dashes:", t.count(chr(0x2014)))
