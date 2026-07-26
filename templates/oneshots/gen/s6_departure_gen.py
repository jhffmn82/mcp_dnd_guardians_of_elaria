import base64, os, sys, time, requests
os.chdir(r"C:/Users/jhffm/dnd-campaign"); sys.path.insert(0, "templates"); import review_gallery
KEY = open(os.path.expanduser("~/.openai_key")).read().strip()
S = "painterly storybook fantasy illustration, lush warm golden palette with teal and brass accents, soft volumetric light, detailed fantasy-anime glow, richly rendered digital painting, no text or lettering anywhere."

# Closing vignette for Session 6's departure page: the heroes leave Wraithpine
# at sunrise on the east road, relics in hand, Ghostbloom (POST-emergence era)
# floating beside them. Era refs: S6+ (sash, staff, dynamo now owned).
PROMPT = (S + " Wide cinematic landscape, seen from behind: THREE small heroes and one floating "
          "spirit walk away down a coastal road toward the rising sun, leaving a fog-wrapped "
          "village of lanterns and pumpkins behind them in the valley below. The three heroes "
          "match their references: LILLY the deep gnome girl (silver hair, goggles), STABBY the "
          "goblin boy with a scarlet sash at his waist and a candy-striped katana on his back, "
          "URSA the red-haired human boy carrying a gnarled staff crowned with tiny hovering "
          "stars. Beside them floats GHOSTBLOOM, matching the fourth reference exactly: a small "
          "creature of translucent teal ghost-light with a glowing bloom on her back, trailing "
          "soft chiming petals. Dawn gold breaking through sea fog, long shadows, hopeful "
          "road-ahead mood.")

refs = ["assets/art_refs/REF_lilly_4_later.png", "assets/art_refs/REF_stabby_3_later.png",
        "assets/art_refs/REF_ursa_3_later.png", "assets/art_refs/REF_ghostbloom.png"]
open("assets/gen_prompts/s6_departure_east.txt", "w", encoding="utf-8").write(PROMPT)
h = {"Authorization": "Bearer " + KEY}
for attempt in range(4):
    try:
        fh = [("image[]", (os.path.basename(f), open(f, "rb"), "image/png")) for f in refs]
        r = requests.post("https://api.openai.com/v1/images/edits", headers=h,
                          data={"model": "gpt-image-2", "prompt": PROMPT,
                                "size": "1536x1024", "quality": "high"}, files=fh, timeout=900)
        j = r.json()
        if "data" not in j:
            print("ERR", str(j.get("error", {}).get("message"))[:200]); break
        open("art_review/PENDING_s6_departure_east.png", "wb").write(base64.b64decode(j["data"][0]["b64_json"]))
        print("ok"); break
    except Exception as e:
        print("retry", attempt, str(e)[:80]); time.sleep(20 * (attempt + 1))
review_gallery.build()
print("done")
