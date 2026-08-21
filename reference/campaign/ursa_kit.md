<!--
Ursa Catchum level-7 KIT CHECKLIST for combat sims.
Custom-content numbers trace to templates/build_compendium.py (the authoritative
relic / gift / path-reward stat blocks). Base-class numbers trace to
templates/build_sheets.py (Ursa is level 5 there) with level-7 derivations shown.
Subclass RAW grounding: reference/expansions/druid-circle-of-stars.md.
House rules: memory/house_rules.md. No em dashes (house style).
-->

# Ursa Catchum, Level 7 Kit Checklist (combat sim reference)

**Human (Mark of Handling) Druid 7, Circle of the Stars. Wisdom-based caster.**

A sim MUST walk this whole list each round or it will drop features. The most-dropped items are called out with (FORGOTTEN) tags and repeated in the final section.

## Level-7 stat block (one line)

HP **52** | AC **18** | Speed **30 ft.** | Init **+2** | Prof **+3** | Spell save **DC 16** | Spell attack **+10** holding the Wand of the War Mage +2 (**+8** without) | Shillelagh (weapon attack, +1 staff) **+9** | STR 8(-1) DEX 14(+2) CON 14(+2) INT 12(+1) **WIS 20 (+5)** CHA 8(-1)

> **[DM RULING 2026-07-25, confirmed] The +1 light bonus is ALLIES ONLY, not Ursa.** build_compendium.py line 122 grants Guiding Light to "allies," and Warden's Mantle (line 626) to "each ally within that light." By the printed text Ursa does NOT raise his own attacks or saves, so his spell attack is **+8**, not +9. Earlier sims used "+9 in his own light," which was wrong. Ursa's own attacks and saves get no bonus from his own light; his spell attack is +8.
Resources: **Wild Shape 3/rest** (1 back on short rest, all on long) | **Spell slots 4/3/3/1** (1st/2nd/3rd/4th) | **Staff 5 charges** (6 on the Starlit road) | **Cosmic Omen = Wis mod = 5 uses/long rest** | **Star Map free Guiding Bolts = Wis mod = 5/long rest**.

### Derivations (base numbers are level-5 on the sheet; level 7 shown here)
- **HP 52.** Sheet HP is 38 at level 5 (build_sheets.py). Druid d8, +2 levels x (5 avg + 2 Con) = +14. 38 + 14 = **52**.
- **AC 18.** Spiked armor + shield, unchanged from the sheet.
- **Prof +3.** Levels 5 through 8 all use +3, so DC and attack are unchanged: DC 16 = 8 + 3 + 5(Wis); spell attack +8 = 3 + 5(Wis), and **+10 while he holds the Wand of the War Mage +2** that Lilly built him. (The Amulet/Warden +1 is allies-only, see the DM CHECK above.) Shillelagh weapon attack = 5(Wis) + 3(PB) + 2(the Staff is a **+2** quarterstaff once awakened on Door B, which he took) = **+10**.
- **Wild Shape 3 uses.** Sheet shows 2 (level 5). Circle-of-Stars RAW: 3 uses at level 7 (druid-circle-of-stars.md). Starry Form spends one of these.
- **Spell slots 4/3/3/1.** Sheet shows the level-5 line 4/3/2. At druid 7 he gains a **4th-level slot**; this sets Mightier Summons' cap (Door C) at spell level 4.
- **Cosmic Omen** gained at druid level 6; **Elemental Fury (Potent Spellcasting)** gained at druid level 7.
- **Star Map free Guiding Bolts = 5**, not the "3" printed on the level-5 sheet: RAW is Wis modifier per long rest (druid-circle-of-stars.md), and Wis 20 = +5. Use 5.

---

## Always on (base class 7 + relic + gift)

Consult every entry below every round.

### Base class (Circle of the Stars, level 7)

- **Starry Form** (Bonus Action, spend 1 Wild Shape use; lasts 10 min; ends on Incapacitated / dismissal / reuse). Sheds Bright Light 10 ft + Dim 10 ft. Keep his own stats. Choose ONE constellation on activation:
  - **Archer.** On activation and **each later turn as a Bonus Action**: ranged spell attack **+10** (wand; +8 without), one creature within **60 ft**, **1d8 + 5 radiant**. (Still 1d8 + Wis at level 7; becomes 2d8 at level 10.) **House rule 1: Starseed does NOT apply to the arrow.**
  - **Chalice.** When he casts a **slot** spell that restores HP, he or a creature within 30 ft also regains **1d8 + 5**.
  - **Dragon.** Treat a d20 of 9 or lower as a 10 on Int/Wis checks and **Con saves to keep Concentration**.
- **Star Map** (druidic focus, always in hand as backup). Guidance + Guiding Bolt always prepared. **Free Guiding Bolt 5/long rest** (no slot). Guiding Bolt = Action, 120 ft, **+10** (spell attack with the wand; +8 without): **4d6 radiant + 1d8 Starseed** (once/turn), and the next attack vs that target before Ursa's next turn has **Advantage**. (FORGOTTEN: spend these 5 free bolts before real slots.)
- **Cosmic Omen** (level 6). **Reaction**, when a creature he can see within 30 ft is about to make a D20 Test: Weal **+1d6+2** or Woe **-1d6-2** (the flat +2 comes from Reader of Omens; the base feature is a plain 1d6). **Uses = Wis mod = 5/long rest** (base form: even roll = Weal, odd = Woe for the day; Door B removes that limit). Declare **before** the die is rolled in the base version; **Ursa took Reader of Omens, so he declares AFTER the die lands** (Read the Moment, below). A sim must resolve his Reaction with the roll already known.
  - [DM CHECK self-target: 2024 wording is ambiguous whether Ursa may target his own D20 Test; safe reading is others-only. See druid-circle-of-stars.md.]
- **Elemental Fury = Potent Spellcasting** (level 7). **+5 (Wis) to the damage of any Druid cantrip** (Starry Wisp, Shillelagh, Thorn Whip, etc.). House rule 2 also lets it ride the kindled staff once/turn; no double-dip with a cantrip the same turn.
- **Wild Shape 3 uses.** Fuels Starry Form (or a beast form). Regain 1 on short rest, all on long.
- **Wild Resurgence.** Once/turn (no action), **only if you have no Wild Shape uses left**: spend a spell slot to regain 1 Wild Shape use. Once/long rest (no action): spend a Wild Shape use to regain a 1st-level slot.
- **Mark of Handling.** Wild Intuition (+1d4 Animal Handling/Nature). **Primal Connection 1/short rest**: free Animal Friendship or Speak with Animals. The Bigger They Are (beasts + dumb monstrosities).

### Relic: Staff of Waking Constellations (attuned; build_compendium.py lines 85-91)

- **+2 quarterstaff, druidic focus** (printed +1; awakened to +2 at his father's shrine on Door B).
- **Charges: 5, regain 1d4 + 1 at dawn.** Spend on: **Guiding Bolt (1)**, **Faerie Fire (1)**, **Moonbeam (2)**. (On the Starlit road: **6 charges, regain 1d4 + 2**, see Door A.) (FORGOTTEN: these charges are separate free casts from the Star Map bolts.)
- **Starseed.** Once per turn, **+1d8 radiant** (1d4 before the shrine awakened the staff) when Ursa deals radiant damage **with a druid spell** (house rule 1: druid spells only, NOT the Archer arrow). Applies to Guiding Bolt, Moonbeam, Starry Wisp.
- **Starlight.** Bonus Action: 10 ft dim light; advantage on night navigation.
- **Shillelagh** (cantrip, Wis-based; on his sheet). Bonus Action to ignite, 1 min. Ignited staff: **+10 to hit** (Wis 5 + PB 3 + the Staff's +2; the +1 light aura is allies-only, so no self bonus), **1d10 + 7** force/bludgeoning. Potent Spellcasting adds **+5 once/turn** (house rule 2).

### Gift: Amulet of Guiding Light (attuned; build_compendium.py lines 119-124)

- **Guiding Light (Passive, while in Starry Form).** **Every ally within 30 ft** (awakened on Door B; it used to reach only those standing in the light) gets **+1 to attack rolls and saving throws** (allies only, not Ursa himself: build_compendium.py line 122 reads "allies gain +1"). This is a party buff, not a self buff.
- **Starry Glow (Reaction, 1/long rest).** When he or a nearby ally is hit: attacker takes **2d8 radiant** and must make a **DC 15 Con save or be Blinded**. (FORGOTTEN: this is the single most-dropped item on Ursa's sheet. Check it on every enemy hit that lands.)
- **Celestial Resilience (2/long rest).** Reroll a natural 1 (on any of his d20 rolls). (FORGOTTEN.)

---

## Door C: Beast Handler (the wild; build_compendium.py lines 508-609)

Added kit if Ursa walked this road.

- **Feat: Beast Handler** (story feat, no ASI).
  - **Mightier Summons.** Summon Beast takes effect as if cast with **the highest slot he can cast (spell level 4 at level 7), without expending a slot of that level**. Casting still costs a 2nd-level+ slot and Concentration; the spirit just runs at spell level 4 for free. This is the "free Summon Beast" upcast.
  - **Signature Partners.** Summon Beast conjures one of **Arcanine (Land), Lapras (Water), or Noctowl (Air)** using the Signature Partner block, not a nameless spirit.
  - **Wild Speech.** Simple telepathy with any summoned beast.
- **Signature Partner stat block at spell level 4** (derive from build_compendium.py lines 533-591; spell level = 4):
  - **AC = 11 + 4 = 15.** **HP = 30 + 10x(4-2) = 50** (Noctowl **40**). Speed per partner (Arcanine 40 + climb 40; Lapras 30 + swim 40; Noctowl 20 + fly 60).
  - **Multiattack = half spell level round down = 2 Rends.** **Rend:** +8 (Ursa's spell attack), reach 5, **1d8 + 4 + 4 = 1d8 + 8 PIERCING** (the stat block says Piercing, not slashing).
  - **Arcanine:** Intimidate on appearance (enemies within 15 ft, Wis save DC 16 or -2 to attacks until end of their next turn); **Extreme Speed** (move + 1 Rend, +8 fire on hit = twice spell level). Immune Fire, Vuln Cold.
  - **Lapras:** Shell Armor (can't be crit); **Ice Beam** (replace a Rend: ranged +8, 60 ft, 1d8 + 8 cold, target Speed -10). Immune Cold, Vuln Lightning.
  - **Noctowl:** Keen Eye + Flyby; **Hypnosis (Recharge 5-6)**, one creature within 30 ft, Wis save DC 16 or Incapacitated. Immune Necrotic, Vuln Lightning.
- **Keepsake: Wildheart Token.** When a partner Ursa summoned would drop to 0 HP, it drops to **1 HP** instead. **1/dawn.** (FORGOTTEN on the partner's death.)

**Combat loop (Door C):**
- Action: Guiding Bolt (free, Star Map) or Starry Wisp cantrip (2d8 + 5 Potent + 1d8 Starseed). (Summon Beast pre-cast; keep Concentration.)
- Bonus Action: Star-Arrow (Archer, 1d8 + 5) or ignite/refresh a Bonus-Action option.
- Free / Reaction: partner acts on Ursa's initiative (Multiattack or Extreme Speed / Ice Beam / Hypnosis); Reaction held for Cosmic Omen or Amulet Starry Glow; Wildheart Token if the partner drops.

---

## Door A: Starlit Channeler (the sky; build_compendium.py lines 611-656)

Added kit if Ursa walked this road.

- **Feat: Starlit Channeler** (story feat, no ASI; prereq Starry Form).
  - **The Warden's Mantle.** Learns Shillelagh (Wis). On assuming Starry Form, casts Shillelagh through the Staff **as part of the same Bonus Action**, and it **lasts until the form ends** (not 1 min). While Starry Form is active, for **whichever constellation** he chose: the Staff's Starlight kindles with the form (**no action**) and reaches **20 ft**; **each ally in that light gets +1 to attacks and saving throws**; the kindled staff deals **Radiant**, and on a hit the target takes **+1d6 radiant** (2d6 at druid 11, 3d6 at 17, so **1d6 at level 7**); the Warden figure stands guard.
    - [Stacking flag: Warden's Mantle +1 and the Amulet's Guiding Light +1 are the same untyped bonus to the same rolls (both allies-only). They do **not stack**: an ally in the light gets +1, not +2. Neither applies to Ursa himself.]
  - **Warden's Intercession.** **Reaction**, while Starry Form is active, when a creature he can see hits an ally within his Starlight: reduce that damage by **1d8 + 5 (Wis)**.
  - **Constellation Gifts (while Starry Form active):** Archer, on a luminous-arrow hit the next attack vs that creature before his next turn has **Advantage**; Chalice, split the Chalice heal between two creatures within 30 ft; Dragon, allies in Starlight treat a d20 of 9 or lower as 10 on **Con saves to keep Concentration**.
- **Keepsake: The Staff Wakes Further.** Staff now has **6 charges, regain 1d4 + 2 at dawn** (replaces the base 5 / 1d4+1).

**Kindled-staff strike on this road** (Action, melee): **+9 to hit** (Shillelagh: Wis 5 + PB 3 + Staff +1; the light aura is allies-only, no self bonus), damage **1d10 + 6 (base) + 1d6 radiant (Warden's Mantle) + 1d4 Starseed (once/turn, now applies because the staff deals Radiant) + 5 Potent (once/turn, house rule 2)**. Starseed and Potent are each once/turn; Potent cannot also ride a cantrip the same turn.

**Combat loop (Door A):**
- Bonus Action: Starry Form + Shillelagh through the Staff (one Bonus Action) to raise the 20-ft radiant Starlight over the party.
- Action: melee kindled-staff strike (+10, radiant, +1d6 + Starseed + Potent) or Guiding Bolt / cantrip if ranged.
- Reaction: Warden's Intercession (soak 1d8 + 5 for an ally) or Cosmic Omen or Amulet Starry Glow.

---

## Door B: Reader of Omens (the father's trail; build_compendium.py lines 658-717)

Added kit if Ursa walked this road.

- **Feat: Reader of Omens** (story feat, no ASI; prereq Cosmic Omen).
  - **Omen Dreams.** After a Long Rest, roll **two d20s** and record them. When he or a creature he can see is about to make a D20 Test, **replace the d20 roll with one omen** (no action, **before** the roll). Each omen used once; unused omens lost at the next Long Rest.
  - **Both Omens.** After a Long Rest he gains access to **both Weal and Woe** until the next Long Rest (not one or the other).
  - **Read the Moment.** When he takes the Cosmic Omen Reaction, he may wait until **after the d20 is rolled** but before knowing success/failure, then choose Weal (+1d6+2) or Woe (-1d6-2).
  - **The Stronger Tide.** Weal adds **1d6 + 2** and Woe subtracts **1d6 + 2** (the base feature is a plain 1d6).
  - **Awakened Gifts.** The pilgrimage wakes what he already carried: the **Staff becomes a +2** quarterstaff, **Starseed rises from 1d4 to 1d8**, and the **Amulet's Guiding Light reaches every ally within 30 ft**.
  - **Shared Tides.** Cosmic Omen is a **single pool = Wis mod = 5 uses/long rest**, each spent on Weal or Woe; regain all on a Long Rest. [DM CHECK: printed text omits the SRD "(minimum of once)" floor; flagged, not fixed.]
- **Keepsake: Ash's Sigil-Stone** (**no attunement**: DM ruling 2026-08-17, a keepsake rather than a bonded relic, which frees the third slot for Lilly's wand).
  - **Aura of Vitality** cast from the stone **without a slot, 1/long rest**. RAW (verified dnd2024.wikidot.com/spell:aura-of-vitality, 2026-08-19): 3rd-level, **Action** to cast, Self, **Concentration up to 1 minute**, a 30-ft Emanation. It heals **2d6 to one creature in it when he creates the aura AND at the start of each of his turns**, and those ticks cost him **no action at all** (an earlier note here said Bonus Action; that was wrong). Two consequences worth playing: it **competes with Summon Fey and Moonbeam for his concentration**, and out of combat he can simply run the whole minute for about **11 ticks, roughly 70 hit points** across the party, which is the party's only real between-fight healing.
  - **2 charges, regain all at dawn.** Magic action, spend 1 charge: **Ask the Day** (one truthful yes/no about the day), **Glimpse the Trail** (reveal one rift-board space within 1 mile), or **Read the Heart** (a visible creature's mood/attitude). Mostly exploration, but Aura of Vitality is the combat piece.

**Combat loop (Door B):**
- Pre-combat: note the **two Omen Dreams** (bank a high roll to force a hit, or a low roll to sink a boss save); track the **5-use** Weal/Woe pool.
- Turn: Action Guiding Bolt / cantrip; Bonus Action Star-Arrow or Healing Word. (An Aura of Vitality tick is NOT a Bonus Action: it fires automatically at the start of his turn while he concentrates, so he still gets his full turn.)
- Reaction: Cosmic Omen with **Read the Moment** (apply +1d6+2 / -1d6-2 after seeing the die) is the signature play; still holds Amulet Starry Glow as an alternate.

---

## House-rule interactions that apply to this hero

Quoted from memory/house_rules.md:

1. "Ursa's Starseed +1d4 applies only to actual druid spells, NOT the Starry Form Archer luminous arrow." (So Guiding Bolt / Moonbeam / Starry Wisp get +1d4 once/turn; the Archer arrow never does. On Door A the kindled staff deals Radiant and counts as a druid-spell strike, so Starseed rides it.)
2. "Potent Spellcasting rides the kindled staff once per turn (Ursa, from level 7; no double-dipping with a cantrip in the same turn)." (So +5 lands on EITHER a cantrip OR the kindled staff each turn, not both, and only once.)

Relevant 2024 RAW notes (recorded so the sim never regresses):
- Goodberry: eating a berry is a **Bonus Action**.
- Shillelagh replaced Primal Savagery on his sheet (Primal Savagery does not exist in 2024).
- Deep gnome / other migration notes do not affect Ursa; the Air Bestial Spirit has 20 HP by its own block (relevant only to his base Summon Beast, not the Door C Signature Partner).

---

## Easy-to-forget checklist (the things sims dropped)

- **Amulet Starry Glow** (Reaction, 1/long rest): on a hit to Ursa or a nearby ally, attacker takes 2d8 radiant, DC 15 Con or Blinded. The single most-forgotten item.
- **Amulet Guiding Light**: +1 attacks AND saves to **allies** in his Starry Form light (allies only, NOT Ursa; his own spell attack is +8, see the DM CHECK at the top).
- **Amulet Celestial Resilience**: reroll natural 1s, 2/long rest.
- **Star Map free Guiding Bolts**: 5/long rest (NOT the stale "3" on the level-5 sheet), spent before real slots.
- **Staff charges**: 5 (or 6 on Door A), regain 1d4+1 (1d4+2 on Door A) at dawn; Guiding Bolt(1) / Faerie Fire(1) / Moonbeam(2). Separate pool from the Star Map bolts.
- **Starseed +1d8**: once/turn, druid radiant spells only, never the Archer arrow.
- **Potent Spellcasting +5**: druid cantrip damage; rides the kindled staff once/turn; no double-dip with a cantrip the same turn.
- **3 Wild Shape uses** at level 7 (was 2 at level 5); Starry Form spends one; Wild Resurgence converts slot <-> Wild Shape.
- **Cosmic Omen**: 5 Reaction uses/long rest (Door B: single pool, both Weal and Woe, Read-the-Moment after the die).
- **Starry Form Archer**: a Bonus-Action 1d8+5 arrow EVERY turn, not just on activation.
- **Free Animal Friendship / Speak with Animals** (Mark of Handling, 1/short rest), no slot.
- **Door C: Wildheart Token** (partner drops to 1 HP not 0, 1/dawn).
- **Door A: Warden's Intercession** (Reaction, soak 1d8+5 for an ally in the light) and the +1d6 radiant staff rider.
- **Door B: Omen Dreams** (two pre-rolled d20s banked from the morning) and Ash's Sigil-Stone Aura of Vitality (free 1/long rest).

## Conjure Animals (DM 2026-08-21: his damage go-to)

- **3rd level, Action, 60 ft, Concentration 10 min.** SRD 5.2 verified (`reference/srd/10_spells_intro_and_a-c.md:1117`).
- A Large spectral pack appears in an unoccupied space. **When Ursa moves on his turn he may move the pack up to 30 ft**, and that costs no action or bonus action.
- **Trigger, twice over:** whenever the pack moves within 10 ft of a creature he can see, AND whenever a creature he can see enters a space within 10 ft of it or ends its turn there, he may force a **Dex save vs DC 16**. Fail = **3d10 slashing**, no damage on a success. **Once per creature per turn.**
- Upcast: +1d10 per slot level. His 4th-level slot makes it 4d10.
- He also has **Advantage on Strength saves** while within 5 ft of the pack.
- **Starseed does NOT ride it**: the staff's rider is radiant-only, and this is slashing.
- **It is BLANK against the Session 8 boss objective.** The Spike is immune to slashing (it is immune to everything except radiant and force), so the pack does nothing to it. Groudon itself is a fair target; the Spike is not. On that fight his damage is Guiding Bolt and Starry Wisp, and his concentration is better spent on Polymorph.
- **CONCENTRATION**: this competes directly with Summon Beast and Summon Fey. A sim must never run the pack and a summon at the same time. The expected play is pack + Starry Form (Archer), since Starry Form is not concentration.
- Replaced **Thunderwave** on his prepared list; upcast Guiding Bolt covers that job at 120 ft.

## Thorn Whip replaces Shillelagh (DM 2026-08-21)

- **Shillelagh is off his list.** It cost a Bonus Action to light and only paid off in melee, which is the last place a 52-HP druid wants to be. His Bonus Action belongs to the Starry Form arrow.
- **Thorn Whip** (verified on dnd2024.wikidot.com 2026-08-21, not in the SRD subset): Transmutation cantrip, **Action**, **Range 30 ft**, melee spell attack, **1d6 piercing scaling to 2d6 at level 5**, and **if the target is Large or smaller, pull it up to 10 ft closer to you**.
- At his level: **+10 to hit, 2d6 + 5 (Potent Spellcasting) piercing, 30 ft**. No Bonus Action, no duration to track.
- **Starseed does NOT ride it** (piercing, and the staff's rider is radiant only). Same as Conjure Animals.
- **Damage ranking is unchanged: Starry Wisp is still his bigger cantrip** (2d8 + 5 radiant + 1d8 Starseed at 60 ft). Thorn Whip is the *positioning* cantrip.
- **The combo, and the reason for the swap:** the 10-ft pull is forced movement, so it drags a target INTO the Conjure Animals pack's 10-ft aura (triggering its DC 16 Dex save for 3d10 as the creature enters), ACROSS Spike Growth (2d4 per 5 ft travelled), or out of the party's backline. A sim should treat Thorn Whip plus an active emanation as a single combined play.
