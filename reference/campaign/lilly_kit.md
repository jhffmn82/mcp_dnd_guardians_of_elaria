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

**Level-7 stat block.** HP 52 | AC 20 (25 under Shield) | Speed 25 ft. | Initiative +2 | Proficiency +3 | INT 20 (+5) | Spell save DC 16 | Spell attack +8 (+10 with the Storm Cell's Wand of the War Mage) | Spell slots 4x 1st, 3x 2nd | Flash of Genius x5 | Cannon 1/long rest free (more cost a slot) | Darkvision 120 ft.

**Derivations from the level-5 sheet (build_sheets.py).**
- **HP 52.** Sheet L5 = 38. Artificer d8, +5 avg (4.5 rounded) +2 CON = 7 per level; levels 6 and 7 add 14. 38 + 14 = 52.
- **AC 20.** +1 half plate (16) + Dex cap +2 (18) + shield +2 (20). Under the Shield spell: 25.
- **Spell save DC 16** = 8 + PB 3 + INT 5. Unchanged from L5 (PB is still +3 at levels 5 to 8). The Storm Cell's Wand of the War Mage does NOT raise the save DC.
- **Spell attack +8** = PB 3 + INT 5. +10 only with the Storm Cell (Door A).
- **Spell slots 4/3.** L7 Artillerist table (artificer.md): 4 first-level, 3 second-level (L5 was 4/2).
- **Flash of Genius x5** = INT mod (5) uses per long rest.
- **Eldritch Cannon HP 35** = 5 x Artificer level (L5 sheet showed 25 = 5x5). The Sentinel (Door B) instead has HP 40 = 5 + five times level.

**Attunement ledger at L7 (3 slots; Magic Item Adept and a 4th slot come at L10).** Boomstick needs no attunement, so it rides free on every road. Door A: Dynamo + Storm Cell (2 of 3). Door B: the Sentinel only (1 of 3; the Dynamo is rebuilt inside it). Door C: Dynamo + Sphere (2 of 3). The Frostbite Shard Dagger is retired to her belt, unattuned, on every road (Boomstick has taken over its spell-focus and Arcane-Firearm duty).

---

## Always on (base class L7 + relic + gift)

These apply on every road. The weapon, focus, and Arcane Firearm on every road is **Boomstick** (Poots's parting work); the Frostbite Shard Dagger is retired, so the dagger's old "+2 frost on any spell" rider is GONE and spells no longer get it.

| Feature | Action type | Cost | Exact mechanics / dice / DC / range | Rider to not forget |
|---|---|---|---|---|
| **True Strike (through Boomstick)** | Action | none (cantrip) | One attack **using INT for BOTH attack and damage**. To hit **+10** (PB 3 + INT 5 + Boomstick +2). Hit: 1d10 + 2 + **INT 5** thunder (or make the whole hit radiant, your choice) + **1d6 radiant** (cantrip upgrade, L5 to L10 band) + Arcane Firearm 1d8 thunder. Range 30/90. | The **+5 INT on damage** is the single most-dropped number. Choose radiant vs thunder by target resistance. |
| **Fire Bolt** | Action | none (cantrip) | Ranged spell attack **+8**, range **120 ft**, **2d10 fire** (L5 to L10 band) + Arcane Firearm 1d8 thunder. | The long-range option: Boomstick shots only reach 90 ft. |
| **Arcane Firearm (Boomstick, L5)** | Passive rider | per spell cast | When she casts an Artificer spell **through Boomstick**, add **1d8 thunder** to one of the spell's damage rolls. No once-per-turn cap in RAW (in practice about one spell per turn). | Applies to True Strike, Fire Bolt, Scorching Ray (one ray), Shatter, Thunderwave, etc. Easy to forget to add. |
| **Eldritch Cannon (Dynamo-enhanced)** | **Bonus Action** to activate | 1 cannon/long rest (more cost a spell slot) | AC 18, HP 35, Speed 15 ft. **Pick a mode fresh each activation** (house rule): **Flamethrower** 15-ft cone, DC 16 Dex, 2d8 **+2** fire (half on save); **Force Ballista** +8 to hit, 120 ft, 2d8 **+2** force, push 5 ft; **Protector** 1d8 **+ INT (5)** temp HP to Lilly + allies within 10 ft. | **+2 damage** from the Dynamo rides Flamethrower and Force Ballista (it is damage). Protector is 1d8 + 5 temp HP; +2 does NOT apply to temp HP. **Replaced by the Sentinel on Door B.** |
| **Glimmerspire Pocket Dynamo Mk II (relic)** | Free / Passive | attuned | **Deploy or recall the cannon as a free action.** Cannon lasts **24 hours**. Cannon deals **+2 damage**. **Reformat**: 1/long rest, action, change the cannon's model (mostly spare, since modes are per-activation). | The free deploy/recall means her Bonus Action is spent only on activating, not summoning. |
| **Two-action cannon economy** | Passive | none | She activates the cannon as a **Bonus Action** and still takes her **full Action** the same turn (spell, True Strike, or Fire Bolt). | She does both every round. Never make the cannon cost her Action. |
| **Flash of Genius (L7)** | **Reaction** | 5/long rest (= INT mod) | When **she or any creature within 30 ft** fails an ability check or saving throw, add **+5 (INT)** to the roll. | It **reaches allies within 30 ft**, not just Lilly. |
| **Shield spell (always prepared)** | **Reaction** | 1st-level slot | +5 AC until the start of her next turn (**AC 25**), negates Magic Missile. | Turns a hit into a miss; competes with her other reactions. |
| **Absorb Elements** | **Reaction** | 1st-level slot | On taking acid/cold/fire/lightning/thunder: take half; next melee hit adds 1d6 of that type. | Reaction economy again. |
| **Artillerist: Tools of the Trade (L3)** | Passive | none | **Proficiency with Martial Ranged weapons.** This is why she is proficient with Boomstick (a repeating pistol) and adds PB to its attacks. | Without this there is no Boomstick proficiency and no True Strike. |
| **Artillerist spells (always prepared)** | varies | slots | L3: Shield, Thunderwave. L5: Scorching Ray, Shatter. (Fireball/Wind Wall arrive at L9.) These do not count against her 7 prepared. | Scorching Ray: 3 rays, 2d6 fire each, +8 (+10 Door A), Arcane Firearm 1d8 on one ray. |
| **Magic Item Tinker (L6)** | Bonus/Magic action | limited | Charge (spend a slot to recharge a created item), Drain (1/long rest), Transmute (1/long rest). | Mostly utility; Charge can matter mid-fight for a created item. |
| **Replicate Magic Item / Tinker's Magic** | Utility | per rest | Built her +1 Half Plate (base of AC 20) and Stabby's +1 Repeating Longbow. Knows Mending (heals the cannon 2d6). | Mending on the cannon is a real in-combat heal. |
| **Gnomish Magic Resistance** | Passive | none | **Advantage on INT, WIS, and CHA saving throws against spells.** | Big defensive rider, easy to forget on enemy spell saves. |
| **Svirfneblin Camouflage / Gift of the Svirfneblin** | varies | 1/long rest each | Advantage on Stealth; casts Disguise Self and Nondetection free, 1/long rest each. | Utility, but the Stealth advantage is always on. |

---

## Door A: The Storm Cell (Boomstick augmentation)

Attuned: Dynamo + Storm Cell. Boomstick becomes stormcharged. Adds to the always-on kit:

- **Wand of the War Mage.** While holding Boomstick, **+2 to spell attack rolls** (spell attack becomes **+10**), and **ignore Half Cover** on spell attacks. Her **Eldritch Cannon also gains +2 to its attack rolls** (Force Ballista becomes +10).
- **Storm-Arc.** Whenever she **hits a creature with Boomstick**, the target takes an extra **1d6 lightning**, and lightning arcs to up to **two other creatures within 15 ft**: each makes a **DC 16 Dex save**, 2d6 lightning on a fail, half on a success. Triggers on **every** Boomstick hit, including True Strike shots.
- **Charged Rounds** (2 Thunder Wave Rounds + 2 Counter-Bolts, regain on long rest; DC = spell save DC 16):
  - **Thunder Wave Round.** On a Boomstick hit, expend 1: extra **1d10 lightning** and a **CON save or Stunned** until the end of her next turn.
  - **Counter-Bolt.** **Reaction**, expend 1, when a creature within 60 ft attacks **an ally** (NOT Lilly herself, house rule): the triggering attack has **Disadvantage**, and she makes one Boomstick attack, +1d10 lightning on a hit.
- **Made to Channel.** When she casts **True Strike through Boomstick**, it uses **INT**, **counts as a spell attack** (so it gains the Storm Cell's **+2** spell-attack bonus and ignores Half Cover), and on a hit deals Boomstick's thunder plus the spell's radiant.
  - [DM RULING 2026-07-25: the two +2 bonuses do NOT stack. Door A True Strike is **+10** (INT 5 + PB 3 + one +2), same as the other roads. The Cell's +2 does not add on top of Boomstick's weapon +2.]

**Combat loop (Door A).**
- **Action:** True Strike through Boomstick, to hit **+10** (1d10 + 2 + INT 5 thunder + 1d6 radiant + Arcane Firearm 1d8 + Storm-Arc 1d6 to target + arc 2d6 to two more, DC 16 Dex). Spend a Thunder Wave Round for +1d10 and a Stun save when a stun matters.
- **Bonus:** Activate cannon, Force Ballista at **+10** (2d8 + 2 force, push 5), or Flamethrower / Protector as the field needs.
- **Reaction:** Counter-Bolt when an **ally** is attacked (Disadvantage + a free Boomstick shot), else Shield (self) or Flash of Genius.

---

## Door B: The Sentinel (rebuilt cannon)

Attuned: the Sentinel only (the Dynamo is rebuilt inside it). **Rebuilt Dynamo replaces the Eldritch Cannon feature**: she deploys the Sentinel instead of a cannon, never both.

- **The Sentinel.** Medium construct. **AC 18, HP 40** (5 + five times level), Speed **30 ft.**, STR 14 / CON 16, immune Poison, condition-immune Charmed/Exhaustion/Poisoned. **It moves on its own 30 ft** and acts on her command. Permanent (no duration). **Bound Construct:** add her PB to any check or save it makes. Rebuild for a 1st+ level slot if it hits 0 HP; Mending heals it 2d6.
- **Deploy / recall:** a **Bonus Action** per the Sentinel's own statblock (rarely needed, it is permanent).
- **Activate (Bonus Action), pick one:**
  - **Force Blast.** Ranged attack, her spell attack mod (**+8**), 120 ft, **2d8 + INT (5) force**.
  - **Electric Pulse.** Each chosen creature within **15 ft of the Sentinel**, **DC 16 Dex**, **2d8 + INT (5) lightning**; on a fail they **can't take Reactions** until the start of her next turn; half on a save.
- **Guardian Protocol (Reaction, 1/round).** When an ally **within 15 ft of the Sentinel** takes damage, that ally gains **1d8 + INT (5) temp HP**.
- Note: the Sentinel does NOT gain the Storm Cell's +2, and its printed damage is 2d8 + INT (the Dynamo's +2 is subsumed into the rebuild, not added on top).

**Combat loop (Door B).**
- **Action:** True Strike through Boomstick, to hit **+10** (1d10 + 2 + INT 5 thunder + 1d6 radiant + Arcane Firearm 1d8), or Fire Bolt (+8, 2d10 + 1d8) at range, or a leveled spell.
- **Bonus:** Activate the Sentinel: Force Blast (2d8 + 5, 120 ft) at a lone target, or Electric Pulse (2d8 + 5, DC 16, reaction-lock) into a cluster within 15 ft of the Sentinel. The Sentinel also moves 30 ft on its own.
- **Reaction:** Guardian Protocol (1d8 + 5 temp HP to an ally within 15 ft of the Sentinel), or Shield / Flash of Genius. Walk the Sentinel with the melee so Guardian Protocol can reach them.

---

## Door C: The Awakened Essence Sphere

Attuned: Dynamo + Sphere. She keeps the normal Dynamo-enhanced Eldritch Cannon (Always-on section). The Sphere adds a short-rest pool.

- **Mote Channeling.** The Sphere's powers share **2 uses**, regained on a **Short Rest**. DC = spell save DC 16.
- **Aether Ward (base power, the ONLY power online at L7).** **Magic action** (costs her Action), 1 use: she and each ally **within 15 ft** gain **2d8 + INT (5) temp HP**.
- **Elemental Discharges are ALL LOCKED at level 7.** Cinderstorm (Fire), Drowning Lull (Water), Tailwind (Air), Tectonic Slam (Earth), Soul Siphon (Shadow) each unlock only when that rift's Mote is installed. At Session 8 the Sphere grants **Aether Ward alone** (twice per short rest). A sim must not use any discharge until its rift is cleared.
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
- "Counter-Bolt triggers only on attacks against an ALLY, never Lilly herself" (Door A).
- "Boomstick is a repeating pistol at 30/90, so Fire Bolt is the long-range option" (Boomstick shots and True Strike reach 90 ft max, disadvantage past 30 ft; Fire Bolt reaches 120 ft).
- "the Sentinel's Guardian Protocol reaches only 15 ft from the Sentinel, so it must walk with the melee" (Door B).

---

## Easy-to-forget checklist

- **INT (+5) drives True Strike on BOTH the attack roll and the damage.** True Strike substitutes her spellcasting ability for Dex; the +5 to damage is the single most-dropped number.
- **True Strike to-hit is +10 baseline** (PB 3 + INT 5 + Boomstick +2), on every road including Door A (DM ruling 2026-07-25: the Cell's +2 spell-attack bonus does not stack with Boomstick's weapon +2).
- **Arcane Firearm adds 1d8 thunder to one spell's damage each turn** (via Boomstick). Add it to True Strike, Fire Bolt, a Scorching Ray, Shatter, or Thunderwave, once per turn.
- **The Pocket Dynamo gives the cannon +2 damage** on Flamethrower and Force Ballista (not on Protector temp HP).
- **The cannon fires on a BONUS action**; she still gets her full Action the same turn. Never charge her Action for it.
- **The cannon picks its mode fresh every activation** (house rule); it is never locked in.
- **Flash of Genius reaches allies within 30 ft** (+5 to a failed save or check), not just Lilly; 5 uses per long rest.
- **Gnomish Magic Resistance: advantage on INT/WIS/CHA saves vs spells** (defensive, always on).
- **The dagger is retired on every road**, so spells no longer get the old +2 frost rider; only the +1d8 Arcane Firearm (now thunder via Boomstick) remains.
- **Boomstick range is 30/90.** Do not fire Boomstick or a True Strike shot past 90 ft; use Fire Bolt (120 ft) for range.
- **Door A Storm-Arc fires on every Boomstick hit**: +1d6 lightning to the target and a 2d6 DC 16 Dex arc to two more enemies within 15 ft. Free extra area damage, easily dropped.
- **Door A Counter-Bolt triggers only when an ally is attacked**, never Lilly herself.
- **Door B Sentinel acts on its own turn**, moves 30 ft, and its Guardian Protocol reaction only reaches 15 ft, so keep it walking with the melee.
- **Door C has only Aether Ward online at level 7**; all five Elemental Discharges are locked until their rifts are cleared. Aether Ward costs her Action (Magic action), 2/short rest.
- **Shield (reaction) puts her at AC 25.** Remember she competes for her reaction between Shield, Flash of Genius, Absorb Elements, and (Door A) Counter-Bolt.
