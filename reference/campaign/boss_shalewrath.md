<!--
DM-side boss card, sim-tuned v3. NOT in the published bestiary: the compendium
records creatures the kids actually faced, and the Shalewrath has not been
played. It graduates to build_bestiary.py if and when it hits the table.
Tuning provenance: two full adversarially-audited sims against the level-7
four (Lilly Sentinel door, Stabby Beast, Ursa Beast Handler + Arcanine,
Sandshrew). v1 (230 HP, blanket Thunder vulnerability) died in 2 rounds + a
swing; v2 (340 HP, two-way seams, vulnerability kept) died in 2 rounds + a
turn. Sustained party output ~115-200/round across ~10 attack rolls. The v3
changes below implement the sims' verdict. No em dashes (house style).
-->

# THE SHALEWRATH, Corrupted Warden of the Underroot (v3, sim-tuned, unplayed)

An Earth-rift elite for Session 8+: a gentle burrowing warden of the deep
roads, corrupted by rift-light, fighting like a cornered animal until freed.
Epic-not-lethal: spread its attacks, never focus a downed hero, and play the
final blow as the corruption breaking, not a kill.

Huge Elemental (planar-corrupted), unaligned
AC 18 (slate plates)   HP 340   Speed 40 ft., burrow 40 ft.
STR 22 (+6)  DEX 10 (+0)  CON 20 (+5)  INT 6 (-2)  WIS 14 (+2)  CHA 8 (-1)
Saves Con +9, Wis +6   PB +4
Resistances bludgeoning, piercing, slashing from nonmagical attacks
Immunities poison; Charmed, Poisoned, Exhaustion
Senses darkvision 60 ft., tremorsense 60 ft.; passive Perception 12

## Traits
- **Cracked Seams (the thunder hook).** There is NO blanket Thunder
  vulnerability (v1/v2 had one; it doubled Lilly's whole package every turn
  and single-handedly broke the math). Instead, when the Shalewrath takes
  Thunder damage, its plates split along glowing seams until the end of its
  next turn: attack rolls against it have Advantage (all of them, the full
  window), AND rift-light vents from the cracks, so its Slam attacks deal an
  extra 2d10 Force during the window. Telegraph both halves the first time.
  The kids choose when to crack it open.
- **Legendary Resistance (2/day).**
- **Corrupted Guardian.** Counts as planar-corrupted (Stabby's Cleansing Edge
  applies).

## Actions
- **Multiattack.** Two Slams. It can replace one Slam with Grinding Maw if a
  creature is Grappled by it.
- **Slam.** +10 to hit, reach 10 ft., 2d10+6 Bludgeoning. A Medium or smaller
  target hit must succeed on a DC 16 Str save or be Grappled (escape DC 16)
  or knocked Prone, the Shalewrath's choice. (v3: the grab option feeds
  Grinding Maw, which never fired in either sim.)
- **Grinding Maw.** One creature Grappled by it: 3d8+6 Piercing, no attack
  roll (escape DC 16 ends it).
- **Shard Spray (Recharge 5-6).** 30-ft cone: DC 16 Dex, 6d6 Piercing, half
  on success.

## Bonus Actions
- **Quake Step.** Ground within 15 ft becomes Difficult Terrain until its
  next turn; each creature standing there: DC 15 Str save or fall Prone.

## Legendary Actions (3/round, end of another creature's turn; v2 had 2)
- **Slam (1).**
- **Undermine (1).** Burrow up to 20 ft without opportunity attacks and
  surface. SCRIPT THIS AT THE BACKLINE at least once: both sims ended with
  Lilly at literally zero resources spent because nothing ever pressured her.
  One Undermine next to Lilly prices the Sentinel door (Shield, Flash of
  Genius, or a rebuild slot).
- **Tremor Pulse (2).** Each creature within 10 ft: DC 15 Dex save, 2d6
  Bludgeoning and Prone on a failure.

## Sim-validated table notes
- The four-unit party throws ~10 attack rolls a round; HP alone cannot outpace
  it. AC 18 + 3 legendaries + no blanket vulnerability is what targets the
  4-to-6-round arc. If it still melts, vent the seams automatically at the
  start of its turn (2d6 Force to everyone adjacent) rather than adding HP.
- What played great and should be kept on purpose: the seam telegraph as
  Lilly's spotlight, Challenge + Curl Up making Sandshrew feel like a wall,
  the Guiding-Bolt-advantage chain, and the +1 aura rescuing an
  exactly-on-the-AC hit.
- Boss-side reminders the sims underused: attack the Sentinel at least once
  (device-vs-creature targeting is untested), and spend Shard Spray the turn
  it recharges.
