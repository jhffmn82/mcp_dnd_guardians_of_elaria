import base64, os, sys, time, concurrent.futures as cf, requests
os.chdir(r"C:/Users/jhffm/dnd-campaign"); sys.path.insert(0, "templates"); import review_gallery
KEY = open(os.path.expanduser("~/.openai_key")).read().strip()
S = "painterly storybook fantasy illustration, lush warm golden palette with teal and brass accents, soft volumetric light, detailed fantasy-anime glow, richly rendered digital painting."

MAP_PROMPT = ("Reproduce this fantasy campaign map EXACTLY as it is, with one single change: "
              "completely remove the dotted red travel route line and its red dots everywhere on "
              "the map. Keep every label, landmark, ship, sea serpent, compass rose, color and "
              "texture identical to the original. No other changes.")
RELICS_PROMPT = (S + " A museum-style treasure display of THREE magical relics arranged side by side "
                 "on a dark parchment background, each bearing a small glowing seven-pointed star: "
                 "LEFT, a gnarled wooden druid staff crowned with a constellation of tiny hovering "
                 "stars (match the staff in reference 1); CENTER, a flowing water-blue silk sash "
                 "that ripples like a living current (match the sash in reference 2); RIGHT, a "
                 "palm-sized brass clockwork dynamo with frost-blue glowing coils (match the brass "
                 "device in reference 3). No people, no text or lettering anywhere.")

def job_map():
    h = {"Authorization": "Bearer " + KEY}
    for attempt in range(4):
        try:
            fh = [("image[]", ("map.png", open("assets/world/elaria_region_map.png", "rb"), "image/png"))]
            r = requests.post("https://api.openai.com/v1/images/edits", headers=h,
                              data={"model": "gpt-image-2", "prompt": MAP_PROMPT,
                                    "size": "1536x1024", "quality": "high"}, files=fh, timeout=900)
            j = r.json()
            if "data" not in j:
                return "map ERR " + str(j.get("error", {}).get("message"))[:120]
            open("art_review/PENDING_world_map_no_route.png", "wb").write(base64.b64decode(j["data"][0]["b64_json"]))
            return "map ok"
        except Exception:
            time.sleep(20 * (attempt + 1))
    return "map EXC retries exhausted"

def job_relics():
    h = {"Authorization": "Bearer " + KEY}
    open("assets/gen_prompts/three_relics_display.txt", "w", encoding="utf-8").write(RELICS_PROMPT)
    refs = ["assets/items/staff_of_waking_constellations.png",
            "assets/items/sash_of_the_swift_current.png",
            "assets/characters/lilly_with_dynamo.png"]
    for attempt in range(4):
        try:
            fh = [("image[]", (os.path.basename(f), open(f, "rb"), "image/png")) for f in refs]
            r = requests.post("https://api.openai.com/v1/images/edits", headers=h,
                              data={"model": "gpt-image-2", "prompt": RELICS_PROMPT,
                                    "size": "1536x1024", "quality": "high"}, files=fh, timeout=900)
            j = r.json()
            if "data" not in j:
                return "relics ERR " + str(j.get("error", {}).get("message"))[:120]
            open("art_review/PENDING_three_relics_display.png", "wb").write(base64.b64decode(j["data"][0]["b64_json"]))
            return "relics ok"
        except Exception:
            time.sleep(20 * (attempt + 1))
    return "relics EXC retries exhausted"

with cf.ThreadPoolExecutor(max_workers=2) as ex:
    for res in ex.map(lambda f: f(), [job_map, job_relics]):
        print(res, flush=True)
review_gallery.build()
print("done")
