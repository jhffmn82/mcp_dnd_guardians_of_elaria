# Reference Rules (2024)

Authoritative 2024 D&D rules for this campaign, so rules answers come from a source instead of memory. See [ATTRIBUTION.md](ATTRIBUTION.md) for licensing.

**Standing rule (also in CLAUDE.md): never state a 2024 rule from memory.** Check here first; for anything not covered, read the actual text at dnd2024.wikidot.com (via the in-app browser: preview_start + navigate + get_page_text; WebFetch loops on the site and cannot reach it). Cite what you used. If it cannot be verified, say "unverified, check the PHB" rather than asserting.

## srd/ (faithful CC-BY-4.0 transcription of SRD 5.2.1)
The PDF `SRD_CC_v5.2.1.pdf` is authoritative; the markdown is for search. Each file transcribed from the PDF pages and verified against the source.

| File | Contents |
|---|---|
| 01_playing_the_game.md | Core rules: d20 tests, advantage, actions, cover, combat, damage/healing, death saves |
| 02_character_creation.md | Creation steps, ability scores, alignments, leveling, multiclassing, trinkets |
| 03_classes_barbarian_bard_cleric.md | Barbarian, Bard, Cleric (incl. **Divine Order**, Channel Divinity) + SRD subclasses |
| 04_classes_druid_fighter_monk.md | Druid, Fighter, Monk (incl. Weapon Mastery, Monk Focus) + SRD subclasses |
| 05_classes_paladin_ranger_rogue.md | Paladin, Ranger, Rogue + SRD subclasses |
| 06_classes_sorcerer_warlock_wizard.md | Sorcerer, Warlock, Wizard (Metamagic, Pacts, Invocations) + SRD subclasses |
| 07_backgrounds_species.md | Backgrounds and Species (Origin feats come with backgrounds) |
| 08_feats.md | Feats, including **Origin feats** (Magic Initiate, etc.) |
| 09_equipment.md | Coins, weapons + weapon properties/mastery, armor, tools, gear |
| 10_spells_intro_and_a-c.md | Spell rules + descriptions A-C (incl. **Guiding Bolt**) |
| 11_spells_d-h.md | Spell descriptions D-H |
| 12_spells_i-p.md | Spell descriptions I-P (pages 149-154 raw-extracted; see file header) |
| 13_spells_q-z.md | Spell descriptions Q-Z (incl. **True Strike**) |
| 14_rules_glossary.md | Conditions and key term definitions |

## expansions/ (non-SRD 2024 content; summarized mechanics + citations, NOT verbatim)
Not open-licensed, so these are factual mechanics in our own words with a source link, not reproduced prose.

| File | Contents |
|---|---|
| artificer.md | **Artificer** class + **Artillerist** subclass (Lilly). Source: Eberron: Forge of the Artificer (official 2024). |
| druid-circle-of-stars.md | **Circle of the Stars** subclass (Ursa) + the base-Druid level-7 Elemental Fury / Potent Spellcasting. Source: 2024 PHB. Not in the SRD (which has Circle of the Land). |

## campaign/ (per-hero level-7 kit checklists)
Consolidated, verified loadouts so a combat sim forgets nothing. Each covers base class (level 7) + relics + gift + all three path-reward doors + house rules, every number traced to `templates/build_compendium.py`. **Consult the relevant kit before simming or answering a "what can X do" question.**

| File | Hero |
|---|---|
| campaign/stabby_kit.md | Stabby, Monk 7 (Warrior of Breathing: Beast / Water / Shadow doors, Nichirin Katana, Sash Air Dance) |
| campaign/lilly_kit.md | Lilly, Artificer 7 (Artillerist: Storm Cell / Sentinel / Awakened Sphere doors, Boomstick, the +5 INT on True Strike) |
| campaign/ursa_kit.md | Ursa, Druid 7 (Circle of Stars: Beast Handler / Starlit Channeler / Reader of Omens doors, Staff, Amulet Starry Glow) |

Open [DM CHECK]s flagged in the kits: Ursa's +1 light aura is allies-only (his own attack is +8, not +9, contradicting earlier sims); Lilly's Door A True Strike is +10 or +12 depending on whether the two +2 bonuses stack; Cosmic Omen self-target.

## Known coverage gaps (use the wiki, cite it)
- Not in SRD: Artificer (see expansions/), most subclasses beyond the SRD's samples, firearms (DMG optional), the 2014-only Peace Domain.
- The wiki's **UA and HB sections are off by default.** Only pull Unearthed Arcana when the DM explicitly asks; the wiki is where to find it.
