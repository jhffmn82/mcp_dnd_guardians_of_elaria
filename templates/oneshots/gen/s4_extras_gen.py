import base64, os, sys, time, concurrent.futures as cf, requests
os.chdir(r"C:/Users/jhffm/dnd-campaign"); sys.path.insert(0, "templates"); import review_gallery
KEY = open(os.path.expanduser("~/.openai_key")).read().strip()
S = "painterly storybook fantasy illustration, lush warm golden palette with teal and brass accents, soft volumetric light, detailed fantasy-anime glow, richly rendered digital painting, no text or lettering anywhere."

GLADE = (S + " Wide establishing landscape shot, no characters. THE FROSTPINE GLADE in deep "
         "winter: a snowy clearing ringed by pines armored in creaking ice, living mist curling "
         "between the trunks. At the center a massive frozen pine, trunk twisted and blackened, "
         "jagged chains of BLACK ICE wrapped around its roots, pulsing with a sickly blue light. "
         "Eerie but kid-friendly, cold blue shadow against warm late-day light at the clearing's "
         "edge.")

MAP = ("A hand-drawn regional adventure map on aged parchment, in the style of a published "
       "Dungeons and Dragons module map: fine ink linework, wintry watercolor washes (snow "
       "whites, ice blues, deep pine greens, warm lantern gold), tiny illustrated landmarks, a "
       "small compass rose, clean readable serif place-name labels with correct spelling. "
       "Landscape orientation. THE FROZEN WILDS AROUND HAVENMOOR:\n"
       "At the south edge on the coast, the snow-covered harbor town HAVENMOOR with a tall "
       "decorated pine in its square and a lighthouse labeled WYRMGALE LIGHTHOUSE on the point "
       "beside it.\n"
       "North of town, three destinations hidden in the winter wilds, spread apart with pine "
       "forest, frozen ponds and snowy hills between them: FROSTPINE GLADE, a clearing of "
       "ice-armored pines with one huge blackened tree wrapped in black-ice chains, to the "
       "northwest; CRYSTALBROOK STREAM, a half-frozen brook with a small wooden bridge, to the "
       "north; THE WHISPERING HOLLOW, a ring of frost-covered standing stones in a hollow "
       "between two hills, to the northeast.\n"
       "Faint wandering trails, ski and sled tracks, a wolf silhouette in the trees, snow "
       "falling. Kid-friendly storybook charm. No text other than the place names and compass.")

def run(job):
    name, prompt, refs = job
    open("assets/gen_prompts/" + name + ".txt", "w", encoding="utf-8").write(prompt)
    h = {"Authorization": "Bearer " + KEY}
    for attempt in range(4):
        try:
            if refs:
                fh = [("image[]", (os.path.basename(f), open(f, "rb"), "image/png")) for f in refs]
                r = requests.post("https://api.openai.com/v1/images/edits", headers=h,
                                  data={"model": "gpt-image-2", "prompt": prompt,
                                        "size": "1536x1024", "quality": "high"}, files=fh, timeout=900)
            else:
                r = requests.post("https://api.openai.com/v1/images/generations", headers=h,
                                  json={"model": "gpt-image-2", "prompt": prompt,
                                        "size": "1536x1024", "quality": "high"}, timeout=900)
            j = r.json()
            if "data" not in j:
                return name, "ERR " + str(j.get("error", {}).get("message"))[:120]
            open("art_review/PENDING_" + name + ".png", "wb").write(base64.b64decode(j["data"][0]["b64_json"]))
            return name, "ok"
        except Exception as e:
            time.sleep(20 * (attempt + 1))
    return name, "EXC retries exhausted"

JOBS = [
    ("s4_frostpine_glade", GLADE, ["assets/scenes/s4_havenmoor_town.png"]),
    ("s4_havenmoor_wilds_map", MAP, ["assets/world/elaria_region_map.png"]),
]
with cf.ThreadPoolExecutor(max_workers=2) as ex:
    for n, st in ex.map(run, JOBS):
        print(n, st, flush=True)
review_gallery.build()
print("done")
