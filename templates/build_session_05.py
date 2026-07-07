# build_session_05.py
# The Guardians of Elaria, Session 5: The Curse of Davy Jones
# Publication build. Canon: memory/campaign_canon.md + CONTRADICTIONS.md rulings
# (C3 ghost essence, C8 Stormwind/Vigil, C9 farewell crowd, C10 dice game won,
# deck fight fought, Davy Jones destroyed for good).
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc

A = "assets"
BLOCKS = [
    ("titlepage", "THE GUARDIANS OF ELARIA", "SESSION 5",
     "The Curse of Davy Jones",
     "An illustrated adventure. Read the gold boxes aloud; the purple boxes are for the DM."),

    # Session-opening plate: dominates page 1, directly under the title block.
    ("img", f"{A}/scenes/s5_harbor_sendoff.png",
     "A grateful Havenmoor cheers the Guardians up the Stormwind's gangplank.", 6.2,
     {"crop": "3:2", "hmax": 4.5}),

    ("h1", "Previously, on The Guardians of Elaria..."),
    ("gold", "Winter came early to **Havenmoor**, and it came wrong. The **Krampusshade** slipped "
             "out of a crack between worlds and began stealing the town's children into its great "
             "creaking sack, one frosted window at a time. But three young heroes rang the **eight "
             "Winter Bells**, broke the three barriers, and drove the shadow back through its own "
             "door: banished, beaten, and thoroughly embarrassed. Every child came home. Grateful "
             "beyond words, the lorekeeper **Faelan** opened an old chest and gave the heroes three "
             "gifts: a **Frostbite Shard Dagger** for Lilly, a **Candyfang Katana** for Stabby, and "
             "an **Amulet of Guiding Light** for Ursa."),
    ("gold", "And down at the harbor, riding gently at anchor, a tall ship called the **Stormwind** "
             "waited to carry the Guardians east across the open sea, toward the clockwork spires "
             "of **Gearhaven**, where Professor Aelwyn said the Essence Sphere might finally be "
             "understood. The sea, as it turns out, had other plans."),
    ("dm", "The heroes sail into this session at **level 4**. Full creature statistics live in the "
           "compendium; a compact appendix closes the session."),

    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # Part One flows on from the recap; the page before it is well under
    # 70% full, so no hardbreak here.
    ("h1", "Part One: Fair Winds from Havenmoor"),
    ("gold", "Rosy dawn light spills over Havenmoor's busy harbor. Fishing boats lie tethered "
             "beside merchant galleys, sails unfurling in the sea breeze, and salt spray drifts "
             "across the docks with the cries of gulls. On every lamppost flutters a brightly "
             "painted banner, and every banner says the same thing: **“Thank You, Guardians of "
             "Elaria!”** Half the town has come down to the quay to see the heroes off."),
    ("gold", "**Greta Frostbough** presses warm sugarplum buns into every free hand. **Sister "
             "Merida** stands with a whole row of waving orphans, tears bright in her eyes. And "
             "some faces have traveled a long way for this morning: **Alwen**, keeper of the Old "
             "Oak Tavern in Oakshade, and **Garrick and Evelyn**, old friends from Eldridge "
             "Village, who heard what the three young strangers from the Gilded Acorn had become "
             "and could not stay away."),
    ("gold", "**Master Doran Bramblebeard**, shipwright and lighthouse keeper, strides up with his "
             "great booming laugh. **Doran:** “Not bad for a bunch of landlubbers! Saved half this "
             "town, you did!” He claps Lilly on the shoulder and ruffles Ursa's hair. Alwen hugs "
             "Stabby so hard he nearly tumbles into a barrel, then presses a small flask of fresh "
             "seawater into each hero's hands. “For luck,” she says. “Old sailor's custom. Do not "
             "ask me why, just keep it close.”"),

    ("h2", "Captain Brynn Wavewarden"),
    ("imgfloat", f"{A}/npcs/brynn_wavewarden.png", 3.0),
    ("gold", "At the top of the Stormwind's gangplank waits a tall, steely eyed woman in a "
             "weathered naval coat, brass buttons gleaming, salt streaked hair tied back in a knot "
             "so tight it could moor a ship. **Captain Brynn Wavewarden** looks the three small "
             "heroes over exactly once, and misses nothing."),
    ("gold", "**Brynn:** “Listen up. These waters run on shifting currents and hidden shoals; one "
             "misstep and we founder. I need eyes aloft, hands on the helm, strength below decks, "
             "and quick fingers on the sails. Keep your stations, follow orders to the letter, and "
             "you will make Gearhaven in one piece.”"),
    ("h2", "Learning the Ship"),
    ("gold", "The Stormwind casts off, and the crew takes the heroes in hand. High in the crow's "
             "nest perches **Old Marla**, squinting at the horizon: “Keep a weather eye, or we'll "
             "be fish bait.” At the wheel stands **First Mate Breesh**, steady as a lighthouse: "
             "“A firm hand, young'un. This wheel is trickier than it looks, like steering a wild "
             "stallion.” Up in the ropes swings **Rigging Master Hugo**: “Mind your knots! A "
             "broken line in a gale will send you flying overboard faster than a cannonball.” And "
             "down in the bilge sloshes **Quartermaster Sline** with his bucket: “Muck and bilge "
             "water will rot this deck in a week if you slack off. Don't let her drown.”"),
    ("gold", "For two bright days the heroes learn the ship from keel to masthead. Ursa takes to "
             "the crow's nest like he was born aloft, reading the water the way he reads the sky. "
             "Stabby scrambles through the rigging faster than Hugo can shout instructions. Lilly "
             "falls in love with the helm, the pumps, the pulleys, every clever working piece of "
             "the vessel. In the evenings, Captain Brynn herself teaches them knots by lantern "
             "light: bowline, clove hitch, and a curious looping knot she says her grandmother "
             "called a keepsake knot. The heroes' small hands learn every one."),
    ("img", f"{A}/scenes/s5_open_sea.png",
     "The Stormwind under full sail, two bright days east of Havenmoor.", 5.8,
     {"crop": "3:2", "hmax": 4.6}),
    ("dm", "**Learning the ship.** The crew drills each hero at a station over the two bright "
           "days; those stations become the storm rules in Part Two."),
    ("dm", "**Brynn's knot lessons** are not just color. They matter again, one session from now."),
    ("gold", "On the second night, the captain takes a private word with the party at the stern "
             "rail, her voice low under the creak of the rigging. **Brynn:** “Old sailors say "
             "Davy Jones's curse hangs on these currents. Ships found empty, crews never found at "
             "all. I do not truck with ghost stories. But keep your lucky flasks close, little "
             "ones, and do not let the sea hear you boasting.”"),

    # ------------------------------------------------------------------
    ("h1", "Part Two: The Storm in Three Great Blows", {"hardbreak": True}),
    ("bridge", "On the third day the sky went the color of old iron, and the sea rose to meet it."),
    ("gold", "Dark clouds boil up from the horizon, turning the sky into a rolling cauldron of "
             "steel and shadow. The wind shrieks like a living thing, whipping the spray into "
             "stinging needles. Captain Brynn lashes herself to the wheel beside Breesh and roars "
             "over the gale: **“We ride every blow together! Fight this storm as one, or we all "
             "go down!”** Every hero takes a station. The storm comes on in three great blows."),
    ("game", "THE STORM IN THREE GREAT BLOWS", [
        "*The Stormwind rides out the storm as a crew: every hero mans a station, and the ship "
        "endures only what her sailors endure. Play each blow as one group check at stations.*",
        "",
        "**Stations.** Each hero holds one: **Crow's Nest Lookout**, Wisdom (Perception) DC 12. "
        "**Helm**, Dexterity (Acrobatics) DC 13. **Rigging**, Strength (Athletics) DC 14. "
        "**Bilge**, Constitution DC 13.",
        "**Plotting the course.** The moment the last dock line falls, the lookout may call the "
        "safe channels from the crow's nest: Wisdom (Survival) DC 17. Success gives the whole "
        "crew **advantage** on every check during the storm.",
        "",
        "**The storm strikes three times.** At each blow, every hero rolls their station check. "
        "Count the successes and read the sea's answer:",
        "**1. The Wall of Water.** 3 to 4 successes: everyone catches their footing, no damage. "
        "2: each hero takes 1d6 bludgeoning. 1: each takes 2d6. 0: each takes 3d6 and is "
        "knocked prone.",
        "**2. The Lightning Strike.** 3 to 4 successes: no harm done. 2: each hero takes 1d4 "
        "lightning. 1: each takes 2d4. 0: each takes 3d4 and has disadvantage on their next "
        "check.",
        "**3. The Maelstrom.** 3 to 4 successes: no damage, but the ship flips. 2: each hero "
        "takes 1d8 bludgeoning and falls prone. 1: each takes 2d8 and is restrained by debris. "
        "0: each takes 3d8, falls prone, and drops whatever they are holding.",
        "",
        "**No roll saves the ship.** However bravely the crew fights, the maelstrom takes her in "
        "the end: the Stormwind capsizes, and the story continues underwater.",
    ]),
    ("img", f"{A}/scenes/s5_storm.png",
     "The sky turns to rolling iron as the storm breaks over the Stormwind.", 6.0,
     {"crop": "3:2", "hmax": 4.6}),

    ("h2", "The First Blow: The Wall of Water"),
    ("gold", "A monstrous swell rises off the port bow, its crest glowing with strange pale foam. "
             "Time slows as the wave arches high above the masts, hangs there like a held breath, "
             "then crashes down in a thunder that shakes the whole world. Marla's warning cry from "
             "the crow's nest, Ursa hauling a sailor clear of the rail, Stabby knotting a snapped "
             "line with hands quicker than the wind: the Stormwind staggers, shudders, and rises "
             "streaming from the foam. Still afloat."),

    ("h2", "The Second Blow: The Sky Splits"),
    ("gold", "Then the lightning comes. A white hot bolt cleaves the sky and strikes the main "
             "mast with a crack like the world's biggest whip. Wood shatters. Sparks hiss and arc "
             "along the wet rigging, and the great mast groans, leans, and splits. Lilly is "
             "everywhere at once, hands full of rope and clever fixes, shouting over the thunder "
             "which lines to cut and which to save. The Stormwind fights on, wounded but game."),

    ("h2", "The Third Blow: The Maelstrom"),
    ("gold", "But the sea saves its worst for last. The water itself begins to turn, slow and "
             "huge and horribly patient, and the ship's prow dips into the rim of a swirling "
             "maelstrom. The wind plunges to a howling shriek. The wheel spins free of Breesh's "
             "hands. The world tilts, and keeps tilting, and Captain Brynn's last order is "
             "swallowed whole by the roar as the Stormwind heels over, over, over: and capsizes."),
    ("game", "CAPSIZE AND CAPTURE", [
        "*The world turns over. Run this as a ladder of three saves, one scene at a time; every "
        "failure follows a hero down to the next rung.*",
        "",
        "**1. She goes over.** Dexterity saving throw DC 12 to seize a beam or rope as the deck "
        "heaves. Success: you slide into the upturned hold, soaked to the bone but unhurt. "
        "Failure: the sea rips you away; hold your breath (one round of air) before you surface, "
        "coughing, inside the capsized hull.",
        "**2. The air pocket.** Intelligence (Investigation) or Wisdom (Perception) DC 10 to "
        "find sturdy handholds and a deeper bubble of air. Failure: the water surges another "
        "foot; take 1d6 bludgeoning, fall prone, and suffer disadvantage on your first turn of "
        "the next fight. A hero still holding their breath from step 1 takes an extra 1d6 from "
        "near-drowning.",
        "**3. The spectral chains.** When the Dutchman rises beneath the wreck and its chains "
        "come snaking up through the planks: Strength saving throw DC 12 to wrestle free. "
        "Success: you burst onto the ghost ship's deck gasping but unharmed. Failure: the iron "
        "bites deep; take 1d6 slashing, arrive restrained, and make your **first roll of the "
        "Dice Game of Souls at disadvantage**.",
    ]),

    ("h2", "The Air Pocket"),
    ("gold", "Cold. Dark. The rush and boom of water. Then, gasping, the heroes surface inside a "
             "cramped pocket of trapped air under the upturned hull, hearts hammering, soaked to "
             "the bone. Darkness presses in, pierced by a ghostly green glow seeping through "
             "barnacle choked cracks. Brine laps at their ankles. Broken crates and dangling "
             "ropes swing in the gloom, and somewhere in the dark a sailor coughs, and another "
             "answers, and another: the crew, alive, clinging to the ribs of their poor drowned "
             "ship."),
    ("hero", "Stabby", "Everyone always says goblins sink. Ha! Still floating!"),
    # The rising ghost ship floats beside its own sighting: a full plate here
    # could not share page 6 with the capsize card, and stranded alone on the
    # next page it read as filler.
    ("imgfloat", f"{A}/scenes/s5_dutchman_rises.png", 3.3, {"hmax": 3.9}),
    ("gold", "And then, through the largest crack, the heroes see it. Far below, in the inky "
             "deep, something is rising. Ghost white sails unfurl in water where no wind blows. "
             "A barnacle crusted keel, vast and old and glowing sea sick green, climbs toward "
             "the wreck like a whale rising for air. The **Flying Dutchman** is coming up "
             "directly beneath them."),

    # ------------------------------------------------------------------
    ("h1", "Part Three: Aboard the Flying Dutchman", {"hardbreak": True}),
    ("gold", "A deep, resonant groan rolls through the wreck as the Dutchman's hull slides "
             "beneath it and lifts. Water sheets away. Cold luminescence floods the hold. And "
             "then, without warning, **spectral chains** snake up through the broken planks, "
             "glowing links coiling around arms and ankles like living serpents, and haul every "
             "soul aboard the wreck, heroes and sailors alike, up into the green light of the "
             "ghost ship's deck."),
    ("img", f"{A}/scenes/s5_dutchman_deck.png",
     "Spectral chains haul every soul aboard onto the Dutchman's green lit deck.", 5.8,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "The crew of the Dutchman shuffles out to meet them, and they are the funniest "
             "frightening things the heroes have ever seen: drowned sailors gone all barnacled "
             "and green, crabs riding in their beards, seaweed for hair, one with a starfish "
             "stuck to his face exactly where a starfish should not be. They herd Captain Brynn "
             "and her sailors toward the brig with mossy politeness, and march the three small "
             "heroes, still dripping, toward the hold."),

    ("h2", "The Hold of Harvested Magic"),
    ("gold", "Below decks, the Dutchman is not a ship. It is a collection. Crystal jars line "
             "the walls in racks, each one holding a captive glimmer: feywild motes swirling "
             "like caught fireflies, elemental sparks crackling in vials, soft pulsing threads "
             "of raw magic. Iron cages hold living prisoners: a dripping **water sprite** "
             "pressed against the bars, a shivering **flame salamander** burning low and "
             "frightened, an **owl-kin** with great hollow eyes that follow the heroes across "
             "the room. And stacked to the ceiling stand rows of battered crates, every one "
             "stamped with the same sigil: the mark of the **Gearhaven Artificers' Guild**."),
    ("gold", "From the shadows between the racks he comes: tall, tentacle bearded, hook handed, "
             "barnacles glowing along his arms like embers, each one holding some little trapped "
             "spark of life. **Davy Jones** taps one hooked fingertip, very gently, against the "
             "Essence Sphere at Lilly's belt, and smiles like a shipwreck."),
    # The session villain gets a big showing: a centered plate.
    ("img", f"{A}/npcs/davy_jones.png",
     "Davy Jones, captain of the Flying Dutchman.", 4.2),
    ("gold", "**Davy Jones:** “Ah. The bright spark of little Floraburst. Feywild sunlight, "
             "bottled and carried right to my door. The perfect spark to ignite my anchor and "
             "rend the veil open. Surrender her essence... or I shall harvest it by force.”"),
    ("hero", "Lilly", "You will not touch her. Not one petal."),
    ("gold", "The captain's smile widens. He gestures with the hook, and the mess deck hatch "
             "creaks open below. **Davy Jones:** “Force, then. But I am a sporting man, after my "
             "fashion. Welcome aboard, Guardians. Your souls now belong to Davy Jones... unless "
             "you can win them back. Let our game begin.”"),

    # ------------------------------------------------------------------
    # Part Four flows directly under Davy's challenge; the Davy Jones float
    # page is under half full, so no hardbreak here.
    ("h1", "Part Four: The Dice Game of Souls"),
    ("gold", "The mess deck is lit by lanterns burning a sick green. At its center stands a "
             "scarred oak table, and every scar is a name: the names of sailors who sat here, "
             "and gambled, and lost. The heroes are set on rough benches, chains clinking at "
             "their wrists, while Davy Jones looms opposite, tentacles curling around the roof "
             "beams like patient serpents. Onto the table clatter seven dice of ivory and bone: "
             "a d4, a d6, a d8, two d10s, a d12, and one yellowed old d20 that seems to watch "
             "you back."),
    ("gold", "**Davy Jones:** “Three rounds of Seven-Eyes, target seventy and seven. Win, and "
             "your chains fall and your little friend keeps her light. Lose, and I snuff out "
             "every spark of your souls... and her fey light with them.”"),
    ("game", "SEVEN-EYES: THE DICE GAME OF SOULS", [
        "*Old sailors whisper that Davy Jones has played Seven-Eyes for every soul he keeps: "
        "seven dice, two tosses, and a scarred oak table carved with the names of everyone who "
        "ever lost. Nobody living remembers the rules, because everyone who learned them stayed "
        "aboard. Here they are anyway. The target is **seventy-seven**.*",
        "",
        "**The stakes.** Three rounds. If Davy Jones scores **5 points**, he claims the heroes' "
        "souls, and Floraburst's fey light with them. If he ends with 4 points or fewer, the "
        "chains fall and every soul aboard walks free.",
        "",
        "**Your dice.** Each hero keeps a pool of seven: **d4, d6, d8, d10, d10, d12, d20**.",
        "**Each round, every hero:**",
        "**1. First toss.** Roll all seven dice and add them up: your Total.",
        "**2. First gift.** Any hero may pass one die's face value to a teammate, adjusting "
        "both totals before moving on. Teamwork is legal. Davy hates that.",
        "**3. Second toss.** Roll all seven dice again and add the new sum: your Running Total.",
        "**4. Second gift.** Over seventy-seven? You may gift one of your second-toss dice to a "
        "teammate before you bust.",
        "**5. Bust check.** Still over 77 after gifts: you bust this round, and Davy gains "
        "**1 point**.",
        "",
        "**Davy's turn.** The captain rolls all seven dice **three separate times**, and after "
        "each roll he may discard one die (the DM announces which face tumbles off into the "
        "gloom). His Final Total is the sum of the three adjusted rolls. If even his discards "
        "cannot keep him at 77 or under, the old cheat busts himself. Otherwise, every hero "
        "whose Running Total sits below his Final Total gives him **1 point**.",
        "",
        "**Table talk.** Let the dice clatter and the lantern flames shiver as each one lands. "
        "Between rounds, Davy stalks the table's edge: *“Point by point, your hearts grow "
        "colder. Will you fold, or gamble everything on the final roll?”*",
    ]),
    ("gold", "The first round is terror. The dice feel cold as drowned stones, and when Ursa's "
             "second toss threatens to burst past seventy seven, the whole table holds its "
             "breath until Lilly quietly slides her lowest die across and saves him. The second "
             "round is arithmetic and nerve: Stabby, who cannot sit still in a classroom to save "
             "his life, turns out to be terrifying at dice, counting faces and gifting exactly "
             "the right pips at exactly the right moment. Davy's grin gets thinner. His discards "
             "get angrier."),
    ("img", f"{A}/scenes/s5_dice_game.png",
     "Three rounds of Seven-Eyes at the scarred oak table.", 5.8,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "The third round comes down to the last toss of the last die. Davy Jones sits at "
             "seventy six, one smug point from feasting. The heroes' running totals hang just "
             "beneath his. Then the old yellowed d20 tumbles across the scarred names, teeters "
             "on one corner, and lands: and the heroes' total stands at **seventy seven exactly**, "
             "and the captain of the Flying Dutchman is beaten at his own table."),
    ("hero", "Stabby", "Seven-Eyes! Pay up, fish-beard!"),
    ("gold", "Davy Jones rises so fast his chair goes through the wall. The lanterns gutter "
             "green, the chains fall from the heroes' wrists like dead eels, and the captain "
             "snarls one promise as he dissolves into cold mist: **“This isn't over...”** He "
             "was wrong about that."),

    # ------------------------------------------------------------------
    ("h1", "Part Five: No Flesh Leaves This Ship", {"hardbreak": True}),
    ("bridge", "The heroes had won their souls back fairly. They could have slipped away quietly. "
               "Instead, they thought about the cages."),
    ("gold", "Two skeletal wardens, bound by the game's result and clearly disgusted about it, "
             "bow and usher the heroes toward the guest chambers to rest. But through the "
             "bulkheads comes a muffled clinking: jars being packed, cages being rattled, "
             "prisoners being made ready for shipment. And through a salt streaked porthole, "
             "Lilly spots a trim little cutter lashed near the Dutchman's rail, seaworthy and "
             "forgotten, with a name painted on her stern: the **Vigil**."),
    ("hero", "Lilly", "They are rounding up every magical being aboard. If these essences ship "
             "south, the whole coast will suffer. We are not leaving without those cages open."),
    ("gold", "The heroes step out onto the weather deck, and the ghost ship's crew is waiting. "
             "Drowned pirates haul themselves over the rails, cutlasses dripping, barnacles "
             "clacking. At the wheel, a **Spectral Helmsman** turns its lantern eyed head all "
             "the way around and wails: **“No flesh leaves this ship alive!”**"),
    ("gold", "The deck fight is wild and slippery and loud. The pirates fight like the tide, "
             "slow and heavy and everywhere; Stabby fights like the spray, bright and quick and "
             "impossible to hold. Ursa's starlight punches clean holes in the sea fog, and when "
             "the helmsman swoops down shrieking, Lilly's cannon knocks it clean through its own "
             "wheel. When each drowned pirate finally drops, it bursts in a last cold slap of "
             "seawater, which Stabby declares is “rude, even for dead people.”"),
    ("dm", "**The deck fight.** 3 Drowned Pirates and the Spectral Helmsman (appendix). The "
           "pirates fight like the tide, mobbing whoever stands closest and hurling harpoons to "
           "drag heroes apart; the helmsman swoops from the wheel, wailing (its aura: DC 12 "
           "Wisdom or frightened) and phasing through cover."),
    ("dm", "**Terrain.** Slippery deck: at the end of each turn, Dexterity (Acrobatics) DC 12 or "
           "fall prone. Once, mid-fight, a wave surge crashes the deck: everyone makes a DC 12 "
           "Dexterity save or falls prone. Each pirate's **Death Burst** on dropping: DC 12 "
           "Constitution or 2d4 cold."),
    ("dm", "**Clever options.** Climbing the rope ladder (Action plus Athletics DC 14) tips a "
           "lantern-oil bucket over a pirate below: 2d6 fire. Severing the mooring line "
           "(Strength DC 15, best once two foes are down) secures the escape route to the "
           "cutter. The party won the deck and pressed below."),

    ("h2", "Into the Heart of the Hold"),
    ("gold", "The iron bound hatch groans open and stale, salty air rushes out. Below, the hold "
             "stretches away into gloom: the racks of jars, the cages, the Guild stamped crates, "
             "and now, waking one by one, the things that guard them. The timbers themselves "
             "hum with stolen magic."),
    ("hero", "Ursa", "This is not Davy's doing alone. Something darker haunts this ship."),
    ("gold", "Lilly draws her **Frostbite Shard Dagger**, frost curling off its edge into the "
             "green dark, and her eyes narrow. **Lilly:** “Then we cut it out at the source.”"),
    ("img", f"{A}/scenes/s5_hold_of_essences.png",
     "The hold of harvested magic: crystal jars, iron cages, and crates stamped with the "
     "Gearhaven Guild sigil.", 5.8, {"crop": "3:2", "hmax": 4.6}),
    ("gold", "The guardians of the hold come all at once: a hulking **Smuggler's Golem** patched "
             "with metal plates and powered by stolen essences, two **Arcane Corsairs**, guild "
             "artificers turned pirate with enchanted sabers and no shame at all, and a "
             "**Ghost-Light Engineer**, a flickering spirit bound to the ship's arcane engines, "
             "blinking in and out of sight with lightning crawling between its fingers. Every "
             "one of them flinches from the cold. The heroes notice."),
    ("gold", "Frost becomes the whole battle plan. Lilly's dagger bites chunks from the golem's "
             "hide while Ursa's magic rimes the corsairs' sabers with ice. The engineer blinks "
             "invisible, but its glowing core betrays it, and Stabby tracks the glow through "
             "the dark and puts it out with three quick strikes. At the center of the hold "
             "pulses a great **arcane orb**, drinking power from every jar; Ursa raises his "
             "amulet and the party shatters the orb in one blinding burst of radiance that "
             "staggers every undead thing aboard."),
    ("dm", "**The hold fight.** A Smuggler's Golem, 2 Arcane Corsairs, and the Ghost-Light "
           "Engineer (appendix), every one of them **vulnerable to cold**. The golem crushes "
           "crates at the heroes (Dexterity save DC 13 or 2d6 slashing); the corsairs dart "
           "between cover, sneak-attacking where least expected; the engineer blinks invisible "
           "between Shock Touches, its glowing core still faintly visible within 5 feet."),
    ("dm", "**Terrain.** Slick planks: end of each turn, Dexterity (Acrobatics) DC 12 or fall "
           "prone. Arcane fissures leak sparks: stepping on one deals 1d6 lightning (Dexterity "
           "save DC 13 for half). Crates grant half cover, and a Strength (Athletics) DC 14 "
           "shove can slam an enemy into them."),
    ("dm", "**The central orb.** Strength or Arcana DC 15 to shatter it: a 3d6 radiant burst "
           "(Dexterity save DC 13 for half) that **stuns the undead**. And when the golem "
           "falls, its stolen core shatters with it, and every arcane fissure goes dark."),
    ("gold", "As the last foe dissolves into drifting motes, Stabby sheathes his blade and looks "
             "up at the ceiling, toward the captain's quarters. **Stabby:** “That was the heart "
             "of his operation. Now we face the head.”"),

    # ------------------------------------------------------------------
    ("h1", "Part Six: The Captain Goes Down with the Ship", {"hardbreak": True}),
    ("gold", "Lantern light pools on warped floorboards as the final hatch swings open. Davy "
             "Jones's own chambers pulse with stolen power: jars of glowing motes line the "
             "walls, and seawater drips slow and endless from a vaulted skylight onto a raised "
             "dais. On the dais, reassembled from mist and malice and very much out of patience, "
             "stands the captain himself. His hook drips brine. His tentacles curl in quiet "
             "menace."),
    ("gold", "**Davy Jones:** “Brave... or foolish. You beat my dice. You broke my hold. But "
             "the sea only knows one ending, little Guardians. Your light... my feast. Let us "
             "begin.”"),
    ("dm", "**The final duel.** Davy Jones alone (appendix), on his own dais, with the room "
           "itself fighting for him. Multiattack: two Tentacle Slams (reach 10 ft.) and a Hook "
           "Strike; Soul Siphon on a 5-6 recharge."),
    ("dm", "**Sea-fog drift.** Cold mist creeps along the floor at the start of each round. A "
           "creature that starts its turn in the fog makes a DC 13 Wisdom save or has "
           "disadvantage on attack rolls until its next turn."),
    ("dm", "**Barnacle-rimmed planks.** A hero who ends their turn within 5 feet of the dais "
           "makes a Dexterity (Acrobatics) DC 12 check or takes 1d6 slashing."),
    ("dm", "**Protect the Sphere.** If Davy turns his Soul Siphon on the Essence Sphere, a hero "
           "may use their **Reaction** to intercept the damage."),
    ("gold", "He is the worst thing the heroes have ever fought. Cold sea fog crawls across the "
             "floor and drinks their courage. Barnacles bristle along the dais like teeth. His "
             "tentacles strike from ten feet away, his hook rings off Stabby's blade, and again "
             "and again his **Soul Siphon** reaches out, a pulling green hunger, trying to drain "
             "three small souls and the bright sphere they guard. Each time, a hero throws "
             "themselves in the way of the others. Each time, the light holds."),
    ("gold", "At half strength he only laughs louder. **Davy Jones:** “I have swallowed storms "
             "older than your lifetimes! You cannot drown me!”"),
    ("hero", "Ursa", "We are not here to drown you. We are here to let everything you stole go "
             "free."),
    ("gold", "It is Lilly's frost that cracks his barnacle armor, Ursa's radiance that burns "
             "through the crack, and Stabby, running up a falling tentacle with his candy red "
             "sash streaming, who lands the last blow. Davy Jones, captain of the Flying "
             "Dutchman, comes apart the way a wave does: all at once, and forever. There is no "
             "scream. There is only a long green sigh, and then every barnacle on the walls "
             "goes dark, and the curse of Davy Jones is over for good."),
    ("gold", "All through the ship, jars crack open and cages spring wide. The freed essences "
             "rise through the broken skylight in a spiral of soft lights, hundreds of them, "
             "like stars going home. The water sprite bows to the heroes before melting "
             "gratefully into the sea. The flame salamander leaves happy little scorch marks "
             "down the corridor. The owl-kin lands once on Ursa's shoulder, hollow eyes gone "
             "warm and round, and is gone into the night air. Below, cell doors swing open, and "
             "Captain Brynn Wavewarden leads her whole crew blinking up into the strange light: "
             "every sailor of the Stormwind, alive."),

    ("h2", "The Ghost Essence"),
    ("gold", "One light does not fly away. A pale, drifting essence, cold and gentle as sea "
             "mist, circles down out of the spiral and hangs before Floraburst, who has ridden "
             "out the whole battle tucked in Lilly's pack, and who now reaches up toward it "
             "with every leaf and petal she has. Lilly cups her hands around the little ghost "
             "light, steady as her mother taught her, and guides it home."),
    ("img", f"{A}/scenes/s5_ghost_essence.png",
     "Lilly guides the pale ghost essence home to Floraburst.", 5.8,
     {"crop": "3:2", "hmax": 4.6}),
    ("game", "WHAT WILL SHE BECOME?", [
        "*Hundreds of essences spiral free, and one of them answers Floraburst's reaching "
        "petals. Which one is fate's business: the dice decide, and nobody peeks.*",
        "",
        "**The essence roll.** Roll **1d12** to learn which essence finds her: 1 Grass, 2 Fire, "
        "3 Water, 4 Electric, 5 Ice, 6 Rock, 7 Psychic, 8 Ghost, 9 Dark, 10 Fighting, "
        "11 Flying, 12 Fairy.",
        "**The extraction.** Lilly guides it home: **1d12 + her Dexterity modifier**. On 12 or "
        "higher, the essence flows in clean. On 11 or lower, the jar shatters on the way: "
        "Floraburst takes 1d6 cold damage and falls prone, but still absorbs the essence.",
        "",
        "**Sealed until she wakes.** This roll was made blind at the table: not even the "
        "players knew what their sleeping friend would become until she opened her eyes again.",
    ]),
    ("gold", "Floraburst drinks in the essence, shudders once from root to petal, and collapses. "
             "For one terrible heartbeat she is still. Then a slow pulse begins inside her, deep "
             "and rhythmic as a sleeping heart, and before the heroes' eyes each petal comes "
             "away etched in strange new patterns of frost and fire. She is not hurt. She is "
             "*changing*, into what, not even Lilly can say."),
    ("hero", "Lilly", "She is... shifting. I can see new patterns in her petals. Hold on, little "
             "one. We have got you."),

    ("h2", "The Vigil"),
    ("gold", "A low rumble rolls through the floorboards, and cracks spiderweb up the barnacled "
             "walls. With its captain gone and its stolen power flown, the Flying Dutchman is "
             "dying. The heroes and the Stormwind's crew race for the rail, cut the little "
             "cutter **Vigil** free of her lashings with Brynn's own knots, and swing her down "
             "into the black sea. Everyone piles in, Lilly cradling the sleeping, changing "
             "Floraburst against her chest, and the oars bite deep."),
    ("gold", "Behind them, the great ghost ship groans, lists, and with a sound like a very old "
             "door finally closing, **splits in two** and slides beneath the swirling foam. The "
             "green glow fades from the water. The sea rolls flat and clean, as if something "
             "that had been wrong with it for a hundred years had just been put right."),
    ("gold", "**Ursa**, gazing back: “Good riddance.” **Stabby**, panting at his oar: “Aim "
             "east! Gearhaven is that way!”"),
    ("gold", "They row east through the small hours, trading the oars, humming Old Marla's "
             "watch songs, while the sky slowly lightens ahead of them. And as dawn comes up "
             "gold over the water, the heroes see it at last on the horizon: the faint, "
             "gleaming silhouette of clockwork spires. In Lilly's arms their little friend "
             "sleeps on, pulsing gently, petals etched with frost and fire, becoming whatever "
             "she is going to be."),
    ("divider",),
    ("bridge", "The curse of Davy Jones was ended, the stolen magic freed, and every soul of "
               "the Stormwind saved. But the crates below had worn the Gearhaven Guild's "
               "sigil, and somebody south was expecting a shipment that would never come. And "
               "the coast ahead held one more port: a fogbound little town of lanterns and "
               "pumpkins where no one seemed to remember anything wrong at all. In Lilly's "
               "arms, Floraburst went on quietly changing."),
    # Closing showpiece: dawn over the water closes the chapter, with the
    # level note and teaser as the chapter's final lines beneath it.
    ("img", f"{A}/scenes/s5_vigil_dawn.png",
     "The Vigil rows east at dawn, Gearhaven's spires gleaming on the horizon.", 6.2,
     {"crop": "3:2", "hmax": 4.6}),
    ("dm", "Ending this voyage carried the heroes to **level 5**. They return at level 5 next "
           "session."),
    ("gold", "*Next: Session 6, in which the fog rolls in over Wraithpine, the Guardians learn "
             "why you should always tie a keepsake knot, and their sleeping little friend "
             "finally opens her eyes.*"),

    # ------------------------------------------------------------------
    ("h1", "Appendix: Creatures of Session Five", {"pagebreak": True}),
    ("body", "Compact statistics for the table. The full bestiary, with lore and pictures, lives "
             "in the compendium."),
    ("stat", "Davy Jones, Captain of the Flying Dutchman", [
        "Medium undead (formerly humanoid), chaotic evil. **CR 6** (2,300 XP). AC 17 (Barnacle "
        "Armor), HP 85 (10d10 + 30), Speed 30 ft., swim 30 ft.",
        "STR 18, DEX 12, CON 16, INT 14, WIS 12, CHA 16. Saves Con +6, Wis +4, Cha +6; "
        "Intimidation +6, Athletics +7, Perception +4.",
        "Resistances nonmagical B/P/S. Immune to charmed, frightened, poisoned, exhaustion. "
        "Darkvision 60 ft. Amphibious.",
        "**Barnacle Armor.** Nonmagical melee attacks deal half damage. **Legendary Resistance "
        "(3/Day).**",
        "**Multiattack.** Two Tentacle Slams and one Hook Strike.",
        "**Tentacle Slam.** +7, reach 10 ft., 10 (2d6 + 4) bludgeoning and grapple DC 15.",
        "**Hook Strike.** +7, reach 5 ft., 8 (1d6 + 4) piercing plus 7 (2d6) necrotic.",
        "**Soul Siphon (Recharge 5-6).** DC 14 Con or 18 (4d8) psychic; Davy heals half the "
        "damage dealt.",
        "**Legendary Actions (2/round).** Tentacle Strike (one slam); Raise Tide (2 actions): "
        "20-ft. line, DC 14 Dex or 13 (3d8) bludgeoning.",
    ]),
    ("stat", "Drowned Pirate", [
        "Medium undead, chaotic evil. **CR 1**. AC 14, HP 58 (9d8 + 18), Speed 30 ft., swim 30 ft.",
        "Resistant to nonmagical B/P/S; immune to poison; immune to charmed, frightened, "
        "exhaustion. Amphibious; Undead Fortitude.",
        "**Multiattack.** Two melee attacks. **Cutlass.** +6, 8 (1d8 + 4) slashing. "
        "**Harpoon.** +6, reach 10 ft. or range 30/120 ft., 9 (1d10 + 4) piercing and grappled "
        "(escape DC 14).",
        "**Death Burst.** When the pirate dies it bursts: each creature within 5 ft., DC 12 Con "
        "or 5 (2d4) cold damage.",
    ]),
    ("stat", "Spectral Helmsman", [
        "Medium undead, chaotic evil. **CR 1**. AC 12, HP 45 (6d8 + 18), fly 50 ft. (hover).",
        "Incorporeal Movement. Immune to cold, necrotic, poison and to most conditions.",
        "**Sea-Wraith Aura.** Start of its turn, creatures within 5 ft.: DC 12 Wis or frightened "
        "until their next turn.",
        "**Multiattack.** Two Spectral Scimitars: +4, 7 (1d6 + 4) force. **Harpoon Throw.** +4, "
        "range 20/60 ft., 9 (1d10 + 4) piercing and pulled 10 ft.",
        "**Phantom Helm Block (Reaction).** Imposes disadvantage on one weapon attack.",
    ]),
    ("stat", "Smuggler's Golem", [
        "Large construct, unaligned. **CR 2**. AC 14 (natural armor), HP 85 (10d10 + 30), "
        "Speed 30 ft. **Vulnerable to cold.**",
        "Immutable Form; Magic Resistance; immune to poison, psychic, nonmagical B/P/S.",
        "**Multiattack.** Two Slams: +7, reach 10 ft., 2d8 + 5 bludgeoning.",
        "**Crush Crate (Recharge 5-6).** 6d6 damage, DC 15 Dex half; creatures hit are knocked "
        "prone.",
        "**Reinforced Hide (Reaction).** +2 AC against one melee attack.",
    ]),
    ("stat", "Arcane Corsair", [
        "Medium humanoid, chaotic neutral. **CR 1**. AC 14 (studded leather), HP 52 (7d8 + 21), "
        "Speed 30 ft. **Vulnerable to cold.** Guild artificers turned pirate.",
        "Saves Dex +5, Cha +4; resistant fire, lightning; immune to frightened.",
        "**Sneak Attack (1/turn).** +2d6 with advantage or an adjacent ally. **Parry.** +2 AC "
        "against one melee attack.",
        "**Multiattack.** Two Arcane Sabers: +5, 1d8 + 3 slashing plus 1d6 force.",
        "**Riposte (Recharge 5-6).** Reaction attack after a missed melee attack.",
    ]),
    ("stat", "Ghost-Light Engineer", [
        "Tiny undead, neutral evil. **CR 2**. AC 15 (natural armor), HP 27 (6d4 + 12), fly 50 "
        "ft. (hover). **Vulnerable to cold.**",
        "Immune to necrotic, poison, psychic; resistant to nonmagical B/P/S, acid, fire, "
        "lightning, thunder.",
        "**Invisibility (Recharge 4-6).** Invisible until it attacks or casts; its Glowing Core "
        "still shines faintly within 5 ft.",
        "**Shock Touch.** +6, 2d6 + 2 lightning. **Arcane Pulse (Recharge 5-6).** 10-ft. cone, "
        "4d6 force, DC 13 Dex half.",
        "**Engineered Reflexes (Reaction).** Halves the damage from one attack or spell.",
    ]),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    out = build_doc(BLOCKS, "sessions/session_05_curse_of_davy_jones.docx")
    print("built", out)
