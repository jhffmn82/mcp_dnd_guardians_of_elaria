import base64, os, sys, concurrent.futures as cf, requests
os.chdir(r"C:/Users/jhffm/dnd-campaign"); sys.path.insert(0,"templates"); import review_gallery
KEY=open(os.path.expanduser("~/.openai_key")).read().strip()
S="painterly storybook fantasy illustration, lush warm golden palette with teal and brass accents, soft volumetric light, detailed fantasy-anime glow, richly rendered digital painting, no text or lettering anywhere."
PORTRAIT=" A clean solo portrait, the single subject centered on a soft neutral parchment-toned background (not a busy scene)."
def frm(ref): return " Match the subject's design to the attached reference image exactly."

# name, dest, refs[], prompt
JOBS = [
 ("lickgloom","monsters",["assets/scenes/s1_lickgloom_pond.png"], S+PORTRAIT+" A small round Feywild creature the size of a halfling with shimmering skin, huge innocent eyes and a very long prehensile tongue, curious and playful."+frm(1)),
 ("mist_stalker","monsters",["assets/scenes/s1_mist_stalkers.png"], S+PORTRAIT+" A sleek shadowy fey predator made of fog and hunger, with pale glowing eyes, prowling low, wreathed in mist. Spooky but kid-friendly."+frm(1)),
 ("mudskip","monsters",["assets/scenes/s2_mudskip_ambush.png"], S+PORTRAIT+" A slick little salamander-and-fish water elemental creature, glistening, dripping, with big eyes."+frm(1)),
 ("displacer_beast","monsters",["assets/scenes/s3_displacer_beasts.png"], S+PORTRAIT+" A sleek six-legged panther-like beast with two long back-tentacles, cunning glowing eyes."+frm(1)),
 ("enchanted_snowman","monsters",[], S+PORTRAIT+" A living enchanted snowman with coal eyes and stick arms, faintly menacing but whimsical, in a wintry glow."),
 ("ice_spider","monsters",[], S+PORTRAIT+" A crystalline spider made of blue ice, faceted and glittering, sharp legs, cold mist rising."),
 ("drowned_pirate","monsters",["assets/scenes/s5_hold_of_essences.png"], S+PORTRAIT+" A barnacle-crusted undead pirate sailor, seaweed-draped, hollow glowing eyes, tattered coat. Spooky-fun, not gory."+frm(1)),
 ("spectral_helmsman","monsters",["assets/scenes/s5_dutchman_rises.png"], S+PORTRAIT+" A translucent green ghost sailor gripping a ship's wheel, spectral and mournful."+frm(1)),
 ("smugglers_golem","monsters",[], S+PORTRAIT+" A lumbering construct built of ship crates, barrels, chains and salvaged brass, glowing seams, hulking."),
 ("arcane_corsair","monsters",[], S+PORTRAIT+" A pirate-artificer in a weathered coat with brass arcane gauntlets and a spark-pistol, roguish and dangerous."),
 ("ghost_light_engineer","monsters",[], S+PORTRAIT+" A tiny hunched undead engineer-sprite crackling with pale ghost-light, holding glowing tools, eerie."),
 ("false_hydra_body","monsters",["assets/scenes/s6_hydra_lair.png"], S+PORTRAIT+" A huge pale sickly-white many-necked eyeless aberration, four long necks with toothy inhuman maws, NO faces. Storybook-eerie, no gore."+frm(1)),
 ("false_hydra_head","monsters",["assets/monsters/false_hydra.png"], S+PORTRAIT+" A single pale eyeless long-necked head of the False Hydra, a lamprey ring of needle teeth, NO human face. Eerie, no gore."+frm(1)),
 ("scarecrow","monsters",["assets/scenes/s6_pumpkin_row.png"], S+PORTRAIT+" An animated harvest scarecrow, burlap head with stitched grin, straw spilling from tattered clothes, a jack-o-lantern nearby. Spooky-fun."+frm(1)),
 ("strawling","monsters",["assets/scenes/s6_pumpkin_row.png"], S+PORTRAIT+" A small scuttling animate creature of bundled straw and thorny vine with glowing pumpkin-light eyes, knee-high. Spooky-cute."+frm(1)),
 # relic items
 ("staff_of_waking_constellations","items",["assets/characters/ursa_with_staff_2.png"], S+" A single magic item on a soft dark velvet background: a wooden druid quarterstaff etched with glowing blue constellations, a radiant star at its crest, wisps of starlight. Ornate, precious, like a museum relic plate."+frm(1)),
 ("sash_of_the_swift_current","items",["assets/characters/stabby_with_sash.png"], S+" A single magic item on soft dark velvet: a shimmering crimson silk sash rippling as if in wind, embroidered with a seven-point star cupped by wings. Precious relic plate."+frm(1)),
 ("essence_sphere","items",["assets/characters/lilly_holding_the_sphere.png"], S+" A single magic item on soft dark velvet: a brass-and-crystal orb the size of a fist, gears within, glowing with a warm golden spark inside. Steampunk relic plate."+frm(1)),
 ("wraithpine_chest","items",["assets/scenes/s6_chest_opening.png"], S+" A single object on a dark ground: a half-buried treasure chest bound in vines of silver and living root, seams leaking soft golden light, a seven-point star on the lid. Relic plate."+frm(1)),
 # character portraits
 ("ash_catchum","npcs",[], S+PORTRAIT+" A grown human wildfire druid man in his 40s, tousled auburn/red hair and beard, kind weathered face, green-and-amber druid robes with ember motifs, a faint seven-point star token; the lost father of a red-haired boy. Warm, heroic, a little haunted."),
 ("skitch","npcs",["assets/session_08/beat_4/stabby_and_skitch.png"], S+PORTRAIT+" A young scrawny goblin courier boy, green skin, big ears, wide eyes, a satchel of messages, eager and a bit scared."+frm(1)),
 ("pikachu","npcs",["assets/session_08/beat_7/pikachu_returns.png"], S+PORTRAIT+" A small friendly electric fox-spirit made of golden light, long ears and a lightning-bolt tail, glowing and hopeful (the spark inside the Essence Sphere)."+frm(1)),
 ("poots_glimmergear","npcs",[], S+PORTRAIT+" A cheerful older deep gnome woman tinkerer, dark slate-gray skin, silver hair in a bun, brass goggles, oil-smudged apron full of tools, warm and clever (Lilly's mother)."),
 ("brynn_wavewarden","npcs",[], S+PORTRAIT+" A tall steely-eyed human woman sea-captain in a weathered navy coat with brass buttons, salt-streaked hair tied back, confident and kind."),
 ("maera","npcs",[], S+PORTRAIT+" A warm middle-aged human village innkeeper woman with rolled sleeves and an apron, tired kind eyes, a dish towel over her shoulder."),
]
def run(job):
    name,dest,refs,prompt=job
    open(f"assets/gen_prompts/{name}.txt","w",encoding="utf-8").write(prompt)
    h={"Authorization":f"Bearer {KEY}"}
    try:
        if refs:
            fh=[("image[]",(os.path.basename(f),open(f,"rb"),"image/jpeg" if f.endswith(".jpg") else "image/png")) for f in refs]
            r=requests.post("https://api.openai.com/v1/images/edits",headers=h,data={"model":"gpt-image-2","prompt":prompt,"size":"1024x1024","quality":"high"},files=fh,timeout=600)
        else:
            r=requests.post("https://api.openai.com/v1/images/generations",headers=h,json={"model":"gpt-image-2","prompt":prompt,"size":"1024x1024","quality":"high"},timeout=600)
        j=r.json()
        if "data" not in j: return name,"ERR "+str(j.get("error",{}).get("message"))[:90]
        open(f"art_review/PENDING_{name}.png","wb").write(base64.b64decode(j["data"][0]["b64_json"]))
        review_gallery.build(); return name,"ok"
    except Exception as e: return name,"EXC "+str(e)[:90]
if __name__=="__main__":
    print(f"generating {len(JOBS)} gap images, 5 concurrent")
    with cf.ThreadPoolExecutor(max_workers=5) as ex:
        for n,s2 in ex.map(run,JOBS): print(f"  {s2:>6}  {n}",flush=True)
    review_gallery.build(); print("gap batch done")
