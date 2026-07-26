import base64, os, sys, time, requests
os.chdir(r"C:/Users/jhffm/dnd-campaign"); sys.path.insert(0, "templates"); import review_gallery
KEY = open(os.path.expanduser("~/.openai_key")).read().strip()
S = "painterly storybook fantasy illustration, lush warm golden palette with teal and brass accents, soft volumetric light, detailed fantasy-anime glow, richly rendered digital painting, no text or lettering anywhere."

# v2 (DM 2026-07-06): the first take looked like a cozy in-town bridge with no
# corruption. This is a WILDERNESS barrier site with the dark seal visible.
PROMPT = (S + " Wide establishing landscape shot, no characters, deep in the WINTER WILDERNESS "
          "far from any town: a half-frozen stream winding through a snowy grove of bare "
          "silver-barked trees, its water glittering under a skin of ice. A rickety, weathered "
          "wooden footbridge crosses at the narrows. THE DARK SEAL IS CLEARLY VISIBLE: black, "
          "icy tendrils snake along the underside of the bridge planks, pulsing with a sickly "
          "blue-violet glow, and shadowy twisted shapes flicker frozen UNDER the ice of the "
          "stream. Black frost blooms across the bridge boards. No buildings, no lanterns, no "
          "village: only snow, wild trees, cold daylight, and the wrongness under the bridge. "
          "Eerie but kid-friendly.")

open("assets/gen_prompts/s4_crystalbrook_stream_v2.txt", "w", encoding="utf-8").write(PROMPT)
h = {"Authorization": "Bearer " + KEY}
refs = ["assets/scenes/s4_frostpine_glade.png"]
for attempt in range(4):
    try:
        fh = [("image[]", (os.path.basename(f), open(f, "rb"), "image/png")) for f in refs]
        r = requests.post("https://api.openai.com/v1/images/edits", headers=h,
                          data={"model": "gpt-image-2", "prompt": PROMPT,
                                "size": "1536x1024", "quality": "high"}, files=fh, timeout=900)
        j = r.json()
        if "data" not in j:
            print("ERR", str(j.get("error", {}).get("message"))[:200]); break
        open("art_review/PENDING_s4_crystalbrook_v2.png", "wb").write(base64.b64decode(j["data"][0]["b64_json"]))
        print("ok"); break
    except Exception as e:
        print("retry", attempt, str(e)[:80]); time.sleep(20 * (attempt + 1))
review_gallery.build()
print("done")
