# Stabby Sharpblade: Level-7 Kit Checklist

Goblin Monk 7, Warrior of Breathing (homebrew subclass taken at level 7 in place of Kensei). This is the actionable kit a combat sim must consult so nothing is dropped. Every number traces to `templates/build_compendium.py` (custom content), `templates/build_sheets.py` (base sheet, printed at level 5), the Monk SRD (`reference/srd/04_classes_druid_fighter_monk.md`), and `memory/house_rules.md`. Where a level-7 number is derived from the level-5 sheet, the derivation is shown.

## Level-7 stat block (one line)

HP 59; AC 18; Focus/feature save DC 13; Nichirin attack +10 (1d10+7); base Speed 45 (55 with Sash Fleetstep, 65 while ignited on the Beast door); Focus Points 7 (all refill on a Short Rest, and Uncanny Metabolism refills them on initiative); Proficiency +3; Martial Arts die 1d8; Extra Attack (2 swings) + Bonus-Action Martial Arts strike.

Abilities (unchanged from the level-5 sheet; no ASI falls between level 5 and 7, Monk ASIs are at 4/8/12/16): STR 8 (-1), DEX 20 (+5), CON 16 (+3), INT 8 (-1), WIS 14 (+2), CHA 8 (-1).

Derivations:
- HP 59 = level-5 sheet 43 + 2 levels x (avg 5 on d8 + CON +3) = 43 + 16.
- AC 18 = Unarmored Defense (10 + DEX 5 + WIS 2 = 17) + 1 Sash. (The level-5 sheet already printed 18. The old "jumps to 20 via Agile Parry" note is retired: Kensei is gone.)
- Save DC 13 = 8 + WIS 2 + PB 3. This is the DC for Stunning Strike (CON), every First Form's Prone rider (DEX), and Deflect Attacks redirect (DEX).
- Nichirin +10 = DEX 5 + PB 3 + magic 2. Damage 1d10 (Versatile, two-handed) + DEX 5 + magic 2 = 1d10+7 (Martial Arts 1d8 is smaller, so he keeps the 1d10).
- Speed 45 = goblin 30 + Unarmored Movement +15 (Monk level 6+). The level-5 sheet's "50" predates the +10 to +15 bump; do not use 50 at level 7.
- Focus 7 = Monk level-7 Focus Points (SRD Monk table).

## Always on (base class level 7 + relic + gift)

These apply on every door. Action types are labeled.

Base-class Monk features:
- **Attack action (Action).** Extra Attack: 2 attacks. With the Nichirin: +10 to hit, 1d10+7 each, plus the ignited breath's +2 elemental rider per hit (see doors).
- **Martial Arts strike (Bonus Action, free).** When he takes the Attack action, one Unarmed Strike as a Bonus Action: +8 to hit (DEX 5 + PB 3), 1d8+5. Competes for his Bonus Action with the door's First Form and with Patient Defense / Step of the Wind: he gets exactly one Bonus Action per turn.
- **Empowered Strikes (Passive).** His Unarmed Strike may deal Force instead of its normal type (bypasses bludgeoning resistance).
- **Stunning Strike (Free rider on a hit, 1 Focus, once per turn).** Once per turn when he hits with a Monk weapon or Unarmed Strike, spend 1 Focus: target makes a CON save DC 13. Fail = Stunned until the start of his next turn; success = Speed halved and the next attack against it has Advantage.
- **Patient Defense (Bonus Action).** Free tier: Disengage for 0 Focus (house rule / 2024 RAW). Spend 1 Focus to also Dodge.
- **Step of the Wind (Bonus Action).** Free tier: Dash for 0 Focus. Spend 1 Focus to also Disengage and double jump distance.
- **Deflect Attacks (Reaction).** When an attack that includes Bludgeoning/Piercing/Slashing hits him, reduce total damage by 1d10 + DEX 5 + Monk level 7 = **1d10+12**. If reduced to 0, spend 1 Focus to redirect: a creature within 5 ft (melee) or 60 ft (ranged) makes a DEX save DC 13 or takes 2d8+5 of the attack's type. (Level-5 sheet said 1d10+10; at level 7 it is 1d10+12.)
- **Evasion (Passive, new at level 7).** On any effect allowing a DEX save for half: success = no damage, failure = half.
- **Uncanny Metabolism (Free, on initiative, 1/long rest).** When he rolls Initiative, regain ALL expended Focus and heal 7 (Monk level) + 1d8. (Level-5 sheet said 5 + 1d8; at level 7 it is 7 + 1d8.)
- **Slow Fall (Reaction).** Reduce fall damage by 35 (5 x Monk level 7).
- **Unarmored Movement.** +15 ft (folded into Speed 45 above).

Goblin traits (Passive unless noted):
- **Fury of the Small.** When he hits a creature larger than him (almost everyone), +3 damage. Once per turn, 3/long rest.
- **Nimble Escape (Bonus Action).** Disengage or Hide as a Bonus Action every turn (another Bonus-Action competitor).
- **Fey Ancestry.** Advantage on saves against the Charmed condition.
- **Darkvision 60 ft** (extended to 120 ft on the Shadow door). Speaks Common, Goblin, Orc.

Relic, the Sash of the Swift Current, Rewoven (attuned, always worn):
- **+1 AC (Passive).** Stacks with Unarmored Defense; already in the AC 18 above.
- **Fleetstep (Passive).** +10 ft walking Speed; already in the 55-with-Sash figure.
- **Air Dance (Bonus Action, 1/day). THE MOST-FORGOTTEN ITEM.** Gain a fly speed equal to his walking speed for 1 minute. A sim must remember Stabby can take the fight into the air once per day.
- **Feather Fall (Reaction, 1/day, no components).**

Gift, the Candyfang Katana (heirloom, superseded by the Nichirin):
- Retired from the loadout: it is a keepsake at his belt, unattuned, since the Nichirin took the blade slot. Do not stack Candyfang's cold rider or Sugar Rush with the Nichirin. (Sugar Rush, if the DM ever re-attunes it: Bonus Action, 1/long rest, 2d8 + CON temp HP. Not active by default.)

Signature weapon, the Nichirin Katana (attuned, replaces Kensei loadout):
- **Weapon stats.** Longsword profile: 1d8 Slashing, Finesse, Versatile (1d10), counts as a Monk weapon, uses DEX. +2 magic to attack and damage. So +10 / 1d10+7 two-handed.
- **Cleansing Edge (Free rider, once per turn). EASY TO FORGET.** Once per turn when he hits a Fiend, Undead, shadow creature, or planar-corrupted creature, until the start of his next turn that target can't regain Hit Points and can't benefit from magical Darkness or shadowy concealment against him. Pure upside against the campaign's rift enemies.
- **Breath-Kindled Steel (Passive).** The blade takes the color of the ignited form and sheds Dim Light.

Retired at level 7 (do NOT use): Agile Parry (no more +2 AC after punch-and-swing), Kensei's Shot (+1d4 on longbow), Kensei weapon tricks. The Repeating Longbow +1 is now just a good +1 bow: +9 to hit, 1d8+6, no Kensei rider.

## Door A: Beast Breathing (the Bloodfang Form)

Granted at monk levels he has (3 and 6). Grants the Nichirin Katana. First Form replaces Flurry of Blows.

Level 3 kit:
- **Monk Weapons.** The katana counts as a Monk weapon (Martial Arts die usable; Bonus-Action Unarmed Strike still available).
- **Beast Sense (Passive).** Advantage on WIS (Survival) to track, WIS (Perception) relying on smell/hearing, and CHA (Intimidation).
- **Igniting the Breath (Free, on initiative, 1 Focus).** Lasts until combat ends / Incapacitated / he ends it. Weapon glows blood-red; every hit with it deals +2 Force damage.
- **Beast's Vigor (Passive while ignited).** Speed +10 (this is the source of the 65 ft figure: 45 base + 10 Sash + 10 Vigor) and Advantage on DEX saving throws.

Level 6, First Form: Devour (Bonus Action, 1 Focus; replaces Flurry):
- Move up to 15 ft without provoking Opportunity Attacks, make one Monk-weapon attack. On hit: **3d8 + DEX 5 + Nichirin 2 + ignited 2 = 3d8+9 Force** instead of normal weapon damage. If it drops the target to 0 HP, **regain the spent Focus.** (The compendium's "3d8 + 5" descriptive line counts only DEX; with the riders it is 3d8+9.)

Beast combat loop:
- Initiative: ignite the breath (1 Focus); Uncanny Metabolism refills Focus to 7 and heals 7+1d8. Speed is now 65.
- Action: Attack, 2 Nichirin swings at +10 for 1d10+7 +2 Force each; Stunning Strike (1 Focus, CON DC 13) on the first hit against a boss; Fury of the Small +3 once.
- Bonus Action: First Form: Devour (1 Focus), a third strike for 3d8+9 Force with 15 ft of free repositioning; Focus refunds if it kills.
- Reaction: Deflect Attacks (reduce 1d10+12; redirect 2d8+5 DEX DC 13 if reduced to 0).

## Door B: Water Breathing (the Monastery Form)

Grants the Nichirin Katana. First Form replaces Flurry of Blows.

Level 3 kit:
- **Monk Weapons.** As above.
- **Igniting the Breath (Free, on initiative, 1 Focus).** Weapon glows pale blue; every hit with IT deals +2 Cold. (House ruling: the rider says "with it," so the Bonus-Action Unarmed Strike does NOT carry the +2 Cold; only Nichirin hits and the First Form do.)
- **Flowing Guard (Passive while ignited).** +2 AC against the first attack roll made against him before the start of each of his turns.

Level 6, First Form: Flowing Strike (Bonus Action, 1 Focus; replaces Flurry):
- Move up to 15 ft without provoking, one Monk-weapon attack. On hit: **3d8+9 Cold** (3d8 + DEX 5 + Nichirin 2 + ignited 2) instead of normal. On a hit, the target also makes a DEX save DC 13 or is knocked Prone.

Level 6, Healing Spring, First Water (Bonus Action, 1/short or long rest):
- Touch self or a creature; it regains **2d8 + WIS 2**. A non-Focus support option that competes for his Bonus Action.

Water combat loop:
- Initiative: ignite (1 Focus); Uncanny Metabolism refills + heals; Flowing Guard is up.
- Action: Attack, 2 Nichirin swings +10 for 1d10+7 +2 Cold each; Stunning Strike option; Fury of the Small +3 once.
- Bonus Action: First Form: Flowing Strike (1 Focus) for 3d8+9 Cold + Prone (DEX DC 13); OR, if an ally is hurt, Healing Spring (1/rest) for 2d8+2.
- Reaction: Deflect Attacks (1d10+12; redirect option).

## Door C: Shadow Breathing (the Idol Form)

Grants the Nichirin Katana. First Form replaces Flurry of Blows.

Level 3 kit:
- **Monk Weapons.** As above.
- **Eyes of the Idol (Passive).** Darkvision +60 ft on top of the goblin's 60 = **Darkvision 120 ft**; Advantage on DEX (Stealth).
- **Igniting the Breath (Free, on initiative, 1 Focus).** Weapon glows violet-black; every hit with it deals +2 Necrotic.
- **One With the Gloom (Passive while ignited).** +2 AC against ranged attack rolls, and he sees normally in magical Darkness.

Level 6, First Form: Umbral Slash (Bonus Action, 1 Focus; replaces Flurry):
- Teleport up to 15 ft to an unoccupied space within 5 ft of a creature. Magical Darkness then fills a 10-ft Cube containing that creature. One Monk-weapon attack against it with **Advantage**. On hit: **3d8+9 Necrotic** (3d8 + DEX 5 + Nichirin 2 + ignited 2) instead of normal. He sees through this Darkness; it lasts until the end of his next turn (or he ends it, no action).
- Table caution (compendium DM note): the gloom is his alone. Allies have Disadvantage on ranged attacks against a creature in the gloom, and spells needing a visible target can't reach it; party should pick other targets while the shadow works.

Shadow combat loop:
- Initiative: ignite (1 Focus); Uncanny Metabolism refills + heals; +2 AC vs ranged and darkvision 120 online.
- Action: Attack, 2 Nichirin swings +10 for 1d10+7 +2 Necrotic each; Stunning Strike option; Fury of the Small +3 once. (Cleansing Edge shines here versus shadow/undead: no HP regain, no darkness benefit against him.)
- Bonus Action: First Form: Umbral Slash (1 Focus), teleport + Advantage strike for 3d8+9 Necrotic, dropping concealing Darkness the enemy can't see through but he can.
- Reaction: Deflect Attacks (1d10+12; redirect option).

## House-rule interactions that apply to this hero

Quoted from `memory/house_rules.md`:

- "Patient Defense's free tier is Disengage as a Bonus Action; Dodge costs 1 Focus Point (2024)."
- "Printed-text rulings confirmed in play (2026-07-18): the Water ignite rider reads 'whenever you hit a target with IT', so Stabby's Bonus Action Unarmed Strike does NOT carry the +2 Cold" (Water door only).
- Subclass rule (compendium): "every First Form replaces Flurry of Blows." Stabby has no Flurry of Blows at level 7; his Bonus-Action attack option is the door's First Form.
- Loadout ruling (compendium, "Setting Down the Kensei's Way"): at level 7 the Kensei tricks retire (Kensei's Shot, Agile Parry) and Candyfang becomes an unattuned heirloom, superseded by the Nichirin.

## Easy-to-forget checklist

- **Sash Air Dance:** 1/day Bonus Action, fly speed = walking speed for 1 minute. The single most-dropped item.
- **Ignite the breath at initiative** (1 Focus): sets the +2 elemental rider on every weapon hit for the whole fight, plus the door's passive (Beast +10 speed and DEX-save Advantage / Water Flowing Guard +2 AC / Shadow darkvision 120 and +2 AC vs ranged). Do not forget the rider on each hit.
- **Uncanny Metabolism** on initiative (1/long rest): full Focus refill + heal 7+1d8. Effectively ignite-for-free on turn one.
- **Nichirin Cleansing Edge:** once per turn vs Fiend/Undead/shadow/planar-corrupted, target can't heal and can't hide in Darkness against him. Free, always available, big against rift enemies.
- **Deflect Attacks:** the Reaction is 1d10+12 at level 7 (not the sheet's old 1d10+10); redirect for 2d8+5 DEX DC 13 on a full block.
- **Patient Defense free Disengage:** 0 Focus (do not charge a Focus for plain Disengage). Nimble Escape also gives Bonus-Action Disengage/Hide.
- **Evasion:** DEX-save-for-half effects deal no damage on success.
- **Empowered Strikes:** the Unarmed Strike can be Force to bypass resistance.
- **Fury of the Small:** +3 once per turn vs larger foes, 3/long rest; sims routinely skip it.
- **First Form damage is 3d8+9, not 3d8+5:** the +2 Nichirin and +2 ignited riders apply; the compendium's "+5" is DEX-only shorthand.
- **Devour Focus refund (Beast):** a killing First Form gives the Focus back.
- **Water +2 Cold does NOT ride the Bonus-Action Unarmed Strike** (house ruling); only Nichirin hits and the First Form.
- **Speed is 45 base at level 7** (55 with Sash, 65 ignited on Beast), not the level-5 sheet's 50.
- **Feather Fall** 1/day and **Slow Fall** (reduce 35) are both available as Reactions.
