import base64, os, sys, time, concurrent.futures as cf, requests
os.chdir(r"C:/Users/jhffm/dnd-campaign"); sys.path.insert(0, "templates"); import review_gallery
KEY = open(os.path.expanduser("~/.openai_key")).read().strip()
S = "painterly storybook fantasy illustration, lush warm golden palette with teal and brass accents, soft volumetric light, detailed fantasy-anime glow, richly rendered digital painting, no text or lettering anywhere."

JOBS = [
 # Compendium frontispiece: a grand open magical tome with creatures and relics
 ("compendium_frontispiece",
  S + " A grand frontispiece for a magical reference volume: a huge open illuminated tome on a "
  "dark wooden lectern in a cozy scholar's study, and rising out of its glowing pages a swirl "
  "of tiny translucent conjured images: a leek-wielding duck, a stone serpent, a ghost-light "
  "flower-spirit, a brass essence-sphere, a star-topped staff, drifting motes of light. Warm "
  "lamplight, teal and gold magic, a sense of every wonder of the world gathered in one book. "
  "Vertical portrait composition, awe and warmth.", []),
 # Treasures & Relics section opener
 ("treasures_opener",
  S + " A treasure-hoard still life for a relics chapter: on deep midnight-blue velvet, an "
  "array of wondrous magical items arranged like a museum display, each glowing softly, a "
  "brass sphere with a star, a candy-striped katana, a flowing water-blue sash, a gnarled "
  "star-crowned staff, three humble glowing potatoes, small enchanted trinkets, all bearing a "
  "faint seven-pointed-star motif. Wide landscape, painterly, reverent.", []),
 # Custom content / subclasses opener: the three heroes' paths
 ("paths_opener",
  S + " A symbolic triptych of three heroic destinies for a homebrew subclass chapter: three "
  "glowing emblems floating in a starry void, a candy-red breath-of-battle flame, a "
  "frost-blue clockwork gear wreathed in lightning, a starlight-purple constellation shaped "
  "like a warden. Elegant, mythic, balanced composition, deep blue and gold. Wide landscape.", []),
]

def run(job):
    name, prompt, refs = job
    open("assets/gen_prompts/" + name + ".txt", "w", encoding="utf-8").write(prompt)
    h = {"Authorization": "Bearer " + KEY}
    size = "1024x1536" if name == "compendium_frontispiece" else "1536x1024"
    for attempt in range(4):
        try:
            r = requests.post("https://api.openai.com/v1/images/generations", headers=h,
                              json={"model": "gpt-image-2", "prompt": prompt, "size": size,
                                    "quality": "high"}, timeout=900)
            j = r.json()
            if "data" not in j:
                return name, "ERR " + str(j.get("error", {}).get("message"))[:120]
            open("art_review/PENDING_" + name + ".png", "wb").write(base64.b64decode(j["data"][0]["b64_json"]))
            return name, "ok"
        except Exception:
            time.sleep(20 * (attempt + 1))
    return name, "EXC retries exhausted"

with cf.ThreadPoolExecutor(max_workers=3) as ex:
    for n, st in ex.map(run, JOBS):
        print(n, st, flush=True)
review_gallery.build()
print("done")
