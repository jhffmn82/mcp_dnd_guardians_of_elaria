# build_compendium.py
# The Guardians of Elaria: running reference volumes.
# Builds two docx files in compendium/: magic items and custom content.
# (The bestiary is built elsewhere.)
# Rebuild after each session revision; add entries as play continues.
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc

NOTE = "A running reference for The Guardians of Elaria. Updated as the chronicle grows."

def title(kicker, sub):
    return ("titlepage", "THE GUARDIANS OF ELARIA", kicker, sub, NOTE)

# ----------------------------------------------------------------------
# VOLUME: MAGIC ITEMS & RELICS
# ----------------------------------------------------------------------
I = [
    title("TREASURES & RELICS", "The Magic of the Chronicle"),
    ("gold", "Every treasure of the Guardians' road, from a mother's parting gift to the relics of "
             "a sleeping goddess. Items marked with the seven-point star are Elaria's own."),

    ("h1", "The Great Mysteries"),
    ("h2", "The Essence Sphere"),
    ("imgfloat", "assets/items/essence_sphere.png", 2.6),
    ("body", "Brass and crystal, warm as a heartbeat, made by the deep-gnome masters of Glimmerspire "
             "BEFORE the cracks ever opened (how they knew is a question nobody has answered). It "
             "holds Pikachu's sleeping spark, and it is a GATHERER: it pulls loose planar motes to "
             "itself and survives holding them, which no other vessel can. It is the missing anchor "
             "of Vane's Rift Portal, and it never leaves the party's keeping. Gained **Planar "
             "Attunement** at the Whispering Glade (advantage on Arcana concerning planar magic)."),
    ("body", "The Circle has no proper word for what the Sphere is, only what it does: it keeps. "
             "Whatever loose scrap of another world drifts past, the Sphere gathers it in and holds "
             "it steady, the way a lantern keeps a single flame out of the wind. Every other vessel "
             "the deep gnomes ever tried cracked, dimmed, or worse. This one only glows a little "
             "warmer, and waits."),
    ("lore", "The Sign of Seven Points",
     "The old tellings agree that Elaria signed her safeguards the way a mother sews a name "
     "into a coat: not so the gift would be admired, but so it could always find its way home. "
     "The seven points are said to be the seven planes she kept turning, and the leafed vine "
     "that wraps them is the world itself, holding on. When one of her gifts is near, the sign "
     "is said to warm, as if glad to be recognized."),

    ("h2", "The Three Enchanted Potatoes"),
    ("imgfloat", "assets/items/three_potatoes.png", 2.6),
    ("body", "Ash Catchum's legacy to his son: three unassuming potatoes that are anything but. The "
             "goddess named them **remnants of a shattered covenant**, safeguards bound from her own "
             "essence in the old lore (Healing, Transformation, Insight). They pulse when the world "
             "thins, a slow warm beat you feel in the palm more than hear, and they have never once "
             "spoiled, sprouted crooked, or agreed to be eaten. Their hour has not yet come, but the "
             "Circle is patient, and so, apparently, are the potatoes."),
    ("body", "Ursa carries them wrapped in a cloth his father knotted, and will not say why he trusts "
             "three root vegetables with the fate of anything. He only shrugs and says they came from "
             "Ash, and that Ash was rarely wrong about which small things turned out to matter."),
    ("lore", "The Enchanted Potatoes",
     "The Circle keeps a very old, very short list titled \"Safeguards, Probable.\" Entry "
     "nine reads: \"The traveling potatoes. Warm to the touch. Kindly disposition. Keep "
     "planting them.\" Nobody knows who wrote it. The handwriting is extremely old."),

    ("h2", "Stabby's Idol"),
    ("imgfloat", "assets/items/stabbys_doll.png", 2.2, "left"),
    ("body", "A small carved figure Stabby found tucked in his bag after Wraithpine, though nobody "
             "saw who put it there. It goes ice cold near rifts, and corruption recoils from it. It "
             "has dreams in it. That is all anyone knows, yet."),
    ("body", "Stabby will not part with it, and cannot say why. He only knows the dark feels friendlier "
             "when the idol rides in his pack, that the coldest nights on the road are the ones it warns "
             "him of, and that once, half asleep, he heard it breathing in time with him. The idol keeps "
             "its own counsel. So, for now, does he."),
    ("lore", "The Scattered Safeguards",
     "No one has ever counted the safeguards, which is the point of scattering. Some hang in "
     "plain sight in tavern rafters. Some sleep in root cellars, humble as potatoes. The old "
     "rule of the Circle is: treat every odd little thing kindly, in case it is holding up "
     "the sky."),

    ("h1", "Relics of Elaria (the Wraithpine Chest)"),
    ("body", "One half-buried chest, bound in vines of silver and root, opened by Ghostbloom's song "
             "beneath the Old Theater. Inside, three gifts, each bearing the seven-point star."),
    ("lore", "One Chest, Three Gifts",
     "The Circle teaches that the Warden never gave a gift to one hand alone. Her safeguards "
     "came in sets, they say, because a thing meant to hold up the sky is too heavy for any "
     "single pair of arms. The chest that opened to a song beneath the old theater held three "
     "gifts and one lesson: a stave for the sky, a sash for the swift, and a small bright core "
     "for the maker, and none of the three was meant to be carried without the other two."),
    ("img", "assets/items/wraithpine_chest.png", "The Wraithpine chest, bound in silver vines.", 3.4),
    ("h2", "Staff of Waking Constellations (Ursa)"),
    ("stat", "Staff of Waking Constellations", [
        "+1 quarterstaff, druidic focus. 5 charges, regain 1d4 + 1 at dawn: guiding bolt (1), faerie fire (1), moonbeam (2).",
        "**Starseed.** Once per turn, +1d4 radiant when Ursa deals radiant damage with a druid spell (house rule: druid spells only).",
        "**Starlight.** Bonus action: 10 ft. dim light; advantage on night navigation.",
        "The counter-weapon: after every great victory, one new star brightens on its haft. The enemy puts stars out; the Staff lights them.",
    ]),
    ("h2", "Sash of the Swift Current, Rewoven (Stabby)"),
    ("stat", "Sash of the Swift Current (Rewoven)", [
        "Scarlet stage-silk rewoven with theater rigging thread. +1 AC (stacks with Unarmored Defense).",
        "**Fleetstep.** +10 ft. walking speed. **Air Dance.** 1/day bonus action: fly speed equal to walking, 1 minute.",
        "**Feather Fall.** 1/day, no components. Its star sigil is cupped by a pair of wings.",
    ]),
    ("h2", "Glimmerspire Pocket Dynamo, Mk II (Lilly)"),
    ("stat", "Glimmerspire Pocket Dynamo (Mk II)", [
        "A thumb-sized brass core stamped PROP ROOM in stage-engraver script (a mystery unexplained).",
        "**Pocket Arsenal.** Deploy or recall the Eldritch Cannon as a free action. **Endurance Overhaul.** Cannon lasts 24 hours.",
        "**Power Sync.** Cannon deals +2 damage. **Reformat.** 1/long rest, action: change the cannon's model.",
        "Near Ghostbloom, the core glows soft ghost-green, like a stage cue waiting for its moment.",
    ]),
    # The three relics share one gallery row instead of stacking dead space.
    ("imgrow", [("assets/items/staff_of_waking_constellations.png",
                 "The Staff of Waking Constellations."),
                ("assets/items/sash_of_the_swift_current.png",
                 "The Sash of the Swift Current, rewoven."),
                ("assets/characters/lilly_with_dynamo.png",
                 "Lilly with the Pocket Dynamo.")], 2.05),

    ("h1", "Gifts of Faelan (Havenmoor, Session 4)"),
    ("h2", "Frostbite Shard Dagger (Lilly)"),
    ("stat", "Frostbite Shard Dagger", [
        "Rare, attunement by an Artificer. Crystalline ice that never melts. 1d4 piercing + 1d4 cold, +1 to attack.",
        "**Spell focus and Arcane Firearm.** +1d8 frost to one spell damage roll cast through it; +2 frost on spell damage.",
    ]),
    ("h2", "Amulet of Guiding Light (Ursa)"),
    ("stat", "Amulet of Guiding Light", [
        "Rare, attunement by a Circle of Stars druid.",
        "**Guiding Light.** Sheds light; allies gain +1 to attacks and saves while Ursa is in Starry Form.",
        "**Starry Glow.** Reaction, 1/long rest: 2d8 radiant, DC 15 Con or blinded. **Celestial Resilience.** Reroll natural 1s, 2/long rest.",
    ]),
    ("h2", "Candyfang Katana (Stabby)"),
    ("stat", "Candyfang Katana", [
        "Rare, attunement by a Monk. A katana of impossible candy-cane steel. 1d8/1d10 slashing, +1 attack and damage.",
        "**Sugar Rush.** Bonus action lick, 1/long rest: 2d8 + Con temporary HP. **Frostbite Infusion.** +2 frost on hit.",
        "Destined to become a Bloodfang heirloom when the Nichirin blade comes.",
    ]),
    # The three gifts share one gallery row instead of stacking dead space.
    ("imgrow", [("assets/items/frostbite_shard_dagger.png",
                 "The Frostbite Shard Dagger."),
                ("assets/items/amulet_of_guiding_light.png",
                 "The Amulet of Guiding Light."),
                ("assets/items/candyfang_katana.png",
                 "The Candyfang Katana.")], 2.05),

    ("h1", "Boons, Baubles & Blessings"),
    ("imgfloat", "assets/items/carol_rune_tablet.png", 2.0),
    ("body", "**Elaria's boons (the Whispering Glade, Session 2):** Ursa, Planar Awareness (sense "
             "planar disturbances, 24 hours); Lilly, the Sphere's Planar Attunement; Stabby, Glimpse "
             "of Possibility (one reroll, because the goddess smiled at the goblin)."),
    ("body", "**The eight Winter Bells (Session 4).** C, D, E, F, G, A, B, High C: relics of "
             "Elaria's light hidden across Havenmoor. Rung in harmony they unmade the Krampusshade. "
             "**Faelan's Frosted Cookies:** 2d8 healing, a short rest's comfort, and one spell slot, "
             "in cookie form."),
    ("body", "**Curios of the road.** The Shadow-Touched Rune Fragment (advantage vs fear, 1 hour); "
             "the Dark Fragment of Stormwatch Cliffs (crystallized chaos, evidence of sabotage); "
             "Terranox's stone fragments and the elemental mud samples of the Grove of Elemental "
             "Waters; beeswax earplugs that beat a monster's song; a bell-handled "
             "blue lantern from Pumpkin Row; Alwen's flasks of lucky seawater."),
    ("lore", "The Bells of the Coast",
     "When the safeguards were scattered, eight fell along the southern coast as bells, each "
     "holding one clear note of the song Elaria sang while she worked. Havenmoor built its "
     "festival around them centuries before anyone remembered why the bells mattered. The "
     "town rang them every winter anyway. Traditions are how a town remembers what its people "
     "forget, and one winter the ringing unmade a fiend."),
]

# ----------------------------------------------------------------------
# VOLUME III: CUSTOM CONTENT (feats, subclasses, house rules)
# ----------------------------------------------------------------------
C = [
    title("THE CUSTOM COMPENDIUM", "Subclasses, Paths & House Rules"),
    ("gold", "Homebrew and rulings of this table: the paths the heroes may walk after the year "
             "apart, and the standing rules of the campaign. 2024 rules throughout; house rules "
             "override the books. The heroes themselves, every number, slot, and spell, now live "
             "in Part IV: The Guardians' Character Sheets."),

    ("h1", "House Rules & Standing Rulings"),
    ("body", "1. Ursa's Starseed +1d4 applies only to actual druid spells, never the Starry Form "
             "Archer's luminous arrow."),
    ("body", "2. Patient Defense grants a free Disengage (add Dodge by spending 1 Focus)."),
    ("body", "3. Shillelagh replaces Primal Savagery on Ursa's sheet (2024 rules)."),
    ("body", "4. Goodberry: eating a berry is a Bonus Action (2024)."),
    ("body", "5. Ursa's summoned Air spirit has 20 HP."),
    ("body", "6. Deep gnome uses the current 2024-era printing (Svirfneblin Camouflage, Disguise "
             "Self and Nondetection 1/long rest each)."),
    ("body", "7. Lilly's cannon picks its mode on EVERY activation (Forge of the Artificer rule)."),
    ("body", "8. Potent Spellcasting rides the kindled staff once per turn (Ursa, from level 7)."),
    ("lore", "The First Listeners",
     "Before there were villages there were listeners. The first druids did not learn magic; "
     "they learned quiet, and the forests, glad of the company, taught them the rest. The "
     "Circle of the Eternal Stars still opens every gathering with a full minute of silence, "
     "in honor of the age when that was the whole religion."),

    ("h1", "The Three Doors"),
    ("gold", "At the close of the Gearhaven chapter the Guardians parted for a year: a year of "
             "workshops and roads and night skies, each hero following their own heart home. "
             "Before each of them stand three doors, three ways that year apart might be spent, "
             "and behind every door waits a different gift."),
    ("body", "The chapters that follow set down what waits behind all nine: Stabby's three breathing "
             "styles, Ursa's three paths of the stars, and Lilly's three artifacts. Each Guardian "
             "will choose exactly one door, and none of the three has chosen yet. When they do, the "
             "doors not taken will remain in these pages, roads not walked, ready for other heroes "
             "in other tellings."),
    # The three heroes at the parting: each stands before a different set of
    # doors. Fills the tail before Stabby's path opens on a fresh page.
    ("imgrow", [("assets/characters/stabby_v3_portrait.png",
                 "Stabby, before the three breathing styles."),
                ("assets/characters/ursa_v3_portrait.png",
                 "Ursa, before the three paths of the stars."),
                ("assets/characters/lilly_v3_portrait.png",
                 "Lilly, before the three artifacts.")], 1.95),
    ("lore", "The Roads Not Taken",
     "The old tellings are gentle about the doors a hero leaves closed. A road not walked is "
     "not a road lost, the Circle says, only a road lent to someone else. Every path in these "
     "pages was true; a Guardian simply cannot be three heroes at once, and the year apart is "
     "the world's kind way of asking each of them who they most wish to become."),

    # ------------------------------------------------------------------
    # WARRIOR OF BREATHING: full text of warrior_of_breathing_v2.pdf
    # ------------------------------------------------------------------
    ("h1", "Warrior of Breathing (Stabby's Path)", {"hardbreak": True}),
    ("body", "A homebrew monk subclass taken at level 7 in place of Kensei. A Warrior of Breathing "
             "kindles an inner style, a visible breath that wreathes the blade. Three doors, three "
             "breathing styles; every road grants the **Nichirin Katana**, and every First Form "
             "replaces Flurry of Blows. The full text of all three follows."),
    ("lore", "What a Breathing Style Is",
     "The mountain monks say a breathing style is not a trick of the lungs but a way of "
     "remembering. Every warrior carries a wild thing, a still river, and a patch of honest "
     "dark somewhere inside them; a breathing style is simply the practice of calling one of "
     "them up on purpose, and setting it down again when the fight is done. The breath, the "
     "old masters warn, is easy to light and hard to quench, which is why they teach the "
     "quenching first."),

    ("h2", "Beast Breathing: the Bloodfang Form"),
    ("gold", "*“You think too much, little storm. The beast does not think. The beast moves, "
             "and the beast is already behind you.”* (the lesson Stabby finally understood)"),
    ("imgfloat", "assets/characters/stabby_breathing_style_red.png", 2.4),
    ("body", "Some warriors learn to still the storm inside them. The Warrior of Beast Breathing "
             "learns to ride it. Where other monks seek calm, this form reaches into the wild, "
             "animal heart of the fighter: the part that does not hesitate, does not flinch, and "
             "does not stop. Practitioners breathe in time with a racing heartbeat rather than a "
             "slow one, and when they ignite their breath, their blade glows blood-red and their "
             "body moves with the loping, unstoppable grace of a hunting beast."),
    ("body", "It is a form born of survival rather than discipline, favored by those who grew up "
             "where the strong eat and the slow are eaten. To master it is not to tame the beast, "
             "but to become it on command, and to remember how to set it down again afterward."),
    ("body", "**Features by Monk Level.** You gain Warrior of Beast Breathing features at Monk "
             "levels 3 (Beast Breathing), 6 (First Form: Devour), 11 (Advanced Beast Breathing), "
             "and 17 (Third Form: Apex Predator)."),
    ("stat", "Level 3: Beast Breathing", [
        "**Monk Weapons.** A katana, as well as any sword you adopt as your signature blade, "
        "counts as a Monk weapon for you. You can use your Martial Arts die with it, and you can "
        "use this subclass's features with it. You can still make an Unarmed Strike as a Bonus "
        "Action.",
        "**Beast Sense.** Your senses are sharp as a hunting animal's, even out of combat. You "
        "have Advantage on Wisdom (Survival) checks made to track creatures, on Wisdom "
        "(Perception) checks that rely on smell or hearing, and on Charisma (Intimidation) checks.",
        "**Igniting the Breath.** When you roll Initiative, you can expend 1 Focus Point to ignite "
        "your breath. It lasts until the combat ends, until you have the Incapacitated condition, "
        "or until you end it (no action required). While your breath is ignited, your weapon "
        "glows blood-red, and whenever you hit a target with it, the target takes an extra 2 "
        "Force damage.",
        "**Beast's Vigor.** While your breath is ignited, your Speed increases by 10 feet, and "
        "you have Advantage on Dexterity saving throws.",
    ]),
    ("stat", "Level 6: First Form: Devour", [
        "**First Form: Devour.** As a Bonus Action, you can expend 1 Focus Point to move up to 15 "
        "feet without provoking Opportunity Attacks and make one attack with your Monk weapon. On "
        "a hit, the target takes Force damage equal to 3d8 plus your Dexterity modifier instead "
        "of the weapon's normal damage. Bonuses to the weapon's damage rolls (such as the "
        "Nichirin katana's +2 bonus and the extra damage from your ignited breath) apply as "
        "normal. If the attack reduces the target to 0 Hit Points, you regain the expended Focus "
        "Point. This feature replaces Flurry of Blows for you.",
    ]),
    ("stat", "Level 11: Advanced Beast Breathing", [
        "**Advanced Breathing.** Your ignited breath grows fiercer. While your breath is ignited, "
        "you retain all its other benefits, you have Resistance to Bludgeoning, Piercing, and "
        "Slashing damage, and the extra Force damage your weapon deals increases from 2 to 3.",
        "**Sharpened Fang.** The damage of your First Form: Devour increases to 5d10 plus your "
        "Dexterity modifier.",
    ]),
    ("stat", "Level 17: Third Form: Apex Predator", [
        "**Third Form: Apex Predator.** You become a blur of fang and steel. As a Bonus Action, "
        "you can expend 3 Focus Points to move up to your Speed without provoking Opportunity "
        "Attacks and make one attack with your Monk weapon against each of up to three different "
        "creatures you move within reach of. On a hit, the target takes Force damage equal to "
        "5d10 plus your Dexterity modifier instead of the weapon's normal damage. Bonuses to the "
        "weapon's damage rolls (such as the Nichirin katana's +2 bonus and the extra damage from "
        "your ignited breath) apply as normal. Each creature hit must succeed on a Strength "
        "saving throw (DC 8 plus your Wisdom modifier and Proficiency Bonus) or have the Prone "
        "condition. You regain 1 expended Focus Point for each "
        "creature this feature reduces to 0 Hit Points.",
    ]),
    ("game", "At Level 7, Beast Breathing Has", [
        "**Live now:** the full Level 3 stance (the katana as a Monk weapon, Beast Sense, "
        "Igniting the Breath for +2 Force on every hit, and Beast's Vigor) plus First Form: "
        "Devour (3d8 + Dex, with 15 feet of free movement).",
        "**Not yet:** Advanced Beast Breathing and Sharpened Fang arrive at Level 11, and Third "
        "Form: Apex Predator at Level 17. They wait further down the road.",
    ]),

    ("h2", "Water Breathing: the Monastery Form"),
    ("gold", "*“Be water. Water does not strike; it flows, and the rock is cut all the same. "
             "Now breathe, and begin again.”* (Master Kaelon Windstep)"),
    ("imgfloat", "assets/characters/stabby_breathing_style_water.png", 2.4),
    ("body", "The Warrior of Water Breathing is the form of the patient master, the discipline that "
             "other monks spend their whole lives chasing. Its practitioners learn to move like a "
             "river: never rigid, never still, every strike flowing into the next, every blow "
             "turned aside by giving way rather than resisting. When they ignite their breath, "
             "their blade runs pale blue and cold, and their guard becomes as fluid and unbroken "
             "as a current that cannot be grasped."),
    ("body", "It is the most traditional of the breathing forms, and the hardest to truly master, "
             "for it asks the warrior to be calm in the middle of chaos. Those who walk this path "
             "are as often menders as fighters, for the same stillness that turns a blade can also "
             "close a wound, and the same patience that wins a duel can sit a long vigil at a "
             "friend's side."),
    ("body", "**Features by Monk Level.** You gain Warrior of Water Breathing features at Monk "
             "levels 3 (Water Breathing), 6 (First Form: Flowing Strike and Healing Spring, First "
             "Water), 11 (Advanced Water Breathing and the full Healing Spring), and 17 (Third "
             "Form: Tidal Crash)."),
    ("stat", "Level 3: Water Breathing", [
        "**Monk Weapons.** A katana, as well as any sword you adopt as your signature blade, "
        "counts as a Monk weapon for you. You can use your Martial Arts die with it, and you can "
        "use this subclass's features with it. You can still make an Unarmed Strike as a Bonus "
        "Action.",
        "**Igniting the Breath.** When you roll Initiative, you can expend 1 Focus Point to ignite "
        "your breath. It lasts until the combat ends, until you have the Incapacitated condition, "
        "or until you end it (no action required). While your breath is ignited, your weapon "
        "glows pale blue, and whenever you hit a target with it, the target takes an extra 2 Cold "
        "damage.",
        "**Flowing Guard.** While your breath is ignited, you gain a +2 bonus to Armor Class "
        "against the first attack roll made against you before the start of each of your turns.",
    ]),
    ("stat", "Level 6: First Form: Flowing Strike", [
        "**First Form: Flowing Strike.** As a Bonus Action, you can expend 1 Focus Point to move "
        "up to 15 feet without provoking Opportunity Attacks and make one attack with your Monk "
        "weapon. On a hit, the target takes Cold damage equal to 3d8 plus your Dexterity modifier "
        "instead of the weapon's normal damage. Bonuses to the weapon's damage rolls (such as the "
        "Nichirin katana's +2 bonus and the extra damage from your ignited breath) apply as "
        "normal. If the attack hits, the target must also succeed on a Dexterity saving throw "
        "(DC 8 plus your Wisdom modifier and Proficiency Bonus) or have the Prone condition. "
        "This feature replaces Flurry of Blows for you.",
        "**Healing Spring (First Water).** As a Bonus Action, you can touch yourself or another "
        "creature, and the target regains a number of Hit Points equal to 2d8 plus your Wisdom "
        "modifier. Once you use this benefit, you can't use it again until you finish a Short or "
        "Long Rest. This benefit improves when you reach Monk level 11 (Healing Spring).",
    ]),
    ("stat", "Level 11: Advanced Water Breathing", [
        "**Advanced Breathing.** Your ignited breath deepens. While your breath is ignited, you "
        "retain all its other benefits, and whenever you hit a creature with your Monk weapon, "
        "that creature's Speed is reduced by 10 feet until the start of your next turn.",
        "**Sharpened Flow.** The damage of your First Form: Flowing Strike increases to 5d10 plus "
        "your Dexterity modifier.",
        "**Healing Spring.** When you use your Healing Spring, the target now regains a number "
        "of Hit Points equal to 4d8 plus your Wisdom modifier. Once you use this benefit, you "
        "can't use it again until you finish a Short or Long Rest.",
    ]),
    ("stat", "Level 17: Third Form: Tidal Crash", [
        "**Third Form: Tidal Crash.** As a Bonus Action, you can expend 3 Focus Points to move "
        "up to 20 feet and make one attack with your Monk weapon against each of up to three "
        "different creatures within your reach during that movement. On a hit, the target takes "
        "Cold damage equal to 5d10 plus your Dexterity modifier instead of the weapon's normal "
        "damage. Bonuses to the weapon's damage rolls (such as the Nichirin katana's +2 bonus "
        "and the extra damage from your ignited breath) apply as normal. Each creature hit must "
        "succeed on a Dexterity saving throw (DC 8 plus your Wisdom modifier and Proficiency "
        "Bonus) or have the Prone condition and a Speed of 0 until the end of its next turn.",
    ]),
    ("game", "At Level 7, Water Breathing Has", [
        "**Live now:** the full Level 3 stance (the katana as a Monk weapon, Igniting the Breath "
        "for +2 Cold on every hit, and Flowing Guard) plus First Form: Flowing Strike (3d8 + Dex "
        "with a tripping save, DC 13) and Healing Spring, First Water (2d8 + Wis, once per "
        "Short Rest).",
        "**Not yet:** the full Healing Spring (4d8 + Wis), Advanced Water Breathing, and "
        "Sharpened Flow arrive at Level 11; Third Form: Tidal Crash at Level 17.",
    ]),

    ("h2", "Shadow Breathing: the Idol Form"),
    ("gold", "*“Do not fear the dark. Breathe it in. Let it fill you, and then there is "
             "nothing left in the dark to fear you.”* (a whisper from the idol)"),
    ("imgfloat", "assets/characters/stabby_breathing_style_shadow.png", 2.4),
    ("body", "The Warrior of Shadow Breathing is the strangest and most secretive of the forms, a "
             "discipline touched by something older than any monastery. Its practitioners breathe "
             "in the gloom itself, drawing the dark into their lungs until it answers to them. "
             "When they ignite their breath, their blade runs violet-black, the shadows fold "
             "around them like a cloak, and they see clearly in darkness that blinds everyone "
             "else."),
    ("body", "Few teach this form openly, for it walks close to powers most monks are warned away "
             "from. Those who carry it often carry a question they cannot yet answer: why the dark "
             "heeds them, where the breath truly comes from, and what waits at the end of the path "
             "they have started down. Mastered well, it makes a warrior into something the night "
             "itself seems to bend around."),
    ("body", "**Features by Monk Level.** You gain Warrior of Shadow Breathing features at Monk "
             "levels 3 (Shadow Breathing), 6 (First Form: Umbral Slash), 11 (Advanced Shadow "
             "Breathing), and 17 (Third Form: Eclipse)."),
    ("stat", "Level 3: Shadow Breathing", [
        "**Monk Weapons.** A katana, as well as any sword you adopt as your signature blade, "
        "counts as a Monk weapon for you. You can use your Martial Arts die with it, and you can "
        "use this subclass's features with it. You can still make an Unarmed Strike as a Bonus "
        "Action.",
        "**Eyes of the Idol.** The idol's gift never fully leaves you. You have Darkvision with a "
        "range of 60 feet (if you already have Darkvision, its range increases by 60 feet), and "
        "you have Advantage on Dexterity (Stealth) checks.",
        "**Igniting the Breath.** When you roll Initiative, you can expend 1 Focus Point to ignite "
        "your breath. It lasts until the combat ends, until you have the Incapacitated condition, "
        "or until you end it (no action required). While your breath is ignited, your weapon "
        "glows violet-black, and whenever you hit a target with it, the target takes an extra 2 "
        "Necrotic damage.",
        "**One With the Gloom.** While your breath is ignited, you gain a +2 bonus to Armor "
        "Class against ranged attack rolls, and you can see normally in magical Darkness.",
    ]),
    ("stat", "Level 6: First Form: Umbral Slash", [
        "**First Form: Umbral Slash.** As a Bonus Action, you can expend 1 Focus Point to "
        "teleport up to 15 feet to an unoccupied space you can see within 5 feet of a creature. "
        "Magical Darkness then fills a 10-foot Cube of your choice, which must contain that "
        "creature's space. You then make one attack with your Monk weapon against that creature, "
        "and you have Advantage on the attack roll. On a hit, the target takes Necrotic damage "
        "equal to 3d8 plus your Dexterity modifier instead of the weapon's normal damage. "
        "Bonuses to the weapon's damage rolls (such as the Nichirin katana's +2 bonus and the "
        "extra damage from your ignited breath) apply as normal.",
        "You can see through Darkness created by this feature. The Darkness lasts until the end "
        "of your next turn, or you can end it early (no action required). This feature replaces "
        "Flurry of Blows for you.",
    ]),
    ("dm", "The gloom is his alone. Stabby sees through his own Darkness; his allies cannot. "
           "Allies make ranged attack rolls with Disadvantage against a creature wrapped in the "
           "gloom, and spells that require a visible target cannot reach it at all, so the party "
           "learns to pick different targets while the shadow does its work."),
    ("stat", "Level 11: Advanced Shadow Breathing", [
        "**Advanced Breathing.** Your ignited breath drinks deeper of the dark. While your "
        "breath is ignited, you retain all its other benefits. In addition, once per turn when "
        "you hit a creature with an attack roll that had Advantage, the target takes an extra "
        "2d6 Necrotic damage.",
        "**Sharpened Gloom.** The damage of your First Form: Umbral Slash increases to 5d10 plus "
        "your Dexterity modifier.",
    ]),
    ("stat", "Level 17: Third Form: Eclipse", [
        "**Third Form: Eclipse.** You vanish into the gloom and strike from everywhere at once. "
        "As a Bonus Action, you can expend 3 Focus Points to fill a 20-foot Cube centered on "
        "yourself with magical Darkness, which you can see through. For each of up to three "
        "different creatures in the Cube, you can teleport to an unoccupied space you can see "
        "within 5 feet of that creature and make one attack with your Monk weapon against it, "
        "and you have Advantage on each attack roll. On a hit, the target "
        "takes Necrotic damage equal to 5d10 plus your Dexterity modifier instead of the "
        "weapon's normal damage. Bonuses to the weapon's damage rolls (such as the Nichirin "
        "katana's +2 bonus and the extra damage from your ignited breath) apply as normal. Each "
        "creature hit has the Blinded condition until the end of your next turn, and creatures "
        "other than you can't see you until the Darkness ends.",
    ]),
    ("game", "At Level 7, Shadow Breathing Has", [
        "**Live now:** the full Level 3 stance (the katana as a Monk weapon, Eyes of the Idol, "
        "Igniting the Breath for +2 Necrotic on every hit, and One With the Gloom) plus First "
        "Form: Umbral Slash (3d8 + Dex from inside a pocket of Darkness only Stabby sees "
        "through).",
        "**Not yet:** Advanced Shadow Breathing and Sharpened Gloom arrive at Level 11, and "
        "Third Form: Eclipse at Level 17. The deeper dark is still ahead.",
    ]),

    ("h2", "The Demon-Slayer's Blade: the Nichirin Katana"),
    ("body", "This sun-forged demon-slayer blade was made from crimson ore that drinks in "
             "dawnlight. While sheathed, the steel looks dark and almost ordinary, but when Stabby "
             "ignites his breathing, the blade catches that breath and burns with the color of his "
             "chosen form."),
    ("stat", "Nichirin Katana", [
        "*Weapon (Katana), Rare (Requires Attunement by Stabby)*",
        "**Weapon Statistics.** The Nichirin katana uses the statistics of a Longsword (1d8 "
        "Slashing damage) and has the Finesse and Versatile (1d10) properties, and it counts as "
        "a Monk weapon for you. Because the weapon has the Finesse property and is a Monk weapon "
        "for you, you can use your Dexterity modifier for its attack and damage rolls.",
        "**Magic Weapon.** You gain a +2 bonus to attack rolls and damage rolls made with this "
        "magic weapon.",
        "**Breath-Kindled Steel.** When you ignite your breathing, the blade glows with the "
        "color and nature of that form: blood-red for Beast Breathing, pale blue for Water "
        "Breathing, or violet-black for Shadow Breathing. This glow is magical but sheds only "
        "Dim Light unless you choose otherwise.",
        "**Cleansing Edge.** Once per turn when you hit a Fiend, an Undead, a shadow creature, "
        "or a creature empowered by planar corruption with this weapon, the blade burns away "
        "corruption until the start of your next turn. Until then, the target can't regain Hit "
        "Points and can't benefit from magical Darkness or shadowy concealment against you. Any "
        "visible corruption around the wound briefly burns, cracks, or peels away in sparks of "
        "purified light.",
        "The katana is especially dangerous to creatures twisted by "
        "darkness, undeath, or planar corruption. It leaves wounds that glow faintly like banked "
        "embers, revealing that the creature has been marked by cleansing sunlight. The blade "
        "wounds the corruption, not the creature beneath. When a corrupted guardian falls to it, "
        "what breaks is the darkness.",
    ]),
    ("h2", "Lore of the Blade"),
    ("body", "They say the first Nichirin blades were quenched not in water or oil but in the "
             "light of dawn itself, folded by smiths who worked only in the hour before sunrise. "
             "The ore came from a single mountain that caught the morning sun before anywhere else "
             "in the world, and steel drawn from it never forgot that first warmth. A finished "
             "blade looks plain and dark in an idle hand; it is waiting. Only a warrior who can "
             "kindle their own breath can wake the color sleeping in the metal."),
    ("body", "For a creature of corruption, that waking light is a death sentence. Where an "
             "ordinary sword cuts flesh, a Nichirin blade cuts the rot itself: the shadow that "
             "hides a fiend, the dark magic that knits an undead back together, the planar taint "
             "that lets a horror shrug off honest steel. Stabby's blade chose its colors from his "
             "own breathing forms, and now it burns red, blue, or violet to match whichever beast, "
             "river, or shadow he calls upon."),
    ("gold", "**A whispered rumor.** Old hunters claim a Nichirin blade can never be truly stolen: "
             "carried by the wrong hand, the steel stays cold and dull and will not take an edge. "
             "Whether that is true, or simply a story told to keep thieves honest, no one in "
             "living memory has dared find out."),
    ("h2", "Setting Down the Kensei's Way"),
    ("body", "When Stabby takes up a breathing form at Level 7, the Kensei's tricks retire with "
             "his old teacher's lessons. He loses Kensei's Shot (the bow's Bonus Action +1d4) and "
             "Agile Parry (his +2 AC after blade-and-fist turns), and the Repeating Longbow "
             "becomes simply a very good bow, no longer a Monk weapon. In exchange he gains a "
             "stance he can ignite every single fight, a First Form that turns his Bonus Action "
             "into a 3d8 + 5 strike with 15 feet of free movement, form gifts that work all day, "
             "and a road that grows with him to Level 17. He is trading a parry for a predator's "
             "gait, and he gains far more than he gives up. (And Candyfang, outshone by the "
             "Nichirin blade, needn't vanish: an heirloom at his belt, or one day, a gift worthy "
             "of a Bloodfang.)"),

    # ------------------------------------------------------------------
    # PATHS OF THE STARS: full text of ursa_path_rewards_v2.pdf
    # ------------------------------------------------------------------
    ("h1", "Paths of the Stars (Ursa's Path)", {"hardbreak": True}),
    ("gold", "*For Ursa Catchum, Circle of the Stars Druid: the year apart, Level 5 to 7.* "
             "Ursa walked one of three roads during the year apart, and came back changed. Each "
             "road grants a feat (what he sought) and a keepsake (what found him): he gains the "
             "pair matching his road. These are special story feats: they grant no Ability Score "
             "Increase."),
    ("lore", "The Star-Paths of the Circle",
     "The Circle holds that no druid chooses the stars; the stars choose, and the druid only "
     "walks to meet them. Three roads are said to open before a sky-reader who has served the "
     "Circle well: one into the wild, where the living world answers; one into the sky, where "
     "the constellations lend their light; and one along a father's trail, where the omens stop "
     "coming at random and begin, at last, to obey. A druid walks one road and comes back "
     "changed, and the two roads not taken wait, patient as starlight, for whoever comes next."),

    ("h2", "Beast Handler: The Living World (the road into the wild)"),
    ("gold", "*“You went out to learn the speech of wild things. You came back, and the wild "
             "things follow you home.”*"),
    ("stat", "Beast Handler (feat)", [
        "*Story Feat*",
        "You gain the following benefits.",
        "**Mightier Summons.** Whenever you cast the Summon Beast spell, the spell takes effect "
        "as if you had cast it using a spell slot of the highest level you can cast, without "
        "expending a slot of that level.",
        "**Wild Speech.** You and any creature you summon can communicate simple ideas with each "
        "other telepathically. In addition, you can understand the sounds and "
        "gestures of ordinary Beasts even without your Mark's magic, and they can understand "
        "yours.",
    ]),
    # [DM CHECK: the Wildheart Token has no italic type line (compare Ash's Sigil-Stone's
    # "*Wondrous Item, Rare (Requires Attunement by Ursa)*"). Adding one forces a rarity call,
    # and adding attunement would change Ursa's slot math on the Beast Handler road, so this
    # is flagged for a DM decision rather than fixed silently.]
    # [DM CHECK: "the player names the beast, and names the friend" is a table instruction
    # inside the item's flavor lead; suggested home is a dm block.]
    ("stat", "The Wildheart Token", [
        "*Carved by his own hand.*",
        "A totem of a beast Ursa befriended during the wild year: the player names the beast, "
        "and names the friend. It refuses to leave you. The Bestial Spirit you summon always "
        "takes that companion's shape. When the spirit would drop to 0 Hit Points, it drops to "
        "1 Hit Point instead. Once this property is used, it can't be used again until the "
        "next dawn.",
    ]),
    ("game", "At Level 7, Beast Handler Has", [
        "**Live now:** Summon Beast cast as a level 4 spell for a level 2 slot, free "
        "thought-speech with his summoned creatures, plain understanding of ordinary Beasts, and "
        "the Wildheart Token (his Bestial Spirit always wears his friend's shape, and once per "
        "day drops to 1 Hit Point instead of 0).",
        "**Not yet:** Mightier Summons keeps growing on its own. When Ursa's highest spell slot "
        "reaches level 5 at Druid level 9, the summons rise with it, no new feat required.",
    ]),

    ("h2", "Starlit Channeler: The Circle of Stars (the road into the sky)"),
    ("gold", "*“You returned to the Circle, and the constellations answered: their light now "
             "runs down your arm and out through the staff. The Warden's spear sweeps between "
             "danger and the party.”*"),
    ("stat", "Starlit Channeler (feat)", [
        "*Story Feat*",
        "You gain the following benefits.",
        "**The Warden.** You learn the Shillelagh cantrip, and Wisdom is your spellcasting "
        "ability for it. In addition, your Starry Form gains a fourth constellation: the Warden, "
        "a spear-bearing figure of starlight that holds its ground. When you assume your Starry "
        "Form, you can choose the Warden. If you do so, you cast Shillelagh through your staff "
        "as part of the same Bonus Action, and the spell lasts until your Starry Form ends "
        "rather than for 1 minute. While the Warden constellation is active, the kindled staff "
        "deals Radiant damage, and when you hit with it, the target takes an extra 1d6 Radiant "
        "damage. The extra damage increases by 1d6 when you reach Druid levels 11 (2d6) and 17 "
        "(3d6).",
        "**The Warden's Light.** While the Warden constellation is active, the radius of the "
        "Staff's Starlight increases to 20 feet, and each ally within that light gains a +1 "
        "bonus to attack rolls and saving throws.",
        "**Warden's Intercession.** "
        "When a creature you can see hits an ally within your Starlight, you can take a "
        "Reaction to reduce the attack's damage against that ally. The reduction equals 1d8 "
        "plus your Wisdom modifier.",
    ]),
    ("dm", "The kindled staff IS the Shillelagh spell: Starseed (+1d4) rides its strikes (unlike "
           "the Archer's arrow, a form feature), and its damage counts as cantrip damage "
           "(Elemental Fury: Potent Spellcasting applies from Druid level 7, once per turn, like "
           "Starseed). Sheet note: the feat grants Shillelagh, so Ursa's known copy frees up for "
           "a cantrip swap at his next level."),
    ("stat", "The Staff Wakes Further", [
        "*The relic grows, as promised.* "
        "The Staff of Waking Constellations has always brightened a new star after every "
        "victory; on this road, it brightens for him. It is the vessel the Warden shines "
        "through: when the constellation widens its Starlight to 20 feet, it is this staff "
        "carrying the light, and the whole party fits inside it. The staff now has 6 charges "
        "and regains 1d4 + 2 expended charges daily at dawn.",
    ]),
    ("game", "At Level 7, Starlit Channeler Has", [
        "**Live now:** the Warden constellation (a kindled staff dealing Radiant damage with an "
        "extra 1d6 Radiant damage on a hit, plus Starseed's +1d4 once per turn), Starlight "
        "widened to 20 feet while the Warden shines, with the Amulet's +1 bonus to attack rolls "
        "and saving throws for every ally inside, Warden's Intercession (a Reaction that "
        "reduces the damage of a hit against an ally in the glow by 1d8 plus his Wisdom "
        "modifier), and the Staff at 6 charges.",
        "**Not yet:** the Warden's extra Radiant damage grows to 2d6 at Druid level 11 and 3d6 "
        "at Druid level 17. The constellation keeps pace with the sky.",
    ]),

    ("h2", "Reader of Omens: The Father's Trail (the road east)"),
    # Ursa's portrait floated into the omens page to fill an otherwise
    # text-only hero-path page (2026-07-09 whitespace pass).
    ("imgfloat", "assets/characters/ursa_v3_portrait.png", 2.7),
    ("gold", "*“Your father read the sky the way other folk read a map. On his trail you "
             "learned his art: the omens no longer come at random, and you choose your "
             "moment.”*"),
    # [DM CHECK: Shared Tides says "a number of times equal to your Wisdom modifier" without
    # the SRD's "(minimum of once)". The PHB Cosmic Omen base feature carries the minimum, so
    # adding it would match the underlying feature, but it touches a floor mechanic, so it is
    # flagged for a DM decision rather than fixed silently.]
    ("stat", "Reader of Omens (feat)", [
        "*Story Feat (Prerequisite: Cosmic Omen Feature)*",
        "You gain the following benefits.",
        "**Both Omens.** When you consult your Star Map after finishing a Long Rest, you don't "
        "roll for a single omen. Instead, you gain access to both Weal and Woe until your next "
        "Long Rest.",
        "**Read the Moment.** When you take the Reaction granted by your Cosmic Omen feature, "
        "you can wait until after the d20 is rolled but before you know whether the roll "
        "succeeds or fails. You then choose whether to apply Weal (adding 1d6 to the roll) or "
        "Woe (subtracting 1d6 from it).",
        "**Shared Tides.** Your uses of Cosmic Omen remain a single pool: you can use the "
        "feature a number of times equal to your Wisdom modifier, expending one use on either "
        "Weal or Woe, and you regain all expended uses when you finish a Long Rest.",
    ]),
    ("dm", "Cosmic Omen is the Circle of Stars feature Ursa gained at Druid level 6."),
    ("body", "Woe lands after the die is cast: turning an enemy's save into a failure at the "
             "perfect moment feels like fate itself."),
    ("stat", "Ash's Sigil-Stone", [
        "*Wondrous Item, Rare (Requires Attunement by Ursa)*",
        "A river-smooth stone etched with a half-finished sigil of Elaria, in Ash's own hand. "
        "Recovered on the trail, it sits warm in the palm whenever it is carried east. Cast "
        "between fights, it knits the party whole and kindles Ursa's Chalice splash besides. "
        "One day, when the sigil is finished, it may wake.",
        "While holding the stone, you can cast Aura of Vitality from it without expending a "
        "spell slot. Once this property is used, it can't be used again until you finish a "
        "Long Rest.",
        "With the Staff and the Amulet, the Stone closes Ursa's third and final attunement "
        "slot.",
    ]),
    ("dm", "The Session 12 clue rides here."),
    ("game", "At Level 7, Reader of Omens Has", [
        "**Live now:** both Weal and Woe after every Long Rest, the patience to expend them "
        "after the d20 is rolled (but before the outcome is known), a pool of uses equal to his "
        "Wisdom modifier, and Ash's Sigil-Stone (Aura of Vitality once per Long Rest without "
        "expending a spell slot).",
        "**Not yet:** the sigil on the stone is only half finished. One day it may wake, and "
        "what it wakes into is a question for the road east.",
    ]),
    ("body", "Ursa gains the one road he walked, feat and keepsake together. The other two roads "
             "remain: the stars are patient, and the wild does not forget him."),

    # ------------------------------------------------------------------
    # GLIMMERSTONE ARTIFACTS: full text of glimmerstone_artifacts_v2.pdf
    # ------------------------------------------------------------------
    ("h1", "Glimmerstone Artifacts (Lilly's Path)", {"hardbreak": True}),
    ("gold", "Three masterworks of deep gnome artifice, forged for Lilly Glimmergear in the year "
             "apart. Three masterworks, one choice. Each door of Lilly's year apart leads to one "
             "of these treasures: stay and build the portal (the Sentinel), go home to "
             "Glimmerspire and Poots (Boomstick), or give the year to mote research (the Awakened "
             "Sphere). She walks one road and claims one masterwork. Every road fits inside her "
             "three attunement slots. On the Sphere's road the ledger closes at exactly three: "
             "Shard, Dynamo, Sphere. On the Sentinel's road a slot stays free, for the Dynamo "
             "itself is rebuilt into the guardian: two of three. And on Boomstick's road the "
             "Shard truly retires, unattuned at her belt, a keepsake and one day a gift: two of "
             "three, with room to spare."),

    ("h2", "Boomstick"),
    ("imgfloat", "assets/items/boomstick.png", 2.2),
    ("gold", "*“It doesn't jam. It doesn't misfire. It simply states its opinion, "
             "loudly.”*"),
    ("body", "On this road, Boomstick takes the dagger's watch. Boomstick becomes Lilly's "
             "spellcasting focus and her designated Arcane Firearm (an artificer designates only "
             "one). With her shield in the other hand, her hands are exactly full: pistol, shield, "
             "and nothing wasted. Its clockwork drum conjures its own rounds, so Lilly will never "
             "want for ammunition again. The Frostbite Shard retires to her belt as a keepsake, or "
             "one day, a gift."),
    ("stat", "Boomstick", [
        "*Weapon (Repeating Pistol), Rare (Requires Attunement by Lilly)*",
        "**Repeating Pistol, +2.** You gain a +2 bonus to attack rolls and damage rolls made "
        "with this magic weapon, which deals 1d10 Thunder damage on a hit. The weapon requires "
        "no ammunition and never needs reloading.",
        "**Wand of the War Mage.** While holding Boomstick, you gain a +2 bonus to spell attack "
        "rolls, and you ignore Half Cover when making a spell attack. Your Eldritch Cannon also "
        "gains a +2 bonus to its attack rolls.",
        "**Spell Focus and Arcane Firearm.** While holding Boomstick, you can use it as a "
        "Spellcasting Focus for your Artificer spells, and it is your designated Arcane Firearm. "
        "When you cast an Artificer spell through Boomstick, you can add 1d8 to one of the "
        "spell's damage rolls; the extra damage is Thunder damage.",
        "**Concussion Infusion.** When a creature takes damage from a spell you cast through "
        "Boomstick, that creature takes an extra 2 Thunder damage and can't take Reactions "
        "until the start of its next turn.",
        "**Made to Channel.** When you cast True Strike using Boomstick, the attack uses your "
        "Intelligence and counts as a spell attack, gaining Boomstick's +2 bonus to spell "
        "attack rolls and ignoring Half Cover. On a hit, the attack deals Boomstick's Thunder "
        "damage plus the spell's Radiant damage.",
        "*Forged by the masters of Glimmerstone.*",
    ]),
    ("game", "At Level 7, Boomstick Has", [
        "**Live now:** everything. The +2 pistol with its bottomless clockwork drum, +2 to spell "
        "attack rolls (a bonus that reaches her Eldritch Cannon's attacks too), ignored Half "
        "Cover on spell attacks, the 1d8 Thunder Arcane Firearm rider, the Concussion boom that "
        "steals Reactions, and True Strike channeled through the barrel.",
        "**Not yet:** nothing held back. Boomstick arrives complete, and this door pays its "
        "whole price on day one; what grows from here is only the legend.",
    ]),

    ("h2", "The Awakened Essence Sphere", {"hardbreak": True}),
    ("imgfloat", "assets/items/awakened_essence_sphere.png", 2.4),
    ("gold", "*“It was never a keepsake. It was a key, and it is finally awake.”*"),
    ("body", "The Sphere has spent the whole journey quietly pulling loose motes from the air. "
             "Now awakened, it holds a swirling jumble of collected aether that powers it from "
             "the start, and as the party clears each elemental rift and installs its pure Mote, "
             "the Sphere learns that plane's mighty discharge. The Sphere is honest about its "
             "bargain: at Session 8 it grants Aether Ward alone (twice per Short Rest), and "
             "every one of its five discharges sleeps behind a rift still to be won. This door "
             "is the campaign's long game: the quietest of the three at the choosing, and by "
             "the end of the arc, the mightiest of them all."),
    ("stat", "The Awakened Essence Sphere", [
        "*Wondrous Item, Rare (Requires Attunement by Lilly)*",
        "**Mote Channeling.** The Sphere's powers share a pool of 2 uses, and you regain all "
        "expended uses when you finish a Short Rest. The Sphere starts with the Aether Ward "
        "power, and it gains one Elemental Discharge each time a rift's Mote is installed in "
        "it. If one of the Sphere's powers requires a saving throw, the DC equals your spell "
        "save DC.",
        "**Aether Ward (Base Power).** As a Magic action, you can expend 1 use "
        "to release the gathered motes as a protective shell. You and each ally within 15 feet "
        "of you gain a number of Temporary Hit Points equal to 2d8 plus your Intelligence "
        "modifier.",
        "**Rift Tracker.** When a rift's Mote is installed in the Sphere, record it: Ignis, "
        "Unda, Aer, Terra, Umbra.",
    ]),
    ("stat", "Elemental Discharges", [
        "*Each unlocks when its rift is cleared and its Mote installed. The menu grows as the "
        "campaign goes.*",
        "**Fire / Ignis, Cinderstorm (LOCKED).** As a Magic action, you can expend 1 use to "
        "unleash a firestorm that fills a 40-foot-radius Sphere centered on a point within 120 "
        "feet of yourself. Each creature in the Sphere must make a Dexterity saving throw, "
        "taking 8d6 Fire damage on a failed save or half as much damage on a successful one. "
        "Until the start of your next turn, the area burns: it is Difficult Terrain, and any "
        "creature that enters the area or starts its turn there takes 2d6 Fire damage.",
        "**Water / Unda, Drowning Surge (LOCKED).** As a Magic action, you can expend 1 use to "
        "release a surge of crushing water in a 30-foot Cone. Each creature in the Cone must "
        "make a Constitution saving throw, taking 6d8 Cold damage on a failed save or half as "
        "much damage on a successful one. On a failed save, the creature also has the Prone "
        "condition, and its Speed is halved until the end of its next turn.",
        "**Air / Aer, Cyclone (LOCKED).** As a Magic action, you can expend 1 use to conjure a "
        "whirlwind that fills a 30-foot-radius Sphere centered on a point within 120 feet of "
        "yourself. Each creature in the Sphere must make a Strength saving throw, taking 6d8 "
        "Thunder damage on a failed save or half as much damage on a successful one. On a "
        "failed save, the creature is also pushed 20 feet away from the Sphere's center and "
        "has the Prone condition.",
        "**Earth / Terra, Tectonic Slam (LOCKED).** As a Magic action, you can expend 1 use to "
        "make the ground erupt in a 20-foot-radius Sphere centered on a point within 120 feet "
        "of yourself. Each creature in the Sphere must succeed on a Dexterity saving throw or "
        "take 7d8 Force damage and have the Prone condition. Until the start of your next "
        "turn, the raised stone makes the area Difficult Terrain, a creature takes 5 Piercing "
        "damage for every 5 feet it moves in the area, and you and your allies have Half Cover "
        "while in the area.",
        "**Shadow / Umbra, Soul Siphon (LOCKED).** As a Magic action, you can expend 1 use to "
        "target one creature within 60 feet of yourself, or you can divide the damage dice "
        "among up to three creatures within that range. Each target must make a Constitution "
        "saving throw, taking 8d6 Necrotic damage on a failed save or half as much damage on a "
        "successful one. You or one ally within 30 feet of you (your choice) regains Hit "
        "Points equal to half the amount of Necrotic damage dealt.",
    ]),
    ("game", "At Level 7, the Awakened Essence Sphere Has", [
        "**Live now:** Aether Ward, twice per Short Rest: Lilly and each ally within 15 feet "
        "gain 2d8 + her Intelligence modifier Temporary Hit Points.",
        "**Not yet:** all five discharges. Cinderstorm, Drowning Surge, Cyclone, Tectonic Slam, "
        "and Soul Siphon each wake only when their rift falls and its Mote comes home. Five "
        "rifts stand between this Sphere and its full voice, and it means to earn every one.",
    ]),

    ("h2", "The Sentinel"),
    ("gold", "*“An upgraded Eldritch Cannon, rebuilt at the bench into a faithful "
             "guardian.”*"),
    ("statblock", {
        "name": "The Sentinel",
        "type": "Medium Construct (the Pocket Dynamo, rebuilt; Requires Attunement by Lilly)",
        "ac": "18",
        "hp": "5 + five times your Artificer level (40 at Level 7); it has a number of d8 Hit "
              "Dice equal to your Artificer level",
        "speed": "30 ft.",
        "abilities": {"STR": 14, "DEX": 10, "CON": 16, "INT": 4, "WIS": 12, "CHA": 6},
        "immunities": "Poison",
        "condition_immunities": "Charmed, Exhaustion, Poisoned",
        "senses": "Darkvision 60 ft., Passive Perception 11",
        "languages": "understands the languages you know",
        "img": "assets/items/upgraded_eldritch_cannon.png",
        "traits": [
            ("Duration", "None. The Sentinel remains until it drops to 0 Hit Points or until "
                         "you dismiss it (no action required). As a Bonus Action, you can "
                         "deploy or recall it."),
            ("Bound Construct", "Add your Proficiency Bonus to any ability check or saving throw "
                                "the Sentinel makes."),
            ("Rebuilt Dynamo", "The Sentinel replaces your Eldritch Cannon feature: while you "
                               "are attuned to it, you deploy the Sentinel instead of a cannon, "
                               "never both at once. Deploying the Sentinel doesn't expend a "
                               "spell slot, and the Sentinel has no maximum duration. When the "
                               "Mending spell is cast on the Sentinel, it regains 2d6 Hit "
                               "Points. If the Sentinel has dropped to 0 Hit Points, you can "
                               "rebuild it by expending a level 1+ spell slot."),
        ],
        "actions": [
            ("Activate", "As a Bonus Action, you can activate the Sentinel, and it then takes "
                         "one of the following actions of your choice."),
            ("Force Blast", "Ranged Attack Roll: Bonus equals your spell attack modifier, range "
                            "120 ft. Hit: 2d8 + your Intelligence modifier Force damage."),
            ("Electric Pulse", "Dexterity Saving Throw: DC equals your spell save DC, each "
                               "creature of your choice within 15 feet of the Sentinel. "
                               "Failure: 2d8 + your Intelligence modifier Lightning damage, and "
                               "the target can't take Reactions until the start of your next "
                               "turn. Success: Half damage."),
        ],
        "reactions": [
            ("Guardian Protocol (1/round)", "Trigger: An ally within 15 feet of the Sentinel "
                                            "takes damage. Response: The ally gains 1d8 + your "
                                            "Intelligence modifier Temporary Hit Points."),
        ],
    }),
    ("body", "**Why this is an upgrade.** The old cannon made Lilly choose a mode; the Sentinel "
             "walks on its own 30 feet, then blasts or pulses on her Bonus Action (her pick every "
             "time), and shields her friends as a Reaction in the same round. Her old kit lives "
             "on inside it: the Force Ballista became the Force Blast, the Storm mode became the "
             "Electric Pulse, and the Protector stands watch as Guardian Protocol. The "
             "Flamethrower was traded for lightning, Gearhaven's own element. Forged by the "
             "masters of Glimmerstone."),
    ("game", "At Level 7, the Sentinel Has", [
        "**Live now:** the whole statblock. 40 Hit Points behind AC 18, its own 30 feet of "
        "Speed, Force Blast or Electric Pulse on her Bonus Action (her pick every round), "
        "Guardian Protocol once per round, and a free attunement slot besides, since the Dynamo "
        "lives on inside the frame.",
        "**Not yet:** its Hit Points keep pace with her, 5 + five times her Artificer level, so "
        "the guardian grows sturdier every time Lilly does.",
    ]),

    ("h1", "Marks & Mysteries"),
    ("body", "**Ursa's Mark of Handling.** A dragonmark that woke when he was six: it prickles near "
             "frightened animals, grants Speak with Animals and Animal Friendship, and has become "
             "the channel through which sleeping and possessed things speak to him (Pikachu, the "
             "Grand Custodian). It has never once stirred for a machine."),
    # Closing vignettes. Whitespace pass 2026-07: as the part's last block at
    # 3.05in the square pair overshot the page foot and jumped whole to a
    # nearly blank page (and at foot-fit sizes its trailing spacer paragraph
    # spilled and stranded a fully blank page ahead of the Part IV
    # hardbreak). Anchored mid-section, between the mark and the star it
    # depicts, the row sits safely and the closing text seals the page foot.
    # (2.4in: at 2.7in the closing paragraph's last line still spilled and
    # stranded a near-blank page before the Part IV opener.)
    ("imgfloat", "assets/characters/ursa_with_amulet.png", 3.0),
    ("body", "**The seven-point star.** Elaria's sigil, wrapped in a leafed vine (or cupped in "
             "wings, on the Sash), found on every gift along the Guardians' path. When you see it, "
             "she saw you coming."),
    ("lore", "The Warden's Price",
     "Elaria spent her power the way a candle spends itself: all at once, on purpose, so "
     "others could see. When Maldrith was sealed beyond the last wall, the Warden had nothing "
     "left but her name and her sign, the seven-pointed star wrapped in a leafed vine. She "
     "scattered what remained into small safeguards and lay down to sleep, trusting the kind "
     "to find them. So far, the old tellings say, her trust has held."),
    # Part III closes on a full-width showpiece of the Warden herself; Part IV
    # opens on its own hardbreak, so this plate fills the section-end page.
    ("img", "assets/world/elaria_goddess.png",
     "Elaria, the sleeping goddess who lit the way.", 6.5, {"crop": "3:2", "hmax": 4.6}),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    for blocks, out in ((I, "compendium/treasures_and_relics.docx"),
                        (C, "compendium/custom_compendium.docx")):
        print("built", build_doc(blocks, out))
