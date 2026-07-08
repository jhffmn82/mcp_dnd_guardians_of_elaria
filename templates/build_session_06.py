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
    ("dm", "The heroes are **level 5** as of this session. Full creature statistics for this "
           "session live in the compendium; a DM run sheet and bestiary close this session."),

    # ------------------------------------------------------------------
    ("h1", "Part One: The Village of Lanterns"),
    ("bridge", "The Vigil ground ashore at dawn on an unfamiliar coast, and the heroes climbed "
               "out of the sea's cold hand and started walking."),

    ("h2", "Landfall"),
    # Ghostbloom floats beside the landfall path and her waking below it: an
    # emotional peak, sized generously. Anchored this high on the page so the
    # full-height portrait clears the bottom margin.
    ("imgfloat", f"{A}/characters/ghostbloom.png", 3.3, {"hmax": 4.0}),
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
             "white light. The **ghost essence** she drew in aboard the Flying Dutchman has "
             "finished its long, quiet work: Floraburst has evolved into a creature of the "
             "**ghost** kind. She is new. She is still, unmistakably, their friend."),
    ("dm", "**The sealed roll comes due.** The blind essence roll from Session 5 is finally "
           "revealed: the d12 gave **Ghost**. Floraburst evolved into a ghost type by the ghost "
           "essence taken from the Dutchman, and nobody at the table knew until she woke."),
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

    ("h2", "Three Tugs at Once"),
    ("gold", "The square pulls at the heroes from three directions at once. Behind the bar, "
             "Maera sighs toward the trapdoor: “If only someone would scare the pests from the "
             "cellar. Ruined a whole pot this morning.” On the hill path, a couple with black "
             "ribbons at their wrists climbs toward the graveyard, flowers in hand and eyes "
             "downcast. And along **Pumpkin Row**, a carver heaves a hay bale toward a waiting "
             "cart while two scarecrows watch from their posts with button-bright stares."),
    ("dm", "**Three threads, any order.** Let the party choose which thread to pull first; all "
           "three point, each in its own way, at the old theater. The song eats clues, so "
           "reward heroes who write things down."),

    # ------------------------------------------------------------------
    ("h1", "Part Two: Three Threads in the Fog", {"hardbreak": True}),
    ("bridge", "Something was wrong in Wraithpine, and it had left threads hanging everywhere. "
               "The heroes pulled three of them: a cellar, a lane of pumpkins, and a hill of "
               "leaning headstones."),
    ("dm", "**The clue chain (keep it unbroken).** Cellar: a chewed dog collar, a drag mark, a "
           "black ribbon thread on the stew pot, and a breathing seam with a hum inside the "
           "hill. Pumpkin Row: every carved face turns toward the theater, and the heart-gourd "
           "map is stamped PROP ROOM, OLD THEATER. Graveyard: a scraped-away name, a stage-mask "
           "maker's mark, and a parcel slip addressed to a man nobody remembers. Those lead to "
           "3 Lantern Lane, then to the bellkeeper (beeswax, and the mouthed words UNDER "
           "THEATER), then to the reveal at the Gasping Gull. If the table stalls, escalate in "
           "order: the Essence Sphere pulls toward the theater like a compass needle; the "
           "chandler murmurs about the black ribbons and the hill; at last the bellkeeper "
           "crosses the square himself and presses his slate into a hero's hands."),

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
    ("dm", "**The cellar fight.** 2 Swarms of Rats and 4 Giant Rats with Pack Tactics, in a "
           "tight aisle of barrels and shelves (book statistics; see the appendix note). One "
           "swarm lurks in the rafters and drops on a hero's shoulders: DC 13 Dexterity or it "
           "lands on you."),
    ("dm", "**Going in.** Torch held high: passive Perception 13 notices the flame leaning "
           "toward a hairline seam in the far wall, as though the crack is quietly inhaling. "
           "Quiet boots: Stealth against the swarms' passive Perception 10 to take position "
           "before the rush. Ghostbloom forward: her chiming petals grant advantage on the "
           "next Perception or Insight check to clock the seam."),
    # Float anchored ABOVE the cellar-toys note so it can never sink past the
    # bottom margin (DM flag 2026-07-06: it was overrunning the page foot).
    ("imgfloat", f"{A}/scenes/s6_cellar_rats.png", 3.1),
    ("dm", "**Cellar toys.** Shove a shoulder-high cask down the tight aisle (once, Strength "
           "DC 12): 1d4 bludgeoning and prone to whatever fails a DC 12 Dexterity save. Pull "
           "down the rickety shelf (an Action): an adjacent creature makes a DC 13 Dexterity "
           "save or is restrained under broken wood until the end of its next turn."),
    ("gold", "When the last tail goes still, the cellar gives up its stranger secrets. Under the "
             "shelves lies a chewed dog collar. On the prep table a dented stew pot sits with "
             "its ladle gnawed to splinters, and a single **black ribbon thread** clings to the "
             "rim, the same black as the ribbons knotted all over town. A thin drag-mark crosses the dust to the far "
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
    ("game", "PUMPKIN ROW: TURN THE FACES", [
        "*The straw only walks while the carved faces watch. Three ways to win; the Guardians "
        "may mix all three.*",
        "",
        "**Say this plainly.** Three big **key pumpkins**, one on the north post, one on the "
        "cart, one on the south post, keep trying to face the theater. Every scarecrow has a "
        "coin-sized **gourd charm** stitched under its ribs. The hay cart could bowl strawlings "
        "over, and the pumpkin stack could be kicked down to make a glorious mess.",
        "**A. Turn the faces (the puzzle).** As an Action, a hero turns or snuffs one key "
        "pumpkin, no check needed. While any two key pumpkins face away from the theater at "
        "the same time, every scarecrow skips its next turn. Manage it in two different rounds "
        "and the magic fizzles: the straw collapses, and the fight is over.",
        "**B. Clip the charm.** From within 5 feet, snip a scarecrow's heart-gourd, no roll: "
        "that scarecrow falls limp on the spot.",
        "**C. Fight it out.** 2 Scarecrows and 6 Strawlings (appendix), a solid scrap among "
        "the flickering jack-o'-lanterns.",
        "",
        "**The spoils.** A clean or clever end earns the carver's **bell-handled lantern** "
        "(1 use: advantage on one Investigation check in Wraithpine while it is lit). A split "
        "heart-gourd holds a map scrap with the old theater and the town well circled, stamped "
        "**PROP ROOM, OLD THEATER**.",
    ]),
    # Pumpkin Row as a wide cinematic plate: the 16:9 crop lets the lane share
    # its page with the rules card above it.
    ("img", f"{A}/scenes/s6_pumpkin_row.png",
     "Pumpkin Row: every carved face along the lane turns toward the old theater roof.", 5.6,
     {"crop": "16:9", "hmax": 4.6}),
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
    # The graveyard intro ends deep on its page; break so the rite card opens
    # its page whole (cards must never split).
    ("pagebreak",),
    ("game", "LAY A RIBBON: THE RITE OF THE FORGOTTEN NAME", [
        "*A grave whose name has been chiseled away will not stay quiet: the dead do not wish "
        "to be laid twice. The rite has four steps, and any hero may perform them.*",
        "",
        "**1. Raise the letter ghosts.** Rub charcoal across the scraped line: Intelligence "
        "(Investigation) DC 12 to make out the ghosts of the letters, faint as footprints in "
        "frost.",
        "**2. Restore the name.** Re-inscribe it with chalk, charcoal, or knife tip, set at "
        "the top of the stone the way a rite demands: Intelligence (Religion) or (History) "
        "DC 12.",
        "**3. Ring the bell.** Untie the black thread from the post bell's clapper and ring "
        "three times, speaking the name aloud (or a vow to remember). Ring one: the fog "
        "shivers. Ring two: the cypresses hush. Ring three: the ground answers with a sigh "
        "from deep below.",
        "**4. Tie the Remembrance Knot.** As an Action: make a loop, wrap twice, pull through "
        "once more, so a small tail points toward the sea. A hero who learned Captain Brynn's "
        "knots aboard the Stormwind ties it with advantage. If the knot is wrong, the ribbon "
        "loosens by itself and coils like a sleeping snake.",
        "",
        "**If the name is wrong or unknown**, the dead stir: 2 Zombies claw free (3 Zombies "
        "and 2 Skeletons if the rite is begun loud and careless). Lay them gently down; the "
        "rite can always be tried again.",
        "**The blessing.** When the knot takes hold, the soil settles and the stone warms in "
        "the palm. Every hero who took part gains **Hold Fast**: once this session, advantage "
        "on one Wisdom save against forgetfulness or the song.",
    ]),
    ("gold", "The heroes put them gently back to rest, and one risen hand, ash-pale, is found "
             "clutching a scrap of something stiff. Stabby pries it free: a **parcel slip**, "
             "creased and dirt-stained but legible, made out in tidy ink. *To HARLAN WICKE, 3 "
             "Lantern Lane.* Nobody in Wraithpine remembers any Harlan. Stabby pockets the "
             "slip."),
    ("dm", "[DM CHECK: the original document never records whose grave this is or what name "
           "the heroes restored. The stage-mask maker's mark points to a performer the "
           "creature took long ago. Any remembered name, laid with care, satisfies the rite.]"),
    # The rite of the forgotten name, as a generous landscape plate between
    # the discovery of the slip and the rite itself.
    ("img", f"{A}/scenes/s6_graveyard_rite.png",
     "Lilly lights the blue lantern and begins the rite of the forgotten name.", 6.0,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "Then they do the older, kinder work. "
             "Charcoal rubbed across the blank line raises the ghosts of letters, like footprints "
             "in frost. The name is written back where it belongs. The post bell's clapper is "
             "untied and rung three times, and at the third ring the ground answers with a sigh "
             "from deep below. Last comes the ribbon: loop, wrap twice, pull through, a small "
             "tail pointing toward the sea, tied exactly the way **Captain Brynn Wavewarden** "
             "taught them aboard the Stormwind, laughing at their tangles all the while. The "
             "knot tightens. The soil settles. For a breath the fog pulls back, and the grave "
             "looks ordinary again: just a stone, with a name, remembered."),

    # ------------------------------------------------------------------
    ("h1", "Part Three: Names the Stone Won't Keep", {"hardbreak": True}),
    ("bridge", "Three threads, one knot. A cellar that breathed, a field of straw that pointed "
               "at the theater, a grave that forgot its name. And in Stabby's pocket, the "
               "parcel slip pried from the churned earth of the hill, made out to a man nobody "
               "in Wraithpine could remember."),

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
    ("gold", "The bellkeeper sees the wobble in their eyes and moves fast, pressing small curls "
             "of beeswax into every palm, wax that smells of summer and smoke. He pulls one of "
             "his own plugs half out, just long enough to speak, and his voice is grave. “Put it "
             "in. All the way. Don't be brave about it. The song is not for bravery.” He reseats "
             "the plug, and then he mouths two words, slow and exaggerated, so there can be no "
             "mistake: **UNDER. THEATER.**"),
    # The belltower scene runs to the page foot; break so the session's
    # signature rules card opens its page whole.
    ("pagebreak",),
    ("game", "THE SONG OF UNREMEMBERING", [
        "*Something under Wraithpine is singing, and to hear the song is to forget. It has "
        "been eating the village one name at a time, and it will happily eat the heroes' "
        "clues too. These rules run for the rest of the session.*",
        "",
        "**When the song swells**, every hero makes a **Wisdom save, DC 13**. Failure: one "
        "fresh memory slips away, just enough to feel wrong, and the day's clues soften like "
        "a dream on waking. Success: a pop behind the eyes, and the sense of something trying "
        "to smooth the mind flat.",
        "**In battle it is worse.** A lone head's hum: start your turn within 30 feet, DC 13 "
        "Wisdom save or your attacks that turn have disadvantage. The full creature's song: "
        "within 60 feet, **DC 15**, and failure also locks your reactions until your next "
        "turn.",
        "**The beeswax remedy.** Soft curls of wax, seated all the way in: a plugged hero has "
        "**advantage** on every save against the song, and its hum can never lock their "
        "reactions. Do not be brave about it. The song is not for bravery.",
        "**The bellkeeper's law: WRITE. DON'T LISTEN.** Ink and chalk do not forget. Anything "
        "written down (a slate, a ledger, one word on a page) stays true even when minds "
        "wobble, and with wax in the ears the writing keeps its edge.",
    ]),
    ("dm", "From this moment the heroes wore their beeswax to the very end of the session."),

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
           "tables, stew pots, and one oblivious innkeeper to keep out of harm's way. It bites, "
           "grapples, and drags victims toward the trapdoor; 20 or more damage in a single turn "
           "makes it recoil and lose its reactions."),
    ("dm", "**Tavern toys.** Kick the stew pot: DC 12 Dexterity or 1d6 fire and disadvantage "
           "on the victim's next attack. Flip the long table: half cover for a round, or shove "
           "it (Strength DC 13) to pin the neck, restrained until it writhes free. Drop the "
           "lantern rack: DC 13 Dexterity or 1d4 slashing, and the burning square puts the "
           "head's next attack at disadvantage. Slam the trapdoor on the neck: Strength DC 14, "
           "and the head makes a DC 13 Dexterity save or takes 1d6 and loses its reactions "
           "until its next turn."),
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
    # No hardbreak: the tavern reveal ends just under half a page, and the
    # descent reads best rolling straight out of the broken floor.
    ("h1", "Part Four: Where the Song Lives"),
    ("bridge", "A trail led from the tavern's broken floor into the dark beneath Wraithpine, "
               "and the thin note grew into a pressure, a hand laid gently on the inside of the "
               "skull. The heroes plugged their ears, lit their lanterns, and followed it down."),

    ("h2", "The Descent"),
    ("gold", "The tunnel curls beneath the village like a rib: wet timber props, black nails, "
             "and, strangest of all, faint chalk marks scrawled on the rock in a stagehand's "
             "quick hand: *Upstage. Hold. Places.* The passage opens at last into the drowned "
             "orchestra pit below the **Old Theater**, crossed by catwalks of beam and rope, "
             "stage machines jutting up like broken ribs."),
    # Lore of Elaria (L7, lore/world_history.md): the Gilded Curtain fills the
    # open foot of the descent page, right under the chalk stage-marks and the
    # first naming of the Old Theater. World legend only; it asserts no table
    # fact, and its "forget the play was a play" chills nicely against the song.
    ("lore", "The Gilded Curtain",
     "Wraithpine's Old Theater was once home to the Gilded Curtain, the most famous "
     "traveling troupe on either coast. Their masks and prop rooms were legendary; it was "
     "said they could make you forget the play was a play. The troupe vanished from the "
     "records generations ago. The theater kept their playbills up, waiting."),
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
           "quiet approach along the high catwalks (Stealth against passive Perception 14) "
           "earned a surprise round, and a focused strike from the high ground dropped the "
           "first head before the song even turned."),
    ("dm", "**The battlefield.** Three elevations: catwalks 10 to 20 feet up, the broken stage "
           "at 5 feet, the bone mound below. Four neck-ports open in the theater floor; a head "
           "can withdraw and re-emerge from any port on its turn, reaching 15 feet from its "
           "hole. Prop flats (AC 12, 12 HP) and sandbag clusters give cover; a pinned neck "
           "(table, rope, tackle) needs Strength against DC 14 to writhe free."),
    ("dm", "**Hazards.** Rotted beams: DC 12 Dexterity or fall 10 feet for 1d6. Bone scree "
           "around the mound is difficult terrain. A pulley cluster can be dropped (Strength "
           "DC 13): 2d6 bludgeoning in a 10-foot line."),
    ("dm", "**Lair actions** (initiative 20, one per round): Stage Drop, sandbags crash in a "
           "10-foot line, DC 13 Dexterity or 2d6 and prone. Mask of Memory, playbills flutter "
           "like moths through a 15-foot radius; an unplugged hero makes a DC 15 Wisdom save "
           "or cannot target the body this round. Gasping Vent, a floor grate hisses open: "
           "10-foot radius of difficult terrain where words are muffled and verbal spells "
           "need a DC 10 Constitution check."),
    ("dm", "**Vital Link.** The body resists weapon damage while heads remain; each destroyed "
           "head strips one layer of that protection, and the body acts more often the more "
           "heads still sing."),
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
    ("reward_card", "Rewards: The Relics of Wraithpine",
     "One chest, three relics: Elaria's gift, opened by Ghostbloom's song beneath the Old "
     "Theater. Each bears the same sigil, a seven-point star wrapped in a leafed vine.",
     [
        ("Staff of Waking Constellations (Ursa)",
         "+1 quarterstaff and druidic focus. 5 charges, regain 1d4 + 1 at dawn: *guiding bolt* "
         "(1 charge), *faerie fire* (1), *moonbeam* (2). **Starseed.** Once per turn, +1d4 "
         "radiant damage when Ursa deals radiant damage with a druid spell (house rule: druid "
         "spells only). **Starlight.** Bonus action: 10 ft of dim light; advantage on night "
         "navigation. After every great victory, one new star brightens on its haft: the enemy "
         "puts stars out; the Staff lights them."),
        ("Sash of the Swift Current, Rewoven (Stabby)",
         "Scarlet stage-silk rewoven with theater rigging thread. **+1 AC** (stacks with "
         "Unarmored Defense). **Fleetstep.** +10 ft walking speed. **Air Dance.** 1/day, bonus "
         "action: a fly speed equal to walking speed for 1 minute. **Feather Fall.** 1/day, no "
         "components. Its seven-point star sigil is cupped by a pair of wings."),
        ("Glimmerspire Pocket Dynamo, Mk II (Lilly)",
         "A thumb-sized brass core filigreed with folding micro-gears, stamped PROP ROOM in "
         "stage-engraver script (a mystery unexplained). **Pocket Arsenal.** Deploy or recall "
         "the Eldritch Cannon as a free action. **Endurance Overhaul.** The cannon lasts 24 "
         "hours. **Power Sync.** The cannon deals +2 damage. **Reformat.** 1/long rest, as an "
         "action: change the cannon's model. Near Ghostbloom, the core glows soft ghost-green, "
         "like a stage cue waiting for its moment."),
     ]),

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
             "comes to take the feeling away. Ursa steps forward and presses something small "
             "into her hand: Harlan's carved whistle, worn smooth by a lifetime in his pocket, "
             "carried up out of the dark. Her children are safe. Their father will be "
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
    # Closing showpiece (DM-approved 2026-07-07): the departure east fills the
    # chapter-end page instead of stranding it 80 percent empty.
    ("img", f"{A}/scenes/s6_departure_east.png",
     "East, toward Gearhaven: three heroes, three relics, and one small ghost-light friend.",
     6.2, {"crop": "3:2", "hmax": 4.5}),
    # Lore of Elaria (F4, lore/world_history.md): the Old Shrine closes the
    # chapter under the departure-east plate, pointing the same way the heroes
    # walk and filling the page's open lower third.
    ("lore", "The Old Shrine",
     "Far east of the sea stands the shrine where, the elders say, the Warden stood last "
     "before her long sleep. Pilgrims once walked a year to reach it. The road is "
     "forgotten now, which troubles the Circle less than the fact that something else "
     "seems to have remembered it."),

    # ------------------------------------------------------------------
    # APPENDIX I: the DM run sheet (Session 7 format).
    ("appendix_title", "APPENDIX", "DM Run Sheet: The Day at a Glance",
     "Every DC, dial, and spotlight, in play order. Keep this page at your elbow."),

    ("h1", "The Shape of the Session"),
    ("body", "▶ One day and one night in Wraithpine. Landfall: GHOSTBLOOM WAKES (the sealed d12 "
             "from Session 5 pays off: Ghost) → Lantern Night: the wrongness tour, the first "
             "song save, the bellkeeper's slate (WRITE. DON'T LISTEN.) → THREE THREADS, any "
             "order, all pointing at the old theater: the cellar (FIGHT 1 + the breathing "
             "seam), Pumpkin Row (FIGHT 2, or the puzzle win) and the graveyard rite (FIGHT 3 "
             "only if it goes wrong; the parcel slip) → 3 Lantern Lane (Ms. Wicke) → the "
             "belltower: BEESWAX in every ear → the reveal at the Gasping Gull (FIGHT 4) → the "
             "descent → the lair (BOSS) → the song stops: the chest, three relics, dawn over "
             "Wraithpine. Natural break point: the belltower."),
    ("body", "**RUNS ALL SESSION: the Song of Unremembering.** Whenever the song swells, every "
             "hero makes a Wisdom save, DC 13 (fail: one fresh memory slips). In battle: a "
             "lone head's hum is 30 ft, DC 13 Wis or attacks at disadvantage; the full "
             "creature's song is 60 ft, DC 15, and failure also locks reactions. BEESWAX = "
             "advantage on every save and no reaction lock. Ink and chalk do not forget: "
             "anything WRITTEN stays true."),

    ("h1", "Fights at a Glance"),
    ("body", "**FIGHT 1: Maera's Cellar** (Easy; a warm-up hiding a clue). 2x Swarm of Rats "
             "(AC 10, HP 24; resist B/P/S; Bites +2, 2d6, or 1d6 at half HP) + 4x Giant Rat "
             "(AC 12, HP 7; Pack Tactics; Bite +4). One swarm drops from the rafters: DC 13 Dex "
             "or it lands on a hero's shoulders. Toys: shove the cask (Str DC 12: 1d4 and "
             "prone, Dex DC 12), pull the shelf (an action: Dex DC 13 or restrained). The real "
             "prize: torch held high, passive Perception 13 clocks the breathing seam in the "
             "far wall."),
    ("body", "**FIGHT 2: Pumpkin Row** (Medium; three ways to win, let the kids mix all "
             "three). 2x Scarecrow (AC 11, HP 36; VULNERABLE FIRE; Terrifying Glare DC 11 Wis, "
             "frightened) + 6x Strawling (AC 12, HP 11; Straw Lash grapples, escape DC 12). "
             "THE RULE: the straw only walks while the carved faces watch; turn key pumpkins "
             "(an action, no check): two facing away skips every scarecrow's turn, twice in "
             "different rounds ends the fight; a clipped heart-gourd drops a scarecrow, no "
             "roll. Spoils: the bell-handled lantern (1 use) and the PROP ROOM map scrap."),
    ("body", "**FIGHT 3: The Graveyard Risen** (Easy; happens only if the rite goes wrong). "
             "2x Zombie (AC 8, HP 22; Undead Fortitude: Con save, DC 5 + damage taken) if the "
             "restored name is wrong or unknown; 3x Zombie + 2x Skeleton (AC 13, HP 13; "
             "VULNERABLE BLUDGEONING) if the rite is begun loud and careless. The rite: "
             "Investigation DC 12 → Religion or History DC 12 → three rings → the Remembrance "
             "Knot (advantage for Brynn's students). Payout: HOLD FAST, advantage on one "
             "Wisdom save against the song, once this session."),
    ("body", "**FIGHT 4: The Tavern Head** (Hard; the reveal is the point). 1x False Hydra "
             "Tavern Head (AC 14, HP 70; hum: 30 ft, DC 13 Wis or attacks at disadvantage, "
             "beeswax = advantage; Bite +6, grapple escape DC 14, then Lurch and Drag toward "
             "the trapdoor and Wrench, Str DC 14). 20+ damage in a single turn = it recoils and "
             "loses reactions; fire puts its next attack at disadvantage. Toys: stew pot, long "
             "table, lantern rack, slam the trapdoor (Str DC 14). Keep Maera out of harm's way; "
             "the second neck ALWAYS escapes down the tunnel."),
    ("body", "**BOSS: The False Hydra Entire** (the hardest fight since the Dutchman). Body "
             "(AC 15, HP 130) RESISTS ALL WEAPON DAMAGE while heads live; Vital Link: each dead "
             "head strips one layer. 4x Head (AC 14, HP 45; reach 15 ft from a floor port; "
             "withdraws and re-emerges from any port). Song: 60 ft, DC 15 Wis or disadvantage "
             "and no reactions (beeswax: advantage, no lock). Lair actions on initiative 20 "
             "(Stage Drop / Mask of Memory / Gasping Vent); legendary actions one per living "
             "head, max 3 a round. Catwalk Stealth vs. passive 14 buys a surprise round. Kill "
             "heads first."),

    ("h1", "The Resource Picture"),
    ("body", "▶ One long day and night with no long rest inside it, so the spend is hit "
             "points, Wisdom saves, and nerve rather than slots. BEESWAX is the resource that "
             "actually matters: seat it at the belltower and the song mostly stops taxing the "
             "table (do not let anyone be brave about it). HOLD FAST from the graveyard rite "
             "banks one more save; the bell-handled lantern is one Investigation with advantage "
             "in Wraithpine. If the party wants a breather, the natural short rest sits after "
             "the belltower: the tavern head and the lair land back to back. Lilly's cannon "
             "runs all day; watch Ursa's concentration in the lair (one thing at a time) and "
             "Stabby's focus across as many as five fights."),

    ("h1", "Spotlights & Seeds: every kid shines, every door gets planted"),
    ("body", "**Lilly:** she names GHOSTBLOOM on the landfall path (“a bloom made of "
             "ghost-light”) → the chandler's sugared chip, “for remembering” → the Essence "
             "Sphere's heartbeat; it pulls toward the theater when the table stalls "
             "→ emerald fire along the pale neck in the "
             "lair → at the chest, the session's thesis is hers: “They were made for US. It is "
             "ELARIA.” (Door: Elaria's guidance) → her new Dynamo core is stamped PROP ROOM "
             "(Door: a mystery nobody explains)."),
    ("body", "**Stabby:** he carries the clue chain: he cuts the heart-gourd open (the PROP "
             "ROOM map scrap) and pries the parcel slip from a risen hand and pockets it → "
             "Candyfang steel cracks the slate teeth at the Gull → the last head falls to the "
             "Katana and a lance of starlight together → at dawn, “Let's not stick around for "
             "this part”: let him keep the goodbye light. The Sash of the Swift Current is "
             "his."),
    ("body", "**Ursa:** Ghostbloom wakes in his arms → his lantern finds the breathing seam in "
             "the cellar → the rite is his kind of work: the knot ties with advantage for "
             "anyone Captain Brynn taught → he picks up Harlan's whistle in the lair and says "
             "nothing at all → starlight this deep place has never seen → at dawn he presses "
             "the whistle into Ms. Wicke's hand: the session's heart, let it land. The Staff "
             "of Waking Constellations is his (Door: a new star after every victory)."),

    ("h1", "Foreshadow Tracker: say it, then say it again"),
    ("body", "▶ The tells, in order. The thin note under the festival (the first DC 13 save) "
             "• Maera's fourth place at a table laid for three; two cooling bowls; a skipped "
             "ledger line • black ribbons on gates and wrists, and nobody can say why • the "
             "playbill name scrubbed to lace (“moths”) • the slate: WRITE. DON'T LISTEN. • "
             "Ghostbloom's glow leaning toward trouble; the Essence Sphere's heartbeat • every "
             "carved face turning toward the theater; the PROP ROOM stamp • the chiseled "
             "gravestone with a stage-mask maker's mark • the parcel slip: HARLAN WICKE, 3 "
             "LANTERN LANE • Ms. Wicke's eyes skittering off her own portrait • UNDER. "
             "THEATER. • the second neck escaping the Gull • chalk stage-marks in the tunnel: "
             "*Upstage. Hold. Places.*"),

    # ------------------------------------------------------------------
    # APPENDIX II: the bestiary (Session 7 format).
    ("appendix_title", "APPENDIX", "Bestiary: Enemy Stat Blocks",
     "All five encounters of Session 6, in the order the party meets them."),

    ("fight_header", "ENEMIES, Fight 1: Maera's Cellar",
     "The Gasping Gull cellar ✦ Difficulty: Easy ✦ 2x Swarm of Rats + 4x Giant Rat"),
    ("enemy_cards", [
        {
            "name": "Swarm of Rats",
            "sub": "Medium swarm of Tiny beasts, unaligned ✦ CR 1/4 (50 XP) ✦ 2 in the cellar",
            "stats": [
                "**AC** 10  **HP** 24 (7d8 - 7)  **Speed** 30 ft",
                "**STR** 9  **DEX** 11  **CON** 9  **INT** 2  **WIS** 10  **CHA** 3",
                "**Resist** bludgeoning, piercing, slashing",
                "**Imm.** charmed, frightened, grappled, paralyzed, petrified, prone, "
                "restrained, stunned",
                "**Senses** darkvision 30 ft, passive Perception 10",
                "**Challenge** 1/4 (50 XP)",
            ],
            "traits": [
                ("Keen Smell", "The swarm has advantage on Wisdom (Perception) checks that "
                 "rely on smell."),
                ("Swarm", "The swarm can occupy another creature's space and vice versa; it "
                 "cannot regain hit points or gain temporary hit points."),
            ],
            "actions": [
                ("Bites", "*Melee Attack:* +2 to hit, reach 0 ft, one creature in the swarm's "
                 "space. *Hit:* 7 (2d6) piercing damage, or 3 (1d6) if the swarm is at half "
                 "its hit points or below."),
            ],
        },
        {
            "name": "Giant Rat",
            "sub": "Small beast, unaligned ✦ CR 1/8 (25 XP) ✦ 4 in the cellar",
            "stats": [
                "**AC** 12  **HP** 7 (2d6)  **Speed** 30 ft",
                "**STR** 7  **DEX** 15  **CON** 11  **INT** 2  **WIS** 10  **CHA** 4",
                "**Skills** Perception +2",
                "**Senses** darkvision 60 ft, passive Perception 12",
                "**Challenge** 1/8 (25 XP)",
            ],
            "traits": [
                ("Keen Smell", "Advantage on Wisdom (Perception) checks that rely on smell."),
                ("Pack Tactics", "Advantage on attack rolls if an ally is within 5 ft of the "
                 "target."),
            ],
            "actions": [
                ("Bite", "*Melee Attack:* +4 to hit, reach 5 ft. *Hit:* 4 (1d4 + 2) piercing "
                 "damage."),
            ],
        },
    ]),
    ("tactics", "One swarm lurks in the rafters and drops straight for a hero's shoulders: "
                "DC 13 Dexterity or it lands on you. The rest come as a gray tide down the "
                "tight barrel aisle, where Pack Tactics does the work. Fight the room: shove a "
                "cask down the aisle (once, Strength DC 12: 1d4 bludgeoning and prone, "
                "Dexterity DC 12) or pull down the rickety shelf (an action: Dexterity DC 13 "
                "or restrained). The real prize is the hairline seam in the far wall, quietly "
                "inhaling, with a hum inside the hill."),

    ("fight_header", "ENEMIES, Fight 2: Pumpkin Row",
     "Pumpkin Row ✦ Difficulty: Medium (or no fight at all) ✦ 2x Scarecrow + 6x Strawling"),
    ("enemy_cards", [
        {
            "name": "Scarecrow",
            "sub": "Medium construct, neutral ✦ CR 1 (200 XP) ✦ 2 in the lane",
            "img": f"{A}/monsters/scarecrow.png",
            "stats": [
                "**AC** 11  **HP** 36 (8d8)  **Speed** 30 ft",
                "**STR** 16  **DEX** 12  **CON** 11  **INT** 10  **WIS** 10  **CHA** 10",
                "**Vulnerable** fire  **Resist** nonmagical bludgeoning, piercing, slashing",
                "**Imm.** charmed, frightened, paralyzed, poisoned",
                "**Senses** darkvision 60 ft, passive Perception 10",
                "**Challenge** 1 (200 XP)",
            ],
            "traits": [
                ("Heart-Gourd Charm", "A coin-sized gourd charm is stitched under its ribs. "
                 "From within 5 ft, a hero can snip it, no roll: the scarecrow falls limp on "
                 "the spot."),
            ],
            "actions": [
                ("Terrifying Glare", "One creature within 30 ft: DC 11 Wisdom save or "
                 "frightened for 1 minute (repeat the save at the end of each of its turns)."),
                ("Claws", "*Melee Attack:* +3 to hit, reach 5 ft. *Hit:* 9 (2d4 + 4) slashing "
                 "damage."),
            ],
        },
        {
            "name": "Strawling",
            "sub": "Medium plant, neutral ✦ CR 1/4 (50 XP) ✦ reskinned Needle Blight ✦ 6 in "
                   "the lane",
            "img": f"{A}/monsters/strawling.png",
            "stats": [
                "**AC** 12  **HP** 11 (2d8 + 2)  **Speed** 30 ft",
                "**STR** 12  **DEX** 12  **CON** 12  **INT** 4  **WIS** 10  **CHA** 3",
                "**Senses** passive Perception 10",
                "**Challenge** 1/4 (50 XP)",
            ],
            "actions": [
                ("Straw Lash", "*Melee Attack:* +4 to hit, reach 5 ft. *Hit:* 4 (1d6 + 1) "
                 "bludgeoning damage, and the target must succeed on a DC 12 Strength save or "
                 "be grappled (escape DC 12)."),
                ("Chaff Burst", "*Ranged Attack:* +4 to hit, range 30/60 ft. *Hit:* 6 (2d4) "
                 "piercing damage (a spray of straw flechettes)."),
            ],
        },
    ]),
    ("tactics", "The straw only walks while the carved faces watch. Three ways to win, and the "
                "Guardians may mix all three: turn or snuff the three key pumpkins (an action, "
                "no check; while any two face away from the theater every scarecrow skips its "
                "next turn, and managing it in two different rounds collapses the straw for "
                "good), clip the heart-gourds, or fight it out among the flickering "
                "jack-o'-lanterns. The hay cart bowls strawlings over, the pumpkin stack can "
                "be kicked into a glorious mess, and fire is the scarecrows' bad night."),

    ("fight_header", "ENEMIES, Fight 3: The Graveyard Risen",
     "The hilltop graveyard ✦ Only if the rite goes wrong ✦ 2x Zombie (3x Zombie + 2x Skeleton "
     "if loud and careless)"),
    ("enemy_cards", [
        {
            "name": "Zombie",
            "sub": "Medium undead, unaligned ✦ CR 1/4 (50 XP)",
            "img": f"{A}/monsters/wraithpine_zombie.png",
            "stats": [
                "**AC** 8  **HP** 22 (3d8 + 9)  **Speed** 20 ft",
                "**STR** 13  **DEX** 6  **CON** 16  **INT** 3  **WIS** 6  **CHA** 5",
                "**Senses** darkvision 60 ft, passive Perception 8",
                "**Challenge** 1/4 (50 XP)",
            ],
            "traits": [
                ("Undead Fortitude", "When damage drops it to 0 HP (unless the damage is "
                 "radiant or from a critical hit), it makes a Constitution save, DC 5 + the "
                 "damage taken; on a success it drops to 1 HP instead."),
            ],
            "actions": [
                ("Slam", "*Melee Attack:* +3 to hit, reach 5 ft. *Hit:* 4 (1d6 + 1) "
                 "bludgeoning damage."),
            ],
        },
        {
            "name": "Skeleton",
            "img": f"{A}/monsters/wraithpine_skeleton.png",
            "sub": "Medium undead, unaligned ✦ CR 1/4 (50 XP) ✦ only if the rite is begun "
                   "loud and careless",
            "stats": [
                "**AC** 13 (armor scraps)  **HP** 13 (2d8 + 4)  **Speed** 30 ft",
                "**Vulnerable** bludgeoning",
                "**Challenge** 1/4 (50 XP)",
            ],
            "actions": [
                ("Shortsword", "*Melee Attack:* +4 to hit, reach 5 ft. *Hit:* 5 (1d6 + 2) "
                 "piercing damage."),
                ("Shortbow", "*Ranged Attack:* +4 to hit, range 80/320 ft. *Hit:* 5 (1d6 + 2) "
                 "piercing damage."),
            ],
        },
    ]),
    ("tactics", "These are the recently quiet, not villains: they rise only if the restored "
                "name is wrong or unknown, and the bigger roster answers a rite begun loud and "
                "careless. Lay them gently back down; the rite can always be tried again. When "
                "the Remembrance Knot finally takes hold, every hero who took part gains Hold "
                "Fast: once this session, advantage on one Wisdom save against forgetfulness "
                "or the song."),

    ("fight_header", "ENEMIES, Fight 4: The Reveal at the Gasping Gull",
     "The Gasping Gull ✦ Difficulty: Hard ✦ 1x False Hydra Tavern Head"),
    ("enemy_cards", [
        {
            "name": "False Hydra, the Tavern Head",
            "sub": "Large aberration (one head and neck), unaligned ✦ it has been in the "
                   "taproom all along",
            "img": f"{A}/monsters/false_hydra_head.png",
            "img_w": 3.0,
            "stats": [
                "**AC** 14  **HP** 70 (9d10 + 18)  **Speed** 10 ft, climb 10 ft",
                "**STR** 16  **DEX** 12  **CON** 14  **INT** 6  **WIS** 14  **CHA** 7",
                "**Resist** psychic  **Imm.** charmed, frightened, prone",
                "**Senses** blindsight 10 ft, tremorsense 30 ft, darkvision 60 ft, passive "
                "Perception 14",
            ],
            "traits": [
                ("Mind-Humming Aura", "A creature without beeswax that starts its turn within "
                 "30 ft makes a DC 13 Wisdom save or has disadvantage on attack rolls that "
                 "turn; beeswax grants advantage on the save."),
                ("Segmented Neck", "The head ignores forced movement and prone unless it "
                 "chooses otherwise. After taking 20 or more damage in a single turn, it "
                 "recoils 5 ft and loses its reactions until the start of its next turn."),
            ],
            "actions": [
                ("Bite", "*Melee Attack:* +6 to hit, reach 10 ft. *Hit:* 13 (2d8 + 4) piercing "
                 "damage, and the target is grappled (escape DC 14). While it has a creature "
                 "grappled, the head cannot bite a different target."),
                ("Lurch and Drag", "The head drags a creature it is grappling 5 ft toward the "
                 "trapdoor; the creature makes a DC 13 Wisdom save or loses a word or a "
                 "thought for a heartbeat."),
                ("Wrench (Bonus Action)", "A creature the head is grappling makes a DC 14 "
                 "Strength save or is knocked prone and takes 5 (1d6 + 2) bludgeoning damage "
                 "as the jaw grinds it against the floorboards."),
            ],
            "reactions": [
                ("Recoil from Flame", "When the head takes fire damage, it has disadvantage "
                 "on its next attack roll before the end of its next turn."),
            ],
        },
    ]),
    ("tactics", "It bites, grapples, and drags victims toward the trapdoor, and its eyes aim "
                "at the place where thoughts are. Fight the room: kick the stew pot (Dexterity "
                "DC 12: 1d6 fire and disadvantage on the victim's next attack), flip the long "
                "table (half cover, or Strength DC 13 to pin the neck, restrained until it "
                "writhes free), drop the lantern rack (Dexterity DC 13: 1d4 slashing, and the "
                "burning square puts the head's next attack at disadvantage), or slam the "
                "trapdoor on the neck (Strength DC 14; the head saves Dexterity DC 13 or takes "
                "1d6 and loses its reactions). Keep Maera out of harm's way, and when the head "
                "dies, the second neck always escapes: the hum below deepens."),

    ("fight_header", "ENEMIES, BOSS: The False Hydra",
     "The orchestra pit below the Old Theater ✦ The hardest fight since the Dutchman ✦ "
     "1x Body + 4x Head"),
    ("enemy_cards", [
        {
            "name": "False Hydra, Adult",
            "sub": "Huge aberration, unaligned ✦ the boss of Session 6 ✦ one body, four "
                   "singing heads",
            "img": f"{A}/monsters/false_hydra_body.png",
            "img_w": 2.2,
            "stats": [
                "**Body:** AC 15  HP 130 (12d12 + 48)  Speed 10 ft, climb 10 ft",
                "**Heads (4):** AC 14  HP 45 (6d10 + 12) each  Speed 30 ft through the "
                "under-floor tunnels, climb 20 ft  reach 15 ft from a floor port",
                "**Body STR** 18  **DEX** 10  **CON** 18  **INT** 7  **WIS** 14  **CHA** 8  "
                "**Saves** Con +8, Wis +5 (heads Wis +4)",
                "**Resist** psychic  **Imm.** charmed, frightened, prone",
                "**Senses** tremorsense 60 ft, darkvision 60 ft, passive Perception 12",
            ],
            "traits": [
                ("Song of Unremembering", "While any head lives, a creature without earplugs "
                 "that starts its turn within 60 ft makes a DC 15 Wisdom save or has "
                 "disadvantage on attack rolls and cannot take reactions until its next turn. "
                 "Beeswax: advantage on the save, and no reaction lock."),
                ("Vital Link", "While at least one head lives, the body has resistance to all "
                 "weapon damage. Each head destroyed removes one instance of this protection; "
                 "with no heads it has none."),
                ("Head Movement", "A head may withdraw (no opportunity attacks), move up to "
                 "30 ft through the tunnels, and re-emerge from any floor port; a pinned neck "
                 "(table, rope, tackle) needs Strength vs. DC 14 to writhe free."),
                ("Lair Actions", "On initiative count 20, one per round: **Stage Drop** (a "
                 "10-ft sandbag line: DC 13 Dexterity or 2d6 and prone), **Mask of Memory** "
                 "(playbills in a 15-ft radius: an unplugged hero saves Wisdom DC 15 or cannot "
                 "target the body this round), **Gasping Vent** (a 10-ft radius of difficult "
                 "terrain where verbal spells need a DC 10 Constitution check)."),
            ],
            "actions": [
                ("Thrash (Body)", "*Melee Attack:* +7 to hit, reach 10 ft. *Hit:* 13 (2d8 + 4) "
                 "bludgeoning damage."),
                ("Regurgitate Remnants (Body; Recharge 5-6)", "A 15-ft cone of bone and cloth: "
                 "DC 14 Dexterity save or take 13 (3d8) necrotic damage and lose 10 ft of "
                 "speed until the end of the target's next turn. A shattered skull and a black "
                 "ribbon clatter free (a clue)."),
                ("Bite (Head)", "*Melee Attack:* +7 to hit, reach 15 ft. *Hit:* 14 (2d10 + 3) "
                 "piercing damage, and the target is grappled (escape DC 14); while grappling, "
                 "that head cannot bite a different target."),
                ("Reel (Head)", "A creature grappled by a head makes a DC 14 Strength save or "
                 "is pulled 10 ft toward the port and knocked prone."),
            ],
            "reactions": [
                ("Snap (Head)", "When a creature moves within 15 ft of a head, that head makes "
                 "one Bite against it."),
            ],
            "legendary": [
                ("", "One per living head, maximum 3 per round, at the end of another "
                 "creature's turn."),
                ("Hum Surge", "One creature within 60 ft without earplugs: DC 15 Wisdom save "
                 "or lose concentration and move only 10 ft on its next turn."),
                ("Bone Shift", "The body shifts 5 ft and reshapes the mound: one 10-ft square "
                 "within 20 ft becomes difficult terrain or clears."),
                ("Coordinate Strike", "One head makes one Bite."),
            ],
        },
    ]),
    ("tactics", "A quiet catwalk approach (Stealth vs. passive Perception 14) earns a surprise "
                "round; a focused strike from the high ground can drop the first head before "
                "the song even turns. Two heads pressure the front line, one hunts the "
                "backline, one harasses from a different port; Bone Shift reshapes the ground "
                "and Regurgitate Remnants punishes clusters. Hazards: rotted beams (Dex DC 12 "
                "or fall 10 ft, 1d6), bone scree, a droppable pulley cluster (Str DC 13: 2d6 "
                "in a 10-ft line); prop flats (AC 12, 12 HP) give cover. Kill heads first: "
                "each one down quiets the song and thins the body's armor."),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    out = build_doc(BLOCKS, "sessions/session_06_wraithpine.docx")
    print("built", out)
