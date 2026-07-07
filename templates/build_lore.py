# build_lore.py
# The lore primer: the world of Elaria, its cosmology, its goddess and its
# shadow, the relics, and a full gazetteer of every place the Guardians have
# walked or will walk. Drawn from memory/campaign_canon.md and lore/locations.
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc

A = "assets"
BLOCKS = [
    ("titlepage", "A PRIMER FOR PLAYERS AND DUNGEON MASTERS", "The World of Elaria",
     "Cosmology, Powers, and Places",
     "The lore behind the chronicle: how the world is built, who threatens it, and what the Guardians are truly fighting for."),

    # The map leads the whole primer, right on page one, at full text width.
    # Landscape v2 asset (DM-approved 2026-07-06), drawn from the party's real
    # route: the western vale, the highlands, Havenmoor, the sea crossing.
    ("img", f"{A}/world/elaria_region_map.png",
     "The lands of Elaria, and the road the Guardians walked: from Eldridge Vale in the west, "
     "over the Ravenstone Cliffs to wintry Havenmoor, then across the Open Sea to Wraithpine, "
     "Gearhaven, and the Old Shrine beyond.", 6.4,
     {"hmax": 4.8}),

    # Refit note: the title and full-width map fill page 1 to about 78
    # percent; the chronicle proper starts at the top of page 2.
    ("h1", "The Shape of the World", {"hardbreak": True}),
    ("gold", "There is not one world but many, turning side by side like the gears of a single "
             "great clock: the planes of Fire, Water, Air, Earth, and Shadow, and the Material world "
             "at their heart. For a thousand years the clock kept perfect time."),
    ("gold", "The planes do not spin on their own. They are held in place by anchor-stars, fixed "
             "points of light in the dark, each one cradling a plane in its orbit. While the stars "
             "burn, the worlds stay in their courses. When a star goes dark, its plane slips, and a "
             "crack opens between worlds."),
    ("body", "Through those cracks leak Motes: bright drifting fragments of the planes themselves. "
             "Motes drive machines mad and wake strange creatures, the wondrous beasts the Guardians "
             "have met and befriended along their road. Gather the loose Motes, mend the cracks, and "
             "the world steadies again. That, in the simplest telling, is the work."),
    ("body", "But a crack cannot be sealed from our side of it. Each fraying world keeps a guardian "
             "of its own, and the leaking corruption twists that guardian first; free the guardian, "
             "and that world's cracks close on their own. The heroes proved it in Gearhaven, when "
             "they freed the Grand Custodian and the city's wounds knit shut behind it."),

    ("h2", "The Star Map"),
    ("body", "As the Orrery of Planes shows it, plane by plane, anchor by anchor:"),
    ("body", "**Fire, the plane Ignis:** anchored to **Aldebaran**, still burning bright."),
    ("body", "**Water, the plane Unda:** anchored to **Fomalhaut**, still burning bright."),
    ("body", "**Air, the plane Aer:** anchored to **Vega**, going dark."),
    ("body", "**Earth, the plane Terra:** anchored to **Antares**, dimming."),
    ("body", "**Shadow, the plane Umbra:** anchored to **Algol**, dark."),
    ("body", "**Betelgeuse:** the first star put out, the one Ash Catchum chased into the east."),
    ("body", "**Achernar:** a reserve anchor, held back against the worst."),

    ("h1", "Elaria, the Sleeping Warden"),
    ("gold", "Elaria is not a goddess of war or harvest, but of balance: the Warden who once tended "
             "the lights of heaven and kept the planes in their courses. Long ago, in the War of "
             "Fractures, she led the gods against a devouring darkness and spent nearly all her "
             "power to seal it away. What remained she bound into small safeguards and scattered, "
             "and then, diminished, she fell into a deep sleep."),
    ("body", "She sleeps still, and because she sleeps the stars can be put out one by one. Who or "
             "what closed her eyes is a mystery not yet answered. She is not wholly gone, though: she "
             "guides those attuned to balance through visions and through gifts marked with her "
             "sign, a seven-pointed star wrapped in a leafed vine. When you see that star, she saw "
             "you coming."),

    # Refit note: without the break this h1 orphaned at the foot of page 2
    # with a single line; page 2 ends about 80 percent full without it.
    ("h1", "The Shadow: Nyxthid and Maldrith", {"hardbreak": True}),
    ("body", "Two threats stand behind the failing world, one seen and one still hidden."),
    ("gold", "**Nyxthid, the Harbinger of Decay**, is the one the Guardians have glimpsed: a fallen "
             "celestial who once guarded the planes and now, twisted by despair, works to snuff the "
             "anchor-stars out. He deals in shadow, illusion, and fear, and he believes the kindest "
             "thing left is to let the whole clock wind down into dark."),
    ("gold", "**Maldrith, the Weaver of Fractures**, is the darkness Elaria sealed: an ancient, "
             "patient hunger from beyond the planes, pressing on the walls of every world, waiting "
             "for the last star to go dark. Nyxthid is only her herald. The heroes do not yet know "
             "her name, and should not, until the road grows much darker."),

    ("h1", "The Covenant and the Relics"),
    ("body", "When Elaria spent her power, she bound what was left into safeguards and gifts, and "
             "some of these have found their way to the Guardians."),
    ("gold", "**The Enchanted Potatoes**, three of them, carried by Ursa and left by his father "
             "Ash: humble to the eye, but remnants of the shattered covenant, holding fragments of "
             "the goddess's own essence for the day they are needed."),
    ("gold", "**The Essence Sphere**, forged by the deep-gnome masters of Glimmerspire before the "
             "crisis ever began (how they knew is its own mystery): a gatherer of loose Motes, and "
             "the beating heart the world's great Rift Portal has always lacked."),
    ("gold", "**The three relics of Wraithpine**, each bearing the seven-pointed star: the Staff of "
             "Waking Constellations that relights a star with every victory, the Sash of the Swift "
             "Current, and the Pocket Dynamo. One chest, three gifts, one goddess guiding three "
             "chosen hands. Their full powers are set down in the compendium of treasures."),

    ("h1", "A Gazetteer of Elaria"),
    ("body", "The chronicle's road runs west to east, village by village, and every stop on it has "
             "left a mark on the Guardians (and they on it). Here is each place as the chronicle "
             "knows it, followed by the roads not yet taken."),

    # Refit note: the gazetteer h1 and intro fill page 3 to about 72 percent;
    # breaking before the first entry keeps the Eldridge float clear of the
    # page-3 bottom margin and starts the village walk on a fresh page.
    ("pagebreak",),
    ("h2", "Eldridge Village and the Forest of Whispers"),
    ("imgfloat", f"{A}/scenes/s1_eldridge_village.png", 3.1),
    ("body", "A quaint village in the rolling hills of **Eldridge Vale**, known for its bustling "
             "little marketplace, its seasonal festivals honoring Elaria, and the **Gilded Acorn "
             "Tavern**, the warm-hearted inn (Osric behind the bar, Rhea working the tables) where "
             "three young strangers first sat down at one table. Just beyond the fields waits the "
             "**Forest of Whispers**: ancient trees, hidden pathways, and a hush that is not quite "
             "silence, for the leaves seem to murmur with voices of the past."),
    ("body", "Deep in the wood stand the mossy standing stones where the guardian **Duckleaf** kept "
             "its post, drawing power from the Plane of Air, and beyond them the **Grove of "
             "Elemental Waters**, where the party first saw motes drifting loose like sparks from a "
             "cracked lantern. The quiet pond where Lickgloom was befriended lies here too. It was "
             "in this forest that the work of the Guardians truly began."),

    ("h2", "Oakshade Village"),
    ("imgfloat", f"{A}/scenes/s1_oakshade_twilight.png", 3.1, "left"),
    ("body", "A small village in **Oakshade Glade**, shaded by oaks so old the villagers name them "
             "like elders. Oakshade has always been a place of druids and rangers, folk who keep "
             "the surrounding forests and mark the turning seasons, and it serves as the waypoint "
             "for anyone traveling on to Ravenstone. The **Old Oak Tavern** (Alwen, proprietor) "
             "pours a famous mulled cider; Elder Merwin doubles as the blacksmith; Nina the "
             "herbalist knows every root and remedy in the glade."),
    ("body", "The Guardians came here chasing rumors and found trouble worth the trip: Mudskips "
             "boiling up out of the wet fields, a Grimfang goblin ambush on the road, and the "
             "hulking Terranox shaking the earth itself. Merwin's missing herb-gatherers came home "
             "dazed once the Mist Stalkers were dealt with, and Oakshade has counted the party as "
             "friends ever since."),

    # Refit note: Eldridge and Oakshade fill page 4 to about 79 percent; the
    # Glade heading otherwise orphans at the page foot with its float on the
    # next page.
    ("pagebreak",),
    ("h2", "The Whispering Glade"),
    ("imgfloat", f"{A}/scenes/s2_elaria_vision.png", 3.0),
    ("body", "A ring of silver-barked trees off the Ravenstone road where the air goes still and "
             "starlight pools like water. Here, for the first time, **Elaria herself reached out**: "
             "a vision of the sleeping Warden, a warning of cracks between worlds, and a boon laid "
             "on each of the three travelers before the light let them go."),
    ("body", "The glade is the closest thing the campaign has to holy ground. The Circle of the "
             "Eternal Stars whispers that places like it are thin spots in the world's cloth, where "
             "a sleeping goddess can press a hand through. Those who camp there report kind dreams "
             "and wake to find their small hurts mended."),

    ("h2", "Ravenstone Laboratory and the Ravenstone Cliffs"),
    # Refit note: floated left this image sandwiched the section heading
    # between two floats and split its two lines; on the right it stacks
    # cleanly below the Glade image.
    ("imgfloat", f"{A}/scenes/s2_ravenstone_arrival.png", 3.1),
    ("body", "An impressive structure built straight into the **Ravenstone Cliffs**, high above a "
             "shimmering lake. This is the home of **Professor Aelwyn Ravenstone**, tall "
             "silver-haired high elf and the region's great scholar of planar phenomena, and his "
             "patient half-elf assistant Tamsin. Inside it is all alchemical apparatus, enchanted "
             "instruments, and shelves of research on the magical creatures of the region."),
    ("body", "It was Aelwyn who first examined the Essence Sphere and pointed the party toward "
             "Gearhaven, and Aelwyn who offered them their first companion, three small creatures "
             "in three warm crates (they chose Floraburst, who would one day become Ghostbloom). "
             "**Lickgloom** lives at the laboratory still, taste-testing everything the Professor "
             "will allow and some things he will not."),

    # Refit note: anchored lower on page 5 the Stormwatch float clipped the
    # bottom page edge; the Glade and Ravenstone fill page 5 on their own.
    ("pagebreak",),
    ("h2", "The Road South: Brambleshadow, Ironroot, and Stormwatch"),
    ("imgfloat", f"{A}/scenes/s3_stormwatch_vision.png", 3.4, {"hmax": 3.8}),
    ("body", "The long road from the cliffs down to the coast crosses wilder country: the tangled "
             "**Brambleshadow Thicket**, where a Shadowflame stalked the party through the thorns; "
             "**Whisperwind Meadow** and the fog-hung **Mistwood Path**; the stony **Ironroot "
             "Hills**, hunting ground of displacer beasts and the strange singing Shroomyte "
             "groves."),
    ("body", "The road ends at **Stormwatch Cliffs**, where an old puzzle of standing stones "
             "guards the headland. There the Guardians saw him first: a **Dark Figure** wrapped in "
             "shadow, glimpsed in vision above a fractured world, holding a dying star in one hand. "
             "They did not know his name then. The chronicle does now, and it is written a few "
             "pages back."),

    ("h2", "Havenmoor"),
    ("imgfloat", f"{A}/scenes/s4_havenmoor_town.png", 3.1),
    ("body", "A wintry harbor town on the southern coast, all snow-dusted roofs, ships' bells, and "
             "chimney smoke. Its landmarks are dear to the party: the **Sugarplum Hearth** inn "
             "(Greta Frostbough's cocoa is a house rule unto itself), the **Frostwind Market "
             "Square**, the **Hollow Hearth Orphanage** kept by Sister Merida, Master Doran "
             "Bramblebeard's shipyard, and the **Wyrmgale Lighthouse** he tends on the point. A "
             "small **Shrine of Elaria** stands quiet at the town's edge, still unvisited."),
    ("body", "Havenmoor is where the Guardians became heroes in the eyes of ordinary folk: when the "
             "**Krampusshade** stole the town's children, the party rang the eight Winter Bells, "
             "broke the three barriers, and sang the monster back into the dark. The lorekeeper "
             "Faelan sent them onward with three gifts that they carry to this day."),
    # Havenmoor is a showpiece location. 16:9 panorama so the plate fits on
    # the same page as the Havenmoor prose instead of stranding half a page.
    ("img", f"{A}/scenes/s3_havenmoor_arrival.png",
     "Havenmoor from the southern road: snow-dusted roofs, ships' bells, and chimney smoke "
     "over the harbor.", 6.2, {"crop": "16:9", "hmax": 4.6}),

    ("h2", "The Open Sea and the Flying Dutchman"),
    ("imgfloat", f"{A}/scenes/s5_dutchman_rises.png", 3.1),
    ("body", "East of Havenmoor the coast gives way to deep water, and the deep water kept a curse. "
             "The party sailed with Captain Brynn Wavewarden aboard the **Stormwind**, which the "
             "storm took to the bottom; from the wreck they were dragged aboard the **Flying "
             "Dutchman**, the ghost ship of **Davy Jones** himself."),
    ("body", "Below its decks they found something worse than ghosts: a harvest operation, spectral "
             "essences packed in crates stamped with an Artificers' Guild seal, bound south for "
             "buyers unknown. Davy Jones was destroyed at his own dice table, his crew freed, and "
             "the Dutchman finally allowed to sink. The Ghost essence Lilly drew from its hold "
             "began Floraburst's slow change into Ghostbloom. The sea is quiet now. The question of "
             "those crates is not."),

    ("h2", "Wraithpine and the Old Theater"),
    # Wraithpine is a showpiece location: half-page centered plate.
    ("img", f"{A}/monsters/gasping_gull.png",
     "The Gasping Gull on Wraithpine's cobbled square, where the lanterns stay lit on purpose.",
     6.0, {"crop": "3:2", "hmax": 4.6}),
    ("body", "A fog-bound village of carved pumpkins, swaying lanterns, and streets with names like "
             "**Pumpkin Row** and **Lantern Lane**, watched over by the belltower quarter called "
             "Bellshadow. The **Gasping Gull** inn (Maera, proprietor) sits on the cobbled square. "
             "Wraithpine looks like a festival that never ends, and for a while that was the "
             "kindest thing about it: a **False Hydra** nested beneath the **Old Theater**, singing "
             "the whole town into forgetting its missing neighbors."),
    # The Old Theater floats beside the closing paragraph so the Wraithpine
    # page fills instead of stranding its bottom third (DM flag 2026-07-06).
    ("imgfloat", f"{A}/scenes/s6_old_theater.png", 3.0),
    ("body", "The Guardians stuffed their ears with beeswax, followed the silence to the lair below "
             "the stage, and ended the song for good. In the quiet afterward they found the chest "
             "bearing Elaria's seven-pointed star: one chest, three relics, and a goddess's thanks. "
             "Wraithpine remembers everything now, and keeps its lanterns lit on purpose. The Old "
             "Theater stands empty on its hill, boarded and quiet; the town has not decided what "
             "to do with it, and the theater, for its part, is not telling."),

    # Fresh page: beside the Old Theater float the heading orphans at the
    # foot of the Wraithpine page otherwise.
    ("pagebreak",),
    ("h2", "Gearhaven, the Clockwork City"),
    ("img", f"{A}/session_08/beat_1/team_arrives_at_gearhaven.png",
     "The eastern gate of Gearhaven, where every arriving traveler is wished steady gears.",
     6.0, {"crop": "3:2", "hmax": 4.6}),
    ("body", "The great city of inventors and the party's home base: brass towers, steam vents, "
             "tram lines, and Mechagnome citizens whose eyes flicker when the planes act up. Its "
             "heart is the **Artificer's Guild**, where Guildmaster Vane (the locksmith) and the "
             "silver archivist Quill keep ten years of impossible work: **Vane's Folly**, the Rift "
             "Portal, finished at last around the Essence Sphere. Beneath the Guild turns the "
             "**Great Governor**, the engine that makes the city's heartbeat, and above it the "
             "**Orrery of Planes** maps every anchor-star in the sky."),
    ("body", "The chronicle's Gearhaven runs from the eastern gate and the Street of Small Wonders "
             "to Henna Brasspot's **Gilded Gear** tavern, Cogtooth Market, and down into the "
             "**Underworks**, where the party fought a rift swarm and rescued the goblin courier "
             "Skitch. In the **Verdant Plaza**, the city's one green place, they freed the corrupted "
             "**Grand Custodian** and laid it gently to rest, proving that a fraying world is saved "
             "by mercy, not by force. The city's wounds closed behind them."),

    # Refit note: without the break the Bloodthorn float clipped the bottom
    # page edge; Gearhaven fills its page about three quarters on its own.
    ("pagebreak",),
    ("h2", "Roads Not Yet Taken"),
    ("imgfloat", f"{A}/scenes/bloodthorn_hollow.png", 3.0),
    ("body", "The map does not end at Gearhaven, and neither will the chronicle. These places are "
             "spoken of, dreamed of, or marked in old logbooks, and every one of them is waiting."),
    ("body", "**Bloodthorn Hollow**, called simply the Hollow: the thorn-ringed home of the "
             "Bloodfang Clan, where Stabby was born. Word has come by way of the courier Skitch "
             "that cracks are opening near the Hollow and the clan blames the artificers. Someone "
             "will have to go home and set that right."),
    ("body", "**Glimmerspire and Deepforge Hollow**, far below in the Underdark: the deep-gnome "
             "city of forges and the academy where Lilly built her first turret, home of her mother "
             "Poots and Master Crafter Droven Sparkwick. Glimmerspire forged the Essence Sphere "
             "before the crisis ever began. How they knew it would be needed is a question with a "
             "long answer."),
    # Glimmerspire is a showpiece location: half-page centered plate. It sits
    # after its paragraph so the text clears the Bloodthorn float first;
    # placed higher, the plate's top band collides with that float.
    ("img", f"{A}/scenes/glimmerspire.png",
     "Glimmerspire, the deep-gnome city of forges in the Underdark, where the Essence Sphere "
     "was made before anyone knew why.", 6.0, {"crop": "3:2", "hmax": 4.6}),
    # Refit note: anchored after the Glimmerspire plate this float ran off
    # the bottom page edge; page 10 ends about 90 percent full without it.
    ("pagebreak",),
    ("imgfloat", f"{A}/scenes/old_shrine.png", 3.2, "left"),
    ("body", "**The Old Shrine in the east**: Ash Catchum's last logbook entry reads, \"The pattern "
             "leads east. Following the dark. To the old shrine.\" The Circle's elders believe he "
             "meant the **Ancient Shrine of the Forgotten Glade**, a hidden temple of Elaria deep "
             "in old-growth wood, said to hold secrets of the covenant and of the enchanted "
             "potatoes themselves. Ursa's road bends that way, sooner or later."),
    ("body", "**The Crystal Cavern of Crystal Hollow**: deep within the Ravenstone Cliffs, a cavern "
             "of luminescent crystals glowing in every color, said to house creatures tied to the "
             "elemental forces. Professor Aelwyn's notes mention it often. No Guardian has yet set "
             "foot inside."),
    # Refit note: floated right this image collided with the shrine float's
    # bottom edge and the renderer shoved it past the page edge; floated left
    # it stacks cleanly below the shrine image.
    ("imgfloat", f"{A}/world/dark_figure.png", 2.7, "left"),
    ("body", "**The five rift-worlds** beyond the portal: Terra the earth-plane first, under "
             "dimming Antares, then Unda, Ignis, Aer, and last of all Umbra, the plane of Shadow, "
             "under a star already dark. Each failing world keeps a corrupted guardian of its own, "
             "and each guardian is waiting, whether it knows it or not, to be freed."),

    ("gold", "Why the gazetteer matters: the sky is going out, one anchor-star at a time, and in "
             "one year the Rift Portal opens. Every road on these pages leads, in the end, to a "
             "star: one to relight, one to guard, or one to follow east into the dark. Wherever "
             "the Guardians go next, they have already walked the first half of the map."),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    print("built", build_doc(BLOCKS, "frontmatter/lore_primer.docx"))
