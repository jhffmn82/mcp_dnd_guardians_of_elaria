# Art Production Guide

The master list of campaign art: what exists, what is missing, and a ready-to-paste DALL-E prompt for every gap. Goal: bring Sessions 1-6 up to Session 8's illustration density (roughly 5-8 images per part) in ONE consistent style.

## How to use this guide

1. Every prompt below = STYLE BLOCK + the character block(s) named + the scene line. Paste all parts together.
2. ATTACH REFERENCE IMAGES when a hero appears. DM-approved canonical references live in `assets/art_refs/`, split by era because the heroes' gear changes:
   - EARLY (Sessions 1-3, no relics): Lilly REF_lilly_1 (shop scene), REF_lilly_2 (flower portrait), REF_lilly_3 (sphere close-up, timeless); Stabby REF_stabby_1 (crossed arms), REF_stabby_2 (white hood grin); Ursa REF_ursa_1 (leaf-tattoo portrait), REF_ursa_2 (turnaround sheet).
   - LATER (Session 4+ items, Session 6+ relics): Lilly ADD REF_lilly_4_later (winter coat + Frostbite Shard Dagger, S4+) and REF_lilly_5_later (holding the Pocket Dynamo with Elaria's star sigil, S6+); Stabby ADD REF_stabby_3_later (crimson sash + Candyfang, S6+); Ursa ADD REF_ursa_3_later (staff + fur cloak, S6+).
   - Companions: REF_ghostbloom.png (S6+); REF_floraburst.png (S3-S5).
   - When generating an early-session scene, do NOT attach the later refs (they carry gear that does not exist yet), and vice versa.
3. Save each result into the listed path with the listed filename, then tell Claude: the build scripts get updated and the prompt gets recorded in `image_manifest.md` (prompts are always preserved).
4. Gear continuity matters: Ursa's staff and Stabby's sash exist only from Session 6 on; the Candyfang Katana only from late Session 4 on; Floraburst (green) before Session 6, Ghostbloom (pale teal) after.

## STYLE BLOCK (paste into every prompt)

> painterly storybook fantasy illustration, lush warm golden palette with teal and brass accents, soft volumetric light, detailed fantasy-anime glow, digital painting, no text or lettering anywhere in the image

## CHARACTER BLOCKS

**[LILLY]** Lilly, a 7-year-old deep gnome girl, tiny, with dark slate-gray skin, long flowing silver hair, large bright red eyes, brass goggles pushed up on her head, a little leather tool-harness over travel clothes with frost-blue accents, carrying a small glowing brass-and-crystal sphere.

**[STABBY]** Stabby, an 8-year-old goblin boy, bright green skin, spiky light-green hair, big red eyes, long pointed ears, a huge sharp-toothed grin, simple brown monk garb with a candy-red cloth belt. (From Session 4 night on: carrying a candy-cane-striped katana. From Session 6 on: wearing a shimmering crimson silk sash.)

**[URSA]** Ursa, a 7-year-old human boy druid, short red hair, pale skin with freckles, bright purple eyes, a faint star-shaped mark on his forearm, rustic green-and-brown druid clothes with starlight-purple accents. (From Session 6 on: carrying a wooden staff etched with glowing constellations.)

**[FLORABURST]** Floraburst, a small cheerful fey creature like a tiny leafy dinosaur with a large flower bud on its back, bright spring green, friendly round eyes. (Sessions 3-5 only.)

**[GHOSTBLOOM]** Ghostbloom, a tiny ghostly plant-fey, pale translucent teal, floating, with a glowing glass-pale flower on her back and petals like frost crystals, soft teal glow. (Session 6 on.)

---

## WHAT EXISTS (usable now)

| Asset | Used in |
|---|---|
| Region map (`world/elaria_region_map.png`), academy + circle symbols | S1 frontispiece |
| DALL-E portraits: Lilly w/ sphere, Ursa w/ potato, Stabby, Stabby twilight forest, Aelwyn, Ravenstone Lab | S1-S3 |
| `monsters/grimfang_clan.png`, `monsters/false_hydra.png`, `monsters/gasping_gull.png` | S2, S6 |
| Character art: lilly/stabby/ursa 2,4,5-series, with-staff, with-sash, holding-sphere, ghostbloom.png | S4-S6 |
| Scene art: ursa_vs_rats, stabby_vs_strawlings, lilly_vs_zombies, ghostbloom_vs_hydra_head, lilly_opening_chest | S6 |
| Stabby breathing styles (red/water/shadow), boomstick, awakened sphere, eldritch cannon | Compendium/paths |
| Session 8: 41 beat images | S8 |

---

## THE GAP LIST (prompts to generate)

### Session 1: The Gathering of Friends
| Save as | Characters | Scene line (add STYLE + character blocks) |
|---|---|---|
| `scenes/s1_gilded_acorn_meeting.png` | LILLY STABBY URSA | Scene: inside a cozy candlelit medieval tavern with a stone hearth, the three children meet at a small wooden table, the gnome girl showing the glowing sphere to the curious druid boy while the goblin boy leans in with a huge grin. |
| `scenes/s1_bar_brawl.png` | STABBY | Scene: a comedic non-lethal tavern brawl, the tiny goblin boy ducking under a burly farmer's wild swing while mugs and a chair fly, patrons laughing and cheering. |
| `scenes/s1_lickgloom_pond.png` | URSA | Scene: a moonlit pond ringed with reeds and glowing wildflowers, the druid boy kneeling to offer bread to a small round fey creature with an impossibly long tongue and huge innocent eyes, fireflies drifting. |
| `monsters/duckleaf_stone_circle.png` | none | Scene: an ancient mossy stone circle in a misty forest clearing, and perched atop the tallest rune-carved stone a proud sturdy duck warrior holding a long leek like a sword, wind swirling leaves around it. |
| `monsters/cognifin_grove.png` | none | Scene: a hidden forest grove with a pond glowing soft blue from below, water droplets hanging frozen in the air, a duck-like guardian creature hovering above its reflection wrapped in rippling psychic light. |
| `scenes/s1_mist_stalkers.png` | LILLY STABBY URSA | Scene: a foggy twilight road blocked by gnarled roots, the three small heroes standing back to back as two sleek shadowy predators with glowing eyes circle them in the mist, brave not gory. |
| `scenes/s1_oakshade_twilight.png` | none | Scene: a small village nestled beneath enormous ancient oak trees at twilight, lantern-lit cottages, a great oak hung with faded ribbons and charms beside an old stone well. |

### Session 2: The Road to Ravenstone
| Save as | Characters | Scene line |
|---|---|---|
| `scenes/s2_villagers_return.png` | none | Scene: joyful dawn reunion in a village square under giant oaks, three teenage herb-gatherers stumbling home dazed but smiling into the arms of relieved villagers, an old blacksmith elder beaming. |
| `scenes/s2_mudskip_ambush.png` | LILLY | Scene: a muddy forest clearing where three slick salamander-like water elementals leap from puddles, the tiny gnome girl zapping one with a sparking gadget. |
| `scenes/s2_grimfang_ambush.png` | STABBY | Scene: a forest road ambush, the small goblin monk boy standing defiant before a scarred goblin war boss flanked by a snarling worg, banners of a rival clan in the trees. |
| `scenes/s2_elaria_vision.png` | LILLY STABBY URSA | Scene: THE key image: in a moonlit glade before a mossy runestone, the three children look up in awe at a colossal translucent goddess woven of starlight, flowing water and blooming vines, her face kind and sorrowful, stars wheeling behind her. |
| `monsters/terranox.png` | none | Scene: a huge serpent made of living stone and crystal rearing from a mountain path, geodes glowing along its spine, boulders floating around it. |
| `scenes/s2_ravenstone_arrival.png` | LILLY STABBY URSA FLORABURST-less | Scene: the three children cresting a hill at dusk to see a wondrous stone-and-glass laboratory built into a cliff over a shimmering lake, whimsical glowing creatures grazing around it. |

### Session 3: The Quest for Knowledge
| Save as | Characters | Scene line |
|---|---|---|
| `scenes/s3_sphere_examination.png` | LILLY | Scene: inside a magical laboratory of brass instruments and floating lights, a tall silver-haired elf professor with emerald eyes examining a glowing sphere through a rune-etched magnifying lens while the gnome girl watches anxiously. |
| `scenes/s3_choose_companion.png` | LILLY STABBY URSA FLORABURST | Scene: the elf professor presenting three small magical creatures to the delighted children: a leafy dinosaur with a flower bud, a turtle wrapped in a watery aura, and a fiery fox-like creature with flame-tipped paws. |
| `scenes/s3_lickgloom_farewell.png` | URSA | Scene: a bittersweet goodbye at the laboratory door, the round long-tongued fey creature waving its tongue at the departing children while magical lab creatures gather around it, morning light. |
| `monsters/shadowflame.png` | none | Scene: a thorny twilight thicket where a creature of living shadow wreathed in cold purple fire stands among three flickering mirror-copies of itself. |
| `scenes/s3_displacer_beasts.png` | STABBY | Scene: a foggy ancient forest path, two sleek panther-like beasts with six legs and whip tentacles prowling toward the goblin boy, who grins back completely unafraid. |
| `monsters/shroomyte_grove.png` | none | Scene: a grove of giant bioluminescent mushrooms at night, four squat fungus guardians with glowing spore caps rising from the earth in defense. |
| `scenes/s3_stormwatch_vision.png` | LILLY STABBY URSA | Scene: storm-lashed sea cliffs crowned with four elemental monoliths, lightning frozen mid-strike, and above them a towering hologram of a figure in a dark cloak, face hidden in shadow, the children small and defiant below. |
| `scenes/s3_havenmoor_arrival.png` | none | Scene: a festive snow-dusted coastal town at dusk decorated for a winter holiday, garlands and lanterns, a towering decorated pine in the square, ships in the harbor beyond. |

### Session 4: Awakening to Shadows and Songs
| Save as | Characters | Scene line |
|---|---|---|
| `scenes/s4_children_singing.png` | none | Scene: a snowy village street at pale dawn, a huddle of entranced children singing with vacant eyes while frightened parents watch from doorways, spooky-beautiful not scary. |
| `scenes/s4_bell_hunt_market.png` | LILLY | Scene: a festive winter market square with a towering decorated pine tree, the gnome girl climbing garlands to reach a small golden bell hidden among the ornaments. |
| `scenes/s4_orphanage_milo.png` | URSA | Scene: a dim orphanage attic, the druid boy kneeling gently before a frightened small child clutching a little golden bell, warm lantern light pushing back the shadows. |
| `scenes/s4_lighthouse.png` | STABBY | Scene: a storm-battered lighthouse on sea cliffs in whirling snow, the goblin boy scampering up the spiral stair while an old bearded keeper holds a lantern below. |
| `npcs/faelan.png` | none | Scene: portrait of an ancient kindly half-elf lorekeeper in an ivy-covered cottage full of books and candles, offering a plate of frosted cookies. |
| `scenes/s4_barrier_carol.png` | LILLY STABBY URSA | Scene: the three children playing eight small golden handbells in a snowy moonlit glade before a great pine sheathed in black ice, the ice cracking with golden light where the music touches it. |
| `monsters/krampusshade.png` | none | Scene: the villain reveal: a ten-foot shadowy goat-horned fiend with frost-covered black fur, chains of ice, and a big lumpy burlap sack over its shoulder, looming out of swirling snow, storybook-scary not gruesome. |
| `scenes/s4_carol_of_the_bells.png` | LILLY STABBY URSA | Scene: the final battle: the three children ringing bells in glowing golden harmony as the great goat-horned shadow fiend unravels into wisps of darkness above them, snowflakes suspended in the light. |
| `scenes/s4_children_freed.png` | none | Scene: the burst-open burlap sack and a dozen laughing children tumbling out unharmed into the lantern-lit snow, one small boy running into his weeping mother's arms. |

### Session 5: The Curse of Davy Jones
| Save as | Characters | Scene line |
|---|---|---|
| `scenes/s5_harbor_sendoff.png` | LILLY STABBY URSA FLORABURST | Scene: a cheering harbor crowd waving the three children up a gangplank, banners strung between lampposts, a proud tall ship with white sails waiting, morning sun on the water. |
| `scenes/s5_storm.png` | none | Scene: a tall ship battling a monstrous night storm, a wall of black water towering over it, lightning splitting the mainmast, sailors clinging to rigging, dramatic but heroic. |
| `scenes/s5_dutchman_rises.png` | none | Scene: from beneath a capsized hull in dark water, a ghostly barnacled galleon rising out of the deep wrapped in green spectral light, anglerfish lanterns glowing on its hull. |
| `npcs/davy_jones.png` | none | Scene: portrait of a ghost-pirate captain with a beard of small tentacles, barnacle-crusted coat and hook hand, green spectral light, theatrical and menacing but kid-friendly. |
| `scenes/s5_dice_game.png` | LILLY STABBY URSA | Scene: a candlelit ghost-ship cabin, the three small heroes seated across a table from the tentacle-bearded ghost captain, glowing bone dice mid-tumble between them, souls' wagers hanging in green lantern light. |
| `scenes/s5_hold_of_essences.png` | URSA | Scene: a ghost ship's cargo hold stacked with glowing jars of captured magical light and sad caged creatures (a water sprite, a small flame salamander, an owl-like being), the druid boy reaching toward a cage. |
| `scenes/s5_ghost_essence.png` | LILLY FLORABURST | Scene: the gnome girl gently pouring a swirling ribbon of pale ghost-light from a jar into her small leafy dinosaur companion, whose petals are beginning to turn glassy and pale, tender and luminous. |
| `scenes/s5_vigil_dawn.png` | LILLY STABBY URSA FLORABURST | Scene: a small rowing cutter at golden dawn, the exhausted children rowing toward distant clockwork spires on the horizon while a ghostly galleon splits and sinks far behind them. |

### Session 6: Lanterns in the Fog
(DM verdict 2026-07-06: the existing S6 scene art is off-style (older pre-anchor generation batch) and is to be REPLACED wholesale with S8-style regenerations. Attach the LATER refs: Stabby sash era, Ursa staff era, Lilly Dynamo era, Ghostbloom. The build swaps files one-for-one on approval; old files retire to _triage/old_art/.)

REPLACEMENT SET (regenerate in house style):
| Save as | Characters | Scene line |
|---|---|---|
| `scenes/s6_cellar_rats.png` | URSA GHOSTBLOOM | Scene: a stone tavern cellar by lantern light, the druid boy standing firm as a chittering tide of rats boils out of a cracked wall seam, the ghostly plant-fey glowing above his shoulder. |
| `scenes/s6_pumpkin_row.png` | STABBY | Scene: a moonlit lane of hay bales where jack-o'-lanterns all stare one direction, the goblin boy mid-leap between two lurching scarecrows trailing straw, candy-striped katana flashing. |
| `scenes/s6_graveyard_rite.png` | LILLY | Scene: a cypress-ringed graveyard in fog, the tiny gnome girl holding up a blue-glass lantern before a headstone whose name has been chiseled away, gentle golden light pushing back rising shadows. |
| `scenes/s6_tavern_reveal.png` | GHOSTBLOOM | Scene: a warm inn common room where, above an open trapdoor, a single pale long-necked creature head looms unseen by the cheerful patrons below, the little ghost-fey blazing teal in warning, spooky-storybook not gruesome. |
| `scenes/s6_chest_opening.png` | LILLY STABBY URSA GHOSTBLOOM | Scene: in a golden shaft of light underground, the three children kneel around a half-buried chest bound in silver vines as the ghost-fey sings it open, three faint treasures glowing within. |
| `monsters/false_hydra_lair.png` | none | Scene: a vast drowned orchestra pit beneath a ruined theater, a pale bulbous many-necked creature rising from dark water among floating playbills and ribbons, four serpent necks through holes in the stage above, eerie-beautiful storybook horror. |

(These older originals also fill the holes below if regeneration is deferred.)
| Save as | Characters | Scene line |
|---|---|---|
| `scenes/s6_ghostbloom_naming.png` | LILLY STABBY URSA GHOSTBLOOM | Scene: on a morning coastal path among wind-bent pines, the three children gathered in wonder around their transformed companion, now pale translucent teal and floating, frost-crystal petals chiming. |
| `scenes/s6_lantern_night.png` | LILLY STABBY URSA GHOSTBLOOM | Scene: a harvest festival in a fog-wrapped village at dusk, carved pumpkins on every doorstep, paper moons and cat masks strung over market stalls, the three children walking beneath the lantern arch. |
| `scenes/s6_maera_tavern.png` | none | Scene: a warm seaside inn interior where a kindly innkeeper sets a fourth place at a table for three, an old spaniel asleep by the hearth, something almost imperceptibly wrong in the cozy scene. |
| `npcs/bellkeeper.png` | none | Scene: portrait of a weathered old bellkeeper beneath his bell tower at night, beeswax in his ears, holding up a slate with a warning written on it, moonlit fog behind him. (Note: image itself must contain no readable text; slate faces away.) |
| `scenes/s6_orchestra_pit.png` | LILLY STABBY URSA GHOSTBLOOM | Scene: a vast drowned theater beneath the earth, flooded orchestra pit glowing with pale light, four long pale serpent necks rising through holes in the stage floor, the tiny heroes brave at the water's edge. |
| `scenes/s6_names_return.png` | none | Scene: a village at dawn as golden threads of light drift down every street and into windows, villagers stepping outside with faces of dawning memory, a bell tower ringing three clean notes. |

### The big-picture set (any session, compendium, and the finale of the book)
| Save as | Characters | Scene line |
|---|---|---|
| `world/elaria_goddess.png` | none | Scene: full portrait of Elaria, sleeping Warden of Balance: a serene colossal goddess drifting in starry darkness, hair flowing into constellations, vines and water woven through her robes, a seven-point star glowing faintly at her brow. |
| `world/dark_figure.png` | none | Scene: a tall figure of living shadow on a broken starfield, face hidden, one hand closing around a tiny dying star, wisps of darkness trailing like a cloak, ominous but elegant. |
| `items/three_potatoes.png` | none | Scene: three humble potatoes on a velvet cloth, each faintly aglow with a different inner light (warm gold, shifting green, cool silver), painted like precious relics. |
| `items/wraithpine_chest.png` | none | Scene: a half-buried chest bound in vines of silver and living root, seams leaking golden light, in a dark theater underground. |
| `world/seven_point_star.png` | none | Scene: an ornate emblem illustration: a seven-point star wrapped in a leafed vine, engraved in brass and glowing, on parchment (decorative, no words). |
| `items/stabbys_doll.png` | none | Scene: a small old carved wooden doll wearing a tiny stitched cat-mask, lying on a goblin's open travel bag by a campfire at night, faint cold aura, mysterious not menacing. |

---

## Workflow after generation

Drop finished images in the listed folders, then tell Claude which ones landed. Claude will: (1) record every generation prompt verbatim in `image_manifest.md`, (2) wire the images into the session build scripts, (3) rebuild the docx files, (4) update this guide's EXISTS table.
