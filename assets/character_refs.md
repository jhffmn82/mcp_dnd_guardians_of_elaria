# Character Reference Registry

The canonical look of every significant, recurring character. Whenever art featuring one of these characters is generated or regenerated, ATTACH their reference file(s) from `assets/art_refs/` so they stay consistent across the whole book. Heroes use era-split refs (see `art_production_guide.md`); everyone else has a single canonical portrait.

## Standing design rules (DM ruling 2026-08-17, applies to all art from here on)

These must be stated in every prompt as explicit negatives. Reference images alone will not enforce them: the generator copies jewelry it sees in the refs, so the older refs actively work against these rules and the prompt has to override them.

- **Earrings.** Lilly wears exactly ONE small earring, on one ear only, and her other ear is bare. Stabby and Ursa wear NONE: both ears completely bare, no rings, hoops, studs, cuffs, or dangling charms. Every hero ref generated before 2026-08-17 has extra earrings and is wrong on this point.
- **Boomstick is brass and ELECTRIC BLUE.** Its chamber is a glass cylinder holding caged blue-white lightning, never orange or amber. Always attach `assets/items/boomstick.png`.
- **Puff's ears are upright triangles** with blue inner faces, not cat ears and not tufted. Always attach `assets/art_refs/REF_homunculus.png`.

This governs all NEW art immediately.

**Backlog (DM asked for this 2026-08-17): strip the extra earrings from the existing plates too.** The heroes' jewelry drifted upward generation by generation until all three were wearing several rings apiece, and it reads as strange once noticed. The fix is per-image and mechanical: pass the finished plate to the image edits endpoint with a tight instruction to remove ear jewelry and change nothing else, then perceptually diff the result against the original to confirm only the ears moved. Do NOT regenerate these plates from scratch: they are DM-approved compositions and a re-roll loses them. Work session by session, newest first, and re-run `templates/audit_embedded_art.py` after each batch so nothing lands in the wrong slot. Expect some images to refuse the edit (the provider has blocked hero-art edits before); leave those and log them rather than forcing it.

## Pending: the three-ref set per hero (blocked 2026-08-17 on API credits)

Each hero is getting three level-7 references instead of one, so scene art has the right source for whatever it needs: a **portrait** (done, locked), a **full body** turnaround for outfit and gear continuity, and a **painted** version in traditional media for when a plate should read hand-made rather than rendered. The six remaining prompts are written and staged in `assets/gen_prompts/` as `<hero>_level7_fullbody.txt` and `<hero>_level7_painted.txt`; each generation stalled on `credit_balance_exhausted`. To finish, add API credits and run, from the repo root:

```
GENART_SIZE=1024x1024 python templates/genart.py assets/art_refs/REF_<hero>_<n>_fullbody.png assets/gen_prompts/<hero>_level7_fullbody.txt <that hero's level-7 portrait ref> <their signature item>
```

Attach the same refs used for the portraits: Lilly gets `REF_lilly_6_level7.png` + `items/boomstick.png` + `REF_homunculus.png`; Stabby `REF_stabby_4_level7.png` + `items/nichirin_katana.png`; Ursa `REF_ursa_4_level7.png` + `items/staff_of_waking_constellations.png`.

## Heroes and companions (era-split; see art guide)

| Character | Refs | Notes |
|---|---|---|
| Lilly Glimmergear | REF_lilly_1/2/3 (early), REF_lilly_4/5_later (S4+/S6+), **REF_lilly_6_level7 (S8+)** | Deep gnome artificer. From S8 she carries **Boomstick** (her mother's repeating pistol: brass and blued steel, a glass cylinder chamber full of caged blue-white lightning, blue runes, brown leather grip with a blue rune-gem) and **Puff rides her shoulder**. The frost dagger is retired to her belt. |
| Stabby Sharpblade | REF_stabby_1/2 (early), REF_stabby_3_later (S6+ sash), **REF_stabby_4_level7 (S8+)** | Goblin monk; Candyfang katana S4-S7. From S8 he wields the **Nichirin katana**, crimson sun-forged steel that glows blood-red, and his ignited breath trails red. |
| Ursa Catchum | REF_ursa_1/2 (early), REF_ursa_3_later (S6+ staff), **REF_ursa_4_level7 (S8+)** | Human star-druid. From S8 he is a year older and carries **Ash's Sigil-Stone**, a river-smooth grey stone with a half-finished golden spiral, in his off hand. |
| Ghostbloom | REF_ghostbloom | Ghostly-Bulbasaur of translucent teal light (S6+) |
| Floraburst | REF_floraburst | Ghostbloom's earlier form (S3-S5) |

## Recurring NPCs, villains, and powers

| Character | Ref file | Appears in | Notes |
|---|---|---|---|
| Professor Aelwyn Ravenstone | REF_aelwyn.webp | S2, S3 (logbook S7) | Tall silver-haired high elf, emerald eyes |
| Guildmaster Vane | REF_vane.png | S7, recurs S8+ | Wild-haired old human inventor, brass goggles |
| Quill | REF_quill.png | S7, recurs S8+ | Elegant silver Mechagnome archivist, blue eyes |
| Elaria (the goddess) | REF_elaria.png | S2 vision, S6, throughout | Sleeping Warden; starlight-and-vine goddess, seven-point star at brow |
| Nyxthid / the Dark Figure | REF_nyxthid.png | S3 vision, S12+ | Hooded shadow herald; unnamed to the party until late |
| Davy Jones | REF_davy_jones.png | S5 (defeated) | Tentacle-bearded ghost captain |
| The Krampusshade | REF_krampusshade.png | S4 (banished) | Ten-foot goat-horned winter fiend |
| Faelan | REF_faelan.png | S4 | Ancient half-elf lorekeeper |
| Ash Catchum | REF_ash_catchum.png | mentioned S1-S7, reveal S12 | Ursa's lost father, wildfire druid |
| Puff (Lilly's homunculus) | REF_homunculus.png | S7 onward, permanent | DM-SUPPLIED design, not generated: a tiny clockwork companion, round polished brass body with engraved filigree and inset gears, two large upright triangular ears lit blue inside, a curled brass forelock, huge round blue clockwork eyes, four small rounded feet. FAIRY-SIZED, fits in a child's two cupped hands; never draw it larger than Lilly's head. Ritual-built in Session 7. |
| Skitch | REF_skitch.png | S7, recurs S8+ | Young Bloodfang courier |
| Pikachu (Spark Fox) | REF_pikachu.png | in the Sphere; returns S13 | Golden light fox-spirit (cropped from S7 art). GENERATION NOTE (DM, 2026-08-13): words alone will not produce him, the model returns a generic fox with no lightning tail. Feed the anime/cartoon reference image for the creature; that is what worked. Fallback if no reference is available: describe the silhouette exhaustively (round cheeks, long dark-tipped upright ears, jagged lightning-bolt tail called out as prominent). |
| Poots Glimmergear | REF_poots_glimmergear.png | recurs if Lilly's Door B | Lilly's mother, Glimmerspire tinkerer |
| Captain Brynn Wavewarden | REF_brynn_wavewarden.png | S5 | Sea-captain of the Stormwind |
| Maera | REF_maera.png | S6 | Keeper of the Gasping Gull |

## Reference gaps (recurring characters still needing a canonical portrait)

Generate a clean portrait for these when convenient, then add to the table and `art_refs/`:
- **Henna Brasspot, Burl, Mara Sprocket, Tock, Pinion** - Gearhaven hub regulars (S7+); portraits exist inside S7 scenes, crop if they recur.

## How to use

1. Composing a prompt with a listed character? Attach their ref file(s) and describe them tersely; the ref carries the likeness.
2. Approving new art of a character who has NO ref yet? That approved image becomes their canonical ref: copy it to `art_refs/REF_<name>` and add a row here.
3. Keep this registry and `art_production_guide.md` in sync.
