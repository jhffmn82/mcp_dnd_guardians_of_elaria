import base64, os, sys, concurrent.futures as cf, requests
os.chdir(r"C:/Users/jhffm/dnd-campaign"); sys.path.insert(0, "templates"); import review_gallery
KEY = open(os.path.expanduser("~/.openai_key")).read().strip()
S = "painterly storybook fantasy illustration, lush warm golden palette with teal and brass accents, soft volumetric light, detailed fantasy-anime glow, richly rendered digital painting, no text or lettering anywhere."
P = " A clean solo portrait, single subject centered, soft parchment-toned background."
W = " Wide establishing landscape shot, no main characters (or tiny for scale), a place the reader can step into."
JOBS = [
 ("s1_stabby_intro", ["assets/art_refs/REF_stabby_1.png", "assets/art_refs/REF_stabby_2.png"], S+P+" STABBY, an 8-year-old goblin boy: bright green skin, spiky light-green hair, big red eyes, pointed ears with rings, huge sharp-toothed grin, simple brown monk garb, NO weapons or relics (his first day of adventure). Match the references exactly. Waist-up."),
 ("s1_ursa_intro", ["assets/art_refs/REF_ursa_1.png", "assets/art_refs/REF_ursa_2.jpg"], S+P+" URSA, a 7-year-old human druid boy: short tousled red hair, pale freckled skin, bright purple eyes, purple leaf-tattoos on cheek and neck, rustic green-brown druid clothes, holding one humble faintly-golden-glowing potato, NO staff (his first day). Match the references exactly. Waist-up."),
 ("s1_forest_of_whispers", [], S+W+" The three tiny child heroes seen from behind at the bottom edge, stepping into the FOREST OF WHISPERS: ancient towering trees closing overhead, starlight in coins and slivers, thick ground mist, faint teal and gold motes drifting between distant trunks, the forest seeming to lean and listen."),
 ("skitch", ["assets/session_08/beat_4/stabby_and_skitch.png"], S+P+" A young scrawny goblin courier boy, green skin, big ears, wide eyes, a satchel of messages, eager and a bit scared. Match the smaller goblin in the reference exactly."),
 ("pikachu", ["assets/session_08/beat_7/pikachu_returns.png"], S+P+" A small friendly electric fox-spirit made of golden light, long ears, lightning-bolt tail, glowing and hopeful. Match the reference exactly."),
 ("poots_glimmergear", ["assets/art_refs/REF_lilly_1.png"], S+P+" A cheerful older deep gnome woman tinkerer, dark slate-gray skin like her daughter in the reference, silver hair in a bun, brass goggles, oil-smudged apron full of tools, warm and clever."),
 ("brynn_wavewarden", [], S+P+" A tall steely-eyed human woman sea-captain in a weathered navy coat with brass buttons, salt-streaked hair tied back, confident and kind."),
 ("maera", [], S+P+" A warm middle-aged human village innkeeper woman, rolled sleeves, apron, dish towel over her shoulder, tired kind eyes."),
 ("s1_eldridge_village", [], S+W+" ELDRIDGE VILLAGE at dusk: a peaceful storybook village in rolling green hills, thatched cottages, chimney smoke, a warm busy tavern with a golden acorn sign, an ancient whispering forest dark on the horizon."),
 ("s2_oakshade_morning", ["assets/scenes/s1_oakshade_twilight.png"], S+W+" OAKSHADE VILLAGE square at golden morning: cottages beneath enormous ancient oaks, the great oak hung with faded ribbons beside a stone well, villagers beginning the day, mist burning off. Match the village look from the reference."),
 ("s2_whispering_glade", ["assets/scenes/s2_elaria_vision.png"], S+W+" THE WHISPERING GLADE by day: a serene mossy clearing with an ancient runestone at its heart, shafts of sunlight, drifting seeds, sacred stillness. Match the glade from the reference."),
 ("s2_mountain_path", ["assets/monsters/terranox.png"], S+W+" A narrow mountain pass of raw rock and glinting crystal veins, cliffs on both sides, the trail winding up toward the light."),
 ("s3_whisperwind_meadow", [], S+W+" WHISPERWIND MEADOW: an endless windswept grass meadow under a huge sky, waves rolling through the grass, ribbons of wind almost visible, one crooked signpost."),
 ("s3_brambleshadow_thicket", ["assets/monsters/shadowflame.png"], S+W+" BRAMBLESHADOW THICKET at twilight: a dense thorny fey woodland, purple dusk light, twisted brambles arching over a narrow path, distant cold blue flickers."),
 ("s3_ironroot_hills", ["assets/monsters/shroomyte_grove.png"], S+W+" THE IRONROOT HILLS: rugged iron-red hills threaded with enormous exposed roots, valleys glowing with bioluminescent mushrooms, the road stitching through."),
 ("s4_havenmoor_town", ["assets/scenes/s3_havenmoor_arrival.png"], S+W+" HAVENMOOR in deep winter: the snow-covered coastal town from above the rooftops, the towering decorated Great Pine in the square, garlands and lanterns, the frozen harbor beyond. Match the town from the reference."),
 ("s4_sugarplum_hearth", [], S+W+" Inside THE SUGARPLUM HEARTH tavern: cozy firelit common room dressed for the winter festival, stockings and garlands, steaming mugs, snow piling at the windows."),
 ("s4_crystalbrook_stream", [], S+W+" THE CRYSTALBROOK STREAM: a half-frozen brook under a frost-slick wooden bridge, black ice creeping unnaturally along the banks, moonlight on snow."),
 ("s5_open_sea", ["assets/scenes/s5_storm.png"], S+W+" The tall ship STORMWIND under full white sail on a bright calm open sea, gulls, sun on the water, the last headland falling behind (the calm before the storm). Match the ship from the reference."),
 ("s5_dutchman_deck", ["assets/scenes/s5_dutchman_rises.png"], S+W+" The deck of the ghostly FLYING DUTCHMAN: barnacled masts, tattered sails, green spectral lanterns, mist coiling over the planks. Eerie, kid-friendly. Match the ship from the reference."),
 ("s6_wraithpine_ridge", ["assets/monsters/gasping_gull.png"], S+W+" First view of WRAITHPINE from the coastal ridge: a fog-pooled hollow of slate roofs and cedar eaves below wind-gnarled pines, lantern light like a braid of ember eyes in the mist. Match the village from the reference."),
 ("s6_old_theater", [], S+W+" THE OLD THEATER of Wraithpine: an abandoned boarded theater looming over the village rooftops in fog, peeling playbills, one dark round window like an eye, jack-o-lanterns glowing in the lane below."),
 ("s6_belltower_square", [], S+W+" BELLSHADOW: the old belltower quarter of a fog-bound village at dusk, the great bronze bell in its weathered tower, crooked lanes, black ribbons on the lantern posts."),
 ("glimmerspire", [], S+W+" GLIMMERSPIRE, deep-gnome academy-city of the Underdark: a vast cavern lit by crystal and brass, tiered workshops spiraling a glowing central spire, forges twinkling like stars."),
 ("bloodthorn_hollow", [], S+W+" BLOODTHORN HOLLOW: a goblin clan-hold woven into a ravine of giant thorny briars, rope bridges, bone-and-banner totems, cookfires glowing, wild and alive, kid-friendly."),
 ("old_shrine", ["assets/world/dark_figure.png"], S+W+" THE OLD SHRINE, far to the east: a ruined ancient shrine to a seven-pointed star half-swallowed by a forgotten glade, broken pillars, moss, one star-shaped aperture glowing faintly at the altar. Mysterious, waiting."),
]
def run(job):
    name, refs, prompt = job
    open("assets/gen_prompts/" + name + ".txt", "w", encoding="utf-8").write(prompt)
    h = {"Authorization": "Bearer " + KEY}
    try:
        if refs:
            fh = [("image[]", (os.path.basename(f), open(f, "rb"), "image/jpeg" if f.endswith(".jpg") else "image/png")) for f in refs]
            r = requests.post("https://api.openai.com/v1/images/edits", headers=h, data={"model": "gpt-image-2", "prompt": prompt, "size": "1024x1024", "quality": "high"}, files=fh, timeout=600)
        else:
            r = requests.post("https://api.openai.com/v1/images/generations", headers=h, json={"model": "gpt-image-2", "prompt": prompt, "size": "1024x1024", "quality": "high"}, timeout=600)
        j = r.json()
        if "data" not in j:
            return name, "ERR " + str(j.get("error", {}).get("message"))[:80]
        open("art_review/PENDING_" + name + ".png", "wb").write(base64.b64decode(j["data"][0]["b64_json"]))
        review_gallery.build()
        return name, "ok"
    except Exception as e:
        return name, "EXC " + str(e)[:80]
print("generating %d images, 5 concurrent" % len(JOBS))
with cf.ThreadPoolExecutor(max_workers=5) as ex:
    for n, st in ex.map(run, JOBS):
        print("  %6s  %s" % (st, n), flush=True)
review_gallery.build()
print("final batch done")
