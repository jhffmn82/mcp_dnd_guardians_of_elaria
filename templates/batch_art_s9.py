# batch_art_s9.py
# Session 9 (Unda, the Undersea) art queue. Same contract as batch_art.py:
# composes STYLE + character blocks + scene line, attaches the LEVEL-7 reference
# set, runs N in parallel, drops PENDING_<name>.png into art_review/ and rebuilds
# the gallery. Key from ~/.openai_key (never in repo).
#
# Plates are 1536x1024 (3:2), matching every Session 7 and 8 plate.
#
# Run:  python templates/batch_art_s9.py            (whole queue)
#       python templates/batch_art_s9.py loc_       (substring filter)
import base64, os, sys, concurrent.futures as cf
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, "templates"))
import review_gallery

KEY = open(os.path.expanduser("~/.openai_key")).read().strip()
MODEL = os.environ.get("GENART_MODEL", "gpt-image-2")
SIZE = os.environ.get("GENART_SIZE", "1536x1024")
GEN = os.path.join(ROOT, "art_review")
os.makedirs(GEN, exist_ok=True)
os.makedirs("assets/gen_prompts", exist_ok=True)

# The campaign's house style is a warm golden palette (see batch_art.py, which
# still uses it for Sessions 1 to 7). Session 9 is a WATER plane and its board
# map is cool throughout: turquoise, jade, petrol blue, bone-grey sand, olive
# and rust coral. The warm string fought the map and won, which is why the first
# location passes came back as honey-gold tropical postcards. Session 9 gets its
# own palette so the whole volume agrees with its own board.
STYLE = ("painterly storybook fantasy illustration, soft-edged painterly oils with depth haze, "
         "a COOL sea palette of turquoise, jade and petrol blue over pale bone-grey sand, with "
         "coral in olive, moss, ochre and rust; light arrives cool and already spent by the water "
         "it came through; no honey-gold sand, no amber sunbeams, no tropical-postcard warmth; "
         "no text or lettering anywhere in the image.")

# Level-7 blocks. The heroes are two years older than the Session 1 art and carry
# the post-timeskip kit. The earring rule holds: Lilly wears exactly one, the
# boys wear none.
BLK = {
 "lilly": "LILLY is a small deep gnome girl with dark slate-gray skin, long silver hair, large bright red eyes, brass goggles pushed up on her head, exactly one earring, a leather tool-harness, and a brass repeating pistol called Boomstick; match her reference exactly.",
 "stabby": "STABBY is a goblin boy with bright green skin, spiky light-green hair, big red eyes, long pointed ears, no earrings, simple crimson-and-brown monk garb, carrying a slender crimson katana two-handed with the glow on the OUTER cutting edge; match his reference exactly.",
 "ursa": "URSA is a human boy druid with short red hair, pale freckled skin, bright purple eyes, delicate purple leaf-tattoos, no earrings, rustic green-and-brown druid clothes, carrying a tall gnarled staff crowned with a pale star; match his reference exactly.",
 "sandshrew": "SANDSHREW is a small sturdy pale-yellow pangolin-like creature with a segmented armoured back, big digging claws and a cheerful blunt face; match his reference exactly.",
 "piplup": "PIPLUP is a small round penguin-like creature, deep blue above and white below, with a short pointed beak, a stubby crest of three blue spikes and two flipper-arms; proud and serious; match his reference exactly.",
 "aelwyn": "PROFESSOR AELWYN RAVENSTONE is a tall silver-haired HIGH ELF with emerald green eyes, ink-stained fingers and a worn scholar's coat; kind, precise, a teacher rather than a wizard; match his reference exactly.",
}
REF = {
 "lilly": ["assets/art_refs/REF_lilly_6_level7.png"],
 "stabby": ["assets/art_refs/REF_stabby_4_level7.png"],
 "ursa": ["assets/art_refs/REF_ursa_4_level7.png"],
 "sandshrew": ["assets/characters/sandshrew.png"],
 "piplup": ["assets/companions/piplup.png"],
 # Canonical, per assets/character_refs.md. He is an ELF, not the human I
 # briefly invented for him.
 "aelwyn": ["assets/art_refs/REF_aelwyn.webp"],
}

# name, [character/ref tokens], scene line
QUEUE = [
 # ---- cover ----
 ("s9_frontispiece", [],
  "Scene: a cathedral of sunlit green ocean seen from the seafloor, colossal shafts of light falling "
  "through clear water onto white sand, three tiny distant figures standing together in a dome of "
  "clear air at the bottom of it, and far out in the blue a shape the size of a hill moving away "
  "from them. Awe and scale, not menace. This is a world worth saving."),

 # ---- locations ----
 ("s9_loc_brightshoal", [],
  "Scene: a shallow coral shoal of impossible colour, greens that are almost gold and a red so deep "
  "it seems to hum, under a ceiling of clear moving seawater fifty feet up. Bright sunshafts you "
  "could walk between fall onto dry white sand. Coral heads the size of wagons stand around the "
  "edges. A living, loud, crowded, joyful place."),
 ("s9_loc_kelp_cathedral", [],
  "Scene: the interior of a drowned cathedral made of living kelp, columns hundreds of feet tall "
  "rising into a dim green canopy, with domes of trapped silver air caught in the fronds overhead "
  "like hanging lanterns. Shafts of deep green light, motes drifting, a floor of pale sand far "
  "below. Vast, hushed, and beautiful."),
 ("s9_loc_blackwater_seam", [],
  "Scene: a long crack torn across a pale seafloor with black water pouring UP out of it in slow "
  "ribbons, staining the clear green sea above into murk. The coral at the edges is bleached white "
  "and dying. One failing dome of clear air still stands to one side, its edge trembling. Wrong, "
  "fresh, and being made right now. Ominous but never gruesome."),
 ("s9_loc_guardians_trench", [],
  "Scene: the lip of an enormous ocean trench dropping away into blue-black nothing, ledges of pale "
  "rock stepping down into the dark, faint bioluminescence tracing the walls, and very far below a "
  "single vast shape suggested rather than shown. Enormous depth, held breath."),

 # ---- pivotal moments (locked; independent of the enemy roster) ----
 ("s9_the_crossing", ["lilly", "stabby", "ursa", "sandshrew"],
  "Scene: the three young heroes stepping through a brass ring portal onto dry white sand, and "
  "stopping. Above and around them is clear sunlit seawater held back in a perfect dome, fish "
  "hanging in it like birds. Their faces are lit from above, astonished. After a season underground "
  "they are standing somewhere glad they came. Their small armoured pangolin companion stands at "
  "their feet, staring up at the water ceiling with open suspicion."),
 ("s9_the_dive", ["lilly", "stabby", "ursa", "sandshrew"],
  "Scene: the three young heroes swimming downward together in open dark blue water, small and "
  "close together, trailing silver bubbles, the last dome of light far above them. Passing beneath "
  "them in the deeper dark is an immense shadow, only its scale readable. Their armoured pangolin "
  "companion paddles grimly along beside them, extremely far from home. Wonder and fear at once."),
 ("s9_aelwyn_and_the_reed", ["ursa", "aelwyn"],
  "Scene: a warm lamplit study crowded with books and charts, the elderly scholar seated beside the "
  "red-haired druid boy with the boy's spell notes spread between them, pointing at one line on the "
  "page. In his other hand he holds out a short worn river reed. A teaching moment, quiet and kind."),
]


# The remaining 54 plates (locations, plot beats, and every monster card) are
# generated into s9_art_queue.py from the reconciled art list, so the queue and
# the design cannot drift. Everything lands in art_review/ for DM approval.
if "--locations" in sys.argv:
    # Stage 1. Six rooms, no cast, nothing else.
    from s9_locations import (LOCATIONS as _L, EMPTY, EMPTY_EXCEPT_THE_GATE,
                              BELL, SUBMERGED, SUBMERGED_PLATES)
    QUEUE = [("s9_" + n, [],
              (SUBMERGED if n in SUBMERGED_PLATES else BELL) + " " + s +
              (EMPTY_EXCEPT_THE_GATE if n == "loc_rift_gate" else EMPTY))
             for n, s in _L]
else:
    from s9_art_queue import QUEUE as _SCENES
    from s9_monster_queue import QUEUE as _MONSTERS
    QUEUE = [q for q in _SCENES if not q[0].startswith("mon_")] + _MONSTERS


import s9_art_plan


def refs_for(tokens, name=None):
    """Location reference first, then everyone in frame. See s9_art_plan."""
    if name:
        planned = s9_art_plan.refs_for_plate(name)
        if planned:
            return [p for p in planned if os.path.exists(p)]
    files = []
    for t in tokens:
        files += REF.get(t, [])
    return files


def blocks_for(tokens):
    return " ".join(BLK[t] for t in tokens if t in BLK)


def gen_one(item):
    name, tokens, scene = item
    prompt = STYLE + " " + blocks_for(tokens) + " " + scene
    open(f"assets/gen_prompts/{name}.txt", "w", encoding="utf-8").write(prompt)
    files = refs_for(tokens, name)
    headers = {"Authorization": f"Bearer {KEY}"}
    try:
        if files:
            fh = [("image[]", (os.path.basename(f), open(f, "rb"),
                   "image/webp" if f.endswith(".webp") else "image/png")) for f in files]
            r = requests.post("https://api.openai.com/v1/images/edits", headers=headers,
                              data={"model": MODEL, "prompt": prompt, "size": SIZE, "quality": "high"},
                              files=fh, timeout=900)
        else:
            r = requests.post("https://api.openai.com/v1/images/generations", headers=headers,
                              json={"model": MODEL, "prompt": prompt, "size": SIZE, "quality": "high"},
                              timeout=900)
        if r.status_code == 429:
            import time
            time.sleep(int(r.headers.get("retry-after", 20)) + 5)
            return gen_one(item)
        j = r.json()
        if "data" not in j:
            return name, f"ERR {j.get('error', {}).get('message', '?')}"
        img = base64.b64decode(j["data"][0]["b64_json"])
        open(os.path.join(GEN, f"PENDING_{name}.png"), "wb").write(img)
        return name, "ok"
    except Exception as e:
        return name, f"EXC {e}"


if __name__ == "__main__":
    # Stage 2 cannot run until the locations are approved into assets/, because
    # every plate uses its location as a setting reference.
    if "--locations" not in sys.argv:
        gaps = s9_art_plan.missing_locations()
        if gaps:
            print("STOP. These locations are not approved into assets/ yet, and every")
            print("other plate needs one of them as its setting reference:")
            for g in gaps:
                print("   ", g)
            print()
            print("Run:  python templates/batch_art_s9.py --locations")
            sys.exit(1)

    todo = QUEUE
    if len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
        todo = [q for q in QUEUE if sys.argv[1] in q[0]]

    # Resume by default: a plate already sitting in art_review is done. Pass
    # --force to regenerate everything.
    if "--force" not in sys.argv:
        before = len(todo)

        def already_done(name):
            # Pending review, or already approved and banked. Without the second
            # check, approving a plate moves it out of art_review and the next
            # run helpfully regenerates the thing the DM just signed off on.
            if os.path.exists(os.path.join(GEN, f"PENDING_{name}.png")):
                return True
            return bool(s9_art_plan.banked_path(name))

        todo = [q for q in todo if not already_done(q[0])]
        if before != len(todo):
            print(f"resuming: {before - len(todo)} already generated, {len(todo)} to go")

    # Only requests carrying reference images hit the org's input-images-per-
    # minute cap, and roughly two thirds of this queue carries none. Splitting
    # the pools lets the ref-free plates run wide instead of queueing behind
    # rate-limited ones.
    plain = [q for q in todo if not refs_for(q[1], q[0])]
    withref = [q for q in todo if refs_for(q[1], q[0])]
    print(f"generating {len(todo)} images at {SIZE}: "
          f"{len(plain)} ref-free at 10 concurrent, {len(withref)} with refs at 3", flush=True)

    def run(items, workers):
        if not items:
            return
        with cf.ThreadPoolExecutor(max_workers=workers) as ex:
            for fut in cf.as_completed([ex.submit(gen_one, it) for it in items]):
                name, status = fut.result()
                print(f"  {status:>6}  {name}", flush=True)

    with cf.ThreadPoolExecutor(max_workers=2) as outer:
        a = outer.submit(run, plain, 10)
        b = outer.submit(run, withref, 3)
        a.result(); b.result()
    review_gallery.build()
    print("batch done")
