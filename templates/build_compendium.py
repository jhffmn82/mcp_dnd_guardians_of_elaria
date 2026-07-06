# build_compendium.py
# The Guardians of Elaria: running reference volumes.
# Builds three docx files in compendium/: bestiary, magic items, custom content.
# Rebuild after each session revision; add entries as play continues.
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc

NOTE = "A running reference for The Guardians of Elaria. Updated as the chronicle grows."

def title(kicker, sub):
    return ("titlepage", "THE GUARDIANS OF ELARIA", kicker, sub, NOTE)

# ----------------------------------------------------------------------
# VOLUME I: BESTIARY
# ----------------------------------------------------------------------
B = [
    title("THE BESTIARY", "Creatures of the Chronicle"),
    ("gold", "Every strange creature the Guardians have faced, befriended, or freed. Motes mark "
             "the planar wanderers: when one falls, a gleam of its home plane rises and fades. "
             "Compact statistics live with each session's appendix; this volume gathers the whole "
             "menagerie with its lore."),

    ("h1", "Companions", {"pagebreak": True}),
    ("h2", "Ghostbloom (formerly Floraburst)"),
    ("img", "assets/characters/ghostbloom.png", "Ghostbloom, Elaria's little voice.", 3.6),
    ("body", "**Tiny fey, chaotic good.** The party's companion since Session 3, chosen from "
             "Professor Aelwyn's three wards as **Floraburst**, a leafy sprout-backed creature that "
             "loved sunlight and berries. Aboard the sinking Dutchman (Session 5) Lilly infused her "
             "with a Ghost essence drawn from the harvest jars; the change began there and completed "
             "in Wraithpine's ghost-light (Session 6). Now her petals are glass-pale and chime like "
             "frost, she floats, speaks in soft telepathy, and glows brighter near planar wounds: "
             "Elaria's voice, some say."),
    ("stat", "Ghostbloom", [
        "Tiny fey (Ghost/Grass), chaotic good. AC 15, HP 52 (8d4 + 32), fly 30 ft. (hover).",
        "Vulnerable fire AND cold (mind the friendly fire). Resistant necrotic, poison, nonmagical weapons.",
        "**Guardian's Light.** Reaction, 3/short rest: heal an ally 1d8 + 3; ends charm or fear; sheds light.",
        "**Vine Lash / Ghostly Wail.** See the v3 statblock (characters/ghostbloom_statblock_v3.pdf).",
    ]),
    ("h2", "Pikachu, the Spark Fox"),
    ("body", "**The spark in the Sphere.** An old friend of the Glimmergear family, bodiless since "
             "before the chronicle began, sleeping inside the Essence Sphere. His golden projection "
             "first appeared in Gearhaven (Session 8): two long ears, a lightning-bolt tail, and a "
             "warning carried through Ursa's Mark. He is more than a lost friend; he is a key. His "
             "full return is coming."),
    ("h2", "Lickgloom"),
    ("body", "**Small fey of the pond (CR 1).** Befriended on the party's first night (Session 1): "
             "round bodied, endlessly curious, with a tongue longer than it is tall and a telepathic "
             "voice of feelings (*Food? Friend?*). Traveled with the party to Ravenstone Laboratory, "
             "where it chose to stay among Professor Aelwyn's creatures. Visits are owed."),

    ("h1", "Session 1: The Forest of Whispers", {"pagebreak": True}),
    ("body", "**Duckleaf (CR 4).** Elemental Air. A sturdy duck with a leek for a sword, wind-quick "
             "and proud, guardian of the rune-stone circle. Its gusts died with the circle's stones. "
             "Left a green air mote."),
    ("body", "**Cognifin (CR 3).** Elemental Water. The psychic guardian of the Grove of Elemental "
             "Waters; tested the party with waves and whirlpools, and yielded with grace. Left a "
             "blue water mote."),
    ("body", "**Mist Stalkers (CR 2).** Feywild predators of fog and fear, hunting the Oakshade "
             "road. Their howls scatter the timid; the party stood back to back and did not scatter."),

    ("h1", "Session 2: The Road to Ravenstone"),
    ("body", "**Mudskips (CR 1/2).** Slick little water elementals ambushing from a muddy clearing; "
             "dissolved into water motes."),
    ("body", "**The Grimfang war band.** A rival goblin clan with an old grudge against the "
             "Bloodfang: two goblins, a worg, an orc, a hobgoblin, and a scar-faced boss who taunted "
             "Stabby and regretted it. Driven off, not destroyed; grudges keep."),
    ("img", "assets/monsters/grimfang_clan.png", "The Grimfang, the rival clan.", 4.6),
    ("body", "**Terranox (CR 4).** A serpent of living stone from the Plane of Earth, blocking the "
             "mountain path with no interest in parley. Collapsed into inert rock; left an Earth Mote "
             "and fragments the party still carries."),

    ("h1", "Session 3: The Road South"),
    ("body", "**Shadowflame (CR 4).** A shadow wreathed in cold fire, fighting behind three illusory "
             "duplicates in Brambleshadow Thicket. Left a dark mote that felt wrong to hold."),
    ("body", "**Displacer Beasts (pair).** Six-legged, tentacled, and impossibly, TALKING ("
             "\"Fresh prey... too easy.\"): planar distortion gives old monsters new tricks. Their "
             "fall revealed rune-tears in the forest floor."),
    ("body", "**Shroomytes (CR 2, four).** Fungal wardens of a glowing grove in the Ironroot Hills "
             "(\"The grove... must be protected!\"). Left a fungal mote."),

    ("h1", "Session 4: The Longest Night of Havenmoor", {"pagebreak": True}),
    ("body", "**The Krampusshade (CR 5).** Once a guardian of winter, twisted by bitterness into a "
             "ten-foot goat-horned fiend with chains of frost and a burlap sack that swallowed "
             "children's laughter. His power hid behind three barriers of darkness; eight holiday "
             "bells rung in harmony unmade him, and every child came home safe."),
    ("stat", "Krampusshade", [
        "Large fiend, chaotic evil. **CR 5**. AC 15, HP 102.",
        "**Claw and Chains of Despair** multiattack; **Gift of Despair** (fear); **Icy Retaliation** (reaction);",
        "**Shadow Step** (legendary). Weakened by the eight Winter Bells rung together.",
    ]),
    ("body", "**His winter court.** Shadow imps (CR 2), Frozen Wolves, Frostbite Pixies, an Icy "
             "Specter at the Whispering Hollow, Enchanted Snowmen, Frost Golems, a Yule Cat, a Frost "
             "Hag, Ice Spiders, Frozen Will-o'-Wisps: the frozen roads bred dangers all that week. "
             "Friendlier meetings too: a resting reindeer whose glowing nose blessed kind travelers, "
             "and Aurora Spirits, messengers of Elaria."),

    ("h1", "Session 5: The Flying Dutchman"),
    ("body", "**Davy Jones (CR 6).** Captain of the Flying Dutchman: barnacle armor, a hook hand, "
             "tentacled beard, and a hold full of stolen magic. He harvested essences and caged "
             "magical creatures for shipment south in crates stamped with a guild sigil. He gambled "
             "for souls (Seven-Eyes, target 77) and lost; he fought, and lost; and when the Dutchman "
             "split and sank, he went down with it, for good."),
    ("stat", "Davy Jones, Captain of the Flying Dutchman", [
        "Medium undead, chaotic evil. **CR 6**. AC 17 (barnacle armor), HP 85.",
        "**Soul Siphon**, hook and tentacles, Legendary Resistance, lair actions aboard the Dutchman.",
    ]),
    ("body", "**His drowned crew.** Drowned Pirates (CR 1, burst when destroyed), a Spectral "
             "Helmsman (CR 1), a Smuggler's Golem (CR 2), Arcane Corsairs (guild artificers gone "
             "pirate), and a Ghost-Light Engineer: all vulnerable to cold, all gone down with the ship."),

    ("h1", "Session 6: The False Hydra of Wraithpine", {"pagebreak": True}),
    ("img", "assets/monsters/false_hydra.png", "The False Hydra beneath the Old Theater.", 4.6),
    ("body", "**The False Hydra.** The worst monster the Guardians have faced, because no one knew "
             "it was there: a pale many-necked thing beneath the Old Theater whose endless song made "
             "the whole village forget the people it took. Beeswax in the ears let the truth through. "
             "The tavern head died in the Gasping Gull; the body and its four heads died in the "
             "drowned orchestra pit; and the moment the song stopped, every stolen name came flooding "
             "home."),
    ("stat", "False Hydra (adult)", [
        "Huge aberration, unaligned. Body AC 15, HP 130; Heads AC 14, HP 45 each (tavern head HP 70).",
        "**Song of Unremembering.** DC 15 Wisdom within 60 ft.; beeswax earplugs grant advantage.",
        "**Vital Link.** The body resists weapons while any head lives. Legendary actions per living head.",
    ]),
    ("body", "**Festival frights.** Animated Scarecrows and six Strawlings on Pumpkin Row; rats and "
             "rat swarms in Maera's cellar; restless Zombies at the graveyard rite. All echoes of the "
             "hydra's hungry song."),

    ("h1", "Session 8: Gearhaven, the Clockwork City"),
    ("body", "**Rogue Servitors (CR 2) and the Cargo Hauler (CR 3).** Pinion's delivery constructs "
             "with red-lit eyes, seized by something that reached INTO them. Shut-off levers ended it "
             "kindly. The Hauler hated lightning."),
    ("body", "**Voltcrawlers (swarm of 6) and the Broodmother.** Skittering planar intruders pouring "
             "from the Underworks rift, phase-blinking between strikes (force and radiant pinned them "
             "down). Slain crawlers collapsed into motes; the Sphere drank them."),
    ("body", "**Iron Drudges (three) and Corrupted Sproutlings.** The Verdant Plaza's own caretaker "
             "machines and garden, turned by corruption bleeding up through the cracks. Vulnerable "
             "to fire; freed, not killed: corruption leaks out of a felled Drudge like smoke."),
    ("img", "assets/session_08/beat_5/iron_drudge.png", "An Iron Drudge in the Verdant Plaza.", 4.2),
    ("body", "**The Grand Custodian.** Gearhaven's beloved gentle giant, keeper of the Great "
             "Governor, possessed by the corruption and grieving inside it. Legs toppled, core "
             "reached, and with the last blow the corruption drained away; the freed Custodian "
             "warned of something old and hungry reaching through, and Ursa's Mark granted it rest. "
             "Its freedom closed every rift in the city."),
    ("stat", "The Grand Custodian (possessed)", [
        "Gargantuan construct. Body AC 17, HP 220; Legs (x2) AC 15, HP 90 each. Two phases: Standing, Crashed.",
        "**Chain Lightning Burst** (deflected by Stabby's awakening). A gentle death, never an execution.",
    ]),
]

# ----------------------------------------------------------------------
# VOLUME II: MAGIC ITEMS & RELICS
# ----------------------------------------------------------------------
I = [
    title("TREASURES & RELICS", "The Magic of the Chronicle"),
    ("gold", "Every treasure of the Guardians' road, from a mother's parting gift to the relics of "
             "a sleeping goddess. Items marked with the seven-point star are Elaria's own."),

    ("h1", "The Great Mysteries", {"pagebreak": True}),
    ("h2", "The Essence Sphere"),
    ("body", "Brass and crystal, warm as a heartbeat, made by the deep-gnome masters of Glimmerspire "
             "BEFORE the cracks ever opened (how they knew is a question nobody has answered). It "
             "holds Pikachu's sleeping spark, and it is a GATHERER: it pulls loose planar motes to "
             "itself and survives holding them, which no other vessel can. It is the missing anchor "
             "of Vane's Rift Portal, and it never leaves the party's keeping. Gained **Planar "
             "Attunement** at the Whispering Glade (advantage on Arcana concerning planar magic)."),
    ("h2", "The Three Enchanted Potatoes"),
    ("body", "Ash Catchum's legacy to his son: three unassuming potatoes that are anything but. The "
             "goddess named them **remnants of a shattered covenant**, safeguards bound from her own "
             "essence in the old lore (Healing, Transformation, Insight). They pulse when the world "
             "thins. Their hour has not yet come."),
    ("h2", "Stabby's Idol"),
    ("body", "A small carved figure Stabby found tucked in his bag after Wraithpine, though nobody "
             "saw who put it there. It goes ice cold near rifts, and corruption recoils from it. It "
             "has dreams in it. That is all anyone knows, yet."),

    ("h1", "Relics of Elaria (the Wraithpine Chest)", {"pagebreak": True}),
    ("body", "One half-buried chest, bound in vines of silver and root, opened by Ghostbloom's song "
             "beneath the Old Theater. Inside, three gifts, each bearing the seven-point star."),
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

    ("h1", "Gifts of Faelan (Havenmoor, Session 4)", {"pagebreak": True}),
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

    ("h1", "Boons, Baubles & Blessings"),
    ("body", "**Elaria's boons (the Whispering Glade, Session 2):** Ursa, Planar Awareness (sense "
             "planar disturbances, 24 hours); Lilly, the Sphere's Planar Attunement; Stabby, Glimpse "
             "of Possibility (one reroll, because the goddess smiled at the goblin)."),
    ("body", "**The eight Winter Bells (Session 4).** C, D, E, F, G, A, B, High C: relics of "
             "Elaria's light hidden across Havenmoor. Rung in harmony they unmade the Krampusshade. "
             "**Faelan's Frosted Cookies:** 2d8 healing, a short rest's comfort, and one spell slot, "
             "in cookie form."),
    ("body", "**Curios of the road.** The Shadow-Touched Rune Fragment (advantage vs fear, 1 hour); "
             "the Dark Fragment of Stormwatch Cliffs (crystallized chaos, evidence of sabotage); "
             "Terranox's stone fragments; beeswax earplugs that beat a monster's song; a bell-handled "
             "blue lantern from Pumpkin Row; Alwen's flasks of lucky seawater."),
]

# ----------------------------------------------------------------------
# VOLUME III: CUSTOM CONTENT (feats, subclasses, house rules)
# ----------------------------------------------------------------------
C = [
    title("THE CUSTOM COMPENDIUM", "Subclasses, Paths & House Rules"),
    ("gold", "Homebrew and rulings of this table: the paths the heroes may walk after the year "
             "apart, and the standing rules of the campaign. 2024 rules throughout; house rules "
             "override the books."),

    ("h1", "House Rules & Standing Rulings", {"pagebreak": True}),
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

    ("h1", "Warrior of Breathing (Stabby's Path)", {"pagebreak": True}),
    ("img", "assets/characters/stabby_breathing_style_water.png", "Water Breathing: the flowing style.", 4.0),
    ("body", "A homebrew monk subclass taken at level 7 in place of Kensei (full document: "
             "characters/path_rewards/warrior_of_breathing_v2.pdf). A Warrior of Breathing kindles "
             "an inner style, a visible breath that wreathes the blade. All roads grant the "
             "**Nichirin Katana** (+2, finesse, monk weapon, glows when breath is kindled, Cleansing "
             "Edge against corrupted creatures), and the First Form replaces Flurry of Blows."),
    ("body", "**Water Breathing** (the Whispering Breeze Monastery road): pale blue breath, +2 cold "
             "damage, Flowing Guard (+2 AC against the first attack each round), First Form: Flowing "
             "Strike (3d8 + Dex cold, knocks prone)."),
    ("body", "**Beast Breathing** (the reform-the-Bloodfang road): blood-red breath, +2 force "
             "damage, Beast Sense, advantage on Dexterity saves and +10 speed while ignited, First "
             "Form: Devour (3d8 + Dex force; a felling blow refunds the Focus)."),
    ("body", "**Shadow Breathing** (the Idol's Dreams road): violet-black breath, +2 necrotic "
             "damage, permanent darkvision 60 ft. and Stealth advantage, half cover against ranged "
             "attacks while ignited, First Form: Umbral Slash (teleport, a cube of darkness, "
             "3d8 + Dex necrotic with advantage)."),

    ("h1", "Paths of the Stars (Ursa's Path)"),
    ("body", "Chosen at level 7 (full document: characters/path_rewards/ursa_path_rewards_v2.pdf)."),
    ("body", "**Starlit Channeler** (the Circle road): learns Shillelagh; the Starry Form gains a "
             "FOURTH constellation, the **Warden**: kindle the staff as part of the same bonus "
             "action, radiant +1d6 rider (2d6 at 11, 3d6 at 17), lasting as long as the form. The "
             "Staff wakes further: 6 charges, brighter starlight."),
    ("body", "**Reader of Omens** (the Father's Trail road): **Weal and Woe**, a pool of "
             "Wisdom-modifier omens applied AFTER a d20 is rolled; and **Ash's Sigil-Stone**, "
             "1/long rest Aura of Vitality without a slot, carrying a half-finished sigil of Elaria "
             "that has more to say."),
    ("body", "**Beast Handler** (the Living World road): Summon Beast always casts at the highest "
             "level Ursa can cast, Wild Speech with his summons, and the **Wildheart Token**: a "
             "named beast-friend whose shape the spirit always takes, and who refuses to die "
             "(1/day drops to 1 HP instead of 0)."),

    ("h1", "Glimmerstone Artifacts (Lilly's Path)"),
    ("img", "assets/items/boomstick.png", "The Boomstick, if Lilly walks the Glimmerspire road.", 3.6),
    ("body", "Chosen at level 7 (full document: characters/path_rewards/glimmerstone_artifacts_v2.pdf). "
             "Every road keeps her at exactly three attunements."),
    ("body", "**The Sentinel** (the stay-and-build road): the Pocket Dynamo rebuilt into a Medium "
             "construct guardian. AC 18, HP 5 + 5 per level, no duration. Force Blast (120 ft., "
             "2d8 + INT) or Electric Pulse (15 ft., jolts Reactions away); Guardian Protocol "
             "(reaction temp HP); self-mending; reboots with a spell slot if destroyed. Replaces the "
             "Eldritch Cannon while attuned."),
    ("body", "**The Boomstick** (the Glimmerspire road): +2 repeating pistol, 1d10 thunder, never "
             "reloads; a Wand of the War Mage and Arcane Firearm (+1d8 thunder) in one; Concussion "
             "knockback; channels True Strike."),
    ("body", "**The Awakened Essence Sphere** (the researcher road): Mote Channeling (2/short rest "
             "shared pool): a base Aether Ward (2d8 + INT temp HP to allies within 15 ft.) and five "
             "LOCKED elemental discharges, one unlocking per Mote installed in the Rift Portal's "
             "ring."),
    ("img", "assets/items/awakened_essence_sphere.png", "The Awakened Essence Sphere.", 3.6),

    ("h1", "Marks & Mysteries"),
    ("body", "**Ursa's Mark of Handling.** A dragonmark that woke when he was six: it prickles near "
             "frightened animals, grants Speak with Animals and Animal Friendship, and has become "
             "the channel through which sleeping and possessed things speak to him (Pikachu, the "
             "Grand Custodian). It has never once stirred for a machine."),
    ("body", "**The seven-point star.** Elaria's sigil, wrapped in a leafed vine (or cupped in "
             "wings, on the Sash), found on every gift along the Guardians' path. When you see it, "
             "she saw you coming."),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    for blocks, out in ((B, "compendium/bestiary.docx"),
                        (I, "compendium/treasures_and_relics.docx"),
                        (C, "compendium/custom_compendium.docx")):
        print("built", build_doc(blocks, out))
