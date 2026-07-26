import base64, os, sys, concurrent.futures as cf, requests
os.chdir(r"C:/Users/jhffm/dnd-campaign"); sys.path.insert(0, "templates"); import review_gallery
KEY = open(os.path.expanduser("~/.openai_key")).read().strip()

# The world map, rebuilt from the party's actual travels (Sessions 1-7):
# S1 Eldridge Village -> Forest of Whispers. S2 Oakshade -> mountain pass
# (Terranox) -> Whispering Glade -> Ravenstone Laboratory. S3 lab -> Whisperwind
# Meadow -> Brambleshadow Thicket -> Ironroot Hills -> Stormwatch Cliffs ->
# Havenmoor. S4 Havenmoor (winter festival). S5 THEY CROSS THE SEA on the
# Stormwind (Flying Dutchman). S6 Wraithpine on the far shore. S7 Gearhaven.
PROMPT = (
 "A hand-drawn fantasy campaign world map on aged parchment, in the style of a published "
 "Dungeons and Dragons adventure module: fine ink linework, warm watercolor washes in gold, "
 "teal, and forest green, tiny illustrated landmarks, an ornate compass rose, and clean, "
 "readable serif place-name labels with correct spelling. Landscape orientation.\n"
 "GEOGRAPHY, west to east:\n"
 "WEST (a green vale): the small village ELDRIDGE VILLAGE in rolling hills at the southwest; "
 "the dark ancient FOREST OF WHISPERS just north of it; the oak-shaded hamlet OAKSHADE VILLAGE "
 "to its northeast; a thorny ravine hold BLOODTHORN HOLLOW in the far southwest wilds.\n"
 "CENTER (highlands): a mountain ridge called the RAVENSTONE CLIFFS with a small wizard's "
 "tower labeled RAVENSTONE LABORATORY on the cliff top; below and south of it, open grassland "
 "WHISPERWIND MEADOW, a dark tangle BRAMBLESHADOW THICKET, and rust-red hills threaded with "
 "giant roots called the IRONROOT HILLS; sea cliffs labeled STORMWATCH CLIFFS where the "
 "highlands meet the water.\n"
 "SOUTH COAST: a snowy harbor town HAVENMOOR on the shore, with a tiny decorated pine tree.\n"
 "EAST HALF: a wide sea labeled THE OPEN SEA filling much of the eastern middle of the map, "
 "with a tiny ghost ship and a sea-serpent flourish; on the FAR SHORE across the sea, a "
 "fog-shrouded fishing village WRAITHPINE with tiny lanterns; southeast of it inland, a grand "
 "brass-and-gear city labeled GEARHAVEN with clockwork towers; and in the far east, deep "
 "old-growth forest hiding a ruined temple labeled THE OLD SHRINE.\n"
 "A dotted red travel route traces the heroes' journey: Eldridge Village, Forest of Whispers, "
 "Oakshade Village, over the mountain pass to Ravenstone Laboratory, south through the meadow, "
 "thicket and hills to Havenmoor, then ACROSS THE OPEN SEA by ship to Wraithpine, and on to "
 "Gearhaven.\n"
 "Kid-friendly storybook charm, painterly, warm golden light. No modern lettering, no legend "
 "box, no border text other than the place names and compass."
)

def run(i):
    h = {"Authorization": "Bearer " + KEY}
    try:
        r = requests.post("https://api.openai.com/v1/images/generations", headers=h,
                          json={"model": "gpt-image-2", "prompt": PROMPT,
                                "size": "1536x1024", "quality": "high"}, timeout=900)
        j = r.json()
        if "data" not in j:
            return i, "ERR " + str(j.get("error", {}).get("message"))[:120]
        open("art_review/PENDING_world_map_candidate_%d.png" % i, "wb").write(
            base64.b64decode(j["data"][0]["b64_json"]))
        return i, "ok"
    except Exception as e:
        return i, "EXC " + str(e)[:120]

open("assets/gen_prompts/elaria_world_map.txt", "w", encoding="utf-8").write(PROMPT)
with cf.ThreadPoolExecutor(max_workers=3) as ex:
    for i, st in ex.map(run, [1, 2, 3]):
        print("candidate", i, st, flush=True)
review_gallery.build()
print("map candidates done")
