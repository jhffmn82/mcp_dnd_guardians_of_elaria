# Phase 2 reorganization driver. git mv every file per the approved plan,
# then emit the raw mapping data for assets/image_manifest.md.
import os, subprocess, sys, json

ROOT = r"C:\Users\jhffm\dnd-campaign"
os.chdir(ROOT)

def listdir(p):
    return os.listdir(os.path.join(ROOT, p))

# Resolve exact DALL-E filenames from disk by unique timestamp prefix.
def resolve(folder, prefix):
    hits = [f for f in listdir(folder) if f.startswith(prefix)]
    assert len(hits) == 1, f"prefix {prefix!r} matched {hits}"
    return folder + "/" + hits[0]

M = []  # (src, dst, note)
def mv(src, dst, note=""):
    M.append((src, dst, note))

# ---------------- sessions ----------------
mv("Session 1.docx", "sessions/session_01_gathering_of_friends.docx")
mv("Session 2.docx", "sessions/session_02_oakshade_village.docx")
mv("Session 2.pdf",  "sessions/session_02_oakshade_village.pdf")
mv("Session 3.docx", "sessions/session_03_quest_for_knowledge.docx")
mv("Session 4.docx", "sessions/session_04_shadows_and_songs.docx")
mv("Session 4 Encounter Tables and Stat Blocks.docx", "sessions/session_04_encounter_tables_and_stat_blocks.docx")
mv("Session 4 Item Rewards_.docx", "sessions/session_04_item_rewards.docx")
mv("Session 5.docx", "sessions/session_05_curse_of_davy_jones.docx")
mv("Session 5 Stat Blocks.docx", "sessions/session_05_stat_blocks.docx")
mv("Session 6.docx", "sessions/session_06_wraithpine.docx")
mv("Session 6.pdf",  "sessions/session_06_wraithpine.pdf")
mv("Session_8_Gearhaven_v2.docx", "sessions/session_08_gearhaven.docx")
mv("Session_8_Gearhaven_v2.pdf",  "sessions/session_08_gearhaven.pdf")

# ---------------- lore ----------------
mv("Campaign_Outline_v2.docx", "lore/campaign_outline_v2.docx")
mv("Elaria.docx", "lore/elaria_and_nyxthid.docx")
mv("List of Locations.docx", "lore/locations.docx")
mv("BackStory and Introduction to the Characters.docx", "lore/character_backstories.docx")
mv("Pokemon Encounters.docx", "lore/pokemon_encounters.docx")
mv("old stuff/Blossomflare.docx", "lore/blossomflare_statblock.docx")
mv("Character Sheets/Old blocks/Untitled document(1).docx", "lore/floraburst_statblock.docx")

# ---------------- characters (current) ----------------
mv("Character Sheets/Lilly_Glimmergear_Sheet_v3.pdf", "characters/lilly_glimmergear_sheet_v3.pdf")
mv("Character Sheets/Stabby_Sharpblade_Sheet_v3.pdf", "characters/stabby_sharpblade_sheet_v3.pdf")
mv("Character Sheets/Ursa_Catchum_Sheet_v3.pdf", "characters/ursa_catchum_sheet_v3.pdf")
mv("Character Sheets/Ghostbloom_5e_Statblock_v3.pdf", "characters/ghostbloom_statblock_v3.pdf")
mv("Character Sheets/path rewards/Glimmerstone_Artifacts_v2 (4).pdf", "characters/path_rewards/glimmerstone_artifacts_v2.pdf")
mv("Character Sheets/path rewards/Ursa_Path_Rewards_v2 (5).pdf", "characters/path_rewards/ursa_path_rewards_v2.pdf")
mv("Character Sheets/path rewards/Warrior_of_Breathing_v2.pdf", "characters/path_rewards/warrior_of_breathing_v2.pdf")

# ---------------- characters (historical snapshots, chronicle material) ----------------
OB = "Character Sheets/Old blocks"
mv(f"{OB}/lilly glimmergear.pdf",        "characters/historical/lilly_original.pdf")
mv(f"{OB}/lilly glimmergear pre 4.pdf",  "characters/historical/lilly_pre_session_4.pdf")
mv(f"{OB}/lilly glimmergear post 4.pdf", "characters/historical/lilly_post_session_4.pdf")
mv(f"{OB}/lilly glimmergear5.pdf",       "characters/historical/lilly_5.pdf")
mv(f"{OB}/stabby sharpblade.pdf",        "characters/historical/stabby_original.pdf")
mv(f"{OB}/stabby sharpblade pre 4.pdf",  "characters/historical/stabby_pre_session_4.pdf")
mv(f"{OB}/stabby sharpblade post 4.pdf", "characters/historical/stabby_post_session_4.pdf")
mv(f"{OB}/ursa.pdf",                     "characters/historical/ursa_original.pdf")
mv(f"{OB}/ursa pre 4.pdf",               "characters/historical/ursa_pre_session_4.pdf")
mv(f"{OB}/ursa  post 4.pdf",             "characters/historical/ursa_post_session_4.pdf")
mv(f"{OB}/ursa5.pdf",                    "characters/historical/ursa_5.pdf")
mv(f"{OB}/Ghostbloom_5e_Statblock.docx", "characters/historical/ghostbloom_statblock_v1.docx")
mv(f"{OB}/Ghostbloom_5e_Statblock.pdf",  "characters/historical/ghostbloom_statblock_v1.pdf")

# ---------------- _triage: duplicates, zips, superseded ----------------
for f in ["Lilly_Glimmergear_Sheet.pdf", "Lilly_Glimmergear_Sheet (4).pdf", "Lilly_Glimmergear_Sheet (5).pdf",
          "Stabby_Sharpblade_Sheet.pdf", "Stabby_Sharpblade_Sheet (3).pdf",
          "Ursa_Catchum_Sheet.pdf", "Ursa_Catchum_Sheet (1).pdf"]:
    mv(f"{OB}/{f}", f"_triage/duplicate_sheets/{f}")
mv(f"{OB}/DnD_Sheets_Bundle_claude starter.zip", "_triage/zips/DnD_Sheets_Bundle_claude starter.zip")
mv("Character Sheets/files (2).zip", "_triage/zips/files (2).zip")
mv("Character Sheets/files (3).zip", "_triage/zips/files (3).zip")
mv(f"{OB}/Untitled document.docx", "_triage/empty_untitled_document.docx", "empty file")
mv("Character Sheets/Untitled folder/Outline.docx", "_triage/campaign_outline_v1.docx", "superseded by lore/campaign_outline_v2.docx")

PRO = "Character Sheets/path rewards/old"
for f in ["Beast_Breathing_Subclass.pdf", "Shadow_Breathing_Subclass.pdf", "Water_Breathing_Subclass.pdf",
          "Lilly_Path_Rewards.pdf", "Ursa_Path_Feats.pdf", "Warrior_of_Breathing (3).pdf", "Ursa_Catchum_Sheet_v3.pdf"]:
    mv(f"{PRO}/{f}", f"_triage/path_rewards_old/{f}")

# path-reward art stays live in assets
mv(f"{PRO}/awakened essesne sphere.png", "assets/items/awakened_essence_sphere.png", "filename typo fixed")
mv(f"{PRO}/boomstick.png", "assets/items/boomstick.png")
mv(f"{PRO}/upgraded eldritch cannon.png", "assets/items/upgraded_eldritch_cannon.png")
mv(resolve(PRO, "ChatGPT Image Jun 15, 2026, 09_04_16"), "assets/characters/stabby_breathing_style_red.png", "Stabby path-reward art, red/crimson breathing style (likely Beast Breathing)")
mv(resolve(PRO, "ChatGPT Image Jun 15, 2026, 09_06_57"), "assets/characters/stabby_breathing_style_water.png", "Stabby path-reward art, Water Breathing")
mv(resolve(PRO, "ChatGPT Image Jun 15, 2026, 09_24_08"), "assets/characters/stabby_breathing_style_shadow.png", "Stabby path-reward art, Shadow Breathing")

# ---------------- Pictures -> assets ----------------
P = "Pictures"
mv(resolve(P, "DALL·E 2024-10-20 21.53.42"), "assets/world/elaria_region_map.pdf", "DALL-E prompt preserved as original filename")
mv(f"{P}/Artifice Academy Symbol.png", "assets/world/artifice_academy_symbol.png")
mv(f"{P}/Circle of the Eternal Stars Symbol.png", "assets/world/circle_of_the_eternal_stars_symbol.png")

mv(resolve(P, "DALL·E 2024-10-21 21.02.34"), "assets/characters/lilly_with_essence_sphere_dalle.webp", "DALL-E prompt preserved")
mv(resolve(P, "DALL·E 2024-10-21 21.02.55"), "assets/characters/ursa_with_potato_dalle.webp", "DALL-E prompt preserved; character named 'Taurus Catchum' in prompt, early name for Ursa")
mv(resolve(P, "DALL·E 2024-11-08 21.30.11"), "assets/characters/lilly_portrait_dalle.webp", "DALL-E prompt preserved")
mv(resolve(P, "DALL·E 2024-11-08 21.38.30"), "assets/characters/ursa_portrait_dalle.webp", "DALL-E prompt preserved")
mv(resolve(P, "DALL·E 2024-11-08 21.42.23"), "assets/characters/stabby_portrait_dalle.webp", "DALL-E prompt preserved")
mv(resolve(P, "DALL·E 2024-11-08 17.53.29"), "assets/scenes/stabby_twilight_forest_dalle.webp", "DALL-E prompt preserved")
mv(resolve(P, "DALL·E 2024-11-08 18.04.14"), "assets/characters/ursa_celestial_mark_dalle.webp", "DALL-E prompt preserved")
mv(resolve(P, "DALL·E 2024-10-21 21.11.05"), "assets/npcs/professor_aelwyn_dalle.webp", "DALL-E prompt preserved")
mv(resolve(P, "DALL·E 2024-10-21 21.12.29"), "assets/npcs/ravenstone_laboratory_dalle.webp", "DALL-E prompt preserved")

mv(f"{P}/63daf756-11ee-480d-b9b9-1345d5c3a203.pdf", "assets/characters/lilly_original_concept.pdf", "identified: original Lilly concept sheet (browser-saved PDF, Oct 2024)")
mv(f"{P}/c89b2c28-229f-4447-84cf-14025bc42e40.pdf", "assets/characters/stabby_original_concept.pdf", "identified: original Stabby concept portrait (browser-saved PDF, Oct 2024)")

for src, dst in [
    ("Lilly.png","lilly.png"), ("lilly2.png","lilly2.png"), ("lilly4.png","lilly4.png"), ("Lilly5.png","lilly5.png"),
    ("lilly-session4.png","lilly_session4.png"), ("lilly holding the sphere.png","lilly_holding_the_sphere.png"),
    ("Stabby.png","stabby.png"), ("Stabby2.png","stabby2.png"), ("stabby4.jpg","stabby4.jpg"), ("stabby5.png","stabby5.png"),
    ("stabby-cane.png","stabby_cane.png"), ("stabby with sash.png","stabby_with_sash.png"),
    ("URSA2.png","ursa2.png"), ("ursa3.png","ursa3.png"), ("ursa4.png","ursa4.png"), ("ursa5.jpg","ursa5.jpg"),
    ("ursa6.png","ursa6.png"), ("ursa7.png","ursa7.png"),
    ("ursa with staff.png","ursa_with_staff.png"), ("ursa with staff (2).png","ursa_with_staff_2.png"),
    ("ghostbloom.png","ghostbloom.png"),
]:
    mv(f"{P}/{src}", f"assets/characters/{dst}")
mv(f"{P}/stabby with stash..png", "assets/characters/stabby_with_sash_2.png", "filename typo 'stash..' fixed")

for src, dst in [
    ("lilly opening chest..png","lilly_opening_chest.png"), ("lilly vs zombies.png","lilly_vs_zombies.png"),
    ("Ursa vs rats.png","ursa_vs_rats.png"),
]:
    mv(f"{P}/{src}", f"assets/scenes/{dst}")
mv(f"{P}/staby vs strawlings.png", "assets/scenes/stabby_vs_strawlings.png", "filename typo 'staby' fixed")
mv(f"{P}/ghostbloom vs hyrda head.png", "assets/scenes/ghostbloom_vs_hydra_head.png", "filename typo 'hyrda' fixed")

for src, dst in [("False Hydra.png","false_hydra.png"), ("Gasping Gull.png","gasping_gull.png"), ("Grimfang Clan.png","grimfang_clan.png")]:
    mv(f"{P}/{src}", f"assets/monsters/{dst}")

mv(f"{P}/Eldrich-cannon-artificer-robot-SLA-Painted-Back.jpg", "_triage/reference_images/eldritch_cannon_mini_reference.jpg", "third-party reference photo of a painted mini")
mv(f"{P}/maxresdefault.jpg", "_triage/reference_images/false_hydra_lullaby_youtube_thumbnail.jpg", "third-party YouTube thumbnail, Session 6 inspiration")

# ---------------- session 8 folder ----------------
mv("session 8/Campaign_Handoff_v2.docx", "handoffs/campaign_handoff_v2.docx")
mv("session 8/Campaign_Handoff_v2.pdf",  "handoffs/campaign_handoff_v2.pdf")
mv("session 8/old/Campaign_and_Session8_Handoff.docx", "_triage/session_08_old/Campaign_and_Session8_Handoff.docx")
mv("session 8/old/Session 8 - Gearhaven (Complete).docx", "_triage/session_08_old/Session 8 - Gearhaven (Complete).docx")
mv("session 8/old/Session 8.pdf", "_triage/session_08_old/Session 8.pdf")

mv("session 8/beat 1/Session_8_Beat_1_Illustrated.docx", "_triage/session_08_beat_drafts/session_8_beat_1_illustrated.docx")
mv("session 8/beat2/Session_8_Beat_2_Illustrated.docx",  "_triage/session_08_beat_drafts/session_8_beat_2_illustrated.docx")
for n in range(3, 8):
    mv(f"session 8/Beat{n}/Session_8_Beat_{n}_Illustrated (1).docx", f"_triage/session_08_beat_drafts/session_8_beat_{n}_illustrated.docx")

S8 = [
    ("session 8/beat 1", "beat_1", [("Through the Gate.png","through_the_gate.png"), ("burl's cart.png","burls_cart.png"),
        ("city at night.png","city_at_night.png"), ("lamplighter.png","lamplighter.png"),
        ("session8 - The team arrives at Gearhaven.png","team_arrives_at_gearhaven.png"),
        ("sprocket and sons.png","sprocket_and_sons.png"), ("tavern.png","tavern.png"), ("wandering streets.png","wandering_streets.png")]),
    ("session 8/beat2", "beat_2", [("Market.png","market.png"), ("cargo hauler.png","cargo_hauler.png"), ("rogue servitor.png","rogue_servitor.png")]),
    ("session 8/Beat3", "beat_3", [("Entry.png","entry.png"), ("Guild Interior.png","guild_interior.png"), ("Vane's Folly.png","vanes_folly.png"),
        ("ash's logbook.png","ashs_logbook.png"), ("orerey reacts.png","orrery_reacts.png"), ("quill.png","quill.png"),
        ("sphere reacts motes.png","sphere_reacts_motes.png"), ("ursa's revelation.png","ursas_revelation.png"), ("vane.png","vane.png")]),
    ("session 8/Beat4", "beat_4", [("VoltCrawler.png","volt_crawler.png"), ("broodmother.png","broodmother.png"), ("descent.png","descent.png"),
        ("lilly faces the rift.png","lilly_faces_the_rift.png"), ("stabby and skitch.png","stabby_and_skitch.png"),
        ("the swarm decends.png","the_swarm_descends.png"), ("ursa heals skitch.png","ursa_heals_skitch.png")]),
    ("session 8/Beat5", "beat_5", [("Corrupted Sproutling.png","corrupted_sproutling.png"), ("Garden Corrupted.png","garden_corrupted.png"),
        ("Garden.png","garden.png"), ("Grand Custodian.png","grand_custodian.png"), ("Iron Drudge.png","iron_drudge.png")]),
    ("session 8/Beat6", "beat_6", [("Aerial Assault.png","aerial_assault.png"), ("Grand custodiant in the distance.png","grand_custodian_in_the_distance.png"),
        ("Torso.png","torso.png"), ("grand custodian.png","grand_custodian.png"), ("ursa approaches the core.png","ursa_approaches_the_core.png")]),
    ("session 8/Beat7", "beat_7", [("pikachu returns.png","pikachu_returns.png"), ("the party parts.png","the_party_parts.png"),
        ("vane explains the situation.png","vane_explains_the_situation.png")]),
]
for folder, beat, files in S8:
    for src, dst in files:
        mv(f"{folder}/{src}", f"assets/session_08/{beat}/{dst}")
mv(resolve("session 8/Beat5", "ChatGPT Image Jun 13, 2026, 11_38_36"), "assets/session_08/beat_5/lilly_garden_meeting.png", "identified: Lilly meets an elderly artificer in the Custodian's Garden")
mv(resolve("session 8/Beat5", "ChatGPT Image Jun 13, 2026, 11_38_43"), "assets/session_08/beat_5/lilly_at_clockwork_fountain.png", "identified: Lilly channels energy at the clockwork fountain")

# ---------------- execute ----------------
dirs = sorted({os.path.dirname(d) for _, d, _ in M})
for d in dirs:
    os.makedirs(os.path.join(ROOT, d), exist_ok=True)

errors = []
for src, dst, _ in M:
    r = subprocess.run(["git", "mv", src, dst], capture_output=True, text=True)
    if r.returncode != 0:
        errors.append((src, dst, r.stderr.strip()))

print(f"moves attempted: {len(M)}, errors: {len(errors)}")
for e in errors:
    print("ERR:", e)

# dump mapping for manifest generation
with open(os.path.join(ROOT, "_reorg_mapping.json"), "w", encoding="utf-8") as f:
    json.dump(M, f, ensure_ascii=False, indent=1)
