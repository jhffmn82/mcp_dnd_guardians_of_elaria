# Character Reference Registry

The canonical look of every significant, recurring character. Whenever art featuring one of these characters is generated or regenerated, ATTACH their reference file(s) from `assets/art_refs/` so they stay consistent across the whole book. Heroes use era-split refs (see `art_production_guide.md`); everyone else has a single canonical portrait.

## Heroes and companions (era-split; see art guide)

| Character | Refs | Notes |
|---|---|---|
| Lilly Glimmergear | REF_lilly_1/2/3 (early), REF_lilly_4/5_later (S4+/S6+) | Deep gnome artificer |
| Stabby Sharpblade | REF_stabby_1/2 (early), REF_stabby_3_later (S6+ sash) | Goblin monk; Candyfang katana from S4 |
| Ursa Catchum | REF_ursa_1/2 (early), REF_ursa_3_later (S6+ staff) | Human star-druid |
| Ghostbloom | REF_ghostbloom | Ghostly-Bulbasaur of translucent teal light (S6+) |
| Floraburst | REF_floraburst | Ghostbloom's earlier form (S3-S5) |

## Recurring NPCs, villains, and powers

| Character | Ref file | Appears in | Notes |
|---|---|---|---|
| Professor Aelwyn Ravenstone | REF_aelwyn.webp | S2, S3 (logbook S8) | Tall silver-haired high elf, emerald eyes |
| Guildmaster Vane | REF_vane.png | S8, recurs S9+ | Wild-haired old human inventor, brass goggles |
| Quill | REF_quill.png | S8, recurs S9+ | Elegant silver Mechagnome archivist, blue eyes |
| Elaria (the goddess) | REF_elaria.png | S2 vision, S6, throughout | Sleeping Warden; starlight-and-vine goddess, seven-point star at brow |
| Nyxthid / the Dark Figure | REF_nyxthid.png | S3 vision, S13+ | Hooded shadow herald; unnamed to the party until late |
| Davy Jones | REF_davy_jones.png | S5 (defeated) | Tentacle-bearded ghost captain |
| The Krampusshade | REF_krampusshade.png | S4 (banished) | Ten-foot goat-horned winter fiend |
| Faelan | REF_faelan.png | S4 | Ancient half-elf lorekeeper |

## Reference gaps (recurring characters still needing a canonical portrait)

Generate a clean portrait for these when convenient, then add to the table and `art_refs/`:
- **Pikachu** (the Spark Fox) - returns S14; only appears inside the S8 `pikachu_returns` scene so far. Crop or generate a clean ref.
- **Skitch** - the young Bloodfang courier (S8, recurs via the Bloodfang thread); only inside `stabby_and_skitch`.
- **Ash Catchum** - Ursa's lost father; major reveal S13. No portrait at all. A builder sheet exists (`ash catchum.pdf`); a painted portrait would anchor S13.
- **Poots Glimmergear** - Lilly's mother; recurs if Lilly walks the Glimmerspire road.
- **Captain Brynn Wavewarden** - S5 ship captain; taught the knot lessons echoed in S6.
- **Maera** - keeper of the Gasping Gull (S6).
- **Henna Brasspot, Burl, Mara Sprocket, Tock, Pinion** - Gearhaven hub regulars (S8+); portraits exist inside S8 scenes, crop if they recur.

## How to use

1. Composing a prompt with a listed character? Attach their ref file(s) and describe them tersely; the ref carries the likeness.
2. Approving new art of a character who has NO ref yet? That approved image becomes their canonical ref: copy it to `art_refs/REF_<name>` and add a row here.
3. Keep this registry and `art_production_guide.md` in sync.
