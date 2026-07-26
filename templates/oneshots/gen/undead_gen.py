import base64, os, sys, time, concurrent.futures as cf, requests
os.chdir(r"C:/Users/jhffm/dnd-campaign"); sys.path.insert(0, "templates"); import review_gallery
KEY = open(os.path.expanduser("~/.openai_key")).read().strip()
S = "painterly storybook fantasy illustration, lush warm golden palette with teal and brass accents, soft volumetric light, detailed fantasy-anime glow, richly rendered digital painting, no text or lettering anywhere. A clean solo creature portrait, single subject centered, misty graveyard-at-dusk background."

JOBS = [
 ("wraithpine_zombie", S + " A KID-FRIENDLY risen villager of Wraithpine: a mossy, leaf-draped "
  "figure shambling up from a tidy hillside grave, lantern-lit fog, autumn leaves stuck to its "
  "old Sunday coat, confused and sad rather than scary, faint teal ghost-light in its eyes. "
  "Storybook spooky-cozy, absolutely no gore."),
 ("wraithpine_skeleton", S + " A KID-FRIENDLY skeleton of old Wraithpine in the remains of a "
  "fisherman's coat and boots, clacking politely up from a leaning headstone, jack-o-lantern "
  "glow on weathered bone, autumn leaves in its ribs, more rickety-puppet than frightening. "
  "Storybook spooky-cozy, absolutely no gore."),
]

def run(job):
    name, prompt = job
    open("assets/gen_prompts/" + name + ".txt", "w", encoding="utf-8").write(prompt)
    h = {"Authorization": "Bearer " + KEY}
    for attempt in range(4):
        try:
            fh = [("image[]", ("ref.png", open("assets/monsters/scarecrow.png", "rb"), "image/png"))]
            r = requests.post("https://api.openai.com/v1/images/edits", headers=h,
                              data={"model": "gpt-image-2", "prompt": prompt + " Match the palette and painterly style of the reference.",
                                    "size": "1024x1024", "quality": "high"}, files=fh, timeout=900)
            j = r.json()
            if "data" not in j:
                return name, "ERR " + str(j.get("error", {}).get("message"))[:120]
            open("art_review/PENDING_" + name + ".png", "wb").write(base64.b64decode(j["data"][0]["b64_json"]))
            return name, "ok"
        except Exception:
            time.sleep(20 * (attempt + 1))
    return name, "EXC retries exhausted"

with cf.ThreadPoolExecutor(max_workers=2) as ex:
    for n, st in ex.map(run, JOBS):
        print(n, st, flush=True)
review_gallery.build()
print("done")
