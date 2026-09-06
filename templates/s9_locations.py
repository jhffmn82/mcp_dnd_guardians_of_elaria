# s9_locations.py
# Stage 1 of the Session 9 art pipeline: the six Unda locations.
#
# These are generated FIRST and approved FIRST, because every other Session 9
# plate uses its location plate as a reference image. Getting these right is
# what makes the rest of the session look like one place.
#
# No characters appear in any of them, on purpose: a location plate is the
# room, not the scene. Unda is untouched wilderness that has never been built
# on, so EMPTY is enforced in the prompt rather than hoped for: the first pass
# put people and cities in these because nothing forbade them.
#
# THIRD PASS (rewritten from the board, not from imagination). The DM's verdict
# on the second pass: "I don't think they match the map and look too much like
# the old design." Both halves were true, and both had causes:
#
#   1. PALETTE. batch_art_s9.py prepends a STYLE string that asks for a "lush
#      warm golden palette", and with nothing arguing back, all six plates came
#      out drenched in honey-gold sand and amber caustics. The board is cool:
#      turquoise, jade, petrol blue, bone-grey sand, olive and rust coral,
#      acid-olive kelp, and a trench that is nearly black. PALETTE now overrides
#      the style line explicitly, and it runs first because STYLE runs first.
#   2. SAMENESS. All six came back as the same picture: symmetrical, a bright
#      sand avenue running to a centred vanishing point, an arch of water across
#      the top. Every location now carries its own CAMERA instruction, and BELL
#      forbids the default composition outright.
#
# The board image is attached as a reference for every one of these plates (see
# s9_art_plan.refs_for_plate), so the prompts point at it and tell the model to
# take colour, light and landform from it.

# Beats the STYLE line in batch_art_s9.py, which asks for warm gold. Read the
# board: the only warm colour anywhere on that map is the kelp.
PALETTE = ("PALETTE, and this overrides any earlier instruction about a warm or golden style:"
           " this world is COOL. Take the colour, the light and the landforms from the attached"
           " map image. Its palette is turquoise, jade and petrol-blue water; a floor of pale"
           " bone-grey sand; coral in olive, moss, ochre and rust; kelp in acid olive and old"
           " gold; and, in the deep places, a blue so dark it reads as black. Do NOT paint"
           " honey-gold sand, amber sunbeams, warm golden caustics or a tropical-postcard reef."
           " Sunlight here arrives cool and already spent by the water it came through. Match the"
           " map's paint quality too: soft-edged painterly oils, depth haze, nothing photographic.")

# The plane's defining feature, and the thing the first two passes got wrong by
# painting ordinary underwater scenes. Unda makes ROOM for its guests: they walk
# on dry sand inside domes of air with the sea held back overhead. This has to
# lead every prompt, not sit in a clause, or the model paints a reef photo.
BELL = (PALETTE +
        " THE MOST IMPORTANT THING ABOUT THIS PICTURE: the viewer is standing in AIR, not"
        " underwater. This is the inside of a great bubble of air resting on the sea floor. The"
        " ground is DRY rippled sand, dry enough to raise dust. The seawater begins at a visible"
        " curved boundary that stands up like a wall and leans over into a ceiling, with a bright"
        " rippling skin where air meets water. Fish and drifting weed are BEHIND that skin, never"
        " in the foreground air. Nothing floats or drifts in the lower half of the picture and"
        " there is no water in the air. Light comes down through the sea and lands on the dry sand"
        " in slow moving bars. Paint the inside of a glass dome on the seabed, NOT an ordinary"
        " underwater photograph. COMPOSITION: obey the camera described below. Do not default to a"
        " symmetrical view straight down a bright sand avenue with an arch of water across the top"
        " of the frame; that is the wrong picture and it has been made too many times already.")

# The one location that IS underwater: the held-breath dive down to the trench,
# the only time all session the party leaves the air.
SUBMERGED = (PALETTE +
             " Use the attached map for its colour and its brushwork ONLY: this picture contains"
             " none of its landforms. THE MOST IMPORTANT THING ABOUT THIS PICTURE: this is deep"
             " open water, fully submerged, with no air, no ground and no seabed anywhere in the"
             " frame.")

SUBMERGED_PLATES = {"loc_open_water"}

# The Rift Gate is the sole exception to EMPTY: the brass ring is the party's
# own, carried through from Gearhaven, and the location is named for it.
EMPTY_EXCEPT_THE_GATE = (" ABSOLUTELY EMPTY OF INHABITANTS. There must be no people, no"
         " figures, no humanoids, no silhouettes, no faces and no creatures anywhere in the"
         " picture except the fish visible out in the water. Apart from the brass ring"
         " described above, nothing else in the frame is built: no city, town, buildings,"
         " ruins, walls, boats, docks or machinery of any kind.")

EMPTY = (" ABSOLUTELY EMPTY OF INHABITANTS AND OF ANYTHING BUILT. There must be no people, no"
         " figures, no humanoids, no silhouettes, no faces, and no creatures of any kind"
         " anywhere in the picture. There must be no city, town, buildings, towers, spires,"
         " domes, houses, ruins, statues, bridges, roads, walls, boats, ships, docks, lanterns,"
         " furniture or machinery of any kind. Nothing in this world has ever been built by"
         " hands. This is a wild, uninhabited natural place and the picture is of the place"
         " alone: water, light, rock, sand and living reef, and nothing else.")

LOCATIONS = [
 ("loc_rift_gate",
  "The arrival bell, and the smallest of the six: a dome of air perhaps forty paces across sitting "
  "on a pale bone-grey sand flat. CAMERA IS INSIDE THE BELL AND CANNOT LEAVE IT. The viewer stands "
  "on the dry sand with the curved water wall rising directly in front of them and arching over "
  "their head, looking OUT through it at the sea. Do NOT show this dome from the outside; do not "
  "paint a bubble sitting in the distance. The bottom half of the picture is nothing but dry, "
  "swept, rippled sand at the viewer's feet with clear open air above it, and the water wall is "
  "the near, curved, rippling surface that closes that air in. Through it the shallow outside is "
  "visible but softened: rounded coral mounds in olive and rust going blue and vague with "
  "distance, exactly as the map paints them, and small fish hanging in the water overhead the way "
  "birds hang in a sky. THE GATE ITSELF IS THE SUBJECT OF THIS PICTURE AND MUST BE IN IT: standing "
  "upright on the dry sand, facing the viewer, is a great ring of worked brass and dark iron about "
  "twice the height of a person, a free-standing circular portal frame with an empty middle, "
  "banded and riveted and set with small dim lenses, exactly matching the second attached "
  "reference image. It has been carried here and planted in the sand; it does not belong to this "
  "world and it should look like the only made thing for a thousand miles. Nothing else in the "
  "frame is built. Bare, swept and expectant: the doorstep of a world that is still healthy, seen "
  "before anyone has arrived."),
 ("loc_brightshoal",
  "The loudest, most crowded shallow in the world, and the first thing the travellers see that is "
  "worth saving. CAMERA: chest height inside an enormous air-bell, on dry rippled sand, looking "
  "along an open floor that runs away to the LEFT of frame and out of it. THE CEILING IS THE WHOLE "
  "POINT of this picture: forty feet overhead a taut, bright, rippling SKIN of water is stretched "
  "flat across the top of the frame like the underside of a lake, and the sea is on the far side "
  "of it, so shoals of fish and swaying weed are clearly ABOVE that skin, in the water, while the "
  "air below it is completely clear and empty. The near right of the frame is closed by a bank of "
  "coral crowding up to and through the bell edge, plus two or three coral heads the size of "
  "wagons standing free on the dry sand as cover: olive, moss, ochre and rust with a few deep reds "
  "and violets among them, stacked and overlapping and absolutely thick with life. The sand floor "
  "itself is bare and dust-dry, with nothing growing on it. Cool pale bars of light come slanting "
  "down through the skin and pool on the sand. Bright, joyous, teeming, and cool in colour "
  "throughout: turquoise and jade, never a warm tropical postcard."),
 ("loc_kelp_cathedral",
  "A giant kelp forest with a room cleared out beneath it. CAMERA: low and tilted UP, so the "
  "picture is governed by verticals: stipes of giant kelp as thick as tree trunks rising out of "
  "the top of the frame, rank behind rank into the distance, their strap-shaped blades acid olive "
  "and old gold, the gaps between them a deep bottle-green darkness. The bell is a long clear "
  "aisle among the roots: dry pale sand underfoot, and a low taut skin of water stretched from "
  "stipe to stipe overhead like a ceiling threaded through a wood. Above that skin the kelp keeps "
  "climbing for hundreds of feet into a dim green canopy, and pockets of trapped silver air are "
  "caught up in the fronds like held breath. Green shafts, drifting motes, enormous hush. It is a "
  "FOREST, not a building: no arches, no carved columns, no vaults, no hanging orbs or lamps."),
 ("loc_blackwater_seam",
  "A wound opened in the last hour, while the travellers were still on the road. CAMERA: "
  "off-centre and low, looking along the length of a jagged black crack that cuts diagonally from "
  "the bottom right of the frame to the upper left, splitting a floor of bleached, bone-white, "
  "dying coral. Black water rises out of the crack in slow heavy ribbons and spreads overhead, "
  "staining the jade sea into a sour brown-green murk that eats the light. The bell here is "
  "FAILING: the water ceiling sags low and uneven, one whole column of it has already slumped to "
  "the floor and stands there like a fallen curtain, and the trembling edge is losing its shape. "
  "Dim, not dark: a sick pale light in the seam itself, umber and near-black everywhere else. "
  "Wrong, recent, ominous, and never gruesome."),
 ("loc_guardians_trench",
  "The floor of an enormous trench, the last lit room in the world. CAMERA: set well back and low "
  "on a wide shelf of dry pale sand, looking out and up, so the picture is dominated by the "
  "ENORMOUS DARK: ring walls of stepped rock climbing away on every side into blue-black nothing, "
  "turning slowly as they climb so the whole trench reads as a vast spiral bowl, exactly the shape "
  "the map paints at its eye. A black-green water ceiling presses down low and close over the "
  "sand. Threads of cold blue-white bioluminescence trace the ledges and are the only light in the "
  "picture: there is NO gold anywhere here. Enormous, silent and under pressure, an entire ocean "
  "stacked overhead on a small dry floor."),
 ("loc_open_water",
  "The dive: mid-water, with nothing above and nothing below. CAMERA: pointed steeply UP through a "
  "column of deep blue-black ocean. The surface is a small pale coin of light impossibly far "
  "overhead, and the thin shafts falling from it fade out and fail long before they reach the "
  "bottom of the frame. Suspended motes and specks catch what little light there is; in every "
  "other direction the blue simply darkens until it is black. There is NO seabed, NO rock, NO "
  "cliff, NO reef, NO coral, NO kelp and no ceiling: nothing at all to give the space scale except "
  "the emptiness itself. Cold, vast, beautiful and frightening at once."),
]
