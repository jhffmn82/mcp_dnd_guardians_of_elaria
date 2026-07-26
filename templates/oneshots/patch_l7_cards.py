# patch_l7_cards.py: add Ghostbloom's level-7 card (an addition, not a
# replacement) and Sandslash, the Earth-rift companion, to the bestiary.
import ast, os
os.chdir(r"C:\Users\jhffm\dnd-campaign")
p = "templates/build_bestiary.py"
t = open(p, encoding="utf-8").read()

anchor = '''    }]),

    ("lore", "The Kept Company",'''
assert anchor in t, "anchor not found"

new = '''    }]),

    ("body", "*The rift arc asks more of her than the road ever did. This is Ghostbloom as she "
             "stands at the party's side from the Earth Rift onward: the same creature, grown "
             "into the work. Her older card above is kept for the Sessions 1 to 7 chronicle.*"),
    # Level-7 companion card (DM directive 2026-07-18): +1 AC, +1 proficiency,
    # +10 HP, +1 weapon damage, and one more die on Guardian's Light and the
    # Wail. She is the generalist the rift specialists are measured against.
    ("enemy_cards", [{
        "name": "Ghostbloom, Spectral Blossom (Level 7)",
        "sub": "Tiny fey (Ghost/Grass), chaotic good \\u2726 the party's companion, rift arc",
        "img": "assets/characters/ghostbloom.png", "img_w": 2.4,
        "banner": TEAL,
        "stats": [
            "**AC** 16 (natural armor)  **HP** 62 (8d4 + 42)  **Speed** 30 ft., fly 30 ft. (hover)",
            "**STR** 8  **DEX** 18  **CON** 18  **INT** 12  **WIS** 14  **CHA** 16",
            "**Saves** Dex +8, Con +8, Wis +6  **Skills** Perception +6, Stealth +8",
            "**Vulnerable** fire, cold (mind the friendly fire)",
            "**Resist** necrotic; bludgeoning, piercing, and slashing from nonmagical attacks",
            "**Imm.** (cond) charmed, frightened",
            "**Senses** darkvision 60 ft., passive Perception 16",
            "**Languages** Sylvan, telepathy 30 ft. (to her keeper)",
        ],
        "traits": [
            ("Fey Step (1/Short Rest)", "As a bonus action, teleport up to 20 ft. to an unoccupied space "
             "she can see. Her next attack this turn has advantage."),
            ("Spectral Form", "She can move through creatures and objects as difficult terrain. If she "
             "ends her turn inside an object, she is shunted to the nearest space and takes 5 force damage."),
            ("Guardian's Light (3/Short Rest)", "*Reaction, 30 ft.* When an ally she can see takes damage, "
             "that ally regains 12 (2d8 + 3) hit points and immediately ends the charmed or frightened "
             "condition on itself."),
        ],
        "actions": [
            ("Multiattack", "She makes two Spectral Lash attacks."),
            ("Spectral Lash", "*Melee Weapon Attack:* +8 to hit, reach 15 ft., one target. *Hit:* 10 (1d8 + 6) "
             "slashing plus 3 (1d6) necrotic, and the target must succeed on a DC 16 Wisdom save or be "
             "frightened until the end of its next turn."),
            ("Ghostly Wail (1/Long Rest)", "A haunting cry in a 15-ft. cone. Each creature there makes a DC 16 "
             "Wisdom save, taking 17 (5d6) necrotic and frightened until the end of its next turn on a fail, "
             "or half damage and no fear on a success."),
            ("Dread Shroud", "*Bonus Action, 30 ft., one creature.* A chill bloom settles over the target: "
             "DC 16 Wisdom save or disadvantage on all attack rolls until the start of her next turn."),
        ],
    }]),

    ("body", "*The Underroot's own answer to a charge. Sandslash plants itself between the party "
             "and whatever is coming, and the ground it stands on stops being easy to cross.*"),
    # Earth-rift companion (DM directive 2026-07-18): the TANK of the roster.
    # No expendable uses: the Action and the Reaction are the whole limiter.
    ("enemy_cards", [{
        "name": "Sandslash",
        "sub": "Medium beast (Ground), unaligned \\u2726 Earth-rift companion",
        "banner": TEAL,
        "stats": [
            "**AC** 17 (natural armor)  **HP** 78 (12d8 + 24)  **Speed** 30 ft., burrow 40 ft.",
            "**STR** 18  **DEX** 14  **CON** 15  **INT** 6  **WIS** 12  **CHA** 10",
            "**Saves** Str +7, Con +5  **Skills** Athletics +7, Perception +4",
            "**Vulnerable** cold",
            "**Resist** bludgeoning, piercing, and slashing from nonmagical attacks",
            "**Senses** darkvision 60 ft., tremorsense 30 ft., passive Perception 14",
            "**Languages** understands its handler, speaks none",
        ],
        "traits": [
            ("Spiked Coat", "A creature that hits Sandslash with a melee attack takes 5 piercing "
             "damage from its quills."),
            ("Curl and Guard", "*Reaction, 15 ft.* When an ally it can see is hit by an attack, "
             "Sandslash rolls into the path and becomes the target instead. It takes the damage, "
             "reduced by 5."),
        ],
        "actions": [
            ("Multiattack", "It makes two Claw attacks."),
            ("Claw", "*Melee Weapon Attack:* +8 to hit, reach 5 ft., one target. *Hit:* 10 (1d10 + 5) "
             "slashing damage."),
            ("Spike Field", "Sandslash churns the ground into a bristling field: a 20-foot Cube "
             "centered on itself. The field does not move with it and lasts until the start of "
             "Sandslash's next turn. The area is Difficult Terrain, and a creature takes 5 (2d4) "
             "piercing damage for every 5 feet it moves inside it."),
        ],
    }]),

    ("lore", "The Kept Company",'''

t = t.replace(anchor, new, 1)
ast.parse(t)
open(p, "w", encoding="utf-8", newline="\n").write(t)
print("cards added; em dashes:", t.count(chr(0x2014)))
