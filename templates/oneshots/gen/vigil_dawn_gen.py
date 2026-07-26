import base64, os, sys, time, requests
os.chdir(r"C:/Users/jhffm/dnd-campaign"); sys.path.insert(0, "templates"); import review_gallery
KEY = open(os.path.expanduser("~/.openai_key")).read().strip()
S = "painterly storybook fantasy illustration, lush warm golden palette with teal and brass accents, soft volumetric light, detailed fantasy-anime glow, richly rendered digital painting, no text or lettering anywhere."

# Canon fix (DM 2026-07-06): end of Session 5 shows FLORABURST (sleeping,
# glowing, mid-change), NOT Ghostbloom. v2 rejected: Floraburst rendered as a
# humanoid fairy child. She is a QUADRUPED leaf-beast cub; ref goes first.
PROMPT = (S + " The shipwrecked heroes escape across the open sea at dawn in a small wooden "
          "cutter, rowing hard, the shattered ghost ship sinking into the foam far behind them. "
          "In the boat, THREE child heroes matching their references exactly, and one creature: "
          "LILLY the deep gnome girl (dark slate skin, silver hair, red eyes, brass goggles) "
          "cradles an UNCONSCIOUS FLORABURST in her arms. FLORABURST must match the plant "
          "creature in the FIRST reference exactly: a small cat-sized FOUR-LEGGED leaf-armored "
          "beast cub, an ANIMAL with a mossy muzzle (absolutely not humanoid, no human face), "
          "big pointed ears, eyes closed in sleep, a large pink-and-green flower on a stem "
          "growing from her back, a curling vine tail, lying limp and asleep, glowing softly "
          "from within with pale frost-blue and ember light tracing her leaves. STABBY the "
          "goblin boy (green skin, spiky hair, red eyes, candy-striped katana on his back) "
          "hauls an oar; URSA the red-haired human boy (purple eyes, leaf tattoos) sits at the "
          "tiller looking back. Exhausted but hopeful mood, gold dawn light on the water, faint "
          "clockwork spires on the far horizon.")

refs = ["assets/art_refs/REF_floraburst.png", "assets/art_refs/REF_lilly_1.png",
        "assets/art_refs/REF_stabby_1.png", "assets/art_refs/REF_ursa_1.png"]
open("assets/gen_prompts/s5_vigil_dawn_v2.txt", "w", encoding="utf-8").write(PROMPT)
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
        open("art_review/PENDING_s5_vigil_dawn_v2.png", "wb").write(base64.b64decode(j["data"][0]["b64_json"]))
        print("ok"); break
    except Exception as e:
        print("retry", attempt, str(e)[:80]); time.sleep(20 * (attempt + 1))
review_gallery.build()
print("done")
