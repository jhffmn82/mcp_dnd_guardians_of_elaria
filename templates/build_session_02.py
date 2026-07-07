# build_session_02.py
# The Guardians of Elaria, Session 2: The Road to Ravenstone
# Publication build. Canon: memory/campaign_canon.md + CONTRADICTIONS.md rulings
# (C2 Grimfang rival clan, C5 missing villagers resolved, C6 single Aelwyn meeting).
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc

A = "assets"
BLOCKS = [
    ("titlepage", "THE GUARDIANS OF ELARIA", "SESSION 2",
     "The Road to Ravenstone",
     "An illustrated adventure. Read the gold boxes aloud; the purple boxes are for the DM."),

    # Frontispiece: the chapter opener rides page 1 above the recap, cropped
    # to a dominant landscape plate per DM review.
    ("img", f"{A}/scenes/s2_oakshade_morning.png",
     "Dawn breaks over Oakshade Village, and the mist lets go at last.", 6.2,
     {"crop": "3:2", "hmax": 4.5}),

    ("h1", "Previously, on The Guardians of Elaria..."),
    ("gold", "Three young heroes collided at the **Gilded Acorn Tavern** in Eldridge Village: "
             "**Lilly Glimmergear**, a deep gnome artificer carrying the humming **Essence Sphere** "
             "and the sleeping spark of a creature called Pikachu; **Ursa Catchum**, the star reading "
             "son of the vanished druid Ash Catchum; and **Stabby Sharpblade**, a goblin monk with "
             "sharp teeth and a sharper grin. One friendly tavern brawl later, they were a party."),
    ("gold", "In the **Forest of Whispers** they befriended **Lickgloom**, a gentle fey creature "
             "with a heroic tongue, bested the leek wielding guardian **Duckleaf** and the patient "
             "water guardian **Cognifin**, and scattered the fog cloaked **Mist Stalkers** on the "
             "road. Every strange creature left behind a glowing **mote**: a little piece of another "
             "plane, loose in the world. At **Oakshade Village**, Elder Merwin asked the party to "
             "find the young herb gatherers lost in the forest, for fifty gold and the village's "
             "gratitude. The heroes slept in warm beds above the Old Oak Tavern. And then, morning."),

    # ------------------------------------------------------------------
    ("h1", "Part One: Morning in Oakshade"),
    ("gold", "Dawn breaks soft and silver over Oakshade Village. A last ribbon of mist clings to "
             "the square, curling around the great ribbon hung oak and the old well beside it. The "
             "village is waking: shutters open, chimneys breathe, and folk go about their morning "
             "with wary glances at the treeline, as they have every morning since the forest began "
             "to whisper."),
    ("gold", "Down the tavern stairs come four travelers, one of them licking the banister. Behind "
             "the bar, **Alwen** watches them descend with an approving gleam; word of their deeds "
             "in Eldridge arrived ahead of them, the way word always does."),
    ("gold", "**Alwen**, setting down plates of warm bread and fresh berries: “Mornin', young "
             "ones! Word is already spreading about the lot of you. Folk around here could use a "
             "touch of bravery, I will say that much.” She leans in, lowering her voice. “Say, "
             "you would not be interested in the professor, by any chance? Rumor is you came "
             "looking for strange creatures. The professor has got his fair share, and then some. "
             "**Professor Aelwyn** is the name. A peculiar one, that fellow: studies critters and "
             "strange energies, trying to understand what has been going on with the forest. He "
             "keeps a place called **Ravenstone Laboratory** out in the wilds, but not many are "
             "brave enough to go looking.” She glances toward the square. “If you are truly "
             "interested, talk to a few folks here in the village first. Some have seen things, "
             "strange things, while he has been poking about.”"),

    ("h2", "The Lost Come Home"),
    ("gold", "Before the last berry is eaten, a shout rings across the square. Then another, and "
             "another, and suddenly half the village is running. Through the thinning mist come "
             "three young figures with leaves in their hair and empty herb baskets on their arms, "
             "blinking at the morning light like children waking from a long nap. The lost herb "
             "gatherers have come home: footsore, muddled, and completely unharmed."),
    ("imgfloat", f"{A}/scenes/s2_villagers_return.png", 2.85),
    ("gold", "Their story spills out in pieces while mothers cry and neighbors cheer. The forest "
             "fog had turned them around, and around, and around; every path bent back on itself, "
             "and something in the whiteness kept howling, so they hid. Then last night, all at "
             "once, the howling stopped and the fog simply... let go. The paths ran straight again, "
             "and they walked out by starlight."),
    ("gold", "**Elder Merwin** works it through aloud, one smith's thought at a time. “Last "
             "night, you say. The very night these four put down those mist beasts on the road.” "
             "He turns to the party, and his weathered face folds into a rare smile. “That fog was "
             "no weather. It died with the creatures that wore it. Oakshade owes you more than "
             "coin, but coin is what I promised.” And in front of the whole square he counts fifty "
             "gold pieces into their hands, proud as if he were knighting them."),
    ("dm", "Quest closed: the missing herb gatherers came home dazed but unharmed; the misdirecting "
           "fog lifted when the **Mist Stalkers** died. Merwin pays the promised **50 gp**."),

    ("h2", "Whispers in the Square"),
    ("gold", "With the morning suddenly festive, tongues loosen, and the party decides to take "
             "Alwen's advice and spend an hour listening. By the central well, **Nina the herbalist**, elderly and warm, with "
             "weathered hands that never stop sorting leaves, waves them over to her stall."),
    ("gold", "**Nina:** “It is that forest, see? The air feels different. Heavy. Like it is "
             "breathing. I have seen the professor come by in the dead of night, arms full of odd "
             "things: stones, jars of glowing water, plants that do not grow here. Says he is "
             "studying it. I say it is not for mortal minds to meddle in such things. Lately he "
             "goes further out, beyond where the trees are thickest. I only hope he knows what he "
             "is dealing with.”"),
    ("gold", "Near the forge, Merwin adds his own measured warning. “Aelwyn is brilliant, no "
             "doubt. I would also say he is a tad reckless. Always pushing the boundaries of what "
             "is safe to know. If you find him, ask him how far he is willing to go. Tell him to "
             "remember what is at stake here. We cannot afford for Oakshade to become a ground for "
             "planar... experimentation.”"),
    ("gold", "And at the village edge, a knot of children playing tag stops mid game. A bright "
             "eyed girl darts over. “You are looking for the professor, are you not? We see "
             "things at night. Creatures. Glowing lights. Some of them talk, even though there is "
             "nobody there. My mom says it is just stories, but we saw it with our own eyes: a "
             "floating shadow, whispering in the trees.” Another child pipes up: “One of them looked like a giant fox, all "
             "made of sparks! And another like a... like a big fluffy cloud!” The children trade "
             "uneasy looks and scatter back to their game."),

    ("h2", "Tamsin's Map"),
    ("gold", "As the party compares rumors by the well, a half elf woman with a heavy satchel and "
             "a determined look crosses the square to meet them. “You are asking after the "
             "professor,” she says, scanning the rooftops as if the words might carry. “My name "
             "is **Tamsin**. I work with him. Sort of.”"),
    ("gold", "**Tamsin:** “Professor Aelwyn studies what is happening out here, things most "
             "people would not dare go near. He believes the planar boundaries, the thin walls "
             "between our world and others, are shifting. Letting things through. He has been "
             "collecting samples, researching the... anomalies. Lately it has become an obsession. "
             "I could mark the laboratory on your map, if you are set on going. But I warn you: "
             "the road is not safe.” The party is set on going. She unrolls their map on the "
             "well stones and marks a spot in the western wilds: **Ravenstone Laboratory**. “Follow the western path and watch for the fork. "
             "When you start feeling like the trees are watching you, you are almost there.” Her "
             "grim smile fades. “The professor says the creatures are harmless. But I have seen "
             "how some of them act. Like they are protecting something. Whatever is happening, it "
             "will not stop here.”"),
    ("gold", "The party shoulders their packs in the bright morning square. Alwen waves from her "
             "doorway: “Good luck to you! And watch out for the strange ones out there!” "
             "Lickgloom flicks its tongue at a butterfly, misses, and trots after its friends, and "
             "Oakshade watches its newest heroes walk west into the trees."),

    # ------------------------------------------------------------------
    ("h1", "Part Two: The Western Road"),
    ("bridge", "Fifty gold richer and one mystery deeper, the party followed Tamsin's map into the "
               "wilds, where the road itself seemed to grow stranger with every mile."),

    ("h2", "The Mudskip Ambush"),
    ("gold", "Half a mile out, the forest thickens and the path turns soggy underfoot. Little "
             "streams wander across the trail, the air hangs humid and close, and somewhere nearby "
             "water bubbles where no stream should be. The trees open on a clearing pocked with "
             "shallow pools of murky brown water."),
    ("gold", "One of the larger pools ripples. Not the way wind ripples water: the other way. "
             "Then three creatures burst from the mud in a fan of brown spray, part salamander, "
             "part fish, slick and blue green, with fin feet, waggling tails, and wide grins full "
             "of tiny needle teeth. Their eyes gleam with mischief and a flicker of light that "
             "does not belong to this world. **Mudskips**: creatures of the Plane of Water, "
             "slipped through the thinning walls, and absolutely delighted to see travelers."),
    ("dm", "**The ambush.** Three **Mudskips** (CR 1/2 each, appendix). The mud is difficult "
           "terrain for everyone but them: they dart in, splash, and dive back into the pools, "
           "flanking through the water to isolate whoever moves slowest. Resistant to fire, "
           "vulnerable to lightning: the fire tricks Lilly and Ursa lean on need rethinking."),
    ("dm", "**Terrain that fights back.** Each Mud Splash (15-foot cone) leaves fresh slick "
           "ground behind, reshaping the battlefield round by round; a hero blinded by the "
           "spray fights the terrain as much as the ambushers."),
    ("dm", "**Talk, flee, or scale.** A hero who tries talking (or splashing back) can tell the "
           "Mudskips are confused, displaced far from the Plane of Water: mischief, not malice. "
           "If the party withdraws to dry ground, the Mudskips do not pursue past their pools. "
           "Too easy? A fourth Mudskip surfaces from a hidden pool. **XP: 100 each (300 total).**"),
    ("imgfloat", f"{A}/scenes/s2_mudskip_ambush.png", 3.1),
    ("gold", "The fight is half battle, half mud wrestling. The Mudskips spit gobs of muck, slap "
             "with their tails, and skate across the wet ground while the heroes' boots sink and "
             "stick. Stabby goes down face first exactly once and comes up spitting mud and "
             "declaring war. But Lilly's sparks find the water, Ursa's magic pins the pools, and "
             "one by one the giggling ambushers are beaten, until the last Mudskip collapses into "
             "a plain brown puddle with an almost apologetic *blorp*."),
    ("gold", "Where each creature fell, a small **mote of water energy** rises, pulsing with faint "
             "blue light, hovering just long enough to be seen before it thins into the air. The "
             "pattern from the Forest of Whispers holds: the strange creatures are not invaders. "
             "They are leaks. Lilly bottles a few samples of the shimmering elemental mud; the "
             "professor, she suspects, will want to see this."),
    ("dm", "Intelligence (Arcana) or Wisdom (Nature) DC 13: the motes are fragments of elemental "
           "energy from the **Plane of Water**, more proof the boundaries are weakening. On a "
           "failure the motes thin away before anything can be read; Professor Aelwyn can "
           "identify the samples later. Loot: **Elemental Mud Samples** for the professor."),

    ("h2", "The Grimfang War Band"),
    ("gold", "Beyond the marsh the path narrows, dense brush pressing close on either side: the "
             "kind of road that makes a traveler's neck prickle. The birdsong stops. A branch "
             "cracks. And then the brush is full of eyes."),
    ("gold", "Goblins melt out of the shadows on every side, rough faced and hostile, weapons "
             "ready. With them come worse things: a snarling **worg** straining to pounce, a "
             "thick shouldered **orc** with a club like a fence post, and a **hobgoblin** settling "
             "a crossbow on a branch further back. At their center stands a stocky **goblin boss** "
             "with a scar across his face, and when his eyes find Stabby, he grins like a trap "
             "snapping shut. These are the **Grimfang**, a rival clan with an old grudge against "
             "Stabby's people."),
    ("gold", "**Grimfang boss:** “Well, well. If it is not one of the **Bloodfang Clan**, "
             "wandering far from home! You are bold, bringing friends. Shame they will make such a "
             "tasty meal!”"),
    ("imgfloat", f"{A}/scenes/s2_grimfang_ambush.png", 3.0),
    ("dm", "**The Grimfang war band:** 2 goblin archers on the flanks, a worg and an orc in the "
           "melee, a hobgoblin sniping from the rear, and a goblin boss barking orders. The "
           "boss coordinates: archers focus the party's back line while the worg and orc press "
           "the front, and the hobgoblin's covered position hands Stabby a perfect chance to "
           "catch an arrow out of the air with **Deflect Attacks**. The boss taunts Stabby "
           "about the Bloodfang all through the fight. Beaten, the survivors flee."),
    ("dm", "**If it goes wrong.** The Grimfang want to humble the Bloodfang runaway, not finish "
           "anyone: fallen heroes wake at the roadside, bruised and lighter by their shiniest "
           "valuables, with goblin laughter fading in the brush. If you track XP, award "
           "standard 2024 Monster Manual values for the roster."),
    ("gold", "The ambush is coordinated, vicious, and very unlucky in its choice of victims. "
             "Arrows hiss from both flanks; Stabby plucks one out of the air an inch from Lilly's "
             "hat and twirls it like a prize. The worg lunges and meets Ursa's magic head on. The "
             "orc swings his great club in whistling arcs while the boss dances behind him, "
             "shouting insults about the Bloodfang Clan, about weakness, about the little monk who "
             "left. Stabby's grin never moves. His feet do. Between the monk's flashing strikes, "
             "the artificer's crackling bolts, and the druid's starlight, the war band's courage "
             "leaks out of it like sand from a torn sack."),
    ("gold", "The boss is last, back pedaling, still snarling. “This is not over, Bloodfang!” "
             "he spits, and then the Grimfang are gone into the brush, dragging their pride behind "
             "them. The party stands a long moment in the quiet. Stabby picks up the arrow he "
             "caught and tucks it in his sash, and says nothing at all about home."),

    # ------------------------------------------------------------------
    ("h1", "Part Three: The Whispering Glade"),
    ("bridge", "Bruised, muddy, and victorious twice over, the party pressed on as the sun sank "
               "low, and the road repaid them with wonder."),
    ("gold", "Toward sunset the path opens into a serene clearing the Oakshade folk call the "
             "**Whispering Glade**. Ancient trees ring it round, their leaves rustling softly in "
             "air that holds no wind at all, so that the whole glade seems to murmur. At its "
             "center stands an old stone monument, cloaked in moss, carved with runes that glow "
             "faint as embers."),
    # Establishing shot promoted to a half-page landscape plate per DM review.
    ("img", f"{A}/scenes/s2_whispering_glade.png",
     "The Whispering Glade murmurs in windless air around its rune carved monument.", 6.2,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "A calm settles over the party the moment they step inside. Time feels slower here; "
             "the forest's sounds arrive muffled, as if from another room. Then, one by one, "
             "strange things begin to hum. The **Essence Sphere** in Lilly's arms wakes with a "
             "soft glow and a note like a struck glass. The three **enchanted potatoes** in Ursa's "
             "pack grow warm as fresh bread. And along Ursa's arm, his Dragonmark tingles, the way "
             "it does when something living and frightened is near. But nothing here is "
             "frightened. Something here is *waiting*."),
    ("gold", "Ursa feels the pull before he understands it: a quiet insistence, drawing his hand "
             "toward the monument. When his palm touches the mossy stone, the runes flare to life, "
             "gentle light washing across the glade. The Sphere answers in Lilly's arms. The "
             "potatoes pulse, all three in unison, like little buried heartbeats. And the world "
             "folds softly away."),

    ("h2", "The Vision of Elaria"),
    ("gold", "The glade is gone. The party stands together in a vast, ethereal expanse of "
             "swirling mist and drifting lights, and out of the luminescence a figure gathers: a "
             "radiant being woven of intertwining vines, starlight, and flowing water, vast and "
             "gentle at once, her eyes holding the depth of the night sky. This is **Elaria**, "
             "and though none of them has ever heard her name, all of them somehow know it."),
    # Vertical composition: no crop (the goddess rises above the heroes), but a
    # raised height cap so the showpiece reads larger on the page.
    ("img", f"{A}/scenes/s2_elaria_vision.png",
     "Elaria, guardian of the planes, gathers out of starlight and vine above the three heroes.", 5.2,
     {"hmax": 5.2}),
    ("gold", "**Elaria:** “Seekers of truth. You have touched the threads that bind the "
             "realms. I am Elaria, guardian of the planes and of the balance that sustains them. "
             "A great disturbance ripples through existence, and the boundaries between worlds "
             "grow thin.”"),
    ("gold", "Her gaze turns to Ursa, and it is warm as summer. “Child of Ash. Your father "
             "delved into mysteries few dare to explore. The enchanted potatoes you carry are "
             "remnants of a shattered covenant, a safeguard against the unraveling. They hold the "
             "key to restoring what was lost.”"),
    ("gold", "To Lilly: “Ingenious artificer. The Essence Sphere you bear, once a mere power "
             "core, now resonates with energies beyond its making. It can channel and stabilize "
             "the motes of wayward creatures caught between planes.”"),
    ("gold", "And to Stabby, with something almost like a smile in the starlight: “Wanderer of "
             "shadows. Your path is interwoven with chaos and choice. Your actions may sway the "
             "tides toward harmony, or deepen the discord.”"),
    ("gold", "Around them the mists flash with visions: landscapes cracking like ice, elemental "
             "fire and flood, creatures of every plane tumbling through gaps in the world. "
             "**Elaria:** “The disturbances are but a symptom of a greater malady. An ancient "
             "entity seeks to exploit this weakness, consuming the essence of worlds. Unite your "
             "strengths. Restore the safeguards. Mend the fractures, before all is lost.”"),
    ("gold", "The expanse dissolves like breath off a mirror, and the party is standing in the "
             "Whispering Glade again, hands and hearts still tingling. Evening has fallen while no "
             "time passed at all, and the first stars overhead burn with extraordinary brilliance, "
             "as if someone up there knows they are being watched. On the monument, the runes dim slowly "
             "to a patient glow."),
    ("gold", "**Ursa**, quietly: “My father was trying to protect the balance of the planes. "
             "These potatoes are more than heirlooms. We have to finish what he started.”"),
    ("gold", "**Lilly**, turning the Sphere over in her hands: “The power core was never just "
             "a gift. If it can stabilize these planar energies, we might save more than "
             "Pikachu.”"),
    ("gold", "**Stabby**, grinning at the stars: “So causing a bit of chaos might actually "
             "help this time. Good. I am very qualified.”"),
    ("game", "BOONS OF THE WHISPERING GLADE", [
        "*Elaria's gift settles over the heroes as the vision fades, each boon granted then "
        "and there in the glade.*",
        "",
        "**Ursa: Planar Awareness.** For the next 24 hours, Ursa senses planar anomalies "
        "within 1 mile.",
        "**Lilly: Planar Attunement.** The Essence Sphere permanently grants advantage on "
        "Intelligence (Arcana) checks concerning planar magic and creatures.",
        "**Stabby: Glimpse of Possibility.** Advantage on one saving throw or ability check, "
        "spent whenever he chooses.",
    ]),
    ("dm", "The glade is safe ground: the party took a short rest here, talking the vision "
           "through before pressing on."),

    # ------------------------------------------------------------------
    ("h1", "Part Four: The Stone Serpent"),
    ("bridge", "Rested and lit from within by what they had seen, the party climbed on toward "
               "Ravenstone through the deepening dusk, and the mountain itself rose to meet them."),
    ("gold", "The last stretch to Ravenstone climbs through rugged country, the path narrowing "
             "between steep cliffs with loose stones rolling underfoot. The party is picking their "
             "way single file when the ground begins to shake. Pebbles dance. Cracks race along "
             "the trail. And with a deep, resonant rumble, the path ahead heaves upward and "
             "becomes a creature."),
    # Mountain-path approach promoted to a half-page landscape plate per DM review.
    ("img", f"{A}/scenes/s2_mountain_path.png",
     "The last stretch to Ravenstone climbs between crystal studded cliffs.", 6.2,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "**Terranox** rises: a great serpent of living stone and packed earth, rocky scales "
             "glinting in the last purple light, eyes glowing from within like windows onto slow "
             "magma. It regards the party the way a mountain regards weather, and then it strikes. "
             "There is no talking to it, no bargaining, no clever password. Some guardians test. "
             "This one only defends."),
    ("dm", "**Terranox**, CR 4 elemental of the **Plane of Earth** (appendix). No parley. "
           "Immune to fire, so flame tricks fail again. It opens on the nearest intruder, uses "
           "Earthquake Stomp to scatter the party's formation, and saves Stone Coil for "
           "spellcasters and ranged attackers, squeezing them out of the fight early."),
    ("dm", "**The battlefield.** Loose rocks litter the narrow path and make natural cover. "
           "Each round, roll a d6: on a 5 or 6, rocks shake free of the cliffs, DC 12 Dexterity "
           "save or 1d10 bludgeoning. The longer the battle roars, the more attention it "
           "risks drawing."),
    # The session's boss gets a full reveal plate; the encounter notes ride
    # with the reveal paragraph so the plate opens its own page cleanly.
    ("img", f"{A}/monsters/terranox.png",
     "Terranox, the stone serpent of the Plane of Earth, rises from the mountain path.", 5.8,
     {"crop": "4:3", "hmax": 4.6}),
    ("dm", "**Victory, defeat, scaling.** Victory: Terranox collapses into inert stone with the "
           "**Earth Mote** in the rubble. **XP: 1,100.** Defeat: it leaves fallen heroes "
           "unconscious but alive and burrows away; they wake hurt, free to recover and try the "
           "pass again. Easier: 75 HP, save DCs 13, Stone Coil restrains without damage. "
           "Harder: 110 HP, rockfalls on 4 to 6."),
    ("gold", "It is the hardest fight of their young lives. Terranox's tail sweeps like a falling "
             "tree; its stone coils catch Ursa mid spell and squeeze until Stabby's flurry of "
             "blows cracks the grip loose. Fire splashes off the creature like rain off a roof, so "
             "Lilly rewires her cannon on her knees in the dark while Ursa calls down starlight "
             "instead of flame. Chip by chip, crack by crack, the heroes carve the mountain down, "
             "until at last the great serpent shudders, sighs a long gravel sigh, and collapses "
             "into a heap of inert stone and settling dust."),
    ("gold", "In the rubble where its heart was, the party finds an **Earth Mote**: a small "
             "crystalline fragment pulsing with elemental energy, heavy with the raw strength of "
             "the Plane of Earth. This one does not drift away. Lilly wraps it carefully with the "
             "mud samples and a few glittering **stone fragments** of the serpent's hide. The "
             "professor is going to have questions. So do they."),

    # ------------------------------------------------------------------
    # The Terranox fight fills its page well past the 70% mark, which would
    # leave this heading stranded at the page foot; hardbreak starts Part Five
    # at the top of a fresh page.
    ("h1", "Part Five: Ravenstone Laboratory", {"hardbreak": True}),
    ("bridge", "Dusty, weary, and carrying pieces of three planes in their packs, the party "
               "crested the last wooded hill as twilight fell."),
    ("gold", "Below them, nestled in a tranquil valley of ancient oaks and shimmering ponds, "
             "stands **Ravenstone Laboratory**: a graceful structure of stone and glass, its "
             "turrets spiraling upward like reaching fingers, capped with metal domes that catch "
             "the last orange and purple of the sky. Warm light glows from every window. The path "
             "down is lined with luminescent flowers that sway gently in the still air, and among "
             "the trees flit small, impossible creatures: some with wings like leaves, some like "
             "tiny mammals traced in glowing lines."),
    # Part Five opener: the first sight of the laboratory as a half-page
    # landscape plate per DM review.
    ("img", f"{A}/scenes/s2_ravenstone_arrival.png",
     "Lilly points the way as Ravenstone Laboratory glitters awake in the dusk below.", 6.2,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "The creatures are not shy. A little fox with a leaf shaped tail pads right up to "
             "Lilly, sniffs her boot with great scholarly interest, and darts back into the "
             "foliage."),
    ("gold", "**Lilly**, eyes sparkling: “Did you see that? I have never encountered wildlife "
             "like this before!”"),
    ("gold", "**Ursa:** “There is something special about this place. The veil between worlds "
             "feels thinner here.”"),
    ("gold", "**Stabby:** “Or maybe the critters just know a friendly face when they see "
             "one.”"),
    ("gold", "The grand wooden doors swing open on their own as the party approaches, breathing "
             "out the scent of old books, fresh parchment, and a crackle of ozone. Inside, wooden "
             "beams arch beneath ceilings painted with stars and mythical beasts; shelves of books "
             "and artifacts climb the walls between tall windows. And everywhere, creatures. A "
             "rabbit with fur like blooming flowers dozes on a windowsill. A bird with feathers "
             "that flicker like small flames preens on a perch. A turtle drifts past at ankle "
             "height, its shell swirling with what looks like captive seawater. A tiny dragon "
             "whelp with shimmering scales flutters up to the party, studies them with keen eyes, "
             "chirps a melodious greeting, and zips away up a spiral staircase, clearly expecting "
             "to be followed."),
    # The laboratory interior as a centered plate: a float anchored this close
    # to a page foot kept overflowing the bottom margin, and an inline plate
    # paginates safely at any size.
    ("img", f"{A}/npcs/ravenstone_laboratory_dalle.webp",
     "The great hall of Ravenstone Laboratory, where every shelf has a tenant.", 4.6,
     {"crop": "4:3", "hmax": 4.6}),

    ("h2", "Professor Aelwyn Ravenstone"),
    # Portrait float anchored ahead of the study introduction so it never
    # straddles the page foot; the heading and text wrap beside it.
    ("imgfloat", f"{A}/npcs/professor_aelwyn_dalle.webp", 3.1),
    ("gold", "The staircase winds around an atrium of hanging plants and softly glowing crystals, "
             "opening into a vast study where bookshelves rise to a domed ceiling painted as the "
             "night sky. At a great wooden desk buried in open tomes, scrolls, and peculiar brass "
             "instruments stands the master of the house: a **tall high elf** with long silver "
             "hair, sharp emerald eyes, and robes that split the difference between a scholar's "
             "gown and a field jacket. He looks up, and his whole face lights with delight."),
    ("gold", "**Aelwyn:** “Ah, visitors! How wonderful. I do not get many these days.”"),
    ("gold", "Introductions are made all around: Lilly Glimmergear, Ursa Catchum, Stabby "
             "Sharpblade. “Please, call me Aelwyn,” the professor says, spreading his hands to "
             "the creatures perched on cushions and chandeliers around the study. “Any friend of "
             "these marvelous creatures is a friend of mine.” Then his gaze falls on the fourth "
             "traveler, currently tasting a bookshelf, and his emerald eyes go wide. “My word. "
             "Is that a **Lickgloom** you have there? I have only read of them in the ancient "
             "texts. Remarkable!”"),
    ("gold", "**Stabby:** “You would not believe the day we have had. Mud creatures, rock "
             "serpents, a goddess made of stars, and now this place. It is like stepping into a "
             "storybook.”"),
    ("gold", "**Aelwyn**, chuckling: “I can imagine. The world is full of wonders, especially "
             "now, with the boundaries between realms becoming... flexible.” He waves them into "
             "deep chairs by the hearth, and a small bipedal salamander with a cheerful flame "
             "flickering on its tail trots over with a tray of steaming herbal tea, entirely "
             "unbothered by its own job title. “Not originally from here, most of my companions,” "
             "Aelwyn says, sipping. “They have appeared over the past few years, from adjacent "
             "planes intersecting with ours. I have devoted my research to understanding the "
             "shifts in our world's fabric. It sounds as though you four have been doing field "
             "work on my behalf.”"),
    ("gold", "The party talks late into the evening: the motes, the guardians of the forest, the "
             "Grimfang, the vision in the glade. Aelwyn listens the way a dry garden drinks rain. "
             "And more than once, the party notices his sharp eyes drifting to the **Essence "
             "Sphere** in Lilly's lap, where it hums its soft, sleeping note."),

    ("h2", "Guest Quarters"),
    ("gold", "At last Aelwyn notices the road weariness under their excitement and rises. "
             "“Forgive me. You must be exhausted. I insist you stay the night; there is much I "
             "would like to discuss, and none of it improves after midnight.” A small owl like "
             "creature with luminous eyes swoops down at his soft clap and leads the party through "
             "corridors hung with tapestries of distant realms, to adjoining rooms with plush "
             "beds, moonlit garden windows, and floating crystal lamps that brighten at a touch. "
             "On a small table in each room, a tiny luminescent sprite hovers beside a tray of "
             "fruit, bread, and cheese, in case anyone should need a midnight snack."),
    ("gold", "Stabby flops onto his bed with a contented sigh. “Now this is more like it. "
             "Beats the hard ground any day.” Lilly touches a crystal lamp and watches it glow, "
             "already reverse engineering it in her head. Ursa stands at the window, looking up at "
             "stars that seem to look back. Lickgloom curls at the foot of a bed and is asleep in "
             "seconds, tongue out."),
    ("gold", "At the door, the professor pauses, candle in hand, his gaze resting one more moment "
             "on the Essence Sphere glowing gently on Lilly's nightstand. “Rest well, my young "
             "friends,” he says. “Tomorrow, we begin.”"),
    ("divider",),
    ("bridge", "Their second day together held a quest completed, two ambushes weathered, a "
               "goddess's charge laid upon them, a mountain taught respect, and a warm bed in a "
               "house full of impossible creatures. Whatever the professor saw when he looked at "
               "the Sphere, morning would tell."),
    ("gold", "*Next: Session 3, in which the professor examines the Essence Sphere, three small "
             "creatures wait in three baskets, and a dark figure watches from the top of Stormwatch "
             "Cliffs.*"),

    # ------------------------------------------------------------------
    ("h1", "Appendix: Creatures of Session Two", {"pagebreak": True}),
    ("body", "Compact statistics for the table. The full bestiary, with lore and pictures, lives in "
             "the compendium."),
    ("stat", "Mudskip", [
        "Small elemental (Plane of Water), neutral. **CR 1/2** (100 XP). AC 13 (natural armor), "
        "HP 22 (4d6 + 8), Speed 20 ft., swim 30 ft.",
        "STR 12, DEX 14, CON 14, INT 6, WIS 12, CHA 8. Skills Stealth +4, Perception +3.",
        "Resistances fire. Vulnerabilities lightning. Darkvision 60 ft. Understands Aquan.",
        "**Amphibious / Mud Dweller / Slippery.** Breathes air and water; ignores muddy difficult "
        "terrain; advantage on checks and saves to escape a grapple.",
        "**Multiattack.** One Mud Spit and one Tail Slap.",
        "**Mud Spit.** +4, range 30 ft., 1d6 + 2 bludgeoning; DC 12 Dexterity save or speed "
        "reduced 10 ft. until the end of its next turn.",
        "**Tail Slap.** +4, reach 5 ft., 1d8 + 2 bludgeoning.",
        "**Mud Splash (Recharge 5-6).** 15 ft. cone, DC 12 Dexterity save; 2d6 + 2 bludgeoning and "
        "blinded until the end of its next turn on a failure, half damage on a success.",
    ]),
    ("stat", "The Grimfang War Band", [
        "Rival goblin clan raiders: **2 goblins** with shortbows, **1 worg**, **1 orc**, "
        "**1 hobgoblin** with a crossbow, and **1 goblin boss** (scarred; taunts the Bloodfang).",
        "Standard 2024 Monster Manual statistics for each creature.",
        "**Tactics.** The boss coordinates: archers on the flanks pick at the back line, the worg "
        "and orc press the melee, the hobgoblin snipes from cover.",
        "**Outcome.** Beaten soundly; the survivors fled into the brush. The Grimfang remember.",
    ]),
    ("stat", "Terranox", [
        "Large elemental (Plane of Earth), unaligned. **CR 4** (1,100 XP). AC 16 (natural armor), "
        "HP 95 (10d10 + 40), Speed 30 ft., burrow 30 ft.",
        "STR 20, DEX 10, CON 18, INT 5, WIS 11, CHA 6. Darkvision 60 ft., tremorsense 60 ft.",
        "Immunities fire, poison; exhaustion, paralyzed, petrified, poisoned, prone. Resistances "
        "nonmagical bludgeoning, piercing, slashing (non adamantine).",
        "**Earth Glide / Immutable Form / Elemental Resilience / Siege Monster.** Burrows through "
        "unworked stone without a trace; immune to form altering effects; advantage on saves "
        "against magic; double damage to objects and structures.",
        "**Multiattack.** One Bite and one Tail Slam.",
        "**Bite.** +7, reach 10 ft., 2d10 + 5 piercing.",
        "**Tail Slam.** +7, reach 15 ft., 2d8 + 5 bludgeoning; DC 15 Strength save or prone.",
        "**Stone Coil (Recharge 5-6).** DC 15 Dexterity save or grappled and restrained (escape "
        "DC 15), 1d8 + 5 bludgeoning at the start of each of its turns.",
        "**Earthquake Stomp (Recharge 6).** 20 ft. radius, DC 15 Dexterity save; 4d6 bludgeoning "
        "and prone on a failure, half damage on a success.",
    ]),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    out = build_doc(BLOCKS, "sessions/session_02_oakshade_village.docx")
    print("built", out)
