# batch_art.py
# Concurrent art generation for the whole remaining queue.
# Composes each prompt from STYLE + auto-included character blocks + scene line,
# attaches era-correct references, and runs N requests in parallel. Each finished
# image lands in art_review/PENDING_<name>.png and the gallery is rebuilt so the
# review board stays current. Key from ~/.openai_key (never in repo).
import base64, os, sys, io, concurrent.futures as cf
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, "templates"))
import review_gallery

KEY = open(os.path.expanduser("~/.openai_key")).read().strip()
MODEL = "gpt-image-2"
GEN = os.path.join(ROOT, "art_review")
os.makedirs(GEN, exist_ok=True)
os.makedirs("assets/gen_prompts", exist_ok=True)

STYLE = ("painterly storybook fantasy illustration, lush warm golden palette with teal and brass "
         "accents, soft volumetric light, detailed fantasy-anime glow, digital painting, no text "
         "or lettering anywhere in the image.")

BLK = {
 "lilly": "LILLY is a tiny 7-year-old deep gnome girl with dark slate-gray skin, long silver hair, large bright red eyes, brass goggles pushed up on her head, a little leather tool-harness over travel clothes; match her reference exactly.",
 "stabby": "STABBY is an 8-year-old goblin boy with bright green skin, spiky light-green hair, big red eyes, long pointed ears, a huge sharp-toothed grin, simple brown monk garb; match his reference exactly.",
 "ursa": "URSA is a 7-year-old human boy druid with short red hair, pale freckled skin, bright purple eyes, delicate purple leaf-tattoos, rustic green-and-brown druid clothes; match his reference exactly.",
 "ghostbloom": "GHOSTBLOOM is a ghostly Bulbasaur: the classic four-legged Bulbasaur silhouette with a bloom and leaves on its back, but made ENTIRELY of luminous translucent teal ghost-light, fully see-through and spectral like a glowing spirit-flame; match her reference exactly.",
 "floraburst": "FLORABURST is a small cheerful bright spring-green fey creature like a tiny leafy dinosaur with a large flower bud on its back; match her reference exactly.",
}
REF = {
 "lilly": ["assets/art_refs/REF_lilly_1.png", "assets/art_refs/REF_lilly_2.png"],
 "lilly_late": ["assets/art_refs/REF_lilly_4_later.png", "assets/art_refs/REF_lilly_5_later.png"],
 "stabby": ["assets/art_refs/REF_stabby_1.png", "assets/art_refs/REF_stabby_2.png"],
 "ursa": ["assets/art_refs/REF_ursa_1.png", "assets/art_refs/REF_ursa_2.jpg"],
 "ghostbloom": ["assets/art_refs/REF_ghostbloom.png"],
 "floraburst": ["assets/art_refs/REF_floraburst.png"],
 "hydra": ["assets/monsters/false_hydra.png"],
}

# name, [character/ref tokens], scene line
QUEUE = [
 # ---- Session 1 ----
 ("s1_gilded_acorn_meeting", ["lilly","stabby","ursa"], "Scene: inside a cozy candlelit medieval tavern with a stone hearth, the three children meet at a small wooden table, the gnome girl showing a small glowing brass sphere to the curious druid boy while the goblin boy leans in grinning."),
 ("s1_bar_brawl", ["stabby"], "Scene: a comedic non-lethal tavern brawl, the tiny goblin boy ducking under a burly farmer's wild swing while mugs and a chair fly and patrons laugh."),
 ("s1_lickgloom_pond", ["ursa"], "Scene: a moonlit pond ringed with reeds and glowing wildflowers, the druid boy kneeling to offer bread to a small round fey creature with an impossibly long tongue and huge innocent eyes, fireflies drifting."),
 ("s1_mist_stalkers", ["lilly","stabby","ursa"], "Scene: a foggy twilight forest road blocked by gnarled roots, the three small heroes standing back to back as two sleek shadowy panther-like predators with glowing eyes circle them in the mist, brave not gory."),
 ("s1_oakshade_twilight", [], "Scene: a small village nestled beneath enormous ancient oak trees at twilight, lantern-lit cottages, a great old oak hung with faded ribbons beside a stone well."),
 ("duckleaf_stone_circle", [], "Scene: an ancient mossy stone circle in a misty forest clearing, and perched atop the tallest rune-carved standing stone a proud sturdy duck-like creature holding a long leek stalk like a sword, wind swirling leaves around it."),
 ("cognifin_grove", [], "Scene: a hidden forest grove with a pond glowing soft blue from below, water droplets hanging frozen in the air, a serene duck-like guardian creature hovering above its reflection wrapped in rippling psychic blue light."),
 # ---- Session 2 ----
 ("s2_villagers_return", [], "Scene: a joyful dawn reunion in a village square under giant oaks, three dazed teenage herb-gatherers stumbling home into the arms of relieved villagers, an old bearded blacksmith elder beaming."),
 ("s2_mudskip_ambush", ["lilly"], "Scene: a muddy forest clearing where three slick salamander-like water elemental creatures leap from puddles, the tiny gnome girl zapping one with a sparking brass gadget."),
 ("s2_grimfang_ambush", ["stabby"], "Scene: a forest-road ambush, the small goblin monk boy standing defiant before a big scarred goblin war-boss flanked by a snarling wolf-like worg, rival-clan banners in the trees."),
 ("s2_elaria_vision", ["lilly","stabby","ursa"], "Scene: in a moonlit glade before a mossy runestone, the three children seen small from behind gaze up in awe at a colossal translucent goddess woven of starlight, flowing water and blooming vines, her kind sorrowful face high above, stars wheeling behind her."),
 ("terranox", [], "Scene: a huge serpent made of living stone and glowing crystal rearing up from a rocky mountain path, geodes glinting along its spine, boulders floating around it."),
 ("s2_ravenstone_arrival", ["lilly","stabby","ursa"], "Scene: the three children cresting a hill at dusk to behold a wondrous stone-and-glass laboratory built into a cliff above a shimmering lake, whimsical little glowing creatures grazing nearby."),
 # ---- Session 3 ----
 ("s3_sphere_examination", ["lilly"], "Scene: inside a magical laboratory of brass instruments and floating motes of light, a tall silver-haired elf professor with emerald eyes examines a glowing sphere through a rune-etched lens while the little gnome girl watches anxiously."),
 ("s3_choose_companion", ["lilly","stabby","ursa","floraburst"], "Scene: a tall silver-haired elf professor presents three small magical creatures to the delighted children: a leafy green dinosaur-fey with a flower bud, a turtle wrapped in a watery aura, and a fiery fox-like creature with flame-tipped paws."),
 ("s3_lickgloom_farewell", ["ursa"], "Scene: a bittersweet goodbye at a laboratory doorway in morning light, a small round long-tongued fey creature waving its tongue happily at the departing druid boy while other magical lab creatures gather around it."),
 ("shadowflame", [], "Scene: a thorny twilight thicket where a creature of living shadow wreathed in cold blue-purple flame stands among three flickering mirror-image duplicates of itself."),
 ("s3_displacer_beasts", ["stabby"], "Scene: a foggy ancient forest path where two sleek six-legged panther-like beasts with long back-tentacles prowl toward the small goblin boy, who grins back unafraid."),
 ("shroomyte_grove", [], "Scene: a grove of giant glowing bioluminescent mushrooms at night, four squat fungus-guardian creatures with luminous spore-caps rising from the earth."),
 ("s3_stormwatch_vision", ["lilly","stabby","ursa"], "Scene: storm-lashed sea cliffs crowned with four elemental monoliths, lightning frozen mid-strike, and above them a looming translucent hologram of a dark cloaked figure whose face is hidden in shadow, the three children small and defiant below."),
 ("s3_havenmoor_arrival", [], "Scene: a festive snow-dusted coastal town at dusk decorated for a winter holiday, garlands and lanterns, a towering decorated pine in the square, ships in the harbor beyond."),
 # ---- Session 4 (Stabby carries the candy-cane katana here) ----
 ("s4_children_singing", [], "Scene: a snowy village street at pale dawn, a huddle of entranced children singing with vacant eyes while frightened parents watch from doorways, spooky-beautiful not scary."),
 ("s4_bell_hunt_market", ["lilly"], "Scene: a festive winter market square with a towering decorated pine tree, the little gnome girl climbing the garlands to reach a small golden bell hidden among the ornaments."),
 ("s4_orphanage_milo", ["ursa"], "Scene: a dim orphanage attic, the druid boy kneeling gently before a frightened small child who clutches a little golden bell, warm lantern light pushing back the shadows."),
 ("s4_lighthouse", ["stabby"], "Scene: a storm-battered lighthouse on snowy sea cliffs in whirling snow, the goblin boy scampering up the spiral stair while an old bearded keeper holds a lantern below."),
 ("faelan", [], "Scene: portrait of an ancient kindly half-elf lorekeeper in an ivy-covered candlelit cottage full of books, offering a plate of frosted cookies, warm and grandfatherly."),
 ("s4_barrier_carol", ["lilly","stabby","ursa"], "Scene: the three children playing small golden handbells together in a snowy moonlit glade before a great pine sheathed in black ice, the ice cracking with golden light where the music touches it."),
 ("s4_carol_finale", ["lilly","stabby","ursa"], "Scene: the three children ringing bells in glowing golden harmony as a towering ten-foot goat-horned shadow fiend unravels into wisps of darkness above them, snow suspended in the light."),
 ("s4_children_freed", [], "Scene: a burst-open burlap sack spilling a dozen laughing children unharmed into lantern-lit snow, one small boy running into his weeping mother's arms, joyful."),
 # ---- Session 5 ----
 ("s5_harbor_sendoff", ["lilly","stabby","ursa","floraburst"], "Scene: a cheering harbor crowd waving the three children up the gangplank of a proud tall ship with white sails, banners strung between lampposts, morning sun on the water."),
 ("s5_storm", [], "Scene: a tall sailing ship battling a monstrous night storm, a towering wall of black water, lightning splitting the mainmast, sailors clinging to the rigging, dramatic but heroic."),
 ("s5_dutchman_rises", [], "Scene: seen from under a capsized hull in dark water, a ghostly barnacled galleon rising out of the deep wrapped in green spectral light, eerie lantern-glow on its hull."),
 ("davy_jones", [], "Scene: portrait of a ghost-pirate captain with a beard of small tentacles, barnacle-crusted coat and a hook hand, wreathed in green spectral light, theatrical and menacing but kid-friendly."),
 ("s5_dice_game", ["lilly","stabby","ursa"], "Scene: a candlelit ghost-ship cabin, the three small heroes seated across a table from a tentacle-bearded ghost pirate captain, glowing bone dice tumbling between them in green lantern light."),
 ("s5_ghost_essence", ["lilly","floraburst"], "Scene: the little gnome girl gently pouring a swirling ribbon of pale ghost-light from a glass jar into her small green leafy dinosaur companion, whose leaves are beginning to turn glassy and pale, tender and luminous."),
 ("s5_vigil_dawn", ["lilly","stabby","ursa","floraburst"], "Scene: a small rowing cutter at golden dawn, the exhausted children rowing toward distant clockwork spires on the horizon while a ghostly galleon splits and sinks far behind them."),
 # ---- big-picture ----
 ("elaria_goddess", [], "Scene: full portrait of Elaria, the sleeping Warden of Balance: a serene colossal goddess drifting in starry darkness, hair flowing into constellations, vines and water woven through her robes, a seven-pointed star glowing softly at her brow."),
 ("dark_figure", [], "Scene: a tall figure of living shadow standing on a broken starfield, face hidden in a dark hood, one hand closing around a tiny dying star, wisps of darkness trailing like a cloak, ominous but elegant, kid-friendly."),
 ("three_potatoes", [], "Scene: three humble potatoes resting on dark velvet, each faintly glowing with a different inner light (warm gold, shifting green, cool silver), painted like precious sacred relics."),
 ("stabbys_doll", [], "Scene: a small old carved wooden doll wearing a tiny stitched cat-mask, lying on an open goblin travel-bag beside a campfire at night, a faint cold blue aura around it, mysterious not menacing."),
]

def refs_for(tokens):
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
    files = refs_for(tokens)
    headers = {"Authorization": f"Bearer {KEY}"}
    try:
        if files:
            fh = [("image[]", (os.path.basename(f), open(f, "rb"), "image/jpeg" if f.endswith(".jpg") else "image/png")) for f in files]
            r = requests.post("https://api.openai.com/v1/images/edits", headers=headers,
                              data={"model": MODEL, "prompt": prompt, "size": "1024x1024", "quality": "high"},
                              files=fh, timeout=600)
        else:
            r = requests.post("https://api.openai.com/v1/images/generations", headers=headers,
                              json={"model": MODEL, "prompt": prompt, "size": "1024x1024", "quality": "high"}, timeout=600)
        j = r.json()
        if "data" not in j:
            return name, f"ERR {j.get('error',{}).get('message','?')}"
        img = base64.b64decode(j["data"][0]["b64_json"])
        open(os.path.join(GEN, f"PENDING_{name}.png"), "wb").write(img)
        review_gallery.build()
        return name, "ok"
    except Exception as e:
        return name, f"EXC {e}"

if __name__ == "__main__":
    todo = QUEUE
    if len(sys.argv) > 1:  # optional filter by substring
        todo = [q for q in QUEUE if sys.argv[1] in q[0]]
    print(f"generating {len(todo)} images, 5 concurrent")
    with cf.ThreadPoolExecutor(max_workers=5) as ex:
        for name, status in ex.map(gen_one, todo):
            print(f"  {status:>6}  {name}", flush=True)
    review_gallery.build()
    print("batch done")
