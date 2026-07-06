# build_bestiary.py
# The Guardians of Elaria: THE BESTIARY.
# A comprehensive, illustrated field guide to every creature, companion, and
# enemy the party has met across the whole chronicle (Sessions 1-7 / Gearhaven),
# each with a full 5e-style statblock in the Session 7 / Gearhaven appendix style.
#
# Stats are taken AS WRITTEN from the session documents:
#   sessions/session_01_gathering_of_friends.docx (Lickgloom, Duckleaf, Cognifin, Mist Stalker)
#   sessions/session_02_oakshade_village.docx (Mudskip, Grimfang war band, Terranox)
#   sessions/session_03_quest_for_knowledge.docx (Shadowflame, Displacer Beasts, Shroomyte,
#                                                  companions Floraburst/Aqualump/Emberpaws)
#   sessions/session_04_encounter_tables_and_stat_blocks.docx (the Krampusshade winter court)
#   sessions/session_05_stat_blocks.docx (Davy Jones and his drowned crew)
#   sessions/session_06_wraithpine.docx (the False Hydra, Scarecrows, Strawlings, rats, undead)
#   sessions/session_07_gearhaven.docx (the clockwork enemies; this doc's style is the model)
#   lore/floraburst_statblock.docx (the evolved Floraburst / Ghostbloom line)
#
# Build:  python templates/build_bestiary.py   ->   compendium/bestiary.docx
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc

NOTE = "A running reference for The Guardians of Elaria. Updated as the chronicle grows."

# Handy ability-score dict shorthand
def ab(s, d, c, i, w, ch):
    return {"STR": s, "DEX": d, "CON": c, "INT": i, "WIS": w, "CHA": ch}

B = [
    ("titlepage", "THE GUARDIANS OF ELARIA", "THE BESTIARY",
     "Creatures of the Chronicle", NOTE),

    ("gold", "Here is every creature the Guardians have faced, freed, or befriended, gathered "
             "with its lore and its complete statistics. When a planar creature falls, it leaves "
             "no body: a gleaming mote of its home plane rises, hangs a moment, and fades (and the "
             "Essence Sphere tugs toward it). Read on, brave heroes, and know your monsters."),

    # ==================================================================
    ("h1", "Companions & Friends", {"pagebreak": True}),
    ("body", "Not every creature in this book is an enemy. Some walk the road beside the Guardians."),

    ("body", "*Ghostbloom is the party's dearest companion, chosen in Session 3 as Floraburst, "
             "changed aboard the sinking Dutchman and again in Wraithpine's ghost-light. Her petals "
             "are glass-pale now and chime like frost; she floats, speaks in soft telepathy, and "
             "glows brighter near planar wounds. Some say she is Elaria's own little voice.*"),
    ("statblock", {
        "name": "Ghostbloom, Spectral Blossom",
        "type": "Tiny fey (Ghost/Grass), chaotic good",
        "img": "assets/characters/ghostbloom.png", "img_w": 2.4,
        "ac": "15 (natural armor)", "hp": "52 (8d4 + 32)", "speed": "30 ft., fly 30 ft. (hover)",
        "abilities": ab(8, 18, 18, 12, 14, 16),
        "saves": "Dex +7, Con +7, Wis +5",
        "skills": "Perception +5, Stealth +7",
        "vulnerabilities": "fire, cold (mind the friendly fire)",
        "resistances": "necrotic, poison; bludgeoning, piercing, and slashing from nonmagical attacks",
        "condition_immunities": "charmed, frightened, grappled, paralyzed, poisoned, prone, restrained",
        "senses": "darkvision 60 ft., passive Perception 15",
        "languages": "Sylvan, telepathy 30 ft. (to her keeper)",
        "traits": [
            ("Fey Step (1/Combat)", "As a bonus action, teleport up to 20 ft. to an unoccupied space "
             "she can see. Her next attack this turn has advantage."),
            ("Spectral Form", "She can move through creatures and objects as difficult terrain. If she "
             "ends her turn inside an object, she is shunted to the nearest space and takes 5 force damage."),
            ("Guardian's Light (Reaction, 1/Combat)", "When an ally within 30 ft. takes damage, she sheds "
             "bright light in a 10-ft. radius (30-ft. dim) and heals that ally for 1d8 + her Charisma modifier."),
        ],
        "actions": [
            ("Multiattack", "She makes two Vine Lash attacks."),
            ("Vine Lash", "*Ranged Weapon Attack:* +7 to hit, range 15 ft., one target. *Hit:* 9 (1d8 + 5) "
             "slashing plus 3 (1d6) necrotic, and the target must succeed on a DC 13 Wisdom save or be "
             "frightened until the end of its next turn."),
            ("Ghostly Wail (1/Combat)", "A haunting cry in a 15-ft. cone. Each creature there makes a DC 15 "
             "Wisdom save, taking 14 (4d6) necrotic and frightened for 1 round on a fail, or half damage and "
             "no fear on a success."),
        ],
        "legendary": [
            ("Blossom of Dawn (1/Day)", "She releases a burst of fey energy in a 20-ft. radius. Allies there "
             "regain 2d8 + 3 hit points, and undead take 2d8 radiant (DC 14 Dexterity save for half)."),
        ],
    }),

    ("body", "*Floraburst, as she was before the change: a leafy sprout-backed creature who loved "
             "sunlight and berries. This is the form the party first knew and loved in Session 3.*"),
    ("statblock", {
        "name": "Floraburst",
        "type": "Small fey, neutral good",
        "img": "assets/characters/floraburst.png", "img_w": 2.4,
        "ac": "14 (natural armor)", "hp": "45 (6d6 + 18)", "speed": "30 ft.",
        "abilities": ab(14, 12, 16, 10, 14, 10),
        "skills": "Nature +4, Survival +4",
        "resistances": "poison",
        "senses": "darkvision 60 ft., passive Perception 12",
        "languages": "understands Sylvan and Common but cannot speak",
        "traits": [
            ("Plant Camouflage", "Advantage on Stealth checks to hide in heavy foliage."),
            ("Photosynthesis", "During a short or long rest in sunlight, Floraburst recovers 10 extra hit points."),
        ],
        "actions": [
            ("Razor Leaf", "*Ranged Weapon Attack:* +4 to hit, range 30 ft., one target. *Hit:* 10 (2d8 + 2) slashing."),
            ("Vine Lash", "*Melee Weapon Attack:* +4 to hit, reach 15 ft., one target. *Hit:* 8 (1d10 + 2) "
             "bludgeoning, and the target must succeed on a DC 13 Strength save or be restrained until the end "
             "of its next turn."),
            ("Floraberry (3/Day)", "Floraburst produces 1d4 + 1 magical berries. A creature can use an action "
             "to eat one and restore 3 hit points."),
        ],
    }),

    ("body", "*In Session 3, Professor Aelwyn offered the party three little wards; they chose Floraburst. "
             "The two who stayed behind, Aqualump and Emberpaws, are catalogued here too, for they are "
             "part of the story.*"),
    ("statblock", {
        "name": "Aqualump",
        "type": "Small elemental, neutral good",
        "img": "assets/characters/aqualump.png", "img_w": 2.4,
        "ac": "16 (natural armor, Shell Defense)", "hp": "54 (7d6 + 21)", "speed": "25 ft., swim 30 ft.",
        "abilities": ab(15, 14, 17, 10, 13, 11),
        "skills": "Athletics +4, Perception +3",
        "resistances": "cold",
        "senses": "darkvision 60 ft., passive Perception 13",
        "languages": "understands Aquan and Common but cannot speak",
        "traits": [
            ("Shell Defense", "As a bonus action, Aqualump withdraws into its shell, gaining +4 AC until the "
             "start of its next turn; while in its shell its speed is 0."),
            ("Water Veil", "Aqualump cannot be set on fire and has advantage on saves against being ignited or burned."),
        ],
        "actions": [
            ("Water Bolt", "*Ranged Weapon Attack:* +4 to hit, range 30 ft., one target. *Hit:* 10 (2d8 + 2) "
             "bludgeoning, and the target must succeed on a DC 14 Strength save or be knocked prone."),
            ("Surf (Recharge 5-6)", "A 15-ft. cone of water. Each creature there makes a DC 14 Dexterity save, "
             "taking 14 (4d6) cold on a fail (half on a success); those who fail are knocked prone."),
            ("Frost Shell", "*Ranged Weapon Attack:* +4 to hit, range 20 ft., one target. *Hit:* 8 (1d10 + 2) "
             "cold, and the target's speed is reduced by 10 ft. until the end of its next turn."),
        ],
    }),
    ("statblock", {
        "name": "Emberpaws",
        "type": "Small elemental, chaotic good",
        "img": "assets/characters/emberpaws.png", "img_w": 2.4,
        "ac": "15 (natural armor)", "hp": "42 (6d6 + 15)", "speed": "30 ft.",
        "abilities": ab(13, 16, 15, 10, 12, 12),
        "skills": "Acrobatics +5, Perception +3",
        "immunities": "fire",
        "senses": "darkvision 60 ft., passive Perception 13",
        "languages": "understands Ignan and Common but cannot speak",
        "traits": [
            ("Fiery Spirit", "When reduced to 0 hit points, Emberpaws bursts into flame. Each creature within "
             "10 ft. makes a DC 13 Dexterity save, taking 7 (2d6) fire on a fail (half on a success)."),
            ("Heatwave (3/Day)", "As a bonus action, Emberpaws radiates heat for 1 minute; any creature that "
             "hits it with a melee attack takes 4 (1d8) fire."),
        ],
        "actions": [
            ("Ember", "*Ranged Weapon Attack:* +5 to hit, range 30 ft., one target. *Hit:* 9 (2d6 + 2) fire."),
            ("Bite", "*Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 8 (1d8 + 3) piercing."),
            ("Tail Flame Whip", "*Melee Weapon Attack:* +5 to hit, reach 10 ft., one target. *Hit:* 10 (2d6 + 3) "
             "fire, and the target must succeed on a DC 13 Dexterity save or be ignited, taking 2 (1d4) fire at "
             "the start of each of its turns until the flames are put out."),
        ],
    }),

    ("body", "*Lickgloom was the party's very first friend, met on their first night by a pond in the "
             "Forest of Whispers: round-bodied, endlessly curious, with a tongue longer than it is tall "
             "and a telepathic voice of pure feeling ('Food? Friend?'). It chose to stay among Professor "
             "Aelwyn's creatures at Ravenstone. Visits are owed.*"),
    ("statblock", {
        "name": "Lickgloom",
        "img": "assets/monsters/lickgloom.png",
        "type": "Small fey, neutral good",
        "ac": "13 (natural armor)", "hp": "27 (5d6 + 10)", "speed": "30 ft.",
        "abilities": ab(10, 15, 14, 8, 12, 13),
        "cr": "1 (200 XP)",
        "senses": "darkvision 60 ft., passive Perception 11",
        "languages": "telepathy 30 ft. (simple feelings and impressions)",
        "traits": [
            ("Curious Palate", "Lickgloom can taste the world through its tongue, granting an ally advantage "
             "on Investigation or Perception checks it helps with."),
        ],
        "actions": [
            ("Tongue Whip", "*Melee Weapon Attack:* reach 10 ft., one target. *Hit:* 1d6 + 2 bludgeoning."),
            ("Lick Attack", "The tongue delivers a stunning slap. *Hit:* 1d8 + 2 bludgeoning, and the target "
             "must succeed on a DC 12 Constitution save or be stunned until the end of its next turn."),
            ("Sticky Lick (Recharge 5-6)", "Lickgloom tries to steal a small item from a creature within 10 ft.; "
             "the target must succeed on a DC 13 Dexterity save or the item is pulled to Lickgloom."),
        ],
    }),

    ("body", "**Pikachu, the Spark Fox.** *An old friend of the Glimmergear family, bodiless since before "
             "the chronicle began, sleeping inside the Essence Sphere. His golden projection first appeared "
             "in Gearhaven: two long ears, a lightning-bolt tail, and a warning carried through Ursa's Mark. "
             "He has no statistics yet; he is more a key than a creature, and his full return is still to come.*"),

    # ==================================================================
    ("h1", "Session 1: The Forest of Whispers", {"pagebreak": True}),
    ("body", "*The first creatures the Guardians ever faced, all touched by the thinning boundary "
             "between the planes. Each left behind a fading mote, the party's very first clue.*"),

    ("statblock", {
        "name": "Duckleaf",
        "type": "Small beast (Elemental Air), neutral",
        "img": "assets/monsters/duckleaf_stone_circle.png", "img_w": 2.5,
        "ac": "15 (natural armor)", "hp": "52 (8d8 + 16)", "speed": "30 ft., fly 30 ft.",
        "abilities": ab(14, 16, 14, 10, 12, 10),
        "saves": "Dex +5, Wis +3",
        "skills": "Acrobatics +5, Perception +3",
        "resistances": "slashing, bludgeoning (wind-shielded)",
        "senses": "darkvision 60 ft., passive Perception 13",
        "languages": "telepathy 30 ft. (in quacks)",
        "cr": "4 (1,100 XP)",
        "traits": [
            ("Winged Leap", "Duckleaf can leap 30 ft. in any direction without provoking opportunity attacks. "
             "Disrupting a stone of the rune-circle ends this ability for the rest of the battle."),
        ],
        "actions": [
            ("Leek Strike", "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 2d8 + 4 slashing."),
            ("Aerial Slash", "*Ranged Weapon Attack:* +5 to hit, range 20/60 ft., one target. *Hit:* 3d6 + 3 "
             "slashing, a blade of wind."),
            ("Quack of Fury (Recharge 5-6)", "A thunderous telepathic quack. Each creature within 15 ft. makes "
             "a DC 14 Wisdom save or is frightened for 1 minute (repeat save at end of each turn)."),
        ],
    }),
    ("statblock", {
        "name": "Cognifin",
        "type": "Small beast (Elemental Water), neutral",
        "img": "assets/monsters/cognifin_grove.png", "img_w": 2.5,
        "ac": "14 (natural armor)", "hp": "45 (6d8 + 18)", "speed": "0 ft., fly 30 ft. (hover)",
        "abilities": ab(10, 14, 16, 10, 14, 12),
        "saves": "Dex +4, Wis +4",
        "skills": "Perception +4, Arcana +2",
        "resistances": "cold, psychic",
        "senses": "darkvision 60 ft., passive Perception 14",
        "languages": "telepathy 60 ft. (images and feelings)",
        "cr": "3 (700 XP)",
        "actions": [
            ("Headache Blast", "*Ranged Attack:* +4 to hit, range 30 ft., one target. *Hit:* 2d6 + 2 psychic."),
            ("Water Pulse", "*Ranged Spell Attack:* +4 to hit, range 30 ft., one target. *Hit:* 2d6 + 2 "
             "bludgeoning, and the target must make a DC 12 Strength save or be knocked prone."),
            ("Confusion Pulse (Recharge 5-6)", "A wave of psychic energy in a 15-ft. radius. Each creature there "
             "makes a DC 13 Wisdom save or is confused (as the *confusion* spell) for 1 minute (repeat save at "
             "end of each turn)."),
        ],
        "reactions": [
            ("Psychic Shield", "When hit by an attack, Cognifin gains +2 AC until the start of its next turn."),
        ],
        "legendary": [
            ("Whirlpool", "Cognifin makes a 5-ft.-radius whirlpool; creatures there make a DC 12 Strength save "
             "or be pulled 10 ft. to its center and restrained until the end of their next turn."),
            ("Tidal Wave", "A 10-ft. line of water. Creatures in its path make a DC 12 Dexterity save or take "
             "2d4 bludgeoning and are pushed back 5 ft."),
        ],
    }),
    ("statblock", {
        "name": "Mist Stalker",
        "img": "assets/monsters/mist_stalker.png",
        "type": "Medium fey, unaligned",
        "ac": "13", "hp": "39", "speed": "40 ft.",
        "abilities": ab(14, 16, 12, 6, 12, 10),
        "cr": "2 (450 XP)",
        "senses": "darkvision 60 ft.",
        "traits": [
            ("Fog Cloak", "As a bonus action, the stalker wraps itself in fog, becoming heavily obscured for 1 turn."),
        ],
        "actions": [
            ("Claw", "*Melee Weapon Attack:* one target. *Hit:* slashing damage from raking claws."),
            ("Bite", "*Melee Weapon Attack:* one target. *Hit:* piercing damage."),
            ("Howl of the Mist", "Each creature within 30 ft. that can hear it must save or be frightened."),
        ],
    }),

    # ==================================================================
    ("h1", "Session 2: The Road to Ravenstone", {"pagebreak": True}),
    ("body", "*On the road to Oakshade and Ravenstone the party met slick water-elementals, an old "
             "goblin grudge come calling, and a serpent of living stone.*"),

    ("statblock", {
        "name": "Mudskip",
        "img": "assets/monsters/mudskip.png",
        "type": "Small elemental (Plane of Water), neutral",
        "ac": "13 (natural armor)", "hp": "22 (4d6 + 8)", "speed": "20 ft., swim 30 ft.",
        "abilities": ab(12, 14, 14, 6, 12, 8),
        "skills": "Stealth +4, Perception +3",
        "resistances": "fire",
        "vulnerabilities": "lightning",
        "senses": "darkvision 60 ft., passive Perception 13",
        "languages": "understands Aquan but can't speak",
        "cr": "1/2 (100 XP)",
        "traits": [
            ("Amphibious", "The Mudskip can breathe air and water."),
            ("Mud Dweller", "It ignores difficult terrain made of mud or shallow water."),
            ("Slippery", "Advantage on checks and saves to escape a grapple."),
        ],
        "actions": [
            ("Multiattack", "One Mud Spit and one Tail Slap."),
            ("Mud Spit", "*Ranged Weapon Attack:* +4 to hit, range 30 ft. *Hit:* 5 (1d6 + 2) bludgeoning, and "
             "on a failed DC 12 Dexterity save the target's speed drops by 10 ft. until end of its next turn."),
            ("Tail Slap", "*Melee Weapon Attack:* +4 to hit, reach 5 ft. *Hit:* 6 (1d8 + 2) bludgeoning."),
            ("Mud Splash (Recharge 5-6)", "A 15-ft. cone of mud. DC 12 Dexterity save; 9 (2d6 + 2) bludgeoning "
             "and blinded until end of next turn on a fail, half and no blind on a success."),
        ],
    }),

    ("body", "**The Grimfang war band.** *A rival goblin clan carrying an old grudge against Stabby's "
             "Bloodfang: two goblin archers, a worg, a club-swinging orc, a hobgoblin sniper, and a "
             "scar-faced Goblin Boss who taunted Stabby and regretted it. Driven off, not destroyed; "
             "grudges keep. Their statistics are the standard Monster Manual entries.*"),
    ("statblock", {
        "name": "Goblin Boss (the Grimfang leader)",
        "type": "Small humanoid (goblinoid), neutral evil",
        "img": "assets/monsters/grimfang_clan.png", "img_w": 3.6,
        "ac": "17 (chain shirt, shield)", "hp": "21 (6d6)", "speed": "30 ft.",
        "abilities": ab(10, 14, 10, 10, 8, 10),
        "skills": "Stealth +6",
        "senses": "darkvision 60 ft., passive Perception 9",
        "languages": "Common, Goblin",
        "cr": "1 (200 XP)",
        "traits": [
            ("Nimble Escape", "The boss can Disengage or Hide as a bonus action on each of its turns."),
        ],
        "actions": [
            ("Multiattack", "Two attacks with its scimitar (the second only if the first hits)."),
            ("Scimitar", "*Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 5 (1d6 + 2) slashing."),
            ("Javelin", "*Melee or Ranged Weapon Attack:* +4 to hit, reach 5 ft. or range 30/120 ft. *Hit:* "
             "5 (1d6 + 2) piercing."),
        ],
        "reactions": [
            ("Redirect Attack", "When a creature the boss can see targets it with an attack, it swaps places "
             "with a goblin ally within 5 ft.; that ally becomes the target instead."),
        ],
    }),
    ("body", "*The band also fielded standard **Goblins** (AC 15, HP 7), a **Worg** (AC 13, HP 26), an "
             "**Orc** (AC 13, HP 15), and a **Hobgoblin** sniper (AC 18, HP 11).*"),

    ("statblock", {
        "name": "Terranox",
        "type": "Large elemental (Plane of Earth), unaligned",
        "img": "assets/monsters/terranox.png", "img_w": 3.0,
        "ac": "16 (natural armor)", "hp": "95 (10d10 + 40)", "speed": "30 ft., burrow 30 ft.",
        "abilities": ab(20, 10, 18, 5, 11, 6),
        "resistances": "bludgeoning, piercing, and slashing from nonmagical, non-adamantine weapons",
        "immunities": "fire, poison",
        "condition_immunities": "exhaustion, paralyzed, petrified, poisoned, prone",
        "senses": "darkvision 60 ft., tremorsense 60 ft., passive Perception 10",
        "cr": "4 (1,100 XP)",
        "traits": [
            ("Earth Glide", "Terranox burrows through unworked earth and stone without disturbing it."),
            ("Siege Monster", "Deals double damage to objects and structures."),
            ("Elemental Resilience", "Advantage on saves against spells and magical effects."),
            ("Immutable Form", "Immune to any effect that would alter its form."),
        ],
        "actions": [
            ("Multiattack", "One Bite and one Tail Slam."),
            ("Bite", "*Melee Weapon Attack:* +7 to hit, reach 10 ft., one target. *Hit:* 16 (2d10 + 5) piercing."),
            ("Tail Slam", "*Melee Weapon Attack:* +7 to hit, reach 15 ft., one target. *Hit:* 13 (2d8 + 5) "
             "bludgeoning, and the target must succeed on a DC 15 Strength save or be knocked prone."),
            ("Stone Coil (Recharge 5-6)", "One creature within 10 ft. makes a DC 15 Dexterity save or is grappled "
             "and restrained (escape DC 15), taking 9 (1d8 + 5) bludgeoning at the start of each of its turns."),
            ("Earthquake Stomp (Recharge 6)", "A tremor in a 20-ft. radius; each creature on the ground makes a "
             "DC 15 Dexterity save, taking 14 (4d6) bludgeoning and knocked prone on a fail (half, no prone, on a success)."),
        ],
    }),

    # ==================================================================
    ("h1", "Session 3: The Road South", {"pagebreak": True}),
    ("body", "*South toward the sea, the party crossed shadowed thickets and glowing fungal groves, "
             "and learned that the planar wounds are teaching old monsters new tricks.*"),

    ("statblock", {
        "name": "Shadowflame",
        "type": "Medium undead, chaotic evil",
        "img": "assets/monsters/shadowflame.png", "img_w": 2.6,
        "ac": "14 (natural armor)", "hp": "58 (9d8 + 18)", "speed": "0 ft., fly 40 ft. (hover)",
        "abilities": ab(8, 18, 14, 12, 15, 18),
        "skills": "Stealth +8, Intimidation +6",
        "resistances": "acid, fire, lightning, necrotic; bludgeoning, piercing, and slashing from nonmagical weapons",
        "immunities": "poison, psychic",
        "condition_immunities": "charmed, frightened, grappled, paralyzed, poisoned, prone, restrained",
        "senses": "darkvision 60 ft., passive Perception 12",
        "languages": "understands Common, Sylvan, and Abyssal (does not speak)",
        "cr": "4 (1,100 XP)",
        "traits": [
            ("Illusions of Fear", "At the start of combat, the Shadowflame conjures three identical illusions "
             "(AC 14). A creature attacking one must succeed on a DC 18 Arcana or Perception check to know it is "
             "false; on a failure the attack misses and the illusion remains."),
        ],
        "actions": [
            ("Shadow Claw", "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 13 (2d8 + 4) "
             "necrotic, and the target must succeed on a DC 14 Wisdom save or be frightened until end of next turn."),
            ("Terror Wave (Recharge 5-6)", "A 15-ft. cone of dark energy. Each creature makes a DC 14 Wisdom save, "
             "taking 16 (3d10) necrotic and frightened for 1 minute on a fail (repeat save at end of each turn)."),
        ],
        "reactions": [
            ("Shadowmeld", "When hit, the Shadowflame teleports up to 20 ft. to an unoccupied space it can see, "
             "becoming lightly obscured until the start of its next turn."),
        ],
    }),

    ("body", "**Displacer Beasts (a pair).** *Six-legged, tentacled, and impossibly TALKING ('Fresh prey... "
             "too easy.'): the planar distortion had given old monsters new voices. Their shimmering forms "
             "impose disadvantage on attacks against them until they take damage; their barbed tentacles "
             "strike at 10 ft. Their fall revealed rune-tears in the forest floor. (Statistics as the "
             "standard Displacer Beast, CR 3, AC 13, HP 85.)*"),

    ("statblock", {
        "name": "Shroomyte",
        "type": "Small plant, neutral",
        "img": "assets/monsters/shroomyte_grove.png", "img_w": 2.8,
        "ac": "13 (natural armor)", "hp": "27 (5d8 + 5)", "speed": "20 ft.",
        "abilities": ab(12, 12, 14, 6, 12, 7),
        "saves": "Con +4, Wis +3",
        "skills": "Stealth +3, Perception +3",
        "resistances": "poison",
        "condition_immunities": "poisoned",
        "senses": "darkvision 60 ft., passive Perception 13",
        "languages": "understands Sylvan but can't speak",
        "cr": "2 (450 XP)",
        "traits": [
            ("Bioluminescent Glow", "The Shroomyte sheds dim light in a 10-ft. radius, which it can suppress or "
             "rekindle as a bonus action."),
            ("Fungal Resilience", "Advantage on saves against being charmed, frightened, or stunned."),
        ],
        "actions": [
            ("Multiattack", "One Spore Blast and one Mycelium Tendrils."),
            ("Spore Blast", "*Ranged Spell Attack:* +4 to hit, range 30 ft. *Hit:* 9 (2d6 + 2) poison, and the "
             "target must succeed on a DC 13 Constitution save or be poisoned until end of its next turn."),
            ("Mycelium Tendrils", "*Melee Weapon Attack:* +4 to hit, reach 10 ft. *Hit:* 7 (2d4 + 2) bludgeoning, "
             "and a DC 13 Strength save or restrained until end of its next turn."),
        ],
        "reactions": [
            ("Fungal Retribution", "When a creature within 5 ft. hits it in melee, the Shroomyte bursts spores; "
             "the attacker makes a DC 13 Constitution save or takes 5 (2d4) poison."),
        ],
    }),

    # ==================================================================
    ("h1", "Session 4: The Longest Night of Havenmoor", {"pagebreak": True}),
    ("body", "*A whole winter court had risen with the Krampusshade. These are the dangers that stalked "
             "the frozen roads of Havenmoor, and the fiend that ruled them.*"),

    ("statblock", {
        "name": "The Krampusshade",
        "type": "Large fiend, chaotic evil",
        "img": "assets/monsters/krampusshade.png", "img_w": 2.8,
        "ac": "15 (natural armor)", "hp": "102 (12d10 + 36)", "speed": "40 ft.",
        "abilities": ab(18, 14, 16, 12, 14, 17),
        "saves": "Wis +5, Cha +6",
        "resistances": "cold, necrotic; bludgeoning, piercing, and slashing from nonmagical attacks",
        "immunities": "poison",
        "condition_immunities": "charmed, frightened, poisoned",
        "senses": "darkvision 120 ft., passive Perception 14",
        "languages": "Abyssal, Common, Infernal",
        "cr": "5 (1,800 XP)",
        "actions": [
            ("Multiattack", "One Claw and one Chains of Despair."),
            ("Claw", "*Melee Weapon Attack:* +7 to hit, reach 10 ft., one target. *Hit:* 12 (2d6 + 4) slashing "
             "plus 5 (1d10) cold."),
            ("Chains of Despair", "*Melee Weapon Attack:* +7 to hit, reach 15 ft., one target. *Hit:* 11 (2d6 + 4) "
             "bludgeoning, and a DC 14 Strength save or restrained until end of its next turn."),
            ("Gift of Despair (Recharge 5-6)", "It hurls a cursed gift box at a target within 30 ft.; DC 14 Wisdom "
             "save or frightened for 1 minute (repeat save at end of each turn)."),
        ],
        "reactions": [
            ("Icy Retaliation", "When hit by a melee attack, the attacker makes a DC 14 Constitution save or takes "
             "7 (2d6) cold and has its speed reduced by 10 ft. until end of its next turn."),
        ],
        "legendary": [
            ("Shadow Step", "The Krampusshade teleports up to 20 ft. to an unoccupied space in dim light or "
             "darkness. (Rung together, the eight Winter Bells strip away its power.)"),
        ],
    }),

    ("statblock", {
        "name": "Krampus's Imp",
        "type": "Small fiend (shadow), chaotic evil",
        "img": "assets/monsters/krampus_imp.png", "img_w": 2.4,
        "ac": "14 (natural armor)", "hp": "22 (5d6 + 5)", "speed": "30 ft., fly 40 ft.",
        "abilities": ab(10, 16, 12, 13, 11, 14),
        "skills": "Stealth +6, Deception +4",
        "resistances": "cold, fire, necrotic; bludgeoning, piercing, slashing from nonmagical attacks",
        "immunities": "poison",
        "condition_immunities": "poisoned",
        "senses": "darkvision 120 ft., passive Perception 10",
        "languages": "Infernal, Common",
        "cr": "2 (450 XP)",
        "traits": [
            ("Shadow Stealth", "Can Hide as a bonus action in dim light or darkness."),
            ("Invisibility (3/short rest)", "Turns invisible as a bonus action until it attacks or casts a spell."),
            ("Magic Resistance", "Advantage on saves against spells and magical effects."),
            ("Shadow Glide", "Can move through creatures' spaces in dim light or darkness."),
        ],
        "actions": [
            ("Shadow Claws", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 8 (2d4 + 3) slashing plus 3 (1d6) cold."),
            ("Shadowy Grasp (Recharge 5-6)", "A target makes a DC 13 Dexterity save or is restrained until end of "
             "the imp's next turn, taking 5 (1d10) cold at the start of each of its turns while restrained."),
        ],
    }),
    ("body", "*The gift-box mimics were true **Mimics** (CR 2, AC 12, HP 58): a shapechanging monstrosity that "
             "adheres to whatever touches it, biting for 1d8 + 3 piercing plus 1d8 acid.*"),

    ("statblock", {
        "name": "Frozen Wolf",
        "type": "Medium beast, neutral evil",
        "img": "assets/monsters/frozen_wolf.png", "img_w": 2.6,
        "ac": "15 (natural armor)", "hp": "45 (6d10 + 12)", "speed": "40 ft.",
        "abilities": ab(16, 15, 14, 3, 12, 6),
        "immunities": "cold",
        "senses": "darkvision 60 ft., passive Perception 14",
        "languages": "understands Sylvan but cannot speak",
        "traits": [
            ("Pack Tactics", "Advantage on attacks against a creature if an ally is within 5 ft. of it and not incapacitated."),
            ("Icy Terrain", "The ground within 10 ft. of the wolf is difficult terrain for other creatures."),
        ],
        "actions": [
            ("Bite", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 12 (2d6 + 3) piercing plus 4 (1d8) cold, "
             "and a DC 13 Constitution save or speed reduced by 10 ft. until end of its next turn."),
            ("Frost Breath (Recharge 5-6)", "A 15-ft. cone of icy air. Each creature makes a DC 13 Dexterity save, "
             "taking 18 (4d8) cold on a fail (half on a success); those who fail are slowed until end of next turn."),
        ],
    }),
    ("statblock", {
        "name": "Frostbite Pixie",
        "type": "Tiny fey, chaotic neutral",
        "img": "assets/monsters/frostbite_pixie.png", "img_w": 2.4,
        "ac": "15", "hp": "14 (4d4 + 4)", "speed": "20 ft., fly 60 ft.",
        "abilities": ab(3, 20, 12, 14, 11, 16),
        "skills": "Stealth +7",
        "immunities": "cold",
        "languages": "Sylvan, Common",
        "cr": "1/4 (50 XP)",
        "actions": [
            ("Ray of Frost", "*Ranged Spell Attack:* +5 to hit, range 60 ft. *Hit:* 7 (2d8) cold, and the target's "
             "speed is reduced by 10 ft. until end of its next turn."),
            ("Invisibility", "The pixie turns invisible until it attacks or casts a spell."),
        ],
    }),
    ("statblock", {
        "name": "Icy Specter",
        "type": "Medium undead, neutral evil",
        "img": "assets/monsters/icy_specter.png", "img_w": 2.6,
        "ac": "12", "hp": "45 (10d8)", "speed": "0 ft., fly 50 ft. (hover)",
        "abilities": ab(1, 14, 11, 10, 10, 16),
        "resistances": "cold, necrotic; bludgeoning, piercing, and slashing from nonmagical attacks",
        "immunities": "poison",
        "condition_immunities": "charmed, exhaustion, grappled, paralyzed, poisoned, prone, restrained",
        "actions": [
            ("Chilling Touch", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 10 (3d6) cold."),
            ("Wail of Despair (Recharge 5-6)", "Each creature within 30 ft. makes a DC 14 Wisdom save or is "
             "frightened for 1 minute (repeat save at end of each turn)."),
        ],
    }),
    ("statblock", {
        "name": "Frost Golem",
        "type": "Medium elemental, neutral",
        "img": "assets/monsters/frost_golems.png", "img_w": 3.0,
        "ac": "14 (natural armor)", "hp": "42 (5d10 + 15)", "speed": "20 ft.",
        "abilities": ab(16, 10, 16, 6, 10, 5),
        "resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks",
        "condition_immunities": "exhaustion, poisoned",
        "cr": "2 (450 XP)",
        "traits": [
            ("Frost Aura", "At the start of each creature's turn within 5 ft. of the golem, that creature takes 2 cold."),
        ],
        "actions": [
            ("Icy Slam", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 7 (2d6 + 3) bludgeoning plus 3 (1d4) cold."),
        ],
    }),
    ("statblock", {
        "name": "Enchanted Snowman",
        "img": "assets/monsters/enchanted_snowman.png",
        "type": "Small construct, unaligned",
        "ac": "13", "hp": "30 (4d8 + 12)", "speed": "20 ft.",
        "abilities": ab(12, 10, 16, 3, 10, 6),
        "cr": "1 (200 XP)",
        "actions": [
            ("Frostball", "*Ranged Weapon Attack:* +4 to hit. *Hit:* 2d4 cold, and a DC 12 Constitution save or "
             "speed halved until end of its next turn."),
        ],
    }),
    ("statblock", {
        "name": "Yule Cat",
        "type": "Large fey beast, neutral",
        "img": "assets/monsters/yule_cat.png", "img_w": 3.0,
        "ac": "15 (natural armor)", "hp": "52 (7d10 + 14)", "speed": "40 ft., climb 30 ft.",
        "abilities": ab(18, 16, 14, 6, 14, 10),
        "skills": "Perception +4, Stealth +6",
        "resistances": "cold",
        "senses": "darkvision 60 ft., passive Perception 14",
        "cr": "3 (700 XP)",
        "actions": [
            ("Frost Claw", "*Melee Weapon Attack:* +6 to hit, reach 5 ft. *Hit:* 10 (2d6 + 3) slashing plus 3 (1d6) cold."),
            ("Frostbite Pounce", "If the Yule Cat moves 20 ft. and hits with Frost Claw, the target makes a DC 14 "
             "Strength save or is knocked prone; if prone, the cat makes another Frost Claw as a bonus action."),
            ("Chilling Gaze (Recharge 5-6)", "One target within 30 ft. makes a DC 14 Constitution save or takes "
             "9 (2d8) cold and is paralyzed until end of its next turn."),
        ],
    }),
    ("statblock", {
        "name": "Frost Hag (disguised)",
        "type": "Medium fey, neutral evil",
        "img": "assets/monsters/frost_hag_disguised.png", "img_w": 2.6,
        "ac": "15", "hp": "52", "speed": "30 ft.",
        "abilities": ab(14, 14, 14, 13, 12, 14),
        "cr": "4 (1,100 XP)",
        "traits": [
            ("Kindly Guise", "The hag appears as a sweet old woman offering sugared pastries; those who eat them "
             "make a DC 13 Constitution save or are poisoned for 1 hour, taking 1d4 cold."),
        ],
        "actions": [
            ("Icy Claw", "*Melee Weapon Attack:* +6 to hit, reach 5 ft. *Hit:* 10 (2d6 + 3) slashing plus 4 (1d6) cold."),
            ("Frostbite Breath (Recharge 5-6)", "A 15-ft. cone; DC 14 Constitution save, 16 (4d6) cold (half on a "
             "success); on a fail the target is slowed until its next turn."),
            ("Misty Step (Bonus Action)", "The hag teleports 30 ft."),
        ],
    }),
    ("statblock", {
        "name": "Ice Spider",
        "img": "assets/monsters/ice_spider.png",
        "type": "Medium beast, unaligned",
        "ac": "14 (natural armor)", "hp": "26 (4d10 + 4)", "speed": "30 ft., climb 30 ft.",
        "abilities": ab(12, 14, 12, 2, 11, 4),
        "cr": "1 (200 XP)",
        "actions": [
            ("Bite", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 9 (1d8 + 1) piercing plus 4 (1d6) cold, "
             "and a DC 13 Constitution save or poisoned for 1 minute."),
            ("Web (Recharge 5-6)", "*Ranged Weapon Attack:* +4 to hit, range 30 ft. On a hit the target is "
             "restrained by webbing (DC 13 Strength to escape)."),
        ],
    }),
    ("statblock", {
        "name": "Frozen Will-o'-Wisp",
        "type": "Tiny undead, chaotic evil",
        "img": "assets/monsters/frozen_will_o_wisps.png", "img_w": 2.4,
        "ac": "15", "hp": "22 (5d8)", "speed": "0 ft., fly 50 ft. (hover)",
        "abilities": ab(1, 18, 10, 10, 12, 11),
        "resistances": "cold, lightning; bludgeoning, piercing, and slashing from nonmagical attacks",
        "immunities": "poison",
        "condition_immunities": "exhaustion, grappled, paralyzed, prone",
        "cr": "2 (450 XP)",
        "actions": [
            ("Icy Shock", "*Melee Spell Attack:* +5 to hit, reach 5 ft. *Hit:* 9 (2d8) lightning plus 4 (1d6) cold."),
            ("Invisibility", "The wisp turns invisible until it attacks."),
        ],
    }),
    ("statblock", {
        "name": "Snowbound Bandit Leader",
        "type": "Medium humanoid, neutral",
        "img": "assets/monsters/snowbound_bandits.png", "img_w": 3.2,
        "ac": "14", "hp": "32", "speed": "30 ft.",
        "abilities": ab(14, 13, 12, 10, 11, 11),
        "traits": [
            ("Desperate, Not Cruel", "Driven mad by the cold; kindness (food, warmth) or a DC 14 Intimidation "
             "check can end the fight before it begins."),
        ],
        "actions": [
            ("Scimitar", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 7 (1d6 + 3) slashing."),
            ("Dagger", "*Melee or Ranged Weapon Attack:* +5 to hit. *Hit:* 5 (1d4 + 3) piercing."),
            ("Frostbite Strike (Recharge 5-6)", "+5 to hit; an extra 1d6 cold, and a DC 13 Constitution save or "
             "speed reduced by 10 ft. until its next turn."),
        ],
    }),
    ("body", "*Ordinary **Snowbound Bandits** fought alongside their leader (AC 12, HP 20). Kinder meetings "
             "walked the same roads: a resting reindeer whose glowing nose blessed kind travelers, a friendly "
             "caribou that healed the weary, and Aurora Spirits, gentle messengers of Elaria who traded a "
             "prophecy for a moment's respect.*"),

    # ==================================================================
    ("h1", "Session 5: The Flying Dutchman", {"pagebreak": True}),
    ("body", "*Aboard the ghost-ship of Davy Jones the party fought a drowned crew of smugglers and "
             "spirits, all of them (like the Captain) undone by cold and by the sea taking back its own.*"),

    ("statblock", {
        "name": "Davy Jones, Captain of the Flying Dutchman",
        "img": "assets/npcs/davy_jones.png",
        "type": "Medium undead (formerly humanoid), chaotic evil",
        "ac": "17 (barnacle armor)", "hp": "85 (10d10 + 30)", "speed": "30 ft., swim 30 ft.",
        "abilities": ab(18, 12, 16, 14, 12, 16),
        "saves": "Con +6, Wis +4, Cha +6",
        "skills": "Intimidation +6, Perception +4, Athletics +7, Survival +4",
        "resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "condition_immunities": "charmed, frightened, poisoned, exhaustion",
        "senses": "darkvision 60 ft., passive Perception 14",
        "languages": "Common, Aquan",
        "cr": "6 (2,300 XP)",
        "traits": [
            ("Barnacle Armor", "Nonmagical melee attacks against him deal half damage."),
            ("Legendary Resistance (3/Day)", "If Davy fails a save, he can choose to succeed instead."),
            ("Amphibious", "He can breathe air and water."),
        ],
        "actions": [
            ("Multiattack", "Two Tentacle Slams and one Hook Strike."),
            ("Tentacle Slam", "*Melee Weapon Attack:* +7 to hit, reach 10 ft. *Hit:* 10 (2d6 + 4) bludgeoning, and "
             "the target is grappled (escape DC 15)."),
            ("Hook Strike", "*Melee Weapon Attack:* +7 to hit, reach 5 ft. *Hit:* 8 (1d6 + 4) piercing plus 7 (2d6) necrotic."),
            ("Soul Siphon (Recharge 5-6)", "One creature makes a DC 14 Constitution save or takes 18 (4d8) psychic; "
             "Davy heals half the damage dealt."),
        ],
        "legendary": [
            ("Tentacle Strike", "Davy makes one Tentacle Slam."),
            ("Raise Tide (2 actions)", "A 20-ft. line; DC 14 Dexterity save or 13 (3d8) bludgeoning."),
        ],
    }),

    ("statblock", {
        "name": "Drowned Pirate",
        "img": "assets/monsters/drowned_pirate.png",
        "type": "Medium undead, chaotic evil",
        "ac": "14 (studded leather or chain shirt)", "hp": "58 (9d8 + 18)", "speed": "30 ft., swim 30 ft.",
        "abilities": ab(18, 14, 14, 6, 10, 7),
        "saves": "Wis +2",
        "skills": "Perception +2",
        "resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "immunities": "poison",
        "condition_immunities": "charmed, exhaustion, frightened, paralyzed, poisoned",
        "senses": "darkvision 60 ft., passive Perception 12",
        "languages": "understands Common but can't speak",
        "cr": "1 (200 XP)",
        "traits": [
            ("Amphibious", "The pirate can breathe air and water."),
            ("Undead Fortitude", "If reduced to 0 HP (not by radiant or a crit), a DC 5 + damage Constitution save "
             "drops it to 1 HP instead."),
        ],
        "actions": [
            ("Multiattack", "Two melee attacks."),
            ("Cutlass", "*Melee Weapon Attack:* +6 to hit, reach 5 ft. *Hit:* 8 (1d8 + 4) slashing."),
            ("Harpoon", "*Melee or Ranged Weapon Attack:* +6 to hit, reach 10 ft. or range 30/120 ft. *Hit:* "
             "9 (1d10 + 4) piercing, and the target is grappled (escape DC 14)."),
        ],
        "reactions": [
            ("Death Burst", "When the pirate dies it bursts; each creature within 5 ft. makes a DC 12 Constitution "
             "save or takes 5 (2d4) cold and gains one level of exhaustion."),
        ],
    }),
    ("statblock", {
        "name": "Spectral Helmsman",
        "img": "assets/monsters/spectral_helmsman.png",
        "type": "Medium undead, chaotic evil",
        "ac": "12", "hp": "45 (6d8 + 18)", "speed": "0 ft., fly 50 ft. (hover)",
        "abilities": ab(6, 14, 16, 10, 12, 11),
        "saves": "Wis +3, Cha +2",
        "skills": "Perception +3, Stealth +4",
        "resistances": "acid, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks",
        "immunities": "cold, necrotic, poison",
        "condition_immunities": "charmed, exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained",
        "senses": "darkvision 60 ft., passive Perception 13",
        "languages": "understands Common but can't speak",
        "cr": "1 (200 XP)",
        "traits": [
            ("Incorporeal Movement", "Can move through creatures and objects as difficult terrain."),
            ("Sea-Wraith Aura", "At the start of each of its turns, creatures within 5 ft. make a DC 12 Wisdom save "
             "or are frightened until their next turn."),
        ],
        "actions": [
            ("Multiattack", "Two Spectral Scimitar attacks."),
            ("Spectral Scimitar", "*Melee Weapon Attack:* +4 to hit, reach 5 ft. *Hit:* 7 (1d6 + 4) force."),
            ("Harpoon Throw", "*Ranged Weapon Attack:* +4 to hit, range 20/60 ft. *Hit:* 9 (1d10 + 4) piercing and "
             "the target is pulled up to 10 ft."),
        ],
        "reactions": [
            ("Phantom Helm Block", "When attacked, it imposes disadvantage on one weapon attack roll."),
        ],
    }),
    ("statblock", {
        "name": "Smuggler's Golem",
        "img": "assets/monsters/smugglers_golem.png",
        "type": "Large construct, unaligned",
        "ac": "14 (natural armor)", "hp": "85 (10d10 + 30)", "speed": "30 ft.",
        "abilities": ab(19, 9, 16, 3, 10, 5),
        "resistances": "fire, lightning, acid",
        "immunities": "poison, psychic; bludgeoning, piercing, and slashing from nonmagical attacks",
        "vulnerabilities": "cold",
        "condition_immunities": "charmed, exhaustion, frightened, paralyzed, petrified, poisoned, prone",
        "senses": "darkvision 60 ft., tremorsense 30 ft., passive Perception 10",
        "languages": "understands the commands of its creator but can't speak",
        "cr": "2 (450 XP)",
        "traits": [
            ("Immutable Form", "Immune to effects that would alter its form."),
            ("Magic Resistance", "Advantage on saves against spells."),
            ("Siege Monster", "Deals double damage to objects."),
        ],
        "actions": [
            ("Multiattack", "Two Slam attacks."),
            ("Slam", "*Melee Weapon Attack:* +7 to hit, reach 10 ft. *Hit:* 2d8 + 5 bludgeoning."),
            ("Crush Crate (Recharge 5-6)", "One object or creature takes 6d6 (DC 15 Dexterity save for half); a "
             "creature that fails is knocked prone."),
        ],
        "reactions": [
            ("Reinforced Hide", "+2 AC against one melee attack."),
        ],
    }),
    ("statblock", {
        "name": "Arcane Corsair",
        "img": "assets/monsters/arcane_corsair.png",
        "type": "Medium humanoid, chaotic neutral",
        "ac": "14 (studded leather)", "hp": "52 (7d8 + 21)", "speed": "30 ft.",
        "abilities": ab(16, 16, 16, 12, 11, 14),
        "saves": "Dex +5, Cha +4",
        "skills": "Acrobatics +5, Perception +2",
        "resistances": "fire, lightning",
        "vulnerabilities": "cold",
        "condition_immunities": "frightened",
        "languages": "Common, Thieves' Cant",
        "cr": "1 (200 XP)",
        "traits": [
            ("Sneak Attack (1/turn)", "+2d6 damage when it has advantage or an ally is adjacent to the target."),
            ("Parry", "+2 AC against one melee attack."),
        ],
        "actions": [
            ("Multiattack", "Two Arcane Saber attacks."),
            ("Arcane Saber", "*Melee Weapon Attack:* +5 to hit. *Hit:* 1d8 + 3 slashing plus 1d6 force."),
            ("Riposte (Recharge 5-6)", "A reaction attack after an enemy misses it in melee."),
        ],
        "reactions": [
            ("Evasive Step", "It Disengages, moving without provoking opportunity attacks."),
        ],
    }),
    ("statblock", {
        "name": "Ghost-Light Engineer",
        "img": "assets/monsters/ghost_light_engineer.png",
        "type": "Tiny undead, neutral evil",
        "ac": "15 (natural armor)", "hp": "27 (6d4 + 12)", "speed": "0 ft., fly 50 ft. (hover)",
        "abilities": ab(1, 18, 14, 12, 14, 16),
        "saves": "Wis +4, Cha +5",
        "skills": "Arcana +3, Perception +4, Stealth +8",
        "resistances": "acid, fire, lightning, thunder; bludgeoning, piercing, slashing from nonmagical attacks",
        "immunities": "necrotic, poison, psychic",
        "vulnerabilities": "cold",
        "condition_immunities": "charmed, exhaustion, frightened, grappled, paralyzed, petrified, poisoned, prone, restrained",
        "senses": "darkvision 60 ft., passive Perception 14",
        "languages": "Common, its creator's languages",
        "cr": "2 (450 XP)",
        "traits": [
            ("Invisibility (Recharge 4-6)", "Turns invisible until it attacks, casts, or its concentration ends."),
            ("Glowing Core", "A faint glow is visible within 5 ft. even while invisible."),
        ],
        "actions": [
            ("Shock Touch", "*Melee Spell Attack:* +6 to hit. *Hit:* 2d6 + 2 lightning."),
            ("Arcane Pulse (Recharge 5-6)", "A 10-ft. cone; DC 13 Dexterity save, 4d6 force (half on a success)."),
        ],
        "reactions": [
            ("Engineered Reflexes", "Halves the damage from one attack or harmful spell."),
        ],
    }),

    # ==================================================================
    ("h1", "Session 6: The False Hydra of Wraithpine", {"pagebreak": True}),
    ("body", "*The worst monster the Guardians ever faced, because no one knew it was there. Beneath the "
             "Old Theater of Wraithpine, its endless song made the whole village forget the people it took. "
             "Beeswax in the ears let the truth through.*"),

    ("statblock", {
        "name": "False Hydra: Tavern Head",
        "type": "Large aberration (one head and neck), unaligned",
        "img": "assets/monsters/false_hydra.png", "img_w": 3.0,
        "ac": "14", "hp": "70 (9d10 + 18)", "speed": "10 ft., climb 10 ft.",
        "abilities": ab(16, 12, 14, 6, 14, 7),
        "resistances": "psychic",
        "condition_immunities": "charmed, frightened, prone",
        "senses": "blindsight 10 ft., tremorsense 30 ft., darkvision 60 ft., passive Perception 14",
        "traits": [
            ("Mind-Humming Aura", "Creatures without beeswax that start their turn within 30 ft. make a DC 13 "
             "Wisdom save or have disadvantage on attack rolls that turn. Beeswax grants advantage on the save."),
            ("Segmented Neck", "The head ignores forced movement and prone unless it chooses otherwise. When it "
             "takes 20+ damage in a turn, it recoils 5 ft. (no opportunity attacks) and can't take reactions "
             "until the start of its next turn."),
        ],
        "actions": [
            ("Bite", "*Melee Weapon Attack:* +6 to hit, reach 10 ft. *Hit:* 13 (2d8 + 4) piercing, and the target "
             "is grappled (escape DC 14). While grappling it can't bite a different target."),
            ("Lurch & Drag", "A grappled target is dragged 5 ft. toward the trapdoor and, on a failed DC 13 Wisdom "
             "save, loses a word or thought for a heartbeat."),
        ],
        "reactions": [
            ("Recoil from Flame", "When it takes fire damage, it has disadvantage on its next attack."),
        ],
    }),

    ("pagebreak",),
    ("body", "*Deeper still, in the drowned orchestra pit, waited the true body and its four heads, all "
             "singing as one. The moment the song stopped, every stolen name came flooding home.*"),
    ("statblock", {
        "name": "False Hydra (Adult): Body",
        "img": "assets/monsters/false_hydra_body.png",
        "type": "Huge aberration, unaligned",
        "ac": "15", "hp": "130 (12d12 + 48)", "speed": "10 ft., climb 10 ft.",
        "abilities": ab(18, 10, 18, 7, 14, 8),
        "saves": "Con +8, Wis +5",
        "resistances": "psychic",
        "condition_immunities": "charmed, frightened, prone",
        "senses": "tremorsense 60 ft., darkvision 60 ft., blindsight 10 ft., passive Perception 12",
        "traits": [
            ("Song of Unremembering", "While any head lives, creatures without earplugs that start their turn "
             "within 60 ft. make a DC 15 Wisdom save or have disadvantage on attacks and can't take reactions "
             "until their next turn. Beeswax grants advantage and no reaction-lock."),
            ("Many-Minds", "For each head alive, the body has 1 Legendary Action (max 3 per round)."),
            ("Vital Link", "While at least one head lives, the body has resistance to all weapon damage; each head "
             "destroyed removes one instance of this protection."),
        ],
        "actions": [
            ("Thrash", "*Melee Weapon Attack:* +7 to hit, reach 10 ft. *Hit:* 13 (2d8 + 4) bludgeoning."),
            ("Regurgitate Remnants (Recharge 5-6)", "A 15-ft. cone of bone and cloth; DC 14 Dexterity save, 13 "
             "(3d8) necrotic and slowed (speed -10) until end of next turn. A shattered skull and ribbon clatter free."),
        ],
        "legendary": [
            ("Hum Surge", "One creature within 60 ft. (no earplugs) makes a DC 15 Wisdom save or loses "
             "concentration and can move only 10 ft. on its next turn."),
            ("Bone Shift", "Move the body 5 ft. and reshape a 10-ft. square within 20 ft. into (or out of) "
             "difficult terrain."),
            ("Coordinate Strike", "One head makes a Snap."),
        ],
    }),
    ("statblock", {
        "name": "False Hydra Head (x4)",
        "img": "assets/monsters/false_hydra_head.png",
        "type": "Large aberration (an extension of the body), unaligned",
        "ac": "14", "hp": "45 (6d10 + 12)", "speed": "30 ft. (platforms, tunnels), climb 20 ft.",
        "abilities": ab(16, 12, 14, 6, 14, 7),
        "saves": "Wis +4",
        "resistances": "psychic",
        "condition_immunities": "charmed, frightened, prone",
        "actions": [
            ("Bite", "*Melee Weapon Attack:* +7 to hit, reach 15 ft. *Hit:* 14 (2d10 + 3) piercing and grappled "
             "(escape DC 14). While grappling it can't bite a different target."),
            ("Reel", "A creature grappled by the head makes a DC 14 Strength save or is pulled 10 ft. toward the "
             "port and knocked prone."),
        ],
        "reactions": [
            ("Snap", "When a creature moves within 15 ft., the head makes one Bite against it."),
        ],
    }),

    ("body", "**Festival frights.** *Before the theater, the hydra's hungry song had stirred lesser echoes "
             "all over Wraithpine: animated Scarecrows and rustling Strawlings on Pumpkin Row, rats and rat "
             "swarms in Maera's cellar, and restless Zombies (and, if things went loud, Skeletons) at the "
             "graveyard rite.*"),
    ("statblock", {
        "name": "Animated Scarecrow",
        "img": "assets/monsters/scarecrow.png",
        "type": "Medium construct, neutral",
        "ac": "11", "hp": "36 (8d8)", "speed": "30 ft.",
        "abilities": ab(16, 12, 11, 10, 10, 10),
        "vulnerabilities": "fire",
        "resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "condition_immunities": "charmed, frightened, paralyzed, poisoned",
        "senses": "darkvision 60 ft., passive Perception 10",
        "languages": "understands its creator's languages but can't speak",
        "cr": "1 (200 XP)",
        "traits": [
            ("Terrifying Glare", "One creature within 30 ft. must succeed on a DC 11 Wisdom save or be frightened "
             "for 1 minute (repeat save at end of each turn)."),
            ("Heart-Gourd", "A coin-sized gourd charm is sewn under its ribs; snipping it (an action within 5 ft., "
             "no roll) makes the scarecrow fall limp."),
        ],
        "actions": [
            ("Claw", "*Melee Weapon Attack:* two claws, +5 to hit, reach 5 ft. *Hit:* 6 (2d4 + 1) slashing."),
        ],
    }),
    ("statblock", {
        "name": "Strawling",
        "img": "assets/monsters/strawling.png",
        "type": "Medium plant, neutral",
        "ac": "12", "hp": "11 (2d8 + 2)", "speed": "30 ft.",
        "abilities": ab(12, 12, 12, 4, 10, 3),
        "senses": "passive Perception 10",
        "cr": "1/4 (50 XP)",
        "actions": [
            ("Needles", "*Melee or Ranged Weapon Attack:* a bristle of straw-needles; easily bowled over by a "
             "hay cart or a kicked pumpkin stack."),
        ],
    }),
    ("body", "*The cellar vermin were ordinary **Rats** (AC 12, HP 7, CR 1/8) and a **Swarm of Rats** (AC 10, "
             "HP 24, CR 1/4). The graveyard undead were standard **Zombies** (AC 8, HP 22, CR 1/4; Undead "
             "Fortitude) and, only if the rite went loud, **Skeletons** (AC 13, HP 13, CR 1/4).*"),

    # ==================================================================
    ("h1", "Session 7: Gearhaven, the Clockwork City", {"pagebreak": True}),
    ("body", "*In the clockwork city, the enemy was no monster at all but corruption bleeding up through "
             "the cracks, reaching INTO the machines the people loved. Note the rotation: the lightning "
             "eaters and the fire eaters trade off. Freed, not killed: these were innocents.*"),

    ("statblock", {
        "name": "Rogue Servitor",
        "type": "Small construct, unaligned",
        "img": "assets/session_08/beat_2/rogue_servitor.png", "img_w": 2.5,
        "ac": "15", "hp": "39 (6d6 + 18)", "speed": "30 ft.",
        "abilities": ab(13, 16, 16, 3, 8, 5),
        "resistances": "poison; bludgeoning, piercing, and slashing from nonmagical attacks",
        "condition_immunities": "charmed, frightened, poisoned, exhaustion",
        "senses": "darkvision 60 ft.",
        "cr": "2",
        "traits": [
            ("Overclocked Death-Spark", "At 0 HP, each creature within 10 ft. makes a DC 13 Dexterity save or "
             "takes 7 (2d6) lightning."),
            ("Shutdown Switch", "An action within 5 ft. plus a DC 14 Arcana or Sleight of Hand check shuts it "
             "down instantly, no kill needed."),
        ],
        "actions": [
            ("Multiattack", "Two Flailing Slams."),
            ("Flailing Slam", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 8 (1d10 + 3) bludgeoning."),
            ("Spark Lash (Recharge 5-6)", "*Ranged Attack:* +5 to hit, range 30 ft. *Hit:* 10 (3d6) lightning; "
             "the target's speed is halved until end of its next turn."),
        ],
    }),
    ("statblock", {
        "name": "Cargo Hauler",
        "type": "Large construct, unaligned",
        "img": "assets/session_08/beat_2/cargo_hauler.png", "img_w": 2.8,
        "ac": "16", "hp": "76 (8d10 + 32)", "speed": "30 ft.",
        "abilities": ab(19, 8, 18, 3, 8, 5),
        "resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "vulnerabilities": "lightning (overloaded core; telegraph the crackling blue!)",
        "condition_immunities": "charmed, exhaustion, frightened, paralyzed, petrified, poisoned",
        "cr": "3",
        "traits": [
            ("Out-of-Reach Switch", "Its shutdown lever is 15 ft. up on its back; reaching it (climb DC 13 or "
             "flight) plus an action and a DC 15 Arcana or Sleight of Hand check disables it."),
        ],
        "actions": [
            ("Multiattack", "Two Forklift Slams, or one Slam and one Hurl Crate."),
            ("Forklift Slam", "*Melee Weapon Attack:* +6 to hit, reach 10 ft. *Hit:* 13 (2d8 + 4) bludgeoning, "
             "and a DC 14 Strength save or knocked prone."),
            ("Hurl Crate", "*Ranged Weapon Attack:* +6 to hit, range 60 ft. *Hit:* 14 (3d6 + 4) bludgeoning."),
            ("Grab & Crush (Recharge 5-6)", "One creature within 10 ft. makes a DC 14 Dexterity save or is "
             "grappled (escape DC 14), taking 10 (3d6) at the start of each of its turns until it escapes."),
        ],
    }),
    ("statblock", {
        "name": "Voltcrawler",
        "type": "Small aberration (planar intruder), unaligned",
        "img": "assets/session_08/beat_4/volt_crawler.png", "img_w": 2.5,
        "ac": "15", "hp": "22 (5d6 + 5)", "speed": "30 ft., climb 30 ft.",
        "abilities": ab(7, 17, 13, 5, 10, 6),
        "resistances": "lightning",
        "senses": "darkvision 60 ft.",
        "traits": [
            ("Phase-Blink", "At the start of its turn, roll a d6: on a 1-2 it goes Unreal, resisting all damage "
             "except force and radiant, and attacks against it have disadvantage; it can't be webbed or grappled "
             "and must become Real to attack. (Force and radiant are the counter.)"),
            ("Static Cling", "The first time it hits a creature each turn, that target's lightning resistance is "
             "ignored and its allies have advantage on their next attack against it."),
        ],
        "actions": [
            ("Spark Bite", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 1d6 + 3 piercing plus 1d6 lightning."),
            ("Arc (Recharge 5-6)", "A 15-ft. line; DC 13 Dexterity save, 2d8 lightning (half on a success). Two or "
             "more Voltcrawlers within 15 ft. can chain into one 3d8 line."),
        ],
    }),
    ("statblock", {
        "name": "Voltcrawler Broodmother",
        "type": "Medium aberration (planar intruder), unaligned",
        "img": "assets/session_08/beat_4/broodmother.png", "img_w": 2.8,
        "ac": "16", "hp": "95 (10d8 + 50)", "speed": "40 ft., climb 40 ft.",
        "abilities": ab(14, 18, 20, 6, 12, 8),
        "saves": "Dex +7, Con +8",
        "resistances": "lightning; bludgeoning, piercing, and slashing from nonmagical attacks",
        "senses": "darkvision 60 ft.",
        "traits": [
            ("Phase-Blink (greater)", "She chooses to go Unreal as a free action once per round (no roll)."),
            ("Crackling Web", "At the start of her turn, one creature she sees within 30 ft. makes a DC 15 "
             "Dexterity save or is restrained by planar silk (action plus DC 15 Strength to break; web AC 12, "
             "15 HP, immune lightning, VULNERABLE fire and cold)."),
        ],
        "actions": [
            ("Multiattack", "Two Lash attacks."),
            ("Lash", "*Melee Weapon Attack:* +7 to hit, reach 10 ft. *Hit:* 1d10 + 4 slashing plus 1d8 lightning."),
            ("Overcharge (Recharge 6)", "A 20-ft.-radius burst; DC 15 Constitution save, 4d8 lightning (half on a "
             "success). On a fail the target also can't take reactions until end of its next turn."),
        ],
    }),
    ("statblock", {
        "name": "Iron Drudge",
        "type": "Large construct (planar-corrupted), unaligned",
        "img": "assets/session_08/beat_5/iron_drudge.png", "img_w": 2.8,
        "ac": "17", "hp": "68 (8d10 + 24)", "speed": "25 ft.",
        "abilities": ab(19, 8, 17, 3, 8, 1),
        "vulnerabilities": "fire (corrupted wood and vine in its joints; telegraph the smoke!)",
        "resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "condition_immunities": "charmed, frightened, exhaustion, poisoned",
        "senses": "darkvision 60 ft.",
        "cr": "3",
        "traits": [
            ("Slow but Unstoppable", "Can't be knocked prone; ignores difficult terrain. It is slow enough to "
             "outrun, but it keeps coming."),
            ("Corruption Leak", "At 0 HP the blue light gutters out and it slumps, harmless. No death-burst: these "
             "were innocent worker-machines, freed rather than destroyed."),
        ],
        "actions": [
            ("Multiattack", "Two Cargo-Arm Slams."),
            ("Cargo-Arm Slam", "*Melee Weapon Attack:* +6 to hit, reach 10 ft. *Hit:* 2d8 + 4 bludgeoning."),
            ("Sweep (Recharge 5-6)", "A wide swing; each creature within 10 ft. makes a DC 14 Dexterity save, "
             "taking 2d6 + 4 bludgeoning (half on a success) and shoved 10 ft. on a fail."),
        ],
    }),
    ("statblock", {
        "name": "Corrupted Sproutling",
        "type": "Small plant (planar-corrupted), unaligned",
        "img": "assets/session_08/beat_5/corrupted_sproutling.png", "img_w": 2.4,
        "ac": "12", "hp": "7 (2d6)", "speed": "10 ft., climb 10 ft.",
        "abilities": ab(8, 14, 10, 2, 6, 4),
        "vulnerabilities": "fire",
        "senses": "darkvision 30 ft.",
        "traits": [
            ("Weak but Many", "Dies to almost any solid hit; an area effect clears several at once (reward AoE)."),
            ("Group Turn & Spawn", "All Sproutlings act together on one shared initiative. While the engine runs "
             "corrupt, a new one crawls from a crack each time one dies."),
        ],
        "actions": [
            ("Thorn-Lash", "*Melee Weapon Attack:* +4 to hit, reach 5 ft. *Hit:* 1d6 + 2 piercing."),
            ("Latch", "Instead of attacking, it grabs a hero (no damage); the next attack against that hero has advantage."),
        ],
    }),

    ("pagebreak",),
    ("body", "*And then the boss: not a monster, but the city's beloved gentle giant, possessed and "
             "grieving inside its own iron. The Guardians broke its legs to bring the core into reach, and "
             "the last blow drained the corruption away rather than killing it. A gentle death, never an execution.*"),
    ("statblock", {
        "name": "The Grand Custodian (possessed)",
        "type": "Gargantuan construct (planar-possessed), unaligned",
        "img": "assets/session_08/beat_5/grand_custodian.png", "img_w": 2.8,
        "ac": "17 (Body); Legs (x2) AC 15", "hp": "220 (Body); Legs 90 each", "speed": "30 ft.",
        "abilities": ab(24, 6, 22, 3, 10, 5),
        "resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "condition_immunities": "charmed, frightened, exhaustion, poisoned, paralyzed, petrified",
        "traits": [
            ("The Core Is High", "Standing, the core is 40-50 ft. up: only 60-ft.+ ranged attacks and flyers reach "
             "it. The legs are ground-level and anyone can strike them."),
            ("Topple", "Drop both legs (90 HP each) and it crashes to its knees (Phase 2), stops rampaging, and "
             "the core drops to 15-20 ft. within everyone's reach. It may slowly repair a leg (to 25 HP) to rise; re-topple it."),
        ],
        "actions": [
            ("Crushing Stomp", "*Melee:* +8 to hit, reach 15 ft. *Hit:* 2d10 + 5 bludgeoning, and a DC 15 Dexterity "
             "save or knocked prone. (Phases 1 and 2.)"),
            ("Sweeping Backhand (Recharge 5-6)", "(Phase 1) A 15-ft. cone; DC 15 Dexterity save, 3d8 and shoved "
             "10 ft. (half and no shove on a success)."),
            ("Corrupt Bolt", "(Phase 1) +8 to hit, range 60 ft. *Hit:* 3d8 lightning, once per round at someone hanging back."),
            ("Clockwork Barrage (Recharge 4-6)", "(Phase 2) Three projectiles, +8 each. *Hit:* 2d8 + 3 bludgeoning."),
            ("Chain Lightning Burst (Recharge 5-6)", "(Phase 2) +8 to hit, 4d8 lightning, arcing to two more within "
             "15 ft. for 2d8 (DC 15 Dexterity save for half). Meant to be ANSWERED, not to drop a hero."),
            ("Core Flare", "(Phase 2, body below half HP) Each creature within 20 ft. makes a DC 15 Constitution "
             "save or takes 2d6 force and is blinded until end of its next turn."),
        ],
    }),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    print("built", build_doc(B, "compendium/bestiary.docx"))
