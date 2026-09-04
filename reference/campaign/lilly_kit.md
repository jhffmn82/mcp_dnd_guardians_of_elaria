<!--
Consolidated level-7 combat kit checklist for Lilly Glimmergear.
Sources (all read, not from memory):
  templates/build_compendium.py  (relic, gift, all 3 doors: authoritative custom content)
  templates/build_sheets.py      (base sheet, level 5; level-7 numbers derived below)
  memory/house_rules.md          (house rules and standing rulings)
  reference/expansions/artificer.md (Artificer + Artillerist RAW, 2024)
  reference/srd/13_spells_q-z.md (True Strike text), reference/srd/11_spells_d-h.md (Fire Bolt)
No em dashes (house style). Built 2026-07-25.
-->

# Lilly Glimmergear: Level 7 Kit Checklist

Deep Gnome Artificer 7 (Artillerist). A combat sim must consult this before every turn so it forgets nothing. Every number traces to build_compendium.py or the base sheet; derived level-7 numbers show their work.

**Level-7 stat block.** HP 52 | AC 20 (25 under Shield) | Speed 25 ft. | Initiative +2 | Proficiency +3 | INT 20 (+5) | Spell save DC 16 | Spell attack +8 | Spell slots 4x 1st, 3x 2nd | Flash of Genius x5 | Cannon 1/long rest free (more cost a slot) | Darkvision 120 ft.

> **[FEAT CONVERSION 2026-08-07, commits 038b087 + 99ed4b4]** The three doors are now PATH FEATS, not items: Stormgunner (was the Storm Cell), Sentinel Protocol (was the Sentinel construct-item), Aether Channeler (was the Awakened Sphere item). Boomstick stays the base weapon on every road (Very Rare now). Consequences a sim must respect: the Wand of the War Mage +2 spell attack is GONE (spell attack is +8 on every road); Made to Channel is GONE (True Strike is +10 as a weapon-style attack per the base kit, unchanged); Stormgunner instead grants War-Trained (Advantage on Con saves to maintain Concentration, somatic components with Boomstick or Shield in hand); and the Sentinel now STACKS with the Pocket Dynamo instead of replacing it (+2 damage on its blasts, free Bonus-Action deploy/recall, no duration).

**Derivations from the level-5 sheet (build_sheets.py).**
- **HP 52.** Sheet L5 = 38. Artificer d8, +5 avg (4.5 rounded) +2 CON = 7 per level; levels 6 and 7 add 14. 38 + 14 = 52.
- **AC 20.** +1 half plate (16) + Dex cap +2 (18) + shield +2 (20). Under the Shield spell: 25.
- **Spell save DC 16** = 8 + PB 3 + INT 5. Unchanged from L5 (PB is still +3 at levels 5 to 8).
- **Spell attack +8** = PB 3 + INT 5, on every road (the old Storm Cell +2 was removed in the feat conversion).
- **Spell slots 4/3.** L7 Artillerist table (artificer.md): 4 first-level, 3 second-level (L5 was 4/2).
- **Flash of Genius x5** = INT mod (5) uses per long rest.
- **Eldritch Cannon HP 35** = 5 x Artificer level (L5 sheet showed 25 = 5x5). The Sentinel (Door A) instead has HP 40 = 5 + five times level.

**Attunement ledger at L7 (3 slots; Magic Item Adept and a 4th slot come at L10).** The doors are feats, so they cost NO attunement. Every road attunes only the Pocket Dynamo (1 of 3); Boomstick needs no attunement; the awakened Sphere is awakened by the feat, not attuned. Two slots free on every road for whatever the rifts yield. The Frostbite Shard Dagger is retired to her belt, unattuned, on every road (Boomstick has taken over its spell-focus and Arcane-Firearm duty).

---

## Always on (base class L7 + relic + gift)

These apply on every road. The weapon, focus, and Arcane Firearm on every road is **Boomstick** (built by Lilly and Poots together during her year at home); the Frostbite Shard Dagger is retired, so the dagger's old "+2 frost on any spell" rider is GONE and spells no longer get it.

| Feature | Action type | Cost | Exact mechanics / dice / DC / range | Rider to not forget |
|---|---|---|---|---|
| **True Strike (through Boomstick)** | Action | none (cantrip) | One attack **using INT for BOTH attack and damage**. To hit **+10** (PB 3 + INT 5 + Boomstick +2). Hit: 1d10 + 2 + **INT 5** thunder (or make the whole hit radiant, your choice) + **1d6 radiant** (cantrip upgrade, L5 to L10 band) + Arcane Firearm 1d8 thunder. Range 30/90. | The **+5 INT on damage** is the single most-dropped number. Choose radiant vs thunder by target resistance. |
| **Fire Bolt** | Action | none (cantrip) | Ranged spell attack **+8**, range **120 ft**, **2d10 fire** (L5 to L10 band) + Arcane Firearm 1d8 thunder. | The long-range option: Boomstick shots only reach 90 ft. |
| **Arcane Firearm (Boomstick, L5)** | Passive rider | per spell cast | When she casts an Artificer spell **through Boomstick**, add **1d8 thunder** to one of the spell's damage rolls. No once-per-turn cap in RAW (in practice about one spell per turn). | Applies to True Strike, Fire Bolt, Scorching Ray (one ray), Shatter, Thunderwave, etc. Easy to forget to add. |
| **Eldritch Cannon (Dynamo-enhanced)** | **Bonus Action** to activate | 1 cannon/long rest (more cost a spell slot) | AC 18, HP 35, Speed 15 ft. **Pick a mode fresh each activation** (house rule): **Flamethrower** 15-ft cone, DC 16 Dex, 2d8 **+2** fire (half on save); **Force Ballista** +8 to hit, 120 ft, 2d8 **+2** force, push 5 ft; **Protector** 1d8 **+ INT (5)** temp HP to Lilly + allies within 10 ft. | **+2 damage** from the Dynamo rides Flamethrower and Force Ballista (it is damage). Protector is 1d8 + 5 temp HP; +2 does NOT apply to temp HP. **Replaced by the Sentinel on Door A.** |
| **Glimmerspire Pocket Dynamo Mk II (relic)** | Free / Passive | attuned | **Deploy or recall the cannon as a free action.** Cannon lasts **24 hours**. Cannon deals **+2 damage**. **Reformat**: 1/long rest, action, change the cannon's model (mostly spare, since modes are per-activation). | The free deploy/recall means her Bonus Action is spent only on activating, not summoning. |
| **Two-action cannon economy** | Passive | none | She activates the cannon as a **Bonus Action** and still takes her **full Action** the same turn (spell, True Strike, or Fire Bolt). | She does both every round. Never make the cannon cost her Action. |
| **Flash of Genius (L7)** | **Reaction** | 5/long rest (= INT mod) | When **she or any creature within 30 ft** fails an ability check or saving throw, add **+5 (INT)** to the roll. | It **reaches allies within 30 ft**, not just Lilly. |
| **Shield spell (always prepared)** | **Reaction** | 1st-level slot | +5 AC until the start of her next turn (**AC 25**), negates Magic Missile. | Turns a hit into a miss; competes with her other reactions. |
| **Artillerist: Tools of the Trade (L3)** | Passive | none | **Proficiency with Martial Ranged weapons.** This is why she is proficient with Boomstick (a repeating pistol) and adds PB to its attacks. | Without this there is no Boomstick proficiency and no True Strike. |
| **Artillerist spells (always prepared)** | varies | slots | L3: Shield, Thunderwave. L5: Scorching Ray, Shatter. (Fireball/Wind Wall arrive at L9.) These do not count against her 7 prepared. | Scorching Ray: 3 rays, 2d6 fire each, +8 (+10 Door B), Arcane Firearm 1d8 on one ray. |
| **Magic Item Tinker (L6)** | Bonus/Magic action | limited | Charge (spend a slot to recharge a created item), Drain (1/long rest), Transmute (1/long rest). | Mostly utility; Charge can matter mid-fight for a created item. |
| **Replicate Magic Item / Tinker's Magic** | Utility | per rest | Built her +1 Half Plate (base of AC 20) and Stabby's +1 Repeating Longbow. Knows Mending (heals the cannon 2d6). | Mending on the cannon is a real in-combat heal. |
| **Gnomish Magic Resistance** | Passive | none | **Advantage on INT, WIS, and CHA saving throws against spells.** | Big defensive rider, easy to forget on enemy spell saves. |
| **Svirfneblin Camouflage / Gift of the Svirfneblin** | varies | 1/long rest each | Advantage on Stealth; casts Disguise Self and Nondetection free, 1/long rest each. | Utility, but the Stealth advantage is always on. |

---

## Door B: Stormgunner (path feat; was the Storm Cell)

Feat, no attunement. She keeps the normal Dynamo-enhanced Eldritch Cannon (Always-on section). The feat adds:

- **War-Trained.** **Advantage on CON saves to maintain Concentration**, and she can perform **somatic components** with Boomstick or a Shield in one or both hands. (This replaced the old Wand of the War Mage: there is NO +2 to spell attacks and NO ignore-Half-Cover anymore.)
- **Storm-Arc.** Whenever she **hits a creature with Boomstick**, the target takes an extra **1d6 lightning**, and lightning arcs to up to **two other creatures within 15 ft**: each makes a **DC 16 Dex save**, 2d6 lightning on a fail, half on a success. Triggers on **every** Boomstick hit, including True Strike shots.
- **Counter-Bolt (2/long rest).** **Reaction**, when a creature she can see within 60 ft attacks **an ally** (the feat text itself is ally-only): the triggering attack has **Disadvantage**, and she makes one Boomstick attack, +1d10 lightning on a hit.
- **Overloaded Shot (2/long rest).** On a Boomstick hit: extra **1d10 lightning** and a **CON save (DC 16) or Stunned** until the end of her next turn.
- (Made to Channel is GONE in the feat version; True Strike is simply the base kit's weapon-style +10 INT attack.)

**Combat loop (Door B).**
- **Action:** True Strike through Boomstick, to hit **+10** (1d10 + 2 + INT 5 thunder + 1d6 radiant + Arcane Firearm 1d8 + Storm-Arc 1d6 to target + arc 2d6 to two more, DC 16 Dex). Spend an Overloaded Shot for +1d10 and a Stun save when a stun matters.
- **Bonus:** Activate cannon, Force Ballista at **+8** (2d8 + 2 force, push 5), or Flamethrower / Protector as the field needs.
- **Reaction:** Counter-Bolt when an **ally** is attacked (Disadvantage + a free Boomstick shot), else Shield (self) or Flash of Genius.

---

## Door A: Sentinel Protocol (path feat; the cannon rebuilt, STACKS with the Dynamo)

Feat, no attunement; she stays attuned to the Dynamo. **The Sentinel IS her Eldritch Cannon in a new form** ("when you would create your Eldritch Cannon, you can create the Sentinel instead"), so **everything that improves her cannon applies to it, the Pocket Dynamo included**.

- **The Sentinel.** Medium construct. **AC 18, HP 40** (5 + five times level), Speed **30 ft.**, STR 14 / CON 16, immune Poison, condition-immune Charmed/Exhaustion/Poisoned. **It moves on its own 30 ft** and acts on her command. **Bound Construct:** add her PB to any check or save it makes. Rebuild for a 1st+ level slot if it hits 0 HP; Mending heals it 2d6.
- **Dynamo stacking (the 2026-08-07 change):** free **Bonus-Action deploy/recall** (Dynamo), **no maximum duration** (Dynamo), and the Dynamo's **+2 damage applies to Force Blast and Electric Pulse** (printed in the stat lines as "+2 from the Pocket Dynamo while attuned"). It does NOT apply to Guardian Protocol's temp HP.
- **Activate (Bonus Action), pick one:**
  - **Force Blast.** Ranged attack, her spell attack mod (**+8**), 120 ft, **2d8 + INT (5) + 2 force** (Dynamo).
  - **Electric Pulse.** Each chosen creature within **15 ft of the Sentinel**, **DC 16 Dex**, **2d8 + INT (5) + 2 lightning** (Dynamo); on a fail they **can't take Reactions** until the start of her next turn; half on a save.
- **Guardian Protocol (Reaction, 1/round).** When an ally **within 15 ft of the Sentinel** takes damage, that ally gains **1d8 + INT (5) temp HP** (no Dynamo +2; it is not damage).

**Combat loop (Door A).**
- **Action:** True Strike through Boomstick, to hit **+10** (1d10 + 2 + INT 5 thunder + 1d6 radiant + Arcane Firearm 1d8), or Fire Bolt (+8, 2d10 + 1d8) at range, or a leveled spell.
- **Bonus:** Activate the Sentinel: Force Blast (2d8 + 7, 120 ft) at a lone target, or Electric Pulse (2d8 + 7, DC 16, reaction-lock) into a cluster within 15 ft of the Sentinel. The Sentinel also moves 30 ft on its own.
- **Reaction:** Guardian Protocol (1d8 + 5 temp HP to an ally within 15 ft of the Sentinel), or Shield / Flash of Genius. Walk the Sentinel with the melee so Guardian Protocol can reach them.

---

## Door C: Aether Channeler (path feat; awakens the Sphere, no attunement)

Feat, no attunement (the feat awakens the Sphere she already carries; only the Dynamo is attuned). She keeps the normal Dynamo-enhanced Eldritch Cannon (Always-on section). The feat adds a short-rest pool.

- **Mote Channeling.** The Sphere's powers share **2 uses**, regained on a **Short Rest**. DC = spell save DC 16.
- **Aether Ward (base power, the ONLY power online at L7).** **Magic action** (costs her Action), 1 use: she and each ally **within 30 ft** gain **2d8 + INT (5) temp HP**.
- **THE POOL IS SHARED (2 uses, back on a SHORT rest).** Aether Ward and every Elemental Discharge spend from the same two uses. From the end of Session 8 she also has **Tectonic Slam** (Earth Mote installed): Magic action, 20-ft-radius Sphere within 120 ft, Dex save for **6d8 force + prone**, half and no prone on a success, raised stone = difficult terrain, 5 piercing per 5 ft moved, half cover for her side until the start of her next turn. A sim must never let her spend more than 2 total per short rest.
- **Elemental Discharges are ALL LOCKED at level 7.** Cinderstorm (Fire), Drowning Lull (Water), Tailwind (Air), Tectonic Slam (Earth), Soul Siphon (Shadow) each unlock only when that rift's Mote is installed. Through Session 8 the Sphere grants **Aether Ward alone**; Tectonic Slam unlocks at that session's homecoming and shares the same two uses. A sim must not use any discharge until its rift is cleared.
- **Lingering Discharges** (future): only one sustained at a time, no Concentration.

**Combat loop (Door C).**
- **Action:** True Strike through Boomstick (**+10**, 1d10 + 2 + 5 thunder + 1d6 radiant + 1d8 Arcane Firearm) or Fire Bolt (+8, 2d10 + 1d8) or a leveled spell (Scorching Ray: 3x 2d6, +8, +1d8 on one ray). **Or Aether Ward** (Magic action) when the team needs the 2d8 + 5 temp-HP shell.
- **Bonus:** Activate the Dynamo cannon: Force Ballista (+8, 2d8 + 2 force, push 5), Flamethrower (DC 16, 2d8 + 2 fire, cone), or Protector (1d8 + 5 temp HP within 10 ft).
- **Reaction:** Shield (AC 25) or Flash of Genius (+5 to a save by her or an ally within 30 ft).

---

## House-rule interactions that apply to this hero

Quoted from memory/house_rules.md:

- "The Eldritch Cannon picks its mode on every activation (Forge of the Artificer, 2024-era artificer)." (Applies to her Always-on cannon and, by extension, the Sentinel's per-activation Force Blast / Electric Pulse choice.)
- "Deep gnome uses the current 2024-era printing (Svirfneblin Camouflage; Disguise Self and Nondetection 1/long rest each)."
- Counter-Bolt is ally-only by the printed feat text now ("makes an attack roll against one of your allies"); the old house ruling is baked in.
- Door A's Sentinel stacks with the Dynamo by printed text ("anything that improves your cannon still applies to it, the Pocket Dynamo included").
- "Boomstick is a repeating pistol at 30/90, so Fire Bolt is the long-range option" (Boomstick shots and True Strike reach 90 ft max, disadvantage past 30 ft; Fire Bolt reaches 120 ft).
- "the Sentinel's Guardian Protocol reaches only 15 ft from the Sentinel, so it must walk with the melee" (Door A).

---

## Easy-to-forget checklist

- **INT (+5) drives True Strike on BOTH the attack roll and the damage.** True Strike substitutes her spellcasting ability for Dex; the +5 to damage is the single most-dropped number.
- **True Strike to-hit is +10 on every road** (PB 3 + INT 5 + Boomstick +2). Nothing raises it further (the old Storm Cell +2 is gone with the feat conversion).
- **Arcane Firearm adds 1d8 thunder to one damage roll of EVERY artificer spell she casts through Boomstick.** There is no per-turn cap in the printed feature (line 41 is right, this line used to say "once per turn" and was wrong); in practice she casts one spell a turn, so it reads the same at the table. Add it to True Strike, Fire Bolt, a Scorching Ray, Shatter, Thunderwave, or Web's burn. The thunder TYPE is a campaign variant from Boomstick's own card (build_compendium.py); the printed feature grants an untyped bonus.
- **The Pocket Dynamo gives the cannon +2 damage** on Flamethrower and Force Ballista (not on Protector temp HP).
- **The cannon fires on a BONUS action**; she still gets her full Action the same turn. Never charge her Action for it.
- **The cannon picks its mode fresh every activation** (house rule); it is never locked in.
- **Flash of Genius reaches allies within 30 ft** (+5 to a failed save or check), not just Lilly; 5 uses per long rest.
- **Gnomish Magic Resistance: advantage on INT/WIS/CHA saves vs spells** (defensive, always on).
- **The dagger is retired on every road**, so spells no longer get the old +2 frost rider; only the +1d8 Arcane Firearm (now thunder via Boomstick) remains.
- **Boomstick range is 30/90.** Do not fire Boomstick or a True Strike shot past 90 ft; use Fire Bolt (120 ft) for range.
- **Door B Storm-Arc fires on every Boomstick hit**: +1d6 lightning to the target and a 2d6 DC 16 Dex arc to two more enemies within 15 ft. Free extra area damage, easily dropped.
- **Door B Counter-Bolt triggers only when an ally is attacked**, never Lilly herself.
- **Door A Sentinel acts on its own turn**, moves 30 ft, and its Guardian Protocol reaction only reaches 15 ft, so keep it walking with the melee.
- **Door C has only Aether Ward online at level 7**; all five Elemental Discharges are locked until their rifts are cleared. Aether Ward costs her Action (Magic action) and draws on the shared 2/short-rest pool (Tectonic Slam joins that pool from the S8 homecoming).
- **Shield (reaction) puts her at AC 25.** Remember she competes for her reaction between Shield, Flash of Genius, and (Door B) Counter-Bolt.
