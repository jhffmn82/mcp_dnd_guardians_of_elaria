# build_session_03.py
# The Guardians of Elaria, Session 3: The Quest for Knowledge
# Publication build. Canon: memory/campaign_canon.md + CONTRADICTIONS.md rulings.
# Key rulings applied: C6 (no restaged Aelwyn introduction; this session opens the
# next morning at the laboratory), C4 (Lickgloom stays at Ravenstone with Aelwyn),
# Havenmoor over "Brightshore Harbor", Emberpaws described as a fiery fox-like
# quadruped (the original's one "bird-like" line was an error).
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc

A = "assets"
BLOCKS = [
    ("titlepage", "THE GUARDIANS OF ELARIA", "SESSION 3",
     "The Quest for Knowledge",
     "An illustrated adventure. Read the gold boxes aloud; the purple boxes are for the DM."),

    ("h1", "Previously, on The Guardians of Elaria..."),
    ("gold", "In **Oakshade Village**, the missing herb gatherers wandered home dazed but safe the "
             "morning after the Mist Stalkers fell, and Elder Merwin paid his fifty gold with pride. "
             "On the road east the rival **Grimfang** goblins sprang their ambush and learned, loudly, "
             "why nobody ambushes Stabby Sharpblade twice. At the **Whispering Glade**, a sleeping "
             "goddess opened her eyes inside a vision: **Elaria**, her light fading, asking three "
             "young heroes for help, and leaving each of them a gift of her grace. The stone guardian "
             "**Terranox** tested their mettle and let them pass. And as the sun set over the cliffs, "
             "the party reached **Ravenstone Laboratory**, where the planar researcher **Professor "
             "Aelwyn Ravenstone** welcomed them among his impossible creatures and gave them warm "
             "beds for the night."),

    # ------------------------------------------------------------------
    # Half-page establishing plate: fills out page 1 beneath the recap.
    ("img", f"{A}/npcs/ravenstone_laboratory_dalle.webp",
     "Ravenstone Laboratory in the morning light.", 6.0, {"crop": "3:2", "hmax": 4.6}),

    # ------------------------------------------------------------------
    ("h1", "Part One: A Morning of Marvels", {"hardbreak": True}),
    ("bridge", "The heroes woke on their first morning at Ravenstone Laboratory, in a tower where "
               "magic and science share every shelf."),
    ("gold", "Morning sun filters through the high, arched windows of **Ravenstone Laboratory**, "
             "laying golden beams across tables cluttered with strange instruments and arcane "
             "diagrams. Soft, multicolored lights drift through the air, each one a captured mote of "
             "magical essence. Shelves climb the walls, crowded with ancient tomes, glowing crystals, "
             "and devices of intricate gears and shimmering runes. Small automatons scurry between "
             "the tables carrying tools, and somewhere below, one of the laboratory's remarkable "
             "creatures is snoring."),

    ("h2", "The Essence Sphere Under the Glass"),
    ("gold", "**Professor Aelwyn Ravenstone** is already at his workbench, a delicate tool like a "
             "magnifying glass laced with arcane runes in one hand, and the **Essence Sphere** "
             "glowing gently before him. He has clearly been up since dawn. His silver hair glimmers "
             "in the sunlight, and his emerald eyes are wide with wonder."),
    # The workbench study floats right beside the morning dialogue.
    ("imgfloat", f"{A}/scenes/s3_sphere_examination.png", 3.3, {"crop": "4:5", "hmax": 4.2}),
    ("gold", "**Aelwyn:** “By the Spheres! Even after a whole morning's study I can scarcely "
             "believe it. A fully functional Essence Sphere! Poots Glimmergear is a true genius of "
             "her craft. This device is beyond what I thought possible.”"),
    ("gold", "**Lilly**, hovering at his elbow: “But can you help him? Pikachu is trapped in "
             "there. He needs a body again.”"),
    ("gold", "Aelwyn turns the Sphere slowly, and the runes along his lens glow brighter. His face "
             "is kind, and honest, and that is exactly the problem: Lilly can read the answer in it "
             "before he speaks."),
    ("gold", "**Aelwyn:** “The energy within is stable, wonderfully stable. Your friend is safe. "
             "But there simply is not enough of it to weave him a body. I cannot do it here.” He "
             "raises a finger before Lilly's face can finish falling. “But there is hope. The "
             "**Artificer's Guild** in **Gearhaven City** commands power core technology far beyond "
             "my little tower. Upgraded with a proper core, this Sphere could hold many essences at "
             "once, more than enough for your Pikachu to step back into the world.”"),

    # The Essence Sphere section fills page two past the seventy percent mark;
    # break here so the Guardian section carries its page instead of stranding
    # a half-empty part-final page.
    ("pagebreak",),
    ("h2", "The Guardian of Balance"),
    ("gold", "Aelwyn's gaze drifts to the little collection the party has gathered on their travels: "
             "faint captured orbs of water, air, and earth, each one humming softly in its jar."),
    ("gold", "**Aelwyn:** “These motes of yours are not stray magical oddities. They are "
             "fragments of planar essence, torn loose from their home realms. The balance of the "
             "planes is unraveling, and creatures are slipping through the cracks.”"),
    ("gold", "**Ursa**, quietly: “We saw something on the road. A goddess, I think. Her name "
             "was Elaria. She said her power was fading, and that we needed to restore it.”"),
    ("gold", "The professor goes very still. When he speaks again, the scientist's excitement is "
             "gone, and something older and graver has taken its place."),
    # Portrait floats beside the map and the professor's charge; the tall
    # 4:5 crop carries the page to a fuller foot.
    ("imgfloat", f"{A}/npcs/professor_aelwyn_dalle.webp", 3.3, {"crop": "4:5", "hmax": 4.2}),
    ("gold", "**Aelwyn:** “Elaria. The Guardian of Balance. Children, if *her* power is waning, "
             "then the boundaries between the planes will not merely leak. They will collapse. "
             "Everything you have seen, the motes, the strange creatures, the thin places in the "
             "forest, all of it is a world teetering on the brink.”"),
    ("gold", "He crosses to a great ancient map on the wall, the realms of Elaria drawn in faded "
             "ink. Lines of light crisscross it like threads in a loom, and here and there a point "
             "pulses with unstable energy, like a fraying knot."),
    ("gold", "**Aelwyn:** “If you would restore the goddess, you will need more than courage. "
             "You will need knowledge, allies, and tools forged where magic and technology meet. The "
             "Artificer's Guild can upgrade your Sphere, yes. But its archives may also hold the "
             "secret of how to stitch a world back together.”"),

    # ------------------------------------------------------------------
    ("h1", "Part Two: Three Small Wonders", {"hardbreak": True}),
    ("bridge", "Before the road, the professor had one more gift to offer: a choice that would "
               "change the party forever."),
    ("gold", "As Aelwyn speaks, the laboratory's smallest residents come out to investigate the "
             "visitors. A leafy little dinosaur with a folded flower bud on its back lounges in a "
             "sunbeam by the window: a **Floraburst**. A round turtle-like creature wrapped in a "
             "shimmering watery aura waddles past, peering up curiously: an **Aqualump**. And a "
             "small fox-like creature with flames dancing harmlessly along its paws and tail darts "
             "between the table legs, chasing an automaton twice its size: an **Emberpaws**."),
    # The three little wonders float right beside Aelwyn's offer.
    ("imgfloat", f"{A}/scenes/s3_choose_companion.png", 3.2),
    ("gold", "**Aelwyn:** “These little ones are manifestations of the unstable boundaries, each "
             "one carrying a fragment of elemental essence. They are not curiosities. They are "
             "clues. And they can sense planar anomalies long before you or I could.” He kneels "
             "among the three creatures and smiles. “Take one of them with you. Choose wisely; "
             "these little ones are eager to help, and one of them may be the key to understanding "
             "the forces that threaten our world.”"),
    ("gold", "The party crouches down among the three wonders. Aqualump blows a solemn bubble. "
             "Emberpaws sets a very small patch of nothing important on fire, then looks proud. And "
             "the little Floraburst rises from her sunbeam, pads straight across the floor, and "
             "rests her leafy head against Lilly's knee, her bud swaying like a tiny banner. Some "
             "choices make themselves."),
    # The chosen companion floats right beside her adoption.
    ("gold", "**Lilly**, softly: “Hello, Floraburst. Want to come save the world with us?”"),
    ("dm", "**Floraburst** joins the party (statistics in the appendix). She senses planar "
           "anomalies, produces healing Floraberries, and is, by unanimous ruling, a very good "
           "dinosaur."),

    ("h2", "A Farewell to Lickgloom"),
    ("gold", "One companion arrives, and one stays behind. All morning **Lickgloom** has been "
             "everywhere at once: tasting beakers, startling automatons, trading tongue flicks with "
             "creatures no book has ever named. The little fey has not looked this happy since the "
             "night at the pond. Aelwyn watches it herd a family of glimmering hatchlings across the "
             "floor and chuckles."),
    # The farewell scene floats right beside Aelwyn's offer of a home.
    ("imgfloat", f"{A}/scenes/s3_lickgloom_farewell.png", 3.3),
    ("gold", "**Aelwyn:** “You know, the road to Gearhaven is long, and a laboratory full of "
             "planar creatures could use a friendly guide who speaks their language. Lickgloom "
             "would have a home here. Friends here. And you would always know where to find it.”"),
    ("gold", "The party gathers around their first friend of the wilds. Lickgloom tilts its head, "
             "looks once at the door and the long road beyond it, then at the warm, wonder-crowded "
             "laboratory, and a feeling arrives in everyone's minds at once, wordless and content: "
             "*Home. Friends. Visit?*"),
    ("gold", "**Ursa** kneels and presses his forehead gently to Lickgloom's. “Visit. We "
             "promise. Every time we pass this way.” One long tongue wraps the whole party in a "
             "single ridiculous hug, and that is that. Guardians look after their friends, even "
             "when looking after them means letting them stay somewhere happy."),

    ("h2", "The Road to Gearhaven"),
    ("gold", "Aelwyn unrolls a traveling map across the table, the parchment crackling, and traces "
             "the southward road with one slender finger."),
    ("gold", "**Aelwyn:** “First, **Brambleshadow Thicket**, a dense and thorny woodland of "
             "hidden pathways and mischievous fey. Stay alert; illusions are common there. Then "
             "**Whisperwind Meadow**, serene to look at, but the planar veil runs thin, and things "
             "from the Elemental Plane of Air sometimes wander through. Beyond that rise the "
             "**Ironroot Hills**, jagged rock and abandoned mines, home to creatures who do not "
             "take kindly to visitors. And at the last, **Stormwatch Cliffs**, where the lightning "
             "storms never quite end. Past the cliffs lies **Havenmoor**, a friendly coastal town. "
             "That will be your gateway to the seas: from Havenmoor you must take a ship onward "
             "toward Gearhaven.”"),
    ("gold", "He rolls the map, ties it with a crimson ribbon, and presses it into their hands. "
             "Then he looks at each of them in turn. A hand on Lilly's shoulder: “Trust your bond "
             "with these magical creatures. Each step brings you closer.” A respectful nod to "
             "Ursa: “Your connection to the stars, and your father's legacy, will guide you "
             "through the unknown.” And a grin for Stabby: “Your spirit, wild and free, will cut "
             "through the chaos. Keep your blade sharp and your wit sharper.”"),
    ("gold", "**Aelwyn:** “Go now, Guardians of Elaria. The road to Gearhaven awaits.”"),
    ("gold", "With the map in hand, a leafy dinosaur trotting at their heels, and one last wave to "
             "a small fey creature in a laboratory window, the party steps out into the morning. "
             "The wind carries a whisper of adventure, and the promise of revelations to come."),

    # ------------------------------------------------------------------
    ("h1", "Part Three: The Wild Road", {"hardbreak": True}),
    ("bridge", "The road south proved everything the professor promised: beautiful, strange, and "
               "increasingly full of teeth."),

    ("h2", "Shadowflame in Brambleshadow Thicket"),
    ("gold", "**Brambleshadow Thicket** closes around the path like a dark, twisting tunnel. "
             "Gnarled branches knit overhead, thorny undergrowth crowds close, and shafts of pale "
             "sunlight struggle through the canopy. The air grows damp and cold, smelling of moss "
             "and something faintly metallic, like a storm that has not broken yet. Then, all at "
             "once, the birds stop singing."),
    # Establishing plate: the thicket closing over the southward road.
    ("img", f"{A}/scenes/s3_brambleshadow_thicket.png",
     "The southward road disappears into Brambleshadow Thicket.", 5.6,
     {"crop": "3:2", "hmax": 4.6}),
    ("dm", "Wisdom (Perception) DC 14 to notice the unnatural silence; Intelligence (Arcana) DC 15 "
           "to sense necrotic planar energy soaked into the shadows."),
    ("gold", "**Ursa**, whispering, his breath misting: “This does not feel right. Something is "
             "here. The forest itself feels sick.”"),
    ("gold", "The mist thickens until the party can see barely twenty feet. The temperature "
             "plummets. A hollow laughter echoes through the trees, vibrating up through the ground, "
             "and from the swirling shadows two glowing eyes open. A twisted, flickering shape "
             "gathers itself out of dark purple flame: a **Shadowflame**, its jagged mouth curled "
             "into a grin, wisps of shadow trailing from its limbs like ghostly fire."),
    ("gold", "**Shadowflame**, in a whispery, disembodied voice: “Your fears are tasty... let me "
             "see them... let me taste them!”"),
    ("dm", "**The fight.** Shadowflame, CR 4 (appendix), in a 30-foot clearing walled by thorny "
           "brambles, the mist lightly obscuring everything: disadvantage on ranged attacks and "
           "on Perception by sight."),
    ("dm", "**Illusions of Fear.** It opens by splitting into three identical illusions that "
           "move in step with it. Attacking one calls for Intelligence (Arcana) or Wisdom "
           "(Perception) DC 18 to pick the real flame; on a failure the blow passes through and "
           "the illusion remains, and an identified fake bursts into a swirl of shadow."),
    ("dm", "**Round by round.** It stalks a vulnerable hero with Shadow Claw, saves Terror Wave "
           "(15-foot cone, Wisdom DC 14 or frightened) for when the party clusters, and "
           "Shadowmelds through the mist to reposition whenever it is cornered."),
    ("imgfloat", f"{A}/monsters/shadowflame.png", 2.9),
    ("gold", "The clearing becomes a hall of dark mirrors. Four grinning shadows circle the party, "
             "moving as one, and blades pass through two of them before Lilly starts calling out "
             "which flame casts no light. Stabby is frightened for exactly one round, which he later "
             "denies. Floraburst's very first act as a companion is to snap a Razor Leaf through an "
             "illusion, and her second is to hit the real one. When the Shadowflame finally comes "
             "apart with a bone-chilling screech, the mist unravels with it."),
    ("gold", "Where it fell, a **Dark Mote** lingers, swirling with shadowy energy, pulsing faintly "
             "before it fades into the cold air. It does not feel like the others."),
    ("gold", "**Ursa**, shivering: “These motes... it is like each one is a piece of something "
             "much bigger.” **Lilly**, watching the Essence Sphere stir faintly in response: "
             "“Then we keep collecting the pieces. For the world, and for Pikachu.” **Stabby**, "
             "grinning: “More shadows, more fights! We are going to need sharper swords!”"),

    ("h2", "Whisperwind Meadow"),
    # Establishing plate: the one gentle stretch of the wild road. The sky-heavy
    # art crops to a wide panorama, which also keeps this part to four pages.
    ("img", f"{A}/scenes/s3_whisperwind_meadow.png",
     "Whisperwind Meadow, where the wind talks in its sleep.", 5.8,
     {"crop": "16:9", "hmax": 4.6}),
    ("gold", "Beyond the thicket the land opens into **Whisperwind Meadow**, and for one golden "
             "afternoon the road is kind. The grass runs in long silver waves, and the wind moving "
             "through it truly does whisper, half-words in no language anyone knows, as if the air "
             "itself is talking in its sleep. The veil is thin here; everyone can feel it, a hum "
             "behind the breastbone. But nothing wicked wanders through today. Floraburst dozes on "
             "Ursa's pack with her bud turned to the sun, and the Guardians let the meadow's strange "
             "lullaby carry them south."),

    ("h2", "The Talking Beasts of the Mistwood Path"),
    ("gold", "Where the meadow meets the old forest, the trail dives into the **Mistwood Path**, "
             "and the fog comes back with a grudge. Twisted trees knit out the sun, the mist curls "
             "around ankles, and every footstep lands muffled, as if the forest is holding a pillow "
             "over the sound."),
    ("imgfloat", f"{A}/scenes/s3_displacer_beasts.png", 2.9),
    ("dm", "Wisdom (Perception) DC 15: shapes flickering in the fog, pacing the party. Wisdom "
           "(Survival) DC 14: padded tracks that stop abruptly, mid-stride. Intelligence (Arcana) "
           "DC 16: planar distortion is warping the creatures here, granting them abilities they "
           "should not have."),
    ("gold", "**Ursa**, crouched over the tracks: “They just... stop. These creatures are moving "
             "in ways they should not be.”"),
    ("gold", "A low growl rolls out of the fog, then a sharp whip-crack. Two **Displacer Beasts** "
             "flow out of the white: sleek, six-legged, black as spilled ink, long barbed tentacles "
             "lashing over their shoulders. Their outlines shimmer and slide, each one standing a "
             "step to the left of wherever it actually is. And then comes the thing that makes the "
             "party's blood run colder than the fog. The beasts *speak*."),
    ("gold", "**First beast**, flickering in and out of sight: “Fresh prey... too easy.” "
             "**Second beast**, tentacles lashing: “They will never see it coming.”"),
    ("gold", "Displacer beasts do not talk. Everyone knows displacer beasts do not talk. The fog "
             "suddenly feels less like weather and more like a doorway someone left open."),
    ("dm", "**The fight.** Two displacer beasts (appendix) in a 40-foot clearing of fog, fallen "
           "logs, and roots: light obscurement, scattered cover, and difficult terrain. "
           "Displacement: attacks against each beast have disadvantage until it takes damage."),
    ("dm", "**Tactics.** Hit-and-run: they lash from 10 feet with barbed tentacles, then slide "
           "back into the fog to flank and split the party. Ursa's Faerie Fire stripped the "
           "displacement trick away, and Stabby deflected a tentacle mid-swing to turn the tide."),
    ("gold", "When the beasts finally fall, their bodies shimmer and dissolve into wisps of mist, "
             "leaving only faint outlines on the ground. And beneath where they fell, strange runes "
             "lie etched into the forest floor, pulsing with a dark planar light."),
    ("dm", "Intelligence (Arcana) DC 15: the runes are tears in the fabric of reality, seams where "
           "creatures from other planes seep into this one."),
    ("gold", "**Lilly**, tracing the air above the runes: “These symbols are like cracks in a "
             "mirror. The boundaries between the planes are breaking down.” **Ursa:** “Then "
             "worse things than talking cats are going to come through.” **Stabby:** “Good "
             "thing we are here to stop them!”"),

    ("h2", "The Shroomyte Grove"),
    ("gold", "The path climbs into the **Ironroot Hills**, named for the iron-hard roots that twist "
             "through the earth like veins of metal. The higher the party climbs, the stranger the "
             "hills grow: bulbous mushrooms sprout between the rocks, their caps glowing with eerie "
             "blue-green light, until the whole hillside shines like a dream having a dream."),
    ("dm", "Wisdom (Perception) DC 14: the ground pulses faintly; the roots shift. Intelligence "
           "(Arcana) DC 15: the mushrooms are suffused with Feywild energy, reacting to the "
           "party's presence."),
    ("gold", "**Lilly**, adjusting her goggles: “These mushrooms are not just glowing. They are "
             "responding to us. Be ready for anything.” **Stabby**, twirling his sword: "
             "“Living mushrooms? Bet they are not ready for a good stabbing.”"),
    # Establishing plate: the glowing climb into the hills. Placed after the
    # scouting dialogue so the text can fill the previous page's foot.
    ("img", f"{A}/scenes/s3_ironroot_hills.png",
     "Glowing mushrooms light the climb into the Ironroot Hills.", 5.6,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "The moment the party steps into a clearing ringed with glowing caps, the ground "
             "shudders. With a series of wet, tearing sounds, four **Shroomytes** pull themselves "
             "free of the soil, squat fungal bodies pulsing with inner light, tendrils of mycelium "
             "writhing like grasping fingers. A melodic hum rises from them, beautiful and "
             "menacing at once."),
    ("gold", "**Shroomyte**, in a vibrating, musical tone: “Intruders... the grove... must be "
             "protected!”"),
    ("imgfloat", f"{A}/monsters/shroomyte_grove.png", 2.9),
    ("dm", "**The fight.** Four Shroomytes, CR 2 each (appendix), in a 40-foot clearing: dense "
           "mushroom clusters give half cover, 5-foot patches of damp, root-tangled ground are "
           "difficult terrain, and the caps' dim glow throws long, shifting shadows."),
    ("dm", "**Tactics.** They open with Spore Blasts from range to poison and confuse, close in "
           "with Mycelium Tendrils to entangle and slow, then flank through the mushroom cover, "
           "one venting a spore cloud that obscures and poisons whoever stands in it. Lilly's "
           "fire found their weakness; Stabby simply refused to be caught."),
    ("gold", "It is a strange, glowing battle among the toadstools, and when the last Shroomyte "
             "folds gently back into the earth, the air fills with drifting, luminous spores, "
             "falling like warm snow. In the center of the clearing hovers a **Fungal Mote**, "
             "pulsing with otherworldly light."),
    ("gold", "**Ursa**, reaching toward it, its glow reflected in his eyes: “This one feels like "
             "the Feywild, bleeding into our world.” The Essence Sphere in Lilly's pack hums in "
             "quiet agreement. The collection grows, and so does the mystery."),

    # ------------------------------------------------------------------
    # No hardbreak: the Shroomyte aftermath ends high on its page, and the
    # climb to the cliffs rolls straight on from the hills.
    ("h1", "Part Four: Stormwatch Cliffs"),
    ("bridge", "By the time the hills gave way to open sky, the party could hear the sea, and the "
               "storm that lived above it."),
    ("gold", "**Stormwatch Cliffs** rise at the edge of the world: jagged stone ramparts above "
             "crashing waves, crowned with black clouds that flicker and grumble with lightning "
             "that never quite rests. The air crackles against the skin, tasting of salt and "
             "thunder. Etched into the rocks along the clifftop, strange runes glow with a pale "
             "blue light, brightening with every distant strike."),

    ("h2", "The Cliff Path"),
    ("gold", "The only way forward is a narrow path snaking along the cliff's edge, with sheer "
             "drops to the hungry ocean below. The wind shoves like a rude giant. Stone crumbles "
             "where stone should hold. The Guardians rope together, watch each other's feet, and "
             "inch along the ledge while the storm booms overhead."),
    ("dm", "**The cliff path skill challenge.** The narrow ledge: Dexterity (Acrobatics) DC 14; "
           "a slip means Strength (Athletics) DC 12 to catch the edge or take 1d6 bludgeoning "
           "from the fall. The crumbling section: Wisdom (Perception) DC 15 to spot it in time, "
           "or it collapses underfoot, Dexterity save DC 13 or 2d6 bludgeoning. The glowing "
           "runes: Intelligence (Arcana) DC 15 to recognize an ancient magical defense system "
           "guarding a hidden chamber, knowledge that pays off at the monolith."),

    ("h2", "The Monolith of Four Elements"),
    ("gold", "Past the worst of the ledge, the path opens onto a circular stone platform carved "
             "into the cliffside. At its center stands a **monolith**, etched with the same runes "
             "as the cliffs, a lightning rod jutting from its peak. Every few minutes the storm "
             "reaches down and strikes the rod, and the whole platform glows. Around the monolith "
             "stand four smaller pedestals, each crowned with a rotating stone ring of symbols: "
             "**Air**, **Water**, **Earth**, and **Fire**."),
    ("gold", "Etched into the monolith's base, half-worn by centuries of storms, four phrases: "
             "*The winds whisper first. The tide rises after. Stone stands firm next. Flame seals "
             "the fate.*"),
    # The monolith description runs to the page foot; break so the puzzle
    # card opens its page whole.
    ("pagebreak",),
    ("game", "THE LIGHTNING PUZZLE OF STORMWATCH CLIFFS", [
        "*Four pedestals, four elements, one storm that never rests. The monolith opens only "
        "for those who read the cliffs' riddle and dare the lightning's timing.*",
        "",
        "**The pieces.** Each of the four pedestals carries a rotating stone ring of element "
        "symbols: **Air, Water, Earth, Fire**. The monolith's lightning rod takes a strike "
        "every few minutes, and the runes along the cliffs pulse with each one.",
        "**The riddle.** Four phrases are carved into the monolith's base: *The winds whisper "
        "first. The tide rises after. Stone stands firm next. Flame seals the fate.*",
        "**Reading it.** Intelligence (Investigation) or Wisdom (Insight) DC 15 to deduce the "
        "sequence from the clues: **Air, then Water, then Earth, then Fire**. Intelligence "
        "(Arcana) DC 16 to realize the alignment must be finished **as the lightning strikes "
        "the rod**, not before, not after.",
        "**The stakes.** A wrong alignment when the bolt lands discharges wild energy: 2d6 "
        "lightning to everyone standing near the monolith. The right alignment on the storm's "
        "next breath, and the monolith drinks the bolt whole.",
    ]),
    ("gold", "Stone rings grind into place: wind, tide, stone, flame. The storm inhales. Lightning "
             "hammers the rod, and this time the monolith drinks it, humming louder and louder "
             "until a beam of pure light lances up into the clouds and blooms into a shimmering "
             "curtain of energy above the platform."),

    ("h2", "The Dark Figure"),
    ("gold", "Within the curtain of light, a vision takes shape: a towering figure cloaked in "
             "darkness, its face hidden, its presence pressing down on the platform like a cold "
             "hand. The storm itself seems to lean away from it. When it speaks, the voice does not "
             "come through the air. It arrives directly inside their minds."),
    ("gold", "**The dark figure:** “You meddle with forces beyond your comprehension. The "
             "boundaries between realms are mine to shatter and shape. The goddess's light fades, "
             "and chaos will reign. The motes you gather are but embers of a dying flame. You "
             "cannot stop the unraveling.”"),
    # Establishing plate: the vision above the monolith.
    ("img", f"{A}/scenes/s3_stormwatch_vision.png",
     "The dark figure appears above the monolith at Stormwatch Cliffs.", 5.8,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "The vision collapses into darkness, and the light curtain blows out like a candle. "
             "Where it stood, something small falls to the stone with a crystalline chime: a "
             "**Dark Fragment**, a shard of crystallized energy swirling with elemental chaos, cold "
             "to the touch and heavier than it looks."),
    ("dm", "Intelligence (Arcana) DC 15: the fragment is a remnant of the same power corrupting "
           "the planar boundaries, tied directly to the weakening of Elaria. The party keeps it, "
           "carefully wrapped."),
    ("gold", "Until this moment, the breaking of the world might have been an accident: a storm, a "
             "sickness, a slow unlucky fraying. No longer. Someone stood in that light and called "
             "the boundaries *mine*. Someone is doing this on purpose."),
    ("gold", "**Ursa:** “That figure... they want to unravel everything. We have to stop "
             "them.” **Lilly:** “The Artificer's Guild might be our best chance to figure this "
             "out, and to bring Pikachu back.” **Stabby:** “Whoever they are, they are going to "
             "get a taste of my blade!”"),

    # ------------------------------------------------------------------
    ("h1", "Part Five: The Lights of Havenmoor", {"hardbreak": True}),
    ("bridge", "The storm broke behind them, and the path wound down from the cliffs toward the "
               "glow of a town that smelled like cookies."),
    ("gold", "As the party descends, the roar of the sea softens, and new sounds drift up to meet "
             "them: distant laughter, jingling bells, a thread of festive music. The path becomes a "
             "cobblestone road flanked by frost-dusted pines, and the cold air fills with the "
             "mingled scents of sea salt, pine needles, cinnamon, nutmeg, and fresh-baked cookies."),
    # Establishing plate: the town at dusk, dressed for the festival.
    ("img", f"{A}/scenes/s3_havenmoor_arrival.png",
     "Havenmoor at dusk, every window aglow.", 6.2, {"crop": "3:2", "hmax": 4.6}),
    ("gold", "Ahead at dusk lies **Havenmoor**, a coastal town sprung whole from a holiday "
             "fairytale. Stone and timber houses wear wreaths and garlands and twinkling lights. "
             "Red ribbons wrap the lamp posts, snow dusts the rooftops, and warm hearth-glow spills "
             "out of every window onto the cobbles. In the town square towers the **Great Pine of "
             "Havenmoor**, its branches heavy with glass baubles and shimmering ribbons, enchanted "
             "lights flickering among the boughs, a golden star burning at its top. Children pelt "
             "each other with snowballs beneath it. A painted signpost reads: *Welcome to "
             "Havenmoor! May your hearts be warm and your spirits bright!*"),
    ("gold", "A small figure comes bustling up, barely three feet tall, in a green tunic, "
             "red-striped leggings, and a pointed red hat tipped with a jingle bell. His cheeks are "
             "rosy and his grin is enormous."),
    ("gold", "**Festive elf:** “Ho there, travelers! Welcome to Havenmoor, where the chill may "
             "bite, but the cheer warms all! You must be weary after your journey. Come, come! The "
             "Sugarplum Hearth awaits: hot cocoa, cookies, and a warm fire!”"),

    ("h2", "The Sugarplum Hearth"),
    ("gold", "The **Sugarplum Hearth** is a cozy two-story tavern with a thatched roof, holly on "
             "the door, and a wooden sign bearing a steaming mug and a sugarplum. Inside, a hearth "
             "roars beneath a mantel hung with stockings, an enchanted harp plays softly in the "
             "corner, and every table carries frosted cookies, peppermint bark, and mugs of hot "
             "cocoa crowned with whipped cream. Floraburst is an immediate celebrity; three "
             "children and one grandmother declare her the best dinosaur they have ever met."),
    ("gold", "**Greta Frostbough**, the tavern keeper, a stout dwarf woman with silver hair and a "
             "warm smile, appears with extra marshmallows unasked. “A bit of sweetness warms the "
             "soul, do you not think? You lot look like you have seen some excitement. Tell me, "
             "what brings you to Havenmoor?”"),
    ("gold", "By the fire, **Elda Merrywhistle**, a half-elf storyteller with a lute, spins tales "
             "for a knot of wide-eyed children. Between songs she leans toward the party, and her "
             "voice drops low. “They say the sea has been restless of late. Ships vanish in the "
             "fog, and lights dance on the waves. If you are setting sail, beware the spirits of "
             "the deep.”"),
    ("gold", "Night settles over Havenmoor like a quilt. The party is given warm rooms upstairs, "
             "feather beds and thick blankets, each window overlooking the softly glittering square. "
             "In the morning, they are promised, **Master Bramblebeard** the shipwright will come "
             "by to talk of passage north. Below the window, the Great Pine glows on through the "
             "dark: a small, stubborn light against a gathering storm, which is, after all, exactly "
             "what Guardians are."),
    ("divider",),
    ("bridge", "Their third adventure was done: a professor's warning, a leafy new companion, a "
               "farewell to a fey friend, four battles on the wild road, and a shadowy figure who "
               "wanted the world's walls broken. The Guardians of Elaria slept warm in Havenmoor, "
               "and did not yet know how much this bright little town was about to need them."),
    ("dm", "After this session the heroes reached **level 4**."),
    ("gold", "*Next: Session 4, in which Havenmoor's festive lights flicker, a horned shadow comes "
             "creeping for the children of the town, and eight winter bells hold the key to driving "
             "it back into the dark.*"),

    # ------------------------------------------------------------------
    ("h1", "Appendix: Creatures of Session Three", {"pagebreak": True}),
    ("stat", "Shadowflame", [
        "Medium undead, chaotic evil. **CR 4**. AC 14 (natural armor), HP 58 (9d8 + 18), Speed 0 ft., fly 40 ft. (hover).",
        "STR 8, DEX 18, CON 14, INT 12, WIS 15, CHA 18. Skills Stealth +8, Intimidation +6.",
        "Resistances acid, fire, lightning, necrotic, nonmagical piercing and bludgeoning. Immunities poison, psychic; charmed, frightened, grappled, paralyzed, poisoned, prone, restrained. Darkvision 60 ft.",
        "**Illusions of Fear.** Creates three identical illusions of itself (AC 14); DC 18 Arcana or Perception to spot a fake, or the attack misses.",
        "**Shadow Claw.** +6, reach 5 ft., 2d8 + 4 necrotic; DC 14 Wisdom save or frightened one turn.",
        "**Terror Wave (Recharge 5-6).** 15 ft. cone, DC 14 Wisdom save; 3d10 necrotic and frightened 1 minute (repeat save each turn).",
        "**Shadowmeld (Reaction).** When hit, teleports up to 20 ft. and becomes lightly obscured.",
    ]),
    ("stat", "Displacer Beast", [
        "Large monstrosity, unaligned. **CR 3**. AC 13 (natural armor), HP 85 (10d10 + 30), Speed 40 ft.",
        "STR 18, DEX 15, CON 16, INT 6, WIS 12, CHA 8. Darkvision 60 ft.",
        "**Displacement.** Projects an illusion of standing beside itself; attack rolls against it have disadvantage until it takes damage.",
        "**Tentacles (Multiattack x2).** +6, reach 10 ft., 1d6 + 4 bludgeoning plus 1d8 force.",
    ]),
    ("stat", "Shroomyte", [
        "Small plant, neutral. **CR 2**. AC 13 (natural armor), HP 27 (5d8 + 5), Speed 20 ft.",
        "STR 12, DEX 12, CON 14, INT 6, WIS 12, CHA 7. Saves Con +4, Wis +3; Stealth +3, Perception +3.",
        "Resistance poison; immune to the poisoned condition. Darkvision 60 ft. Understands Sylvan.",
        "**Bioluminescent Glow.** Dim light in a 10 ft. radius; can suppress it as a bonus action. **Multiattack.** One Spore Blast and one Mycelium Tendrils.",
        "**Spore Blast.** +4, range 30 ft., 2d6 + 2 poison; DC 13 Constitution save or poisoned one turn.",
        "**Mycelium Tendrils.** +4, reach 10 ft., 2d4 + 2 bludgeoning; DC 13 Strength save or restrained one turn.",
        "**Fungal Retribution (Reaction).** A melee attacker within 5 ft. takes 2d4 poison (DC 13 Constitution negates).",
    ]),
    # Companion blocks merged into one so the appendix holds one page.
    ("stat", "The Professor's Companions", [
        "**Floraburst (the party's companion).** Small fey, neutral good. AC 14 (natural armor), HP 45 (6d6 + 18), Speed 30 ft.",
        "STR 14, DEX 12, CON 16, INT 10, WIS 14, CHA 10. Skills Nature +4, Survival +4. Resistance poison. Darkvision 60 ft. Understands Sylvan and Common.",
        "**Plant Camouflage.** Advantage on Stealth checks in heavy foliage. **Photosynthesis.** Recovers 10 extra HP when resting in sunlight.",
        "**Razor Leaf.** +4, range 30 ft., 2d8 + 2 slashing.",
        "**Vine Lash.** +4, reach 15 ft., 1d10 + 2 bludgeoning; DC 13 Strength save or restrained one turn.",
        "**Floraberry (3/Day).** Produces 1d4 + 1 magical berries; eating one restores 3 HP.",
        "**Aqualump (stayed with Aelwyn).** Small water elemental, neutral good. AC 16 (shell), HP 54, Swim 30 ft. Water Bolt (2d8 + 2, knockdown), Surf (Recharge 5-6, 15 ft. cone, 4d6 cold), Shell Defense (+4 AC as a bonus action).",
        "**Emberpaws.** Small fire elemental, chaotic good: a fox-like creature with flame-wreathed paws and tail. AC 15, HP 42, Speed 30 ft. Immune to fire. Ember (2d6 + 2 fire), Tail Flame Whip (2d6 + 3 fire, may ignite), Heatwave (3/Day, melee attackers take 1d8 fire).",
    ]),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    out = build_doc(BLOCKS, "sessions/session_03_quest_for_knowledge.docx")
    print("built", out)
