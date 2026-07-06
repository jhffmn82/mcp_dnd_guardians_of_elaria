# INVENTORY.md — The Guardians of Elaria

> **Note (Phase 2 complete, 2026-07-05):** paths below describe the PRE-reorganization layout and are now historical. For current locations, see `assets/image_manifest.md` (full old-path → new-path mapping) or git history (`git log --follow`).

Phase 1 (read-only) inventory. Generated 2026-07-05. Nothing was moved, renamed, or edited to produce this file; it is a catalog only. Every path is relative to the repo root.

Total files cataloged: 155 (excluding `.git/`).

---

## 1. Headline findings (read these first)

- **Session 6 is located and RESOLVED (DM adjudicated 2026-07-05).** The Wraithpine / False Hydra arc (internal heading "Session 6 — Introduction: Lanterns in the Fog") was misfiled as `Session 7.docx`/`.pdf`. The DM confirmed it was Session 6 only; there was never a Session 7 at the table, and Gearhaven keeps its "Session 8" branding. Files renamed via `git mv` to `Session 6.docx` / `Session 6.pdf`. Played sequence: 1, 2, 3, 4, 5, 6, 8.
- **Session 8 gold standard** = `Session_8_Gearhaven_v2.docx` (with matching `.pdf`). Its per-beat illustrated source docs live under `session 8/`. An older complete draft sits in `session 8/old/`.
- **Heavy duplication** in `Character Sheets/` (multiple `(1)`,`(3)`,`(4)`,`(5)` copies, pre/post-level-4 variants, and zip bundles that re-contain PDFs already present loose). See section 5.
- **Junk / empty:** `Character Sheets/Old blocks/Untitled document.docx` is 0 bytes of body text. Two UUID-named PDFs in `Pictures/` are unclassified. `Pictures/maxresdefault.jpg` looks like a downloaded thumbnail. See section 6.
- **Long DALL-E / ChatGPT prompt filenames:** 10 `DALL·E …` files and 5 `ChatGPT Image …` files carry their generation prompt as the filename. These must be preserved as art prompts in `assets/image_manifest.md` during Phase 2. See section 4.
- **Name/lore drift spotted in passing** (full pass is Phase 3): "Echoes of Elaria" (Session 1 title) vs "Guardians of Elaria"; "Taurus Catchum" (old DALL-E portrait) vs "Ursa Catchum"; "Alaria's Mark" vs "Elaria" inside Session 7.docx. Recorded here only as pointers for CONTRADICTIONS.md later.

---

## 2. Session documents (the campaign spine)

| File | Type | Session | Notes |
|---|---|---|---|
| `Session 1.docx` | session doc | S1 | Eldridge Village, Gilded Acorn Tavern. Internal title "Echoes of Elaria" (title drift). |
| `Session 2.docx` | session doc | S2 | Oakshade Village, Old Oak Tavern, points toward Prof. Aelwyn. |
| `Session 2.pdf` | export | S2 | PDF render of Session 2 (duplicate format of the docx). |
| `Session 3.docx` | session doc | S3 | Ravenstone Laboratory, journey to Havenmoor. Large (8.5 MB, embedded images). |
| `Session 4.docx` | session doc | S4 | "Awakening to Shadows and Songs," Havenmoor, Krampusshade, child abductions. |
| `Session 4 Encounter Tables and Stat Blocks.docx` | session supplement | S4 | d20 travel table + stat blocks. Largest file in repo (46.9 MB). |
| `Session 4 Item Rewards_.docx` | session supplement | S4 | Magic items (e.g. Frostbite Shard Dagger). |
| `Session 5.docx` | session doc | S5 | "The Curse of Davy Jones," Havenmoor harbor, Capt. Brynn Wavewarden, sea voyage. |
| `Session 5 Stat Blocks.docx` | session supplement | S5 | Stat blocks (Drowned Pirate, etc.). Renamed from misspelled "Sesson 5…". |
| `Session 6.docx` | session doc | S6 | Wraithpine, False Hydra, relic chests ("Lanterns in the Fog"). Renamed from `Session 7.docx` per DM ruling (see headline findings). |
| `Session 6.pdf` | export | S6 | PDF render of the above; renamed from `Session 7.pdf`. |
| `Session_8_Gearhaven_v2.docx` | session doc | S8 | **Gold-standard format.** Gearhaven, the Clockwork City. Compiled illustrated adventure. |
| `Session_8_Gearhaven_v2.pdf` | export | S8 | PDF render of the gold-standard Session 8. |

### Session 8 working / source material — `session 8/`

The illustrated per-beat drafts that were compiled into `Session_8_Gearhaven_v2.docx`, plus their art.

| File | Type | Notes |
|---|---|---|
| `session 8/beat 1/Session_8_Beat_1_Illustrated.docx` | S8 beat source | Arrival at Gearhaven. |
| `session 8/beat2/Session_8_Beat_2_Illustrated.docx` | S8 beat source | Market. |
| `session 8/Beat3/Session_8_Beat_3_Illustrated (1).docx` | S8 beat source | Guild interior, Vane. |
| `session 8/Beat4/Session_8_Beat_4_Illustrated (1).docx` | S8 beat source | Descent, VoltCrawler, broodmother. |
| `session 8/Beat5/Session_8_Beat_5_Illustrated (1).docx` | S8 beat source | Corrupted Garden, Grand Custodian, Iron Drudge. |
| `session 8/Beat6/Session_8_Beat_6_Illustrated (1).docx` | S8 beat source | Grand Custodian fight, the core. |
| `session 8/Beat7/Session_8_Beat_7_Illustrated (1).docx` | S8 beat source | The party parts, Pikachu returns. |
| `session 8/beat 1/*.png` (8 images) | art | Through the Gate, burl's cart, city at night, lamplighter, "The team arrives at Gearhaven," sprocket and sons, tavern, wandering streets. |
| `session 8/beat2/*.png` (3 images) | art | Market, cargo hauler, rogue servitor. |
| `session 8/Beat3/*.png` (8 images) | art | Entry, Guild Interior, Vane's Folly, ash's logbook, orerey reacts, quill, sphere reacts motes, ursa's revelation, vane. |
| `session 8/Beat4/*.png` (7 images) | art | VoltCrawler, broodmother, descent, lilly faces the rift, stabby and skitch, the swarm decends [sic], ursa heals skitch. |
| `session 8/Beat5/*.png` (7 images) | art | Corrupted Sproutling, Garden, Garden Corrupted, Grand Custodian, Iron Drudge, + 2 `ChatGPT Image …` long-name files. |
| `session 8/Beat6/*.png` (6 images) | art | Aerial Assault, Grand custodian (x2), Torso, ursa approaches the core, Grand custodiant [sic] in the distance. |
| `session 8/Beat7/*.png` (3 images) | art | pikachu returns, the party parts, vane explains the situation. |

### Handoff documents

| File | Type | Notes |
|---|---|---|
| `session 8/Campaign_Handoff_v2.docx` | handoff | Current: "Post-Polish, Pre-Session 9," July 2026 polish pass. 2024 core + Eberron: Forge of the Artificer. |
| `session 8/Campaign_Handoff_v2.pdf` | handoff export | PDF of the above. |
| `session 8/old/Campaign_and_Session8_Handoff.docx` | handoff (superseded) | Earlier handoff draft. |
| `session 8/old/Session 8 - Gearhaven (Complete).docx` | session doc (superseded) | Older complete Session 8 draft; superseded by `Session_8_Gearhaven_v2.docx`. |
| `session 8/old/Session 8.pdf` | export (superseded) | Old Session 8 PDF. |

---

## 3. Lore / world documents (root + `old stuff/`)

| File | Type | Notes |
|---|---|---|
| `Campaign_Outline_v2.docx` | lore / roadmap | "Guardians of Elaria" roadmap v2. Hub-and-rifts, mote hunt, one-year time skip, star-anchor cosmology, goddess Elaria. Supersedes original outline. |
| `Elaria.docx` | lore | World/villain lore. Introduces Nyxthid, Harbinger of Decay (fallen celestial antagonist). |
| `List of Locations.docx` | lore | Gazetteer: Eldridge Village/Vale and other regions with descriptions. |
| `BackStory and Introduction to the Characters.docx` | lore / characters | Party backstories (e.g. Lilly's Deepforge Hollow / Glimmerspire Academy origin). |
| `Pokemon Encounters.docx` | lore / bestiary | Chronological list of Pokemon-style creatures per session (Cognifin, Lickgloom, Duckleaf…). |
| `old stuff/Blossomflare.docx` | lore / statblock | Blossomflare, the Floraburst evolution (CR 3 magical beast statblock). |
| `Character Sheets/Untitled folder/Outline.docx` | lore / roadmap (old) | Original per-session plan (S4 Christmas one-shot, S5 Gearhaven, S6 = *Elemental Plane of Earth*, S7 …). Diverges from what was actually played; superseded by `Campaign_Outline_v2.docx`. |
| `Character Sheets/Old blocks/Untitled document(1).docx` | lore / statblock | Floraburst "Spectral Blossom" statblock (pre-evolution form). |

---

## 4. Images with long DALL-E / ChatGPT prompt filenames

These filenames ARE the generation prompts and must be preserved verbatim in `assets/image_manifest.md` when renamed in Phase 2.

### DALL·E files (`Pictures/`)
1. `DALL·E 2024-10-20 21.53.42 - A detailed fantasy map for a DnD campaign … five regions_ Eldridge Vale, Oakshad….pdf` — campaign map.
2. `DALL·E 2024-10-21 21.02.34 - … Lilly Glimmergear … holding an Essence Sphere ….webp`
3. `DALL·E 2024-10-21 21.02.55 - … Taurus Catchum … holding one enchanted potato ….webp` (note old name "Taurus").
4. `DALL·E 2024-10-21 21.11.05 - … Professor Aelwyn Ravenstone … high elf wizard ….webp`
5. `DALL·E 2024-10-21 21.12.29 - … Ravenstone Laboratory ….webp`
6. `DALL·E 2024-11-08 17.53.29 - … Stabby Sharpblade … goblin monk … twilight forest ….webp`
7. `DALL·E 2024-11-08 18.04.14 - … Ursa … human druid … celestial dragon mark ….webp`
8. `DALL·E 2024-11-08 21.30.11 - … Lilly … svirfneblin (deep gnome) ….webp`
9. `DALL·E 2024-11-08 21.38.30 - … Ursa … human druid … no pointed ears ….webp`
10. `DALL·E 2024-11-08 21.42.23 - … Stabby … goblin monk … sharp teeth ….webp`

### ChatGPT Image files (timestamp-only names, source content unclear)
- `Character Sheets/path rewards/old/ChatGPT Image Jun 15, 2026, 09_04_16 PM.png`
- `Character Sheets/path rewards/old/ChatGPT Image Jun 15, 2026, 09_06_57 PM.png`
- `Character Sheets/path rewards/old/ChatGPT Image Jun 15, 2026, 09_24_08 PM.png`
- `session 8/Beat5/ChatGPT Image Jun 13, 2026, 11_38_36 AM.png`
- `session 8/Beat5/ChatGPT Image Jun 13, 2026, 11_38_43 AM.png`

### Other art (`Pictures/`) — short descriptive names, character/scene illustrations
Symbols: `Artifice Academy Symbol.png`, `Circle of the Eternal Stars Symbol.png`.
Party & scenes: `Lilly.png`, `Lilly5.png`, `lilly2.png`, `lilly4.png`, `lilly holding the sphere.png`, `lilly opening chest..png`, `lilly vs zombies.png`, `lilly-session4.png`, `Stabby.png`, `Stabby2.png`, `stabby4.jpg`, `stabby5.png`, `stabby-cane.png`, `stabby with sash.png`, `stabby with stash..png`, `staby vs strawlings.png` [sic], `URSA2.png`, `ursa3.png`, `ursa4.png`, `ursa5.jpg`, `ursa6.png`, `ursa7.png`, `ursa with staff.png`, `ursa with staff (2).png`, `Ursa vs rats.png`, `ghostbloom.png`, `ghostbloom vs hyrda head.png` [sic].
Monsters/factions: `False Hydra.png`, `Gasping Gull.png`, `Grimfang Clan.png`, `Eldrich-cannon-artificer-robot-SLA-Painted-Back.jpg`.

---

## 5. Character sheets & path rewards — `Character Sheets/`

### Current (v3) — likely canonical
| File | Character |
|---|---|
| `Character Sheets/Lilly_Glimmergear_Sheet_v3.pdf` | Lilly |
| `Character Sheets/Stabby_Sharpblade_Sheet_v3.pdf` | Stabby |
| `Character Sheets/Ursa_Catchum_Sheet_v3.pdf` | Ursa |
| `Character Sheets/Ghostbloom_5e_Statblock_v3.pdf` | Ghostbloom (party companion creature) |

### Path rewards (level-7 timeskip material)
| File | Notes |
|---|---|
| `Character Sheets/path rewards/Glimmerstone_Artifacts_v2 (4).pdf` | Lilly's artifacts (current v2). |
| `Character Sheets/path rewards/Ursa_Path_Rewards_v2 (5).pdf` | Ursa's path rewards (current v2; includes "Warden" constellation per CLAUDE.md). |
| `Character Sheets/path rewards/Warrior_of_Breathing_v2.pdf` | Stabby's path reward (current v2). |

### Duplicates / superseded (candidates for `_triage/` in Phase 2 — flag, do not delete)
- **`Character Sheets/Old blocks/`** — earlier character-sheet generations: `Lilly_Glimmergear_Sheet.pdf`, `…(4).pdf`, `…(5).pdf`; `Stabby_Sharpblade_Sheet.pdf`, `…(3).pdf`; `Ursa_Catchum_Sheet.pdf`, `…(1).pdf`; `Ghostbloom_5e_Statblock.docx` + `.pdf`; plus large art-heavy variants `lilly glimmergear.pdf / pre 4 / post 4 / 5`, `stabby sharpblade.pdf / pre 4 / post 4`, `ursa.pdf / pre 4 / post 4 / 5`. These pre/post-4 and numbered copies are older versions of the v3 sheets.
- **`Character Sheets/path rewards/old/`** — superseded reward drafts: `Lilly_Path_Rewards.pdf`, `Ursa_Path_Feats.pdf`, `Ursa_Catchum_Sheet_v3.pdf` (duplicate of the one in `Character Sheets/`, byte-identical size 1,187,542), `Warrior_of_Breathing (3).pdf`, subclass drafts `Beast_Breathing_Subclass.pdf`, `Shadow_Breathing_Subclass.pdf`, `Water_Breathing_Subclass.pdf`, `Beast_Breathing`… , plus art `awakened essesne sphere.png` [sic], `boomstick.png`, `upgraded eldritch cannon.png`, and the three `ChatGPT Image …` files (section 4).
- **Zip bundles** (contents overlap loose files already present):
  - `Character Sheets/Old blocks/DnD_Sheets_Bundle_claude starter.zip` → `build_lilly.py`, `build_stabby.py`, `build_ursa.py`, `lilly_new.png`, `stabby_new.png`, `ursa_new.png`, `README.md` (sheet-generation scripts).
  - `Character Sheets/files (2).zip` → Lilly/Stabby/Ursa PDFs + 3 build_*.py scripts.
  - `Character Sheets/files (3).zip` → the 3 breathing-subclass PDFs.

---

## 6. Junk, empty, and unclassifiable

| File | Issue |
|---|---|
| `Character Sheets/Old blocks/Untitled document.docx` | **Empty** (0 chars of body text). Junk candidate. |
| `Pictures/63daf756-11ee-480d-b9b9-1345d5c3a203.pdf` | UUID filename, contents not yet identified. Needs a look in Phase 2. |
| `Pictures/c89b2c28-229f-4447-84cf-14025bc42e40.pdf` | UUID filename, contents not yet identified. |
| `Pictures/maxresdefault.jpg` | Generic name (typical YouTube-thumbnail filename); likely a downloaded reference image, not original campaign art. Verify/triage. |
| `Character Sheets/Untitled folder/` , `Character Sheets/Old blocks/` , `session 8/old/` , `old stuff/` | Loosely named holding folders; their contents are classified above. Consolidate in Phase 2. |

---

## 7. Referenced-but-missing / flags for DM (F#)

- **F1 — RESOLVED (2026-07-05).** DM ruled: Wraithpine was Session 6 only; no Session 7 was ever played; Gearhaven keeps its "Session 8" number. Files renamed accordingly. Do not flag the 6-to-8 gap as a contradiction.
- **F2 — RESOLVED with F1.** Nothing is missing between the sea voyage (S5) and Gearhaven (S8) beyond the Wraithpine arc.
- **F3 — Campaign title drift.** Session 1 internal title is "Echoes of Elaria"; everything later is "The Guardians of Elaria." (Phase 3 canon item.)
- **F4 — Character name drift.** DALL-E portrait names Ursa as "Taurus Catchum." Session 7.docx spells the goddess "Alaria" in one place vs "Elaria." (Phase 3 canon items.)
- **F5 — `memory/` folder does not exist yet.** CLAUDE.md calls for `memory/campaign_canon.md`, `memory/session_log.md`, `memory/house_rules.md`. Deferred to Phase 2/3 (Phase 1 is read-only apart from this inventory); noting so it is not forgotten.
- **F6 — Filename typos to fix on rename** (Phase 2; `Sesson 5` already fixed): `staby vs strawlings.png`, `ghostbloom vs hyrda head.png`, `the swarm decends.png`, `Grand custodiant in the distance.png`, `awakened essesne sphere.png`, `lilly opening chest..png` / `stabby with stash..png` (double dot).

---

## 8. Suggested Phase 2 target mapping (preview, not executed)

- `sessions/` ← `Session 1.docx` … `Session 6.docx` (`session_06_wraithpine.docx`), `Session_8_Gearhaven_v2.docx`, session supplements, PDFs. There is no session 7 (DM ruling).
- `lore/` ← `Campaign_Outline_v2.docx`, `Elaria.docx`, `List of Locations.docx`, `BackStory…docx`, `Pokemon Encounters.docx`, `Blossomflare.docx`, statblocks.
- `characters/` ← v3 sheets + `path rewards/` current v2 files.
- `assets/` ← everything in `Pictures/` and `session 8/**/*.png`; create `assets/image_manifest.md` capturing every DALL-E/ChatGPT long filename as its art prompt.
- `handoffs/` ← `Campaign_Handoff_v2.docx/.pdf`.
- `templates/` ← (Phase 4) extracted from Session 8.
- `_triage/` ← `Old blocks/`, `path rewards/old/`, `session 8/old/`, empty `Untitled document.docx`, UUID PDFs, `maxresdefault.jpg`, zip bundles.
- `memory/` ← create per F5.

*End of Phase 1 inventory. No files were altered. Awaiting DM go-ahead for Phase 2 (reorganization plan).*
