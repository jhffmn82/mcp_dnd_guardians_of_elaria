# build_session_06.py
# The Guardians of Elaria, Session 6: Lanterns in the Fog
# Publication build. Canon: memory/campaign_canon.md + CONTRADICTIONS.md rulings.
# Rulings baked in: Elaria (never Alaria); ONE chest, three relics; Ghostbloom is SHE
# and completes her evolution this session; Bellshadow is the belltower quarter, the
# bellkeeper unnamed; the Remembrance Knot recalls Captain Brynn Wavewarden's knot
# lessons; Ms. Wicke's children were with kin and come home; the whistle in the lair
# was Harlan's own childhood keepsake; Candyfang Katana; the idol belongs to Session 7.
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc

A = "assets"
BLOCKS = [
    ("titlepage", "THE GUARDIANS OF ELARIA", "SESSION 6",
     "Lanterns in the Fog",
     "An illustrated adventure. Read the gold boxes aloud; the purple boxes are for the DM."),
    # Session-opening showpiece: Wraithpine from the coastal ridge dominates page 1.
    ("img", f"{A}/scenes/s6_wraithpine_ridge.png",
     "Wraithpine from the coastal ridge: Lantern Night glowing through the fog.", 6.2,
     {"crop": "3:2", "hmax": 4.5}),

    # Page 1 is title + the ridge showpiece; the recap starts fresh on page 2
    # and Part One flows directly after it, so no page is left near-empty.
    ("h1", "Previously, on The Guardians of Elaria...", {"hardbreak": True}),
    ("gold", "The sea took almost everything. The **Stormwind** capsized in a storm with a voice "
             "in it, and the heroes woke aboard the **Flying Dutchman**, where **Davy Jones** "
             "harvested the essences of living things into Guild-stamped crates bound for "
             "somewhere south and secret. The heroes won a dice game they were meant to lose, "
             "fought a battle across a cursed deck, and destroyed Davy Jones; the Dutchman split "
             "apart beneath them and sank into the dark. They escaped on a little cutter called "
             "the **Vigil**."),
    ("gold", "And through all of it, **Floraburst** slept. Aboard the ghost ship Lilly had drawn a "
             "drifting ghost-essence into a vial, and their small fey friend had breathed it in and "
             "folded up like a flower at dusk. All through the long row to shore she lay curled in "
             "the bottom of the boat, glowing faintly, changing shape by the hour, dreaming some "
             "long pale dream none of them could follow."),
    ("dm", "The heroes are **level 5** as of this session. Full creature statistics live in the "
           "compendium; a compact appendix closes this session."),

    # ------------------------------------------------------------------
    ("h1", "Part One: The Village of Lanterns"),
    ("bridge", "The Vigil ground ashore at dawn on an unfamiliar coast, and the heroes climbed "
               "out of the sea's cold hand and started walking."),

    ("h2", "Landfall"),
    # Ghostbloom floats beside the landfall path and her waking below it: an
    # emotional peak, sized generously. Anchored this high on the page so the
    # full-height portrait clears the bottom margin.
    ("imgfloat", f"{A}/characters/ghostbloom.png", 2.9, {"hmax": 4.0}),
    ("gold", "The surf leaves salt on lips and sand in boots. Morning fog burns slowly to pearl "
             "as the Guardians of Elaria follow a narrow footpath along wind-gnarled pines, gulls "
             "wheeling far below, the whole world smelling of brine and cold green needles. Ahead, "
             "where the coast dips into a hollow, lanterns glow through the mist like a braid of "
             "ember eyes."),

    ("h2", "She Wakes Changed"),
    ("gold", "On the path beneath the pines, the sleeping bundle in Ursa's arms stirs at last. "
             "Petals unfold, but they are not Floraburst's petals anymore: they are pale and "
             "translucent now, like flower glass, and when the sea wind moves through them they "
             "chime, a tiny frost-cold music. She lifts free of Ursa's arms and simply stays "
             "there, floating at shoulder height, blinking at the fog with eyes full of soft "
             "white light. She is new. She is still, unmistakably, their friend."),
    ("gold", "**Lilly**, very quietly: “She is not Floraburst now, is she. Look at her. She is "
             "like a bloom made of ghost-light.” The little creature chimes, pleased, and turns "
             "a slow circle in the air. And so, on a fog-bound footpath above the sea, she is "
             "named: **Ghostbloom**. All that day, and all the strange night to come, her glow "
             "leans gently toward trouble, the way a compass leans north."),

    ("h2", "Lantern Night"),
    ("gold", "The footpath crests a rise, and the village of **Wraithpine** pools below in a "
             "hollow of slate roofs and cedar eaves. Pumpkins watch from every doorstep. Paper "
             "moons and cat masks sway above a square of harvest stalls, steam rises from copper "
             "kettles, and a fiddle finds its first notes. The air is cider, beeswax, damp "
             "leaves. It is **Lantern Night**, the village's own festival, and everything about "
             "it is warm and bright and welcoming."),
    # (The ridge-crest view now leads the whole session as the page 1 plate.)
    ("gold", "Almost everything. As boots cross under the first lantern arch, a pressure pricks "
             "at the ears, like a mountain pass without a mountain. A thin note is drifting "
             "through the chimney flues and cellar grates. Wind, perhaps. Or the tail of a song "
             "that refuses to end."),
    ("dm", "Group **Wisdom save, DC 13**, the first time the thin note finds their ears. On a "
           "miss, one small fresh memory slips away, just enough to feel wrong; on a success, an "
           "ear-pop and a strange clarity."),

    ("h2", "The Gasping Gull"),
    ("gold", "The **Gasping Gull** throws wide its shutters and its hearth breathes softly. "
             "Behind the bar, the keeper, **Maera**, wipes an already spotless counter and calls "
             "out, “Finally, rush hour! Squeeze in where you can!” The room holds exactly three "
             "customers and one old spaniel asleep by the stove: **Brindle**, gray about the "
             "muzzle, twitching through comfortable dreams."),
    ("gold", "The wrongness is quiet, and it is everywhere. Maera sets a fourth place at a table "
             "laid for three, without seeming to notice. Twelve bowls of stew steam in her ledger, "
             "but two sit cooling on a tray that nobody comes for. Her ledger skips a line, the "
             "numbers hopping neatly over the gap as if something had been neatly erased, or "
             "neatly never was. Keys for every room gleam untouched on their hooks."),
    # Maera floats beside the square's small wrongnesses. Anchored here, high
    # on the page, so the float clears the bottom margin.
    ("imgfloat", f"{A}/npcs/maera.png", 3.3),
    ("gold", "Out in the square it is the same song in different keys. A chandler presses a "
             "sugared chip into Lilly's palm, “for remembering,” then blinks, the thought sliding "
             "off her face like rain. A curio-mender dusts a bundle of old theater playbills; on "
             "one of them a performer's name has been scrubbed so hard the paper has thinned to "
             "lace. “Moths,” the mender mutters, and ties the twine tighter. Black ribbons hang "
             "everywhere, knotted to gates and wrists and lantern posts, and nobody can quite say "
             "why. Villagers forget what they are saying in the middle of saying it."),
    ("gold", "Ghostbloom drifts near a lantern, and the flame dims, then swells, as if testing "
             "harmony with the thin hidden note. In Lilly's pocket, the **Essence Sphere** gives "
             "a heartbeat: two tones seeking each other, failing, seeking again."),

    ("h2", "The Bellkeeper of Bellshadow"),
    ("gold", "Beneath the belltower, in the old quarter the villagers call **Bellshadow**, an old "
             "man stands apart from the festival with a slate under his arm and beeswax glistening "
             "in his ears. His eyes are winter-sharp, the only pair in Wraithpine that seem to be "
             "looking *at* things. He taps his ear. He taps his slate. Then he writes three words "
             "with a patient hand and holds them up:"),
    ("gold", "**WRITE. DON'T LISTEN.**"),
    # Bellshadow as a half-page establishing plate beneath the slate's warning.
    ("img", f"{A}/scenes/s6_belltower_square.png",
     "Bellshadow, the old quarter beneath the belltower, where the bellkeeper keeps watch.", 6.2,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "Above him the bell gives a single accidental chime. Across the square, in the "
             "Gasping Gull, a fourth bowl of stew cools untouched, and Maera smiles at a chair "
             "the village cannot quite hold in mind."),

    # ------------------------------------------------------------------
    ("h1", "Part Two: Three Threads in the Fog", {"hardbreak": True}),
    ("bridge", "Something was wrong in Wraithpine, and it had left threads hanging everywhere. "
               "The heroes pulled three of them: a cellar, a lane of pumpkins, and a hill of "
               "leaning headstones."),

    ("h2", "Maera's Cellar"),
    ("gold", "“If you've stomachs for it,” Maera says, sliding a key from its hook, “give the "
             "pests down there a scare. Ruined a whole pot this morning.” The trapdoor groans. "
             "Stone steps breathe up a cool draft that smells of earth, spilled stew, and, "
             "faintly, the tide. Barrels crouch in the dark like sleeping oxen. Something "
             "chitters, and something else answers a half-beat late, like an echo that forgot "
             "its place."),
    ("gold", "Then the burlap sacks erupt. A gray tide of rats hits the floor, claws skittering, "
             "a hundred pinprick eyes catching the lantern light, and from the rafters something "
             "heavier drops straight for the heroes' shoulders."),
    ("dm", "**The cellar fight.** 2 Swarms of Rats (one starting in the rafters) and 4 Giant "
           "Rats, in a tight aisle of barrels and shelves. Book statistics; see the appendix note."),
    ("imgfloat", f"{A}/scenes/s6_cellar_rats.png", 3.3),
    ("gold", "When the last tail goes still, the cellar gives up its stranger secrets. Under the "
             "shelves lies a chewed dog collar. A thin drag-mark crosses the dust to the far "
             "wall, and there, when Ursa holds the lantern close, the flame leans toward a "
             "hairline seam in the stone, as though the crack is quietly *inhaling*. Pressing an "
             "ear to the rock, the heroes catch it: a faint humming tone hanging inside the "
             "hill like a thread. From above, Maera calls down cheerfully, “Any luck? These old "
             "cellars touch caves beneath the town, you know. Wells to the sea. Smugglers' "
             "tales.”"),

    ("h2", "Pumpkin Row"),
    ("gold", "Pumpkin Row climbs a low hill between cottages, hay bales stacked two high, "
             "jack-o'-lanterns grinning from every fence post and windowsill. As the heroes walk "
             "it, the wind dies. Fog pools like spilled milk. A carver's lantern flares, and in "
             "that flare **every carved face along the lane turns in the same breath**, all of "
             "them looking toward the dark peak of the old theater roof."),
    ("gold", "Two scarecrows creak down from their posts. Straw whispers across the furrows and "
             "gathers itself into small, hunched walkers with button eyes. The thin note in the "
             "fog swells, steady as a bow drawn across the rim of a glass."),
    ("dm", "**Straw stirs.** 2 Scarecrows and 6 Strawlings among the flickering "
           "jack-o'-lanterns. Statistics in the appendix."),
    # Pumpkin Row as a half-page establishing plate.
    ("img", f"{A}/scenes/s6_pumpkin_row.png",
     "Pumpkin Row: every carved face along the lane turns toward the old theater roof.", 6.0,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "It is a wild, whirling scrap among the pumpkins, candy-striped steel flashing, "
             "sparks and starlight scattering straw in every direction. When the last strawling "
             "collapses into a harmless heap, Stabby cuts open the heart-gourd charm stitched "
             "under a scarecrow's ribs. Inside, folded small, is a scrap of a map with the old "
             "theater and the town well circled, and a stamp in stage-engraver script: **PROP "
             "ROOM, OLD THEATER**. The shaken carver, freed of whatever had his lane, presses a "
             "bell-handled lantern into the heroes' hands in thanks."),

    ("h2", "The Graveyard: Lay a Ribbon"),
    ("gold", "The path climbs the hill behind Wraithpine into a wind-crooked cemetery ringed by "
             "cypress, where headstones lean together like old neighbors sharing secrets and "
             "black ribbons hang from the iron gate in neat, whispering knots. Fresh flowers lie "
             "on a plot near the crest. The headstone's name line is a scraped scar: someone has "
             "**carefully chiseled the name away**, chisel dust still pale in the letters. In "
             "one corner is a maker's mark, small and strange for a gravestone: a stage mask. "
             "The blue glass of the bell-handled lantern brightens here, all on its own."),
    ("gold", "As the heroes study the stone, the churned earth stirs. The recently quiet do not "
             "wish to be laid twice, and a pair of the restless dead claw up out of the soil, "
             "moaning, drawn to the same wrongness that scraped the name away."),
    # The rite of the forgotten name, as a generous landscape plate.
    ("img", f"{A}/scenes/s6_graveyard_rite.png",
     "Lilly lights the blue lantern and begins the rite of the forgotten name.", 6.0,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "The heroes put them gently back to rest, and then they do the older, kinder work. "
             "Charcoal rubbed across the blank line raises the ghosts of letters, like footprints "
             "in frost. The name is written back where it belongs. The post bell's clapper is "
             "untied and rung three times, and at the third ring the ground answers with a sigh "
             "from deep below. Last comes the ribbon: loop, wrap twice, pull through, a small "
             "tail pointing toward the sea, tied exactly the way **Captain Brynn Wavewarden** "
             "taught them aboard the Stormwind, laughing at their tangles all the while. The "
             "knot tightens. The soil settles. For a breath the fog pulls back, and the grave "
             "looks ordinary again: just a stone, with a name, remembered."),
    ("dm", "**The rite and its blessing.** Restore the name, ring the bell, tie the Remembrance "
           "Knot. 2 Zombies rose partway through (book statistics). Each hero who took part in "
           "the rite gained **Hold Fast**: once this session, advantage on one Wisdom save "
           "against forgetfulness or the song."),

    # ------------------------------------------------------------------
    ("h1", "Part Three: Names the Stone Won't Keep", {"hardbreak": True}),
    ("bridge", "Three threads, one knot. A cellar that breathed, a field of straw that pointed "
               "at the theater, a grave that forgot its name. And in Stabby's pocket, a parcel "
               "slip found along the way, made out to a man nobody in Wraithpine could remember."),

    ("h2", "3 Lantern Lane"),
    ("gold", "The parcel slip crinkles in the hand: *To HARLAN WICKE, 3 Lantern Lane.* The houses "
             "on Lantern Lane press close like people whispering. A brass 3 is screwed to a green "
             "door, a thin line of light shows under the threshold, and somewhere inside a kettle "
             "ticks as it cools. **Ms. Wicke** opens the door slowly, a small steady woman with a "
             "cloth folded in her hands. “Evening. Oh, visitors. Come in, you'll catch cold.”"),
    ("gold", "The room is neat in the obvious ways and wrong in the quiet ones. On a side table "
             "sits a family portrait: a woman with wind-tossed hair, two children in matching "
             "scarves, and a tall man with a stagehand's smile and coal dust on his cuff. "
             "Children's toys sleep in a basket, waiting. And yet one cup and one plate stand "
             "washed and drying by a window that looks out on an empty street."),
    ("gold", "Shown the slip, she reads it twice, and a tremor crosses her face. **Ms. Wicke:** "
             "“Harlan? That's... that is my name, Wicke, yes. But I live alone.” Her eyes travel, "
             "snag on the portrait, and skitter away, the way a hand skitters off a hot pan. "
             "“You will think me foolish, but most mornings I wake up crying, and I cannot say "
             "why. I wash my face and it stops. Then the day begins.” She hands the slip back "
             "with a gratitude like a bow. “If you meant to find this Harlan, try the theater; "
             "they keep props there, deliveries and such. And please, be careful at night. The "
             "fog keeps... thoughts.”"),

    ("h2", "The Belltower"),
    ("gold", "The square is nearly empty now, stalls shuttered, lanterns burning down to puddles "
             "of wax. Under the belltower of Bellshadow the old bellkeeper is waiting, as if he "
             "knew they would come. “Mouths moving,” he says, too loudly, tapping the wax in his "
             "ears. “Can't hear you. Won't hear *it*, either.” He scratches fast on his slate "
             "and turns it around: **YOU HEAR THE SONG?**"),
    ("gold", "And as if the question summoned it, the note **swells**, rising through the square "
             "like a seam opening, a whistle from two streets away that cannot be placed, a "
             "lullaby with no words and no end, pressing gently, gently, on the inside of every "
             "skull."),
    ("dm", "Second group **Wisdom save, DC 13**, as the song swells. On a miss, the day's clues "
           "slip like a dream on waking; on a success, a pop behind the eyes, and the sense of "
           "something trying to smooth the mind flat."),
    ("gold", "The bellkeeper sees the wobble in their eyes and moves fast, pressing small curls "
             "of beeswax into every palm, wax that smells of summer and smoke. He pulls one of "
             "his own plugs half out, just long enough to speak, and his voice is grave. “Put it "
             "in. All the way. Don't be brave about it. The song is not for bravery.” He reseats "
             "the plug, and then he mouths two words, slow and exaggerated, so there can be no "
             "mistake: **UNDER. THEATER.**"),
    ("dm", "Beeswax earplugs: **advantage** on saves against the song, and its aura cannot lock "
           "a plugged hero's reactions. The heroes wore them from here to the end."),

    ("h2", "The Reveal at the Gasping Gull"),
    ("gold", "With the beeswax seated, the world sharpens. Lantern light cuts cleaner. The air "
             "feels thick, like the moment before thunder. The heroes cross the square to the "
             "Gasping Gull, where Maera is laying out bowls and humming, and the moment they "
             "step inside they finally, truly, **see**."),
    # The session villain, floated large right at the moment of the reveal
    # (directive: 3.4in float with a raised height cap).
    ("imgfloat", f"{A}/scenes/s6_tavern_reveal.png", 3.4, {"hmax": 4.0}),
    ("gold", "There has always been a head in this room. That is the terrible, simple truth the "
             "song has been singing over, night after night. A long pale neck rises out of the "
             "open trapdoor behind the bar, and atop it sways a face that is almost a person's "
             "face and is not, smooth and calm, with rows of small slate teeth. It has been "
             "here all along, drinking up names, and every eye in Wraithpine has slid off it "
             "the way Ms. Wicke's eyes slid off her own portrait. Of poor old Brindle there is "
             "no sign at all: only his bowl by the stove, and two clean tracks in the dust "
             "leading to the trapdoor, and none leading back."),
    ("gold", "**Maera**, smiling at her ledger, not looking at the door: “What a quiet night. "
             "Sometimes it's nice to hear yourself think.” The head turns. Not toward Maera. "
             "Toward the heroes. Its eyes aim at the place where their thoughts are, not the "
             "place where their bodies stand."),
    ("dm", "**The tavern fight.** One **False Hydra Tavern Head** (appendix), in a room full of "
           "tables, stew pots, and one oblivious innkeeper to keep out of harm's way."),
    ("gold", "The fight is close and crashing: tables flipped for cover, the neck writhing "
             "between the rafters, Ghostbloom's chime splitting the hum like frost splitting "
             "stone. Candyfang steel cracks slate teeth, emerald fire skates along the pale "
             "neck, and starlight strikes true. With a final shudder the head sags, the light "
             "goes out of its wrong eyes, and it is destroyed. Across the room a **second** "
             "pale neck, one nobody had seen, snaps back beneath a loose floorboard and pours "
             "itself away down a slime-rimmed tunnel into black stone, and the hum below "
             "deepens, like a choir trying to sing through the floor."),
    ("gold", "Maera stands frozen at the bar, staring at the word **LOOK** the heroes have "
             "written across her ledger, and her breath catches on something with no name left "
             "in it. **Maera:** “Br... where is my...?” The fog tries to soften her eyes again; "
             "she grips the bar until it passes. “Forgive me. I... I'll fetch more bowls.”"),

    # ------------------------------------------------------------------
    ("h1", "Part Four: Where the Song Lives", {"hardbreak": True}),
    ("bridge", "A trail led from the tavern's broken floor into the dark beneath Wraithpine, "
               "and the thin note grew into a pressure, a hand laid gently on the inside of the "
               "skull. The heroes plugged their ears, lit their lanterns, and followed it down."),

    ("h2", "The Descent"),
    ("gold", "The tunnel curls beneath the village like a rib: wet timber props, black nails, "
             "and, strangest of all, faint chalk marks scrawled on the rock in a stagehand's "
             "quick hand: *Upstage. Hold. Places.* The passage opens at last into the drowned "
             "orchestra pit below the **Old Theater**, crossed by catwalks of beam and rope, "
             "stage machines jutting up like broken ribs."),
    # The shuttered theater as a half-page establishing plate above the descent.
    ("img", f"{A}/scenes/s6_old_theater.png",
     "The Old Theater, shuttered and dark, with the song living beneath it.", 5.8,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "And in the center, filling the pit, it waits. The **False Hydra** entire: a pale "
             "bulk resting on a mound of remembrances, boots and playbills, keepsakes and "
             "ribbons, every ribbon black, with four long necks coiled up through round ports "
             "in the theater floor above. The faces at the ends of the necks are almost "
             "featureless, calm as sleep. The song pours off the creature in slow waves; even "
             "through beeswax the heroes feel it, pressing, patient, asking them nicely to "
             "forget they ever came."),
    ("gold", "On a ledge among the props lies a leather toolbelt with a torn name tag: **HARLAN "
             "WICKE**. Beside it, worn smooth by decades of a workman's pocket, a small carved "
             "whistle: Harlan's own, kept since his boyhood, carried all his life. Ursa picks "
             "it up and holds it a long moment, and nobody says anything at all."),

    ("h2", "The Lair Battle"),
    ("dm", "**The lair battle.** The False Hydra Adult: body plus four heads (appendix). A "
           "quiet approach along the high catwalk earned a surprise round, and a focused strike "
           "dropped the first head before the song even turned. **Vital Link:** the body "
           "resists weapon damage while heads remain; each destroyed head strips one layer of "
           "that protection, and the body acts more often the more heads still sing."),
    ("img", f"{A}/scenes/s6_hydra_lair.png",
     "The False Hydra entire, in the drowned orchestra pit below the Old Theater.", 5.8,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "It is the hardest fight since the Dutchman. Necks lash up through the floor ports "
             "and slither between them, hunting; the mound shifts under pale limbs to open and "
             "close the ground; sandbags and pulleys crash down from the fly loft. But the "
             "heroes have wax in their ears and a plan in their heads, and one by one, the "
             "**heads begin to fall**. With the second, the song falters, as if someone cut a "
             "harmony, and blades bite deeper. With the third, the great body's pale flesh "
             "loses its strange stubbornness altogether. Lilly's cannon roars, Stabby dances "
             "along a swaying catwalk, Ursa calls down the light of stars this deep place has "
             "never seen, and Ghostbloom blazes like a lantern in a window, calling everyone "
             "home."),
    ("gold", "The last head rears back to sing, and the Candyfang Katana and a lance of "
             "starlight meet it together. It falls. And the song does not fade. It simply "
             "**stops**, all at once, like a metronome switched off. The great body sinks down "
             "into its mound and is still. Air rushes into the space where the note used to "
             "live."),

    ("h2", "The Song Ends"),
    ("gold", "Then the remembering begins. Ribbons all over the lair untie themselves and drift "
             "to the floor. Somewhere overhead, muffled through stone, voices rise, bewildered, "
             "calling names, more and more of them, a whole village's worth of names flooding "
             "back like riverwater breaking a dam. The bell of Bellshadow rings, properly this "
             "time, three clean notes. And on the ledge beside Harlan's toolbelt, a ledger page "
             "that had lain blank for months finishes its own sentence in tidy ink:"),
    ("gold", "**HARLAN WICKE, HOME.**"),

    # ------------------------------------------------------------------
    # No hardbreak: "HARLAN WICKE, HOME." lands at the very top of this page
    # and Part Five opens right under it, which reads far better than leaving
    # that single line stranded on an otherwise empty page.
    ("h1", "Part Five: The Light Beneath the Earth"),
    ("bridge", "The song was dead, the village was waking, and in the quiet under the theater, "
               "something golden stirred."),

    ("h2", "The Chest"),
    ("gold", "As the last echo dies, silence settles thick as velvet, and Ghostbloom's glow "
             "changes: not a battle light now, but something gentler, pulsing like a heartbeat. "
             "A seam of **golden light** opens through the settling remains of the mound, and "
             "there, half buried, rests a chest bound in vines of silver and root."),
    ("gold", "Ghostbloom drifts to it first, drawn by an unseen will, the pale flower on her "
             "back bending toward the light. She sings, one low melodic tone, and the silver "
             "vines part like curtains and the lid swings open: without sound, without "
             "resistance, as if it had been waiting all along for exactly this moment and "
             "exactly these heroes."),
    ("img", f"{A}/scenes/s6_chest_opening.png",
     "Elaria's gift: the chest bound in silver vines opens without a sound.", 6.2,
     {"crop": "3:2", "hmax": 4.6}),

    ("h2", "Three Relics"),
    ("gold", "Inside rest three objects, each radiating a faint, familiar magic. A slim **staff "
             "etched with constellations**, silver inlays tracing star maps down midnight-dark "
             "wood, a crystal glowing softly at its crown: for Ursa. A **shimmering crimson "
             "sash** of rewoven stage-silk that hangs in the air a heartbeat too long when "
             "tossed, as if water were holding it up: for Stabby. And a **polished brass core**, "
             "thumb-sized, filigreed with folding micro-gears, humming with the same energy as "
             "Lilly's cannon: for Lilly. On each of them, worked small and deliberate, the same "
             "sigil: **a seven-point star wrapped in a leafed vine**. Elaria's mark."),
    ("gold", "Lilly kneels beside the chest, hands trembling. **Lilly:** “These aren't ordinary "
             "relics. They were made for *us*.” She looks up at Ursa, eyes wide and glassy with "
             "realization. “It is **Elaria**. She is guiding us. Testing us. Making us "
             "stronger.” Ghostbloom lets out a low, melodic tone, and for a heartbeat the "
             "golden light swirls upward like petals in a breeze, then fades. The chest turns "
             "dull and ordinary, its purpose fulfilled."),
    ("dm", "**The relics.** The Staff of Waking Constellations (Ursa), the Sash of the Swift "
           "Current, Rewoven (Stabby), and the Glimmerspire Pocket Dynamo Mk II (Lilly). Full "
           "handout text for all three lives in the treasures compendium."),

    ("h2", "Dawn Over Wraithpine"),
    ("gold", "When the heroes climb back into the world, dawn is breaking, and Wraithpine is "
             "waking into grief and gratitude at once. The fog burns away, and with it the "
             "gentleness of forgetting. People stand in doorways staring at spaces where loved "
             "ones should be, remembering, all at once, everyone the creature took. A man turns "
             "over a child's toy he does not remember carving. A woman kneels at the grave on "
             "the hill, saying a name that only just came back to her, and the Remembrance Knot "
             "holds."),
    ("gold", "At the Gasping Gull, Maera meets them with shaking hands and dry, clear eyes. "
             "**Maera:** “They're calling it a **false hydra**. A creature that eats not just "
             "people, but the memory of them. All this time we lived with it and never knew. My "
             "dog. My friends. I didn't even know what I'd lost.” She wipes her eyes and finds "
             "a small, real smile. “Thank you, Guardians. You freed us. And I don't think we "
             "will ever forget again.”"),
    ("gold", "And down Lantern Lane comes the morning's one perfect mending: a cart from the "
             "next village, and two children in matching scarves tumbling out of it, home from "
             "their kin's house where they had stayed through the festival, running up the lane "
             "and into their mother's arms. **Ms. Wicke** holds them so tightly their hats fall "
             "off, weeping for Harlan and for joy in the same breath, and this time no fog "
             "comes to take the feeling away. Her children are safe. Their father will be "
             "remembered. The family grieves together, which is the only way grief ever gets "
             "lighter."),
    ("gold", "**Stabby**, watching from the end of the lane, hand resting on the Candyfang "
             "Katana: “Let's not stick around for this part.” **Ursa** nods, glancing east "
             "toward the hills where the road winds away. “The road to Gearhaven won't walk "
             "itself.”"),
    ("divider",),
    ("bridge", "And so they went, past the village, past the graves, following the rising sun, "
               "three heroes with three star-marked relics and one small ghost-light friend "
               "sailing along above their packs. Wraithpine rang its bell behind them, three "
               "clean notes, remembering. The Guardians of Elaria walked east, guided, it "
               "seemed, by something greater than fate."),
    ("gold", "*Next: Session 7, in which the heroes reach Gearhaven, the clockwork city, where "
             "the Essence Sphere's makers have answers, a locksmith has a ten-year secret, and "
             "the stars themselves turn out to be part of the story.*"),

    # ------------------------------------------------------------------
    ("h1", "Appendix: Creatures of Session Six", {"hardbreak": True}),
    ("body", "Compact statistics for the table. The full bestiary, with lore and pictures, lives "
             "in the compendium."),
    ("stat", "False Hydra, the Tavern Head", [
        "Large aberration (one head and neck), unaligned. AC 14, HP 70 (9d10 + 18), Speed 10 ft., climb 10 ft.",
        "STR 16, DEX 12, CON 14, INT 6, WIS 14, CHA 7. Blindsight 10 ft., tremorsense 30 ft., darkvision 60 ft.",
        "Resistance psychic. Condition immunities charmed, frightened, prone.",
        "**Mind-Humming Aura.** A creature without beeswax starting its turn within 30 ft. makes a "
        "DC 13 Wisdom save or has disadvantage on attack rolls that turn; beeswax grants advantage on the save.",
        "**Bite.** +6 to hit, reach 10 ft., 13 (2d8 + 4) piercing, and the target is grappled (escape DC 14).",
        "**Segmented Neck.** Ignores forced movement and prone; after taking 20+ damage in one turn "
        "it recoils 5 ft. and loses its reactions until its next turn.",
    ]),
    ("stat", "False Hydra, Adult (body and heads)", [
        "Huge aberration, unaligned. **Body:** AC 15, HP 130 (12d12 + 48), Speed 10 ft., climb 10 ft. "
        "**Heads (4):** AC 14, HP 45 (6d10 + 12) each, reach 15 ft. from a floor port; a head may withdraw "
        "and re-emerge from any port on its turn.",
        "Body STR 18, DEX 10, CON 18, INT 7, WIS 14, CHA 8; saves Con +8, Wis +5. Tremorsense 60 ft., "
        "darkvision 60 ft. Resistance psychic; condition immunities charmed, frightened, prone.",
        "**Song of Unremembering.** While any head lives, a creature without earplugs starting its turn "
        "within 60 ft. makes a DC 15 Wisdom save or has disadvantage on attack rolls and cannot take "
        "reactions until its next turn. Beeswax: advantage on the save, and no reaction lock.",
        "**Vital Link.** While at least one head lives, the body has resistance to all weapon damage; "
        "each head destroyed removes one instance of this protection, and with no heads it has none.",
        "**Thrash (body).** +7 to hit, reach 10 ft., 13 (2d8 + 4) bludgeoning. **Bite (head).** +7 to hit, "
        "reach 15 ft., 14 (2d10 + 3) piercing, and the target is grappled (escape DC 14).",
        "**Legendary Actions.** One per living head, max 3/round: Hum Surge (one creature within 60 ft., "
        "DC 15 Wisdom or lose concentration and move only 10 ft. next turn), Bone Shift (reshape the mound; "
        "one 10-ft. square becomes difficult terrain or clears), Coordinate Strike (one head bites).",
    ]),
    ("stat", "Scarecrow (Monster Manual)", [
        "Medium construct, neutral. **CR 1**. AC 11, HP 36 (8d8), Speed 30 ft.",
        "Vulnerable fire; resistant to nonmagical bludgeoning, piercing, and slashing; immune to "
        "charmed, frightened, paralyzed, poisoned. Darkvision 60 ft.",
        "**Terrifying Glare.** One creature within 30 ft.: DC 11 Wisdom save or frightened for 1 minute "
        "(repeat the save at the end of each turn).",
        "**Claws.** +3 to hit, reach 5 ft., 9 (2d4 + 4) slashing.",
    ]),
    ("stat", "Strawling (reskinned Needle Blight)", [
        "Medium plant, neutral. **CR 1/4**. AC 12, HP 11 (2d8 + 2), Speed 30 ft.",
        "**Straw Lash.** +4 to hit, reach 5 ft., 4 (1d6 + 1) bludgeoning, and the target makes a DC 12 "
        "Strength save or is grappled (escape DC 12).",
        "**Chaff Burst.** +4 to hit, range 30/60 ft., 6 (2d4) piercing (a spray of straw flechettes).",
    ]),
    ("body", "The cellar rats (Swarm of Rats, Giant Rat) and the graveyard's restless dead (Zombie) "
             "use their standard book statistics."),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    out = build_doc(BLOCKS, "sessions/session_06_wraithpine.docx")
    print("built", out)
