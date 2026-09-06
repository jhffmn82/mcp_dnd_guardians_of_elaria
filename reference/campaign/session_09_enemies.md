# Session 9 (Unda) enemy roster: the numbers of record

Generated from the reconciled combat-first + difficulty design pass (2026-09-05). **This file is the source of truth for every Session 9 enemy**, including the attack routines, which `memory/campaign_canon.md` deliberately does not carry. The simulator and `templates/build_session_09.py` must both read from here so they cannot drift.

## Difficulty, against the Session 8 anchor

| Slot | Fight | Total enemy HP | Session 8 same slot | Delta |
|---|---|---|---|---|
| 1 | The Brightshoal | **404** | Mosslight Landing 320 | +26% |
| 2 | The Kelp Cathedral | **552** | Chime Reef 444 | +24% |
| 3 | The Blackwater Seam | **530** | Glassed Gallery 412 | +29% |
| 4 | The Guardian's Trench | **558** on the board | Groudon's Hollow 430 | +30% |

**Correction, 2026-09-05:** canon briefly recorded 308 / 444 / 412 / 458. Those were the pre-difficulty-bump numbers from the combat-first pass and are SUPERSEDED. The 458 in particular never added up (Kyogre 250 + the Quiet Hand 120 = 370), which is what the simulator caught. The trench is 558 because it fields five types, not two.


---

## Session 9, Fights 1 and 2 rebuilt harder and more varied: 1 The Brightshoal, 2 The Kelp Cathedral (with the short rest confirmed after Fight 2)

### Glimmerfin  
*Small beast (panicked), unaligned ✦ CR 1/4 (50 XP) ✦ 8 in the first sheet out of the wall*  
**Count:** 8  
**Role:** Skirmisher, and the cheap half of the stampede. It is the reason nobody stands still: eight bodies, Schooling advantage the moment two of them share a target, and a Reaction that puts a missed one somewhere new. It makes the party decide, every round, whether clearing chaff is worth a turn while the Surgehorns are building speed. Kept from the DM's approved roster at AC 14 and 13 hit points; the upgrade is Schooling and a real Reaction, not more hit points.

- **AC** 14  **HP** 13 (3d6 + 3)  **Speed** 40 ft, swim 40 ft
- **STR** 8  **DEX** 18  **CON** 12  **INT** 3  **WIS** 12  **CHA** 6
- **Senses** blindsight 30 ft, passive Perception 11
- **Challenge** 1/4 (50 XP)

**Traits**

- **Schooling.** It has Advantage on attack rolls against a creature if at least one other Glimmerfin is within 5 ft of that creature.
- **Skitter.** Its movement does not provoke Opportunity Attacks. It runs on stiffened fins across dry sand and it is very bad at stopping.
- **Not Hunting.** It never attacks a creature that has 0 hit points, and it will not stay within 5 ft of one. Panic runs away from stillness.

**Actions**

- **Nip.** *Melee Weapon Attack:* +6 to hit, reach 5 ft. *Hit:* 5 (1d6 + 2) piercing damage.

**Reactions**

- **Wall-Slip.** When an attack misses it, it pours into the nearest water wall and reappears in an unoccupied space within 15 ft of where it was. It cannot do this while Grappled or Restrained.

*Art brief:* A hand-sized reef fish the colour of struck silver shot through with electric blue, running rather than swimming: fins stiffened into little legs, body low and skidding across white sand, mouth open, one enormous panicked eye rolled backward at something behind it. Draw it in a sheet of dozens, all pointed the same way, with sunlit water hanging overhead like a ceiling. Bright, kinetic, comic in silhouette and frightened in the face; nothing rotten or grey about it, because this animal is healthy and terrified.

### Surgehorn  
*Large beast (panicked), unaligned ✦ CR 4 (1,100 XP) ✦ 3, and they are not going to stop*  
**Count:** 3  
**Role:** Anchor and battering ram, and the clock. Blind panic that cannot be calmed, only steered. It forces the hardest recurring choice of the fight: hold the lane and take a charge, or give up ground and let the Blackfroth get closer. It BREAKS PAST at 0 rather than dying, so the fight thins on its own and no refugee is killed at this table. Kept from the DM's roster at 68 hit points; AC raised 15 to 16, and the upgrade is the charge and the shove.

- **AC** 16 (shell plate)  **HP** 68 (8d10 + 24)  **Speed** 50 ft, swim 50 ft
- **STR** 19  **DEX** 12  **CON** 16  **INT** 2  **WIS** 10  **CHA** 5
- **Imm.** (cond) charmed, frightened
- **Senses** blindsight 60 ft, passive Perception 10
- **Challenge** 4 (1,100 XP)

**Traits**

- **Blind Panic.** It cannot be calmed, soothed, pacified, or turned. Animal Handling, Animal Friendship, Speak with Animals and the Mark of Handling all fail against it automatically. It is not fighting anyone. It is going through.
- **It Breaks Past.** At 0 hit points it is not killed. It stumbles, goes down to one knee, gets up wobbling and is gone into the nearest water wall. Remove it from the fight. Say out loud that it is alive, because the table will assume otherwise.
- **It Does Not Finish.** A creature at 0 hit points is a hole in the herd's path, and the herd goes around holes. It will not attack, trample, charge through, or end its movement on a downed creature.

**Actions**

- **Gore.** *Melee Weapon Attack:* +8 to hit, reach 10 ft. *Hit:* 13 (2d8 + 4) bludgeoning damage, and the target makes a DC 15 Strength saving throw or is pushed 10 ft and knocked Prone.
- **Blind Charge (Recharge 5-6, never on round one).** It moves up to 50 ft in a straight line without provoking Opportunity Attacks. Each creature in its path makes a DC 15 Dexterity saving throw, taking 23 (4d8 + 5) bludgeoning damage and falling Prone on a failure, or half damage and no Prone on a success. A Surgehorn that charges does not also Gore that round; the charge is its whole turn.

**Reactions**

- **Shoulder.** When a creature within 10 ft hits it, it shoves past: that creature makes a DC 15 Strength saving throw or is pushed 10 ft. No damage. Once per round.

*Art brief:* A pony-sized armoured sea-beast built like a bull that was designed by a crab: overlapping plates of pale barnacled shell, low heavy shoulders, stubby paddling limbs churning dry sand, and one blunt worn horn on a head that has no eyes anywhere on it. Show it mid-charge with a sheet of sand going up behind it and coral splintering under one foot. It must read as frightened and unstoppable at the same time, never cruel: a thing running away that happens to be enormous.

### Inkmantle  
*Medium beast (panicked), unaligned ✦ CR 2 (450 XP) ✦ 2 covering the herd's retreat*  
**Count:** 2  
**Role:** Ranged controller, and the role the approved roster did not have. These are the shoal's shepherds, backing out of the water wall spraying stinging ink to cover the herd. They are the ONLY thing in Fight 1 that can reach Lilly and Ursa where they actually stand, and the Blind is the session's first genuine lost turn. Fifteen feet of reach and a 30-ft speed mean Stabby (65 ft ignited) always has one in reach if he wants one.

- **AC** 14  **HP** 28 (4d8 + 10)  **Speed** 30 ft, swim 40 ft
- **STR** 12  **DEX** 16  **CON** 16  **INT** 5  **WIS** 14  **CHA** 8
- **Senses** darkvision 60 ft, passive Perception 12
- **Challenge** 2 (450 XP)

**Traits**

- **Backward Swimmer.** It always moves away from whatever hit it last and never willingly ends its turn within 5 ft of a creature. Its 15 ft of reach means it never gets to be out of everyone's way.
- **Herd Sense.** It always positions itself between the party and the largest number of fleeing animals. It is guarding, not hunting, and it should be played that way even when it is winning.
- **It Does Not Finish.** It sprays to cover a retreat, never to end one. It ignores creatures at 0 hit points entirely and will not target a space one is lying in.

**Actions**

- **Tendril Lash.** *Melee Weapon Attack:* +7 to hit, reach 15 ft. *Hit:* 11 (2d6 + 4) slashing damage.
- **Ink Sting (Recharge 5-6, never on round one).** A 20-ft-radius Sphere centred on a point within 60 ft. Each creature in it makes a DC 14 Constitution saving throw, taking 7 (2d6) poison damage and being Blinded until the end of its next turn on a failure, or half damage and no Blinding on a success. The two Inkmantles work as a pair: one lashes and one stings, never both stinging in the same round.

**Reactions**

- **Jet.** When it takes damage, it may move up to 20 ft without provoking Opportunity Attacks.

*Art brief:* A living cloak: a pale grey-lavender mantle of a creature about the size of a person, drifting backward with the leading edge rippling, trailing four or five ropy tendrils fifteen feet behind it. No face to speak of, just a horizontal slit of a pupil low on the front of the mantle. Show it half out of a standing wall of water, one tendril still in the water and three on dry sand, with a slow purple-black bloom of ink hanging in the air in front of it like smoke that has forgotten to rise.

### Blackfroth  
*Medium ooze (planar corruption), unaligned ✦ CR 3 (700 XP) ✦ 1, arriving at the top of round three*  
**Count:** 1 (wave: enters at the top of round three, 60 ft out, from the direction the herd came)  
**Role:** The thing that changes the fight when it arrives, and the session's whole argument in one body. It is the leading edge of the corruption, the thing the herd has been running from all along. It barely fights the party: its job is to spoil the animals the party was trying to save, which makes killing it a rescue and makes every round it lives a worse board. This is the target-priority engine, and its radiant vulnerability is the deliberate teaching moment for Fight 3's Blackcask.

- **AC** 15  **HP** 40 (8d8 + 4)  **Speed** 30 ft, swim 30 ft
- **STR** 14  **DEX** 14  **CON** 12  **INT** 3  **WIS** 10  **CHA** 3
- **Resist** necrotic, poison  ✦  **Vuln.** radiant
- **Imm.** (cond) blinded, charmed, deafened, frightened, prone
- **Senses** blindsight 60 ft, passive Perception 10
- **Challenge** 3 (700 XP)

**Traits**

- **Blackwash.** At the end of its turn, each beast within 15 ft of it that is not already Blackwashed becomes Blackwashed for the rest of the fight: its attack rolls gain a +2 bonus and its attacks deal an extra 1d6 necrotic damage. A Blackwashed creature that drops to 0 hit points is still freed, not killed: the black wrings out of it like dirty water out of a cloth and the animal swims away. Say that out loud the first time it happens.
- **Planar Corruption.** It is a corrupted creature for Stabby's Cleansing Edge and for anything else that keys on corruption. (Spending Cleansing Edge here is legal and is a small waste; it is worth far more in the Blackwater Seam, and that is his call to make, not the DM's.)
- **The Leading Edge.** If it is destroyed before the end of round five, the Tide token does not advance after this fight. Do not tell the table this, do not hint at it, and do not explain it afterward. Simply do not move the token, and let somebody ask.
- **Not Hunting, Spreading.** It never attacks a creature at 0 hit points and never stops beside one. It drifts over a fallen hero without pausing, because it is following the current and not the party.

**Actions**

- **Froth Spit.** *Ranged Weapon Attack:* +7 to hit, range 60 ft. *Hit:* 12 (2d8 + 3) necrotic damage.
- **Sour Current (Recharge 5-6).** Each creature within 10 ft makes a DC 15 Constitution saving throw, taking 10 (3d6) necrotic damage and being unable to regain hit points until the end of its next turn on a failure, or half damage and no other effect on a success.

**Reactions**

- **Backwash.** When a creature within 5 ft hits it with a melee attack, that creature makes a DC 14 Constitution saving throw or takes 4 (1d8) necrotic damage and cannot regain hit points until the start of its next turn.

*Art brief:* A shoulder-high smear of absolute black drifting across bright white sand, shaped like nothing: edges going soft and reforming, no limbs, no face, moving without any visible part of it moving. Where it passes, the sand behind it is the dull green-grey of an old coin and the coral has lost its colour. Keep the surrounding water and light brilliantly clear and sunlit so the black reads as a hole cut in a beautiful picture. Unsettling by absence, never gruesome and never a monster.

### Pillarback  
*Huge beast (kelp-wearer), unaligned ✦ CR 8 (3,900 XP) ✦ 2, wearing the two centre columns*  
**Count:** 2  
**Role:** The anchors, and the two things in the room that will not move and cannot be ignored. Ten feet of reach and a grapple on every pincer decide where the fight is fought. Kelp Mantle is the lever that makes the fight move: half cover against everything shot from more than 30 ft away pulls Lilly and Ursa forward out of safety and into the Needlemaws, which is the decision they have to make every single round. Kept from the DM's roster at AC 17 and 126 hit points; the upgrade is the grapple, the Column Fall, and the cover.

- **AC** 17 (shell and kelp)  **HP** 126 (12d12 + 48)  **Speed** 20 ft, swim 30 ft
- **STR** 21  **DEX** 8  **CON** 18  **INT** 3  **WIS** 12  **CHA** 6
- **Resist** bludgeoning, piercing
- **Imm.** (cond) prone  **Senses** tremorsense 60 ft, passive Perception 11
- **Challenge** 8 (3,900 XP)

**Traits**

- **Kelp Mantle.** The living column on its back gives it Half Cover (a +2 bonus to AC and to Dexterity saving throws) against any attack or effect originating more than 30 ft away. A creature within 30 ft ignores it entirely.
- **Rooted Stance.** It cannot be moved against its will and is immune to the Prone condition. It never goes more than 15 ft from its socket, because there is a nest under it.
- **It Does Not Finish.** It is defending the socket, not hunting. It releases any creature that drops to 0 hit points immediately and does not attack it again.

**Actions**

- **Multiattack.** Two Pincers.
- **Pincer.** *Melee Weapon Attack:* +9 to hit, reach 10 ft. *Hit:* 14 (2d8 + 5) bludgeoning damage, and if the target is Large or smaller it is Grappled (escape DC 14). It can grapple one creature per pincer.
- **Column Fall (Recharge 6).** It heaves the whole column over in a 30-ft line, 10 ft wide. Each creature in the line makes a DC 16 Dexterity saving throw, taking 27 (5d10) bludgeoning damage and falling Prone on a failure, or half damage and no Prone on a success. The column groans back upright over the following round.

**Reactions**

- **Shell Over.** When it is hit by an attack made from more than 30 ft away, it tucks under its column: reduce that damage by 10.

*Art brief:* A crab the size of a house wearing a thirty-foot column of living kelp rooted into its slate-grey shell, so that it has been standing in the cathedral's row long enough for the row to grow around it. Show it in the moment of turning: the socket in the sand coming away as a crater, the kelp column swaying like a ship's mast, two claws the width of a doorway unfolding out of the front. Green shafts of underwater light coming down between real columns on either side. Ancient, patient, defensive, not evil.

### Needlemaw  
*Medium beast, unaligned ✦ CR 2 (450 XP) ✦ 5 out of the column shadows*  
**Count:** 5  
**Role:** The fast flankers, and the fight's fear rather than its danger. Their whole job is to grab one hero and drag them twenty feet a turn toward a water wall, which separates the party, breaks Ursa's positioning, and is completely non-lethal because Unda does not let its guests drown. Pack Frenzy makes a grappled or prone hero into a target the whole school piles onto, which is what makes the Pillarbacks' grapple and the Gullet Bells' Drop matter. Kept from the DM's roster at AC 14; count 6 to 5 and hit points 32 to 28 to make room for two new roles.

- **AC** 14  **HP** 28 (5d8 + 5)  **Speed** 40 ft, swim 50 ft
- **STR** 14  **DEX** 16  **CON** 13  **INT** 3  **WIS** 12  **CHA** 5
- **Senses** blindsight 30 ft, passive Perception 11
- **Challenge** 2 (450 XP)

**Traits**

- **Pack Frenzy.** It has Advantage on attack rolls against a creature that is Grappled or Prone.
- **It Does Not Finish.** The instant its prey stops moving it lets go and looks for something that is still moving. It never attacks a creature at 0 hit points, and it releases any creature that reaches 0.

**Actions**

- **Bite.** *Melee Weapon Attack:* +7 to hit, reach 5 ft. *Hit:* 9 (2d4 + 4) piercing damage, and if the target is Medium or smaller it is Grappled (escape DC 13).
- **Drag Under.** If it begins its turn grappling a creature, it can move up to 20 ft dragging that creature with it, and this movement does not provoke Opportunity Attacks. It always drags toward the nearest water wall. A creature carried into the wall is taken three feet and set back down on the sand by the next swell, unharmed. Say the reason out loud the first time, once: Unda does not let its guests drown.

**Reactions**

- **Thrash.** When it takes damage while grappling a creature, it may release that creature and move up to half its Speed without provoking Opportunity Attacks.

*Art brief:* A lean ribbed eel-hound about the length of a person, all shoulder and no waist, with a mouth that cannot close because there is too much needle-thin tooth in the way. Pale sand-coloured with dark banding, small flat eyes set far back, four short paddling limbs it uses to run on dry ground. Show one in mid-drag, jaws locked on a pack strap, hauling backwards across white sand toward a standing wall of green water, with a second one coming in low from the side.

### Quillfrond  
*Large plant, unaligned ✦ CR 3 (700 XP) ✦ 3, rooted on the columns at head height*  
**Count:** 3  
**Role:** Ranged pressure, and the direct answer to the old roster's biggest hole: nothing in the Kelp Cathedral could threaten Lilly or Ursa at their own range. It is ROOTED, Speed 0, permanently, so it can never kite Stabby: the one thing in the session that shoots is the one thing that can never run away from him, and at 65 ft ignited he reaches any of them from the party's starting line on turn one. That is the whole trade. Its Speed-10 rider is what makes a 25-ft gnome genuinely nervous.

- **AC** 15  **HP** 32 (5d10 + 5)  **Speed** 0 ft (rooted)
- **STR** 12  **DEX** 6  **CON** 13  **INT** 1  **WIS** 10  **CHA** 3
- **Imm.** (cond) charmed, frightened, grappled, prone
- **Senses** blindsight 90 ft, passive Perception 10
- **Challenge** 3 (700 XP)

**Traits**

- **Rooted.** Its Speed is 0 and cannot increase. It cannot move, retreat, be pushed, be pulled, or be knocked down. Anything that reaches it can hit it.
- **Range Finder.** It always shoots the farthest creature it can see, and it will not shoot a creature within 10 ft of itself while any other target is available. When Stabby closes, it stops shooting him and starts raking.
- **It Does Not Finish.** It has no interest in a target that has stopped moving and never shoots a creature at 0 hit points.

**Actions**

- **Multiattack.** Two Quills. On round one it fires only one, because it is waking.
- **Quill.** *Ranged Weapon Attack:* +7 to hit, range 80 ft. *Hit:* 7 (1d8 + 3) piercing damage, and the target's Speed is reduced by 10 ft until the end of its next turn.
- **Frond Rake.** *Melee Weapon Attack:* +6 to hit, reach 10 ft. *Hit:* 9 (2d6 + 2) slashing damage.

**Reactions**

- **Bristle Guard.** When a creature within 5 ft hits it with a melee attack, that creature takes 5 (1d10) piercing damage.

*Art brief:* A grey-green rosette the size of a cartwheel growing out of the side of a kelp column at head height, easy to mistake for an enormous barnacle until it opens. Inside the rosette is a bristling packed disc of foot-long black quills aimed outward like the tubes of an organ, with three or four long fleshy fronds trailing from the rim. Show one open and firing, quills leaving trails in the green shafted light, and another still closed and unremarkable further down the same column.

### Gullet Bell  
*Large aberration, unaligned ✦ CR 5 (1,800 XP) ✦ 2, and they have been hanging over the party since they walked in*  
**Count:** 2 (wave: they drop at the top of round three, or round two and out of position if the party spotted them)  
**Role:** The wave, and the moment the table genuinely believes they might lose. Two of the air-bells that have kept this whole session safe are not bells, which weaponises the one piece of terrain the party has been told to trust. Its Toll shuts off Reactions on a failed Constitution save, taking away Deflect Attacks, Shield, Flash of Genius, Cosmic Omen and Guardian's Light all at once on the highest-damage round of the night. Use the Toll exactly twice in the fight, never three times. It lands on the sand and fights in melee, so Stabby always has a body.

- **AC** 15  **HP** 46 (7d10 + 7)  **Speed** 25 ft, swim 30 ft
- **STR** 16  **DEX** 10  **CON** 13  **INT** 4  **WIS** 12  **CHA** 8
- **Resist** thunder  ✦  **Imm.** (cond) deafened, prone
- **Senses** blindsight 60 ft (it has no eyes), passive Perception 11
- **Challenge** 5 (1,800 XP)

**Traits**

- **Bell-Shaped.** Until it opens it is indistinguishable from a real air-bell. A creature that spends an action studying the canopy can find the difference with a DC 17 Perception or Nature check: the two false bells do not sway with the water. If the party spots them, the bells drop on round TWO instead, in the open, with nobody underneath them: no Drop damage, no grapple, and the party gets the first swing on both. Pay that enormously. Somebody looked up.
- **It Does Not Finish.** It shuts over movement, not over meat. The moment a creature inside it stops moving, it opens and leaves that creature on the sand and goes looking for something that is still going.
- **Only Twice.** The DM uses Toll at most twice in the whole fight regardless of recharge rolls. Once is a shock and twice is a fight.

**Actions**

- **Drop (on arrival only).** Each creature in the 10-ft space beneath it makes a DC 15 Dexterity saving throw. On a failure: 13 (3d8) bludgeoning damage, Prone, and Grappled (escape DC 14) as the bell closes over it. On a success: half damage and the creature steps clear. The two bells always drop on two different heroes, never the same one, and always in open sand outside any Pillarback's reach.
- **Slam.** *Melee Weapon Attack:* +7 to hit, reach 10 ft. *Hit:* 13 (2d8 + 4) bludgeoning damage.
- **Toll (Recharge 5-6).** It rings itself: one enormous flat brass note out of a thing with no bell inside it. Each creature within 20 ft makes a DC 15 Constitution saving throw, taking 10 (3d6) thunder damage and being unable to take Reactions until the start of its next turn on a failure, or half damage and no other effect on a success. No hero takes a Toll and a Column Fall in the same round.

**Reactions**

- **Ring Out.** When it takes damage from a creature it has Grappled, the bell opens, releases that creature, and moves up to 10 ft away. A swallowed hero only has to hit it once, from the inside, and they are free. Do not tell the table this; let them have four seconds of real fear and then let the trapped one swing.

*Art brief:* A silver, trembling, translucent dome thirty feet across, exactly like the harmless air-bells caught throughout the kelp canopy, caught in the moment it stops being one: the underside opening into a smooth rimmed mouth with no teeth and no face anywhere on it, descending slowly over a patch of dry white sand where a small figure stands looking up. Beautiful and wrong in the same frame, with forty identical bells still hanging peacefully in the green canopy behind it. No gore, no menace in the design itself; the horror is entirely that it looks like the safe thing.


---

## Session 9, Fight 3: The Blackwater Seam

### The Blackcask  
*Large construct (a made thing), unaligned ✦ CR 7 (2,900 XP) ✦ 1, on an iron frame straddling the crack*  
**Count:** 1  
**Role:** Anchor and soak, and the fight's centre of gravity. It is immobile with 15 feet of reach, it heals 15 a round unless somebody brings radiant damage or Cleansing Edge, and it is the reason every Chorister near it is twice as hard to kill. It makes the party decide, every round, between the thing that is doing the damage and the thing that is making everything else durable. The Tripod is the hidden answer to all of it.

- **AC** 17 (iron bands over tarred oak)  **HP** 152 (16d10 + 64)  **Speed** 0 ft
- **STR** 18  **DEX** 6  **CON** 18  **INT** 1  **WIS** 8  **CHA** 1
- **Resist** cold, necrotic; bludgeoning, piercing and slashing from nonmagical weapons
- **Imm.** poison ✦ (cond) charmed, exhaustion, frightened, paralyzed, poisoned, prone
- **Senses** tremorsense 60 ft, blindsight 30 ft, passive Perception 9
- **Challenge** 7 (2,900 XP)

**Traits**

- **Still Pouring.** At the start of its turn it regains **15 hit points**, unless it took **radiant damage** or was hit by **Cleansing Edge** since the end of its last turn. It loses this permanently if it comes off the crack.
- **The Tripod (the fight's lever; the DM must not offer this).** It stands on a three-legged iron frame straddling the crack. The frame is an object: **AC 13, 20 hit points**, and any effect that would push, pull, or knock prone a Large creature may be aimed at the frame instead of at the cask. If the frame is destroyed or moved 5 feet, the Blackcask **comes off the crack** and immediately and permanently loses **Still Pouring** and **Blackwater Surge**, and **Sheathed in Black** ends for every creature in the encounter. It keeps its hit points and its Band Lashes and fights on, on its side.
- **Sheathed in Black.** Every Hollowsong and the Notched Fin **within 20 feet of it** has **Resistance to bludgeoning, piercing and slashing damage**. Twenty feet, not thirty: the Choristers charge whoever last hurt them, so they walk out of their own armour, and that is a lesson the party can learn by watching.
- **Pouring (round one only).** It takes no actions on round one. It is finishing the job. It comes up at the start of round two.
- **It Does Not Look Down.** It perceives creatures as weight moving on the sand. It cannot find a creature at 0 hit points and will never target one. It was built to pour, not to fight, and it has no idea anybody is fighting it.

**Actions**

- **Multiattack.** Two Band Lashes.
- **Band Lash.** *Melee Attack:* +8 to hit, reach 15 ft. *Hit:* 11 (2d6 + 4) bludgeoning damage plus 3 (1d6) cold damage.
- **Blackwater Surge (Recharge 5-6; NOT AVAILABLE UNTIL ITS SECOND TURN).** The crack has to fill before it can breathe out, so this cannot happen before round three. The seam exhales. Each creature in a **30-foot cone** makes a **DC 16 Constitution saving throw**, taking 17 (5d6) cold damage and having its **Speed halved until the end of its next turn** on a failure, or half damage and no slowing on a success.

**Reactions**

- **Overflow.** When a creature it can perceive hits it with a melee attack, the cask slops over the rim. That creature makes a **DC 15 Dexterity saving throw**, taking 7 (2d6) necrotic damage on a failure. Once per round, since a creature has one reaction. Stabby's Evasion applies, which is worth letting him discover.

*Art brief:* A squat barrel of tar-black oak the height of a man and a half, bound in cold iron bands that move like slack muscle, tipped forward on a three-legged iron frame that straddles a lightless crack in white sand. A slow black rope of water runs from its lip into the dark. The sand for ten feet around the crack is bleached bone-white. No face, no limbs, nothing to appeal to. Overhead a sagging blue-green ceiling of water hangs low, with columns of water slumping to the floor on either side, and the light is dim.

### Hollowsong  
*Medium elemental (corrupted native of Unda), unaligned ✦ CR 3 (700 XP) ✦ 4, two at the start and two more at the end of round one*  
**Count:** 4  
**Role:** The fast melee flanker, and the heart of the fight. They are the Kelp Cathedral's Choristers wearing black water. They do not defend themselves, they charge whoever last cut them, and freeing one calls the rest down on whoever did it. They force Stabby to decide, every single turn, whether Cleansing Edge goes to freeing a life or to shutting off the Blackcask's regeneration.

- **AC** 15 (black water skin)  **HP** 38 (7d8 + 7)  **Speed** 30 ft, swim 40 ft
- **STR** 14  **DEX** 16  **CON** 13  **INT** 7  **WIS** 12  **CHA** 14
- **Resist** cold, necrotic (plus **Sheathed in Black**, on the Blackcask's card)
- **Imm.** poison ✦ (cond) charmed, frightened, poisoned
- **Senses** blindsight 60 ft, passive Perception 11
- **Challenge** 3 (700 XP)

**Traits**

- **It Was Singing Yesterday (THE CURE).** When Stabby hits it with the Nichirin Katana and spends **Cleansing Edge** on that hit, check its hit points **after that hit's damage is applied**. If it is **Bloodied** (half its hit points or fewer), the black water lets go. It is **freed**: removed from the encounter alive and whole, swimming up out of the seam, and it does not come back. It is not killed, it is not a kill, and nobody at the table should call it one. If it is not Bloodied, Cleansing Edge simply works as printed (it cannot regain hit points until the start of his next turn).
- **Answering the Cut.** On its turn it moves toward and attacks whichever creature most recently damaged it, if it can reach one. It has no self-preservation and it never runs. This is what walks it out of the Blackcask's 20-foot armour.
- **The Chorister Remembers.** It will not attack a creature at 0 hit points and it will not move within 5 feet of one. The song goes badly off-key near a fallen creature. Something inside it still knows what a hurt thing looks like, and it is trying.

**Actions**

- **Multiattack.** Two Raking Fins.
- **Raking Fin.** *Melee Attack:* +7 to hit, reach 5 ft. *Hit:* 6 (1d6 + 3) slashing damage plus 2 (1d4) cold damage.

**Reactions**

- **Chorus.** When another Hollowsong within 30 feet is **freed or reduced to 0 hit points**, this one moves up to its Speed toward the creature that did it, without provoking Opportunity Attacks. Freeing one calls the others, and that cost is the point: the good thing the kid wants to do is the thing that brings the choir down on him.

*Art brief:* A slender coral-and-pearl fish-person with long trailing fin-veils and a small crown of pale coral, the silhouette unmistakably the same lovely creature that was singing in the kelp canopy an hour ago, but every pale surface now sheeted in a film of black water running off it like oil on glass. The throat is still working and the mouth is still open on a note. Dim blue-green seam light, white bleached sand underfoot, a lightless crack behind.

### Lancefin  
*Small aberration (corrupted), unaligned ✦ CR 2 (450 XP) ✦ 3, hanging in the sagging water columns*  
**Count:** 3  
**Role:** The ranged threat the fight did not have, and the punishment for clumping. Each lance passes through the target and clips whoever is standing next to them, so the party cannot bunch up in front of the Blackcask. Own Lane keeps them from ever ganging on one hero, and the Half Cover of the water columns is a printed reason to close with them rather than trade shots, which puts Stabby to work at range without ever giving him a ranged attack.

- **AC** 16 (needle scales)  **HP** 22 (4d6 + 8)  **Speed** 10 ft, swim 50 ft
- **STR** 8  **DEX** 18  **CON** 14  **INT** 3  **WIS** 12  **CHA** 5
- **Resist** cold ✦ **Imm.** poison ✦ (cond) poisoned, prone
- **Senses** blindsight 60 ft, passive Perception 11
- **Challenge** 2 (450 XP)

**Traits**

- **In the Column.** It swims inside the failing bell's hanging columns of water and moves freely between any two of them within its swim Speed. While it is inside a column, a creature attacking it from more than 5 feet away treats it as having **Half Cover** (+2 AC and +2 to its Dexterity saving throws, SRD Cover). Stepping up to it removes that entirely. **It can never end its turn more than 30 feet from dry sand**, so Stabby, at Speed 65, always has one he can reach.
- **Own Lane.** It will not attack a creature that another Lancefin has already attacked this round if any other target is available. **Never more than one Lancefin on one hero in one round.** This is a printed alpha-strike guard, not a courtesy.
- **Blind Aim.** It aims at motion in the water. It cannot find a creature at 0 hit points and will never target one.

**Actions**

- **Bone Lance.** *Ranged Attack:* +7 to hit, range 60 ft, one target. *Hit:* 8 (1d8 + 4) piercing damage. **Pass-Through:** the lance keeps going. One other creature within 5 feet of the target, of the Lancefin's choice, makes a **DC 14 Dexterity saving throw**, taking 3 (1d6) piercing damage on a failure. (Stabby's Evasion means a success is no damage at all.)

**Reactions**

- **Slip the Column.** When it is hit by a melee attack, it sinks into the water wall and surfaces in another column up to 20 feet away. It then has the **Invisible** condition (granted by this trait, not by the Hide action, so Hide's cover requirements do not apply) until it attacks or until a creature finds it with a **DC 13 Wisdom (Perception) check**, which is at Disadvantage in the seam's Dim Light. That penalty touches Ursa only: Lilly and Stabby have Darkvision and read Dim Light as Bright Light. It cannot Slip again until the end of its next turn.

*Art brief:* A hand-length dart of a fish, all needle scales and one flat black eye, hanging perfectly still inside a column of water that runs from a low sagging water ceiling down to white sand. A barbed white spine is already half out of its jaw, aimed. Two more of them are visible as silhouettes deeper inside the same column. Dim blue-green light, the water column faintly refracting the shapes behind it.

### Tanglehand  
*Large aberration (the black water itself), unaligned ✦ CR 4 (1,100 XP) ✦ 2, rising off the crack lip at the end of round one*  
**Count:** 2  
**Role:** The controller, and the thing that makes the black water dangerous to stand near without turning the fight into terrain management. It is rooted, it reaches 20 feet, it grapples and drags toward the crack, and it takes a free swing at anyone who ends a turn on the lip. It is squishy on purpose: it is the round's target-priority question, because leaving it up costs somebody their movement and their positioning.

- **AC** 16  **HP** 40 (8d10 - 4)  **Speed** 0 ft (rooted in the crack)
- **STR** 17  **DEX** 14  **CON** 14  **INT** 3  **WIS** 10  **CHA** 6
- **Resist** cold, necrotic; bludgeoning, piercing and slashing from nonmagical weapons
- **Imm.** poison ✦ (cond) blinded, charmed, deafened, exhaustion, frightened, poisoned, prone
- **Senses** tremorsense 60 ft (blind beyond it), passive Perception 10
- **Challenge** 4 (1,100 XP)

**Traits**

- **Rooted in the Seam.** It cannot leave the crack and never tries. It is not a creature that came out of the water; it is the water putting out a hand. **When the Blackcask comes off the crack or is destroyed, every Tanglehand sinks at once** and does not come back. They do not regrow: the party's win on the cask is a real win and must not be taken back from them.
- **It Lets Go.** If a creature it is grappling drops to 0 hit points, the Tanglehand releases it immediately and the next wave rolls it gently back onto dry sand. Unda still keeps that rule, even here, even with this in it. Say it out loud the first time it happens.

**Actions**

- **Black Grasp.** *Melee Attack:* +7 to hit, reach 20 ft, one target. *Hit:* 10 (2d6 + 3) bludgeoning damage, the target has the **Grappled** condition (Speed 0, Disadvantage on attacks against anything but the grappler), and the Tanglehand drags it up to 10 feet toward the crack. **Escape DC 14**, an Action, **Strength (Athletics) or Dexterity (Acrobatics)**, per the glossary; it grapples only one creature at a time.
- **Drown the Grip (no action).** At the start of each of its turns, the creature it is grappling takes 4 (1d8) necrotic damage as the black water closes over it. This is not drowning and it never becomes drowning: it is the corruption, and it burns cold.

**Reactions**

- **Second Hand.** When a creature it can sense **ends its turn within 10 feet of the crack**, the Tanglehand makes one Black Grasp against it. This is the whole reason not to stand on the lip, and it is an enemy reaction resolved in initiative, not a floor hazard: the DM never tracks squares and never asks for a save to walk.

*Art brief:* An arm of pure black water rising three times the height of a person off the lip of a lightless crack in white sand, fingers too long and too many, the whole limb translucent-dark like ink poured into a glass of clear water and held there. Where the fingers brush the sand the sand bleaches white. A second identical arm is rising behind it on the far side of the crack. Dim blue-green light from a low water ceiling.

### The Notched Fin  
*Large elemental (corrupted native of Unda), unaligned ✦ CR 6 (2,300 XP) ✦ 1, arriving at the start of round three or when the Blackcask is first Bloodied*  
**Count:** 1  
**Role:** The arrival that changes the fight, and the fight's real ending. She is the Chorister the party actually met in the Kelp Cathedral, recognizable by an old torn fin, and freeing her frees the entire remaining choir at once. She is not immune to Frightened, which is Lilly's forgotten Pipes of Haunting waiting to matter. Killing her is allowed and costs nothing but the good ending.

- **AC** 16  **HP** 80 (10d10 + 25)  **Speed** 40 ft, swim 60 ft
- **STR** 16  **DEX** 18  **CON** 16  **INT** 8  **WIS** 13  **CHA** 17
- **Resist** cold, necrotic (plus **Sheathed in Black** while within 20 ft of the Blackcask)
- **Imm.** poison ✦ (cond) charmed, poisoned. **She is NOT immune to Frightened.** That is deliberate and nobody should be told.
- **Senses** blindsight 60 ft, passive Perception 11
- **Challenge** 6 (2,300 XP)

**Traits**

- **It Was Singing Yesterday (THE CURE, and the end of the fight).** As the Hollowsong trait: a Nichirin hit, **Cleansing Edge** spent on that hit, **Bloodied** after the damage is applied, and the black water lets go. And when she goes, the song goes with her: **every remaining Hollowsong is freed in the same breath** and the encounter ends. Killing her does not do this. Only the cut does.
- **The Notch.** The party has met her. She was the one in the Cathedral canopy with the old white notch torn through her dorsal fin, and the notch is still there. **Say nothing.** Describe the fin and stop. Let a player be the one who recognizes her.
- **She Does Not Finish Them.** She will not attack a creature at 0 hit points, and any Hollowsong within 10 feet of a fallen creature has **Disadvantage** on its attacks. Something in there is trying very hard to stop, and standing over a friend is the one place in this fight where the corruption is weakest.

**Actions**

- **Multiattack.** Two Rakes.
- **Rake.** *Melee Attack:* +8 to hit, reach 10 ft. *Hit:* 11 (2d6 + 4) slashing damage.
- **The Wrong Song (Recharge 5-6).** Every creature within 30 feet that can hear makes a **DC 15 Wisdom saving throw**, taking 13 (3d8) psychic damage on a failure and having to spend its **next** movement moving as far as it can toward the nearest black water, or half damage and no compulsion on a success. **This is not a spell**, so Lilly's Gnomish Magic Resistance (advantage on Wisdom saves **against spells**) does not apply and the DM must not grant it. Ursa's Cosmic Omen and Lilly's Flash of Genius both do.

**Reactions**

- **The Choir Turns.** When a Hollowsong within 30 feet is reduced to **0 hit points** (not freed), the Notched Fin moves up to half her Speed toward the creature responsible and makes one Rake against it. Killing her choir is more expensive than freeing it, and the party will work that out on their own by about the second one.

*Art brief:* A Chorister half again the size of the others: a tall coral-crowned fish-person with long pearl fin-veils, one dorsal fin torn clean through by an old healed white notch. The whole shape is sheeted in black water running off her in falling sheets like rain off glass, and her mouth is open on a note that is visibly, painfully wrong. She is rising out of a lightless crack in bleached white sand, dim blue-green water ceiling sagging low above her, columns of water standing on either side.


---

## Session 9, Fight 4: The Guardian's Trench (boss rebuild, harder and wider)

### Kyogre, the Deep That Holds the World  
*Gargantuan elemental (Plane of Unda, Guardian), unaligned ✦ run as CR 12 (8,400 XP) ✦ it is not a monster, it is a hostage*  
**Count:** 1  
**Role:** Anchor and area threat, and the objective. It is the only thing on the board whose total ending at 0 wins the fight, and reducing that total is freeing it, not killing it. It makes the party decide every round whether to spend the turn on the whale or on the pressure, and in phase three it stops being weather and becomes an ally that cannot say so.

- **AC** 18 (living plate and cold water)  **Black Water** 280 (this is NOT hit points, see the trait)  **Speed** 20 ft (dragging itself on sand), swim 60 ft in the trench beyond the bell
- **STR** 27 (+8)  **DEX** 10 (+0)  **CON** 25 (+7)  **INT** 14 (+2)  **WIS** 18 (+4)  **CHA** 20 (+5)
- **Resist** bludgeoning, piercing, slashing from nonmagical attacks
- **Imm.** cold, poison ✦ (cond) charmed, frightened, grappled, paralyzed, petrified, prone, restrained, stunned
- **Senses** blindsight 120 ft, passive Perception 18
- **Challenge** run as CR 12 (8,400 XP)

**Traits**

- **Black Water, Not Blood.** The 280 is the corruption riding it, not its life. At 0 the corruption is gone and Kyogre is FREE. It is never killed, it never dies, no death saves are rolled for it, and no wound is ever described. Say this out loud at the table before initiative if the players look worried.
- **THE SPIKE IS NOT A TARGET.** The black glass in its back cannot be attacked, moved, dispelled, sundered, grappled, or targeted by any effect whatsoever. That was last session. The three SPENT spikes the Quiet Hand plants in the sand later are ordinary objects and are entirely fair game; the party is allowed to notice the difference without help.
- **The Water Closes.** At the start of each of its turns it regains **15 Black Water** unless **Cleansing Edge** touched it since its last turn.
- **It Is Not Aiming (phase one only).** Its Flukes, including the legendary one, strike the two creatures NEAREST it that it can reach, never the same creature twice in a round. A Fluke with no second target in reach hits the seabed. It does not move at all in phase one.
- **Three Phases, No Numbers Read Aloud.** Phase one (280 to 181), The Weight: head turned away, colour of a bruise, two Flukes, ONE legendary use, Undertow uncharged at initiative. Phase two (180 to 101), It Notices: turn the miniature side-on, black coming off in ribbons, blue underneath, two Flukes, TWO legendary uses, The Deep Voice online, It Is Not Aiming ends. Phase three (100 to 0), The Undertow Turns: turn the miniature to face the party, mostly blue with black in the seams, THREE Flukes, THREE legendary uses, and it stops trying to leave.
- **It Does Not Finish Them.** A creature at 0 hit points is sand to it. It never attacks one, never targets one, and never moves toward one. It never knew they were there.

**Actions**

- **Multiattack.** Two Flukes. Three in phase three.
- **Fluke.** *Melee Weapon Attack:* +13 to hit, reach 20 ft. *Hit:* 18 (3d8 + 5) bludgeoning damage, and the target is pushed 10 ft away.
- **Undertow (Recharge 5-6; UNCHARGED at initiative, first roll at the start of its second turn).** A 60-ft Cone. DC 17 Dexterity saving throw: 22 (4d10) cold damage, half on a success. A creature that fails is also pushed 15 ft. (Evasion applies: this is a half-on-success effect.)
- **The Deep Voice (phase two and three only, Recharge 6).** A 30-ft Emanation. DC 17 Wisdom saving throw: 18 (4d8) psychic damage, half on a success. A creature that fails is Frightened of Kyogre until the end of its next turn. This is not an attack. It is a word in a language nobody here speaks, and it is far too loud.

**Reactions**

- **Not You (1/fight, phase three only).** When a hero would be reduced to 0 hit points by an attack from the Quiet Hand or one of the Kept, Kyogre puts itself in the way and takes the damage instead, as Black Water. The guardian, half free, picking a side. Play it for the image, not the arithmetic, and note that the corruption it soaks comes off its own total.
- **Legendary Actions (1 use in phase one, 2 in phase two, 3 in phase three; regains all uses at the start of its turn; one at a time, at the end of another creature's turn).**
- **Surge (1).** One creature within 30 ft: DC 17 Strength saving throw or pushed 20 ft and knocked Prone. No damage.
- **Cold Squall (1).** A 10-ft-radius Sphere at a point within 60 ft: DC 16 Constitution saving throw, 9 (2d8) cold damage, half on a success.
- **Take the Deep (2).** It makes one Fluke attack.
- **The Undertow Turns (2, phase three only).** It drags itself up to 30 ft without provoking Opportunity Attacks and makes one Fluke. This is how a beached whale chases three children across a trench floor.

*Art brief:* A whale the size of a cathedral lying on pale dry sand beneath a hanging ceiling of seawater, seen from ground level so the horizon is all whale. Its hide is bruise-black in sheets that are tearing loose in ribbons, and where they have torn away the skin beneath is a deep clean ocean blue. A spike of black glass stands half-driven into its shoulder, and one enormous eye is turning to look back down its own flank. The trench walls behind it are packed with thousands of small blue-green living lights.

### The Quiet Hand  
*Medium humanoid (unknown), lawful evil ✦ CR 7 (2,900 XP) ✦ the first person the party has met who works for the enemy and does not care that they are there*  
**Count:** 1  
**Role:** The anchor and the bruiser, and the fight's real antagonist. For two rounds it is a defenceless object that will not stop, which teaches the party that hurting it does not solve it. From round three it is a wall with a hammer that presses, pursues and freezes the ground behind it. It makes the party decide whether to kill the man or free the whale, and there is not time for both.

- **AC** 17 (oiled leather, and it never flinches)  **HP** 150 (20d8 + 60)  **Speed** 30 ft
- **STR** 16 (+3)  **DEX** 14 (+2)  **CON** 16 (+3)  **INT** 16 (+3)  **WIS** 14 (+2)  **CHA** 8 (-1)
- **Resist** cold ✦ **Imm.** (cond) frightened
- **Senses** darkvision 120 ft, passive Perception 16
- **Challenge** 7 (2,900 XP)

**Traits**

- **At Work (rounds one and two).** It takes no actions but driving the spike. It does not attack, does not move, and does not take Reactions. Every attack roll against it has **Advantage**, and it automatically fails every saving throw. It does not defend itself because defending itself is not the job.
- **It Notices You.** The first time it takes 30 or more damage in a single round, it starts making saves normally and taking Reactions, and Advantage against it ends. It keeps hammering.
- **It Looks Up.** At the start of round three, fixed, it stops. It opens the case, plants three spent spikes in the sand, and **the Kept rise**. From that moment it fights.
- **Near the Work.** At the start of each of its turns, if it is within 30 ft of Kyogre, it regains **10 hit points**, unless **Cleansing Edge** touched it since its last turn. Dragging it out of that 30 feet is a legitimate answer and Ursa's Thorn Whip does it in one pull.
- **It Steps Over Them.** It never attacks or targets a creature at 0 hit points. It steps over them and goes back to work. Say that out loud, flatly, the first time it happens.
- **It Does Not Die.** At 0 hit points it comes apart into cold seawater and empty leather and the case falls in the sand and stays. Nobody sees a face. Nobody ever hears it speak.

**Actions**

- **Multiattack.** Two Hammers.
- **Hammer.** *Melee Weapon Attack:* +8 to hit, reach 5 ft. *Hit:* 14 (3d6 + 4) bludgeoning damage plus 5 (1d10) cold damage.
- **Nail (Recharge 5-6).** It drives the hammer into the sand and something under the sand answers. A 30-ft Line, 5 ft wide. DC 16 Dexterity saving throw: 22 (4d10) force damage, half on a success. A creature that fails is knocked Prone.
- **Cold Step (Bonus Action).** It moves up to 15 ft without provoking Opportunity Attacks. The sand it crosses freezes and is Difficult Terrain until the end of its next turn.

**Reactions**

- **Cold Answer.** When a creature it can see within 5 ft hits it, that creature takes 5 (1d10) cold damage. Not available while it is At Work.

*Art brief:* A hooded figure in a long coat and heavy gloves standing braced on the shoulder of an enormous whale, hammer raised two-handed over a spike of black glass, seen in silhouette against the glow of a trench wall so the face is never resolved. On the sand far below, a long flat leather case lies open with five padded loops in it, two of them holding black spikes and three of them empty.

### Brine-Thing  
*Small ooze (Black Water), unaligned ✦ CR 1/2 (100 XP) ✦ four loose at initiative, one more at the start of each of Kyogre's turns, maximum four on the board*  
**Count:** 4 at start (cap 4, respawning)  
**Role:** Fast chaff and the fight's guarantee that Stabby always has a body in reach. They spread rather than pile on, which is what makes the round-one math safe, and their grip hands Kyogre's cone a target that cannot dodge. They are also the cluster that rewards Lilly's Flamethrower and Tectonic Slam and Ursa's pack.

- **AC** 15  **HP** 22 (4d6 + 8)  **Speed** 40 ft, swim 40 ft
- **STR** 12 (+1)  **DEX** 16 (+3)  **CON** 14 (+2)  **INT** 3 (-4)  **WIS** 8 (-1)  **CHA** 3 (-4)
- **Imm.** cold, poison ✦ (cond) blinded, charmed, deafened, exhaustion, frightened, prone
- **Senses** blindsight 60 ft, passive Perception 9
- **Challenge** 1/2 (100 XP)

**Traits**

- **They Share.** Two Brine-Things never grip the same creature. Each one goes for a different warm body. This is a hard rule, not a preference, and it is the structural reason no hero can be swarmed to 0 in a single round.
- **Undertow's Friend.** A creature Grappled by a Brine-Thing has **Disadvantage on Dexterity saving throws**. This is the chain the fight is built on: the little ones hold you still and the big one sweeps the floor.
- **One Every Turn.** At the start of each of Kyogre's turns, one new Brine-Thing rises out of the sand, to a maximum of four on the board.
- **Cold, Not Cruel.** It never attacks or targets a creature at 0 hit points. The grip needs something to pull against.
- **They Go With It.** When Kyogre is freed, every Brine-Thing on the board is ordinary seawater in the same instant, mid-lunge, wherever it is. Sweep them off the table with your hand and say nothing while you do it.

**Actions**

- **Cold Grip.** *Melee Weapon Attack:* +7 to hit, reach 5 ft. *Hit:* 8 (1d8 + 3) cold damage, and the target has the **Grappled** condition (escape DC 13).

**Reactions**

- **It Lets Go.** When the creature it has grappled drops to 0 hit points, it releases immediately and moves up to its Speed toward the nearest creature still standing.

*Art brief:* A knee-high shape of dark seawater standing upright on dry pale sand, holding its own form the way a wave should not, with two long arms of water reaching forward and hands that are just hands enough to close. Where it stands the sand goes dark and frosts. No face, only a suggestion of one.

### Drownbell  
*Small aberration (corrupted), unaligned ✦ CR 2 (450 XP) ✦ one in the ceiling at initiative, a second descends at the start of round three*  
**Count:** 1 at start, 2 by round three  
**Role:** The ranged controller, and the only thing in the room Stabby cannot reach without spending his Sash. It forces Lilly and Ursa into a genuine target-priority argument every round, and its Hush is the single hardest thing in the fight because it switches off Deflect Attacks, Shield, Flash of Genius and Cosmic Omen. It has three separate answers (radiant, a Thorn Whip pull, and Air Dance), one per hero.

- **AC** 15  **HP** 40 (9d6 + 9)  **Speed** 0 ft, fly (hover) 20 ft
- **STR** 6 (-2)  **DEX** 16 (+3)  **CON** 12 (+1)  **INT** 6 (-2)  **WIS** 14 (+2)  **CHA** 10 (+0)
- **Imm.** cold ✦ (cond) grappled, restrained
- **Senses** blindsight 60 ft, passive Perception 12
- **Challenge** 2 (450 XP)

**Traits**

- **In the Ceiling.** It hovers just inside the water ceiling, 20 ft above the sand. Melee attacks cannot reach it without flight or forced movement.
- **Out of Water.** If it is ever pushed or pulled out of the water ceiling and into the air of the bell, it falls to the sand, has the **Prone** condition, its Speed is 0, and it cannot use Cold Lamp until something puts it back in water, which nothing will. **Thorn Whip pulls a Small creature up to 10 ft closer to the caster (verified 2026-09-05, dnd2024.wikidot.com/spell:thorn-whip)**, so one pull from below does it. Lilly's Force Ballista push moves it 5 ft, which does it from the right angle. Stabby's Air Dance gets him up there the honest way.
- **It Lamps the Far Ones.** It attacks the creature FARTHEST from Kyogre that it can see. This is a hard rule and it is why the round-one arithmetic works: it never piles onto the hero already in melee.
- **Cold, Not Cruel.** It never targets a creature at 0 hit points. The lamp follows what moves.

**Actions**

- **Cold Lamp.** *Ranged Spell Attack:* +7 to hit, range 60 ft. *Hit:* 13 (2d8 + 4) cold damage, and the target is pulled 10 ft toward the bell.
- **Hush (Recharge 5-6; UNCHARGED at initiative, first roll at the start of its second turn).** One creature it can see within 60 ft makes a DC 16 Constitution saving throw. On a failure, that creature cannot take **Reactions** until the end of its next turn. It does not make a sound. It just stops the sound of everything else.

**Reactions**

- **Guttering.** When it takes radiant damage, the lamp gutters and it cannot use Cold Lamp until the end of its next turn. Roughly half of this party's damage is radiant, so a Guiding Bolt or a Starry Wisp buys a round for free, and finding that out should be theirs.

*Art brief:* A pale jellyfish bell the size of a lantern hanging upside down just inside the underside of a hanging ceiling of seawater, lit from within by a cold blue-white glow, with long fine trailing threads hanging down into the dry air below it. Seen from beneath, so the water ceiling reads as a rippling silver sky.

### The Kept  
*Medium construct (a print left in black glass), unaligned ✦ CR 3 (700 XP) each ✦ three of them, rising at the start of round three ✦ they are not alive and they never were*  
**Count:** 3 (the Horned One, the Winged One, the Heavy One)  
**Role:** The arrival, and the moment the table believes it might lose. Three bodies with three different speeds, reaches and behaviours drop into the fight at once and change every target-priority answer the party had settled on. They also carry the loudest silent clue in the campaign: they are the three spent spikes standing up, wearing the shapes of guardians already taken, with dead stars at their chests except one.

- **AC** 16 (black glass)  **HP** 45 each (the Heavy One 60)  **Speed** by shape, see Remembered Shapes
- **STR** 16 (+3)  **DEX** 14 (+2)  **CON** 16 (+3)  **INT** 1 (-5)  **WIS** 6 (-2)  **CHA** 1 (-5)
- **Imm.** poison, psychic ✦ (cond) charmed, deafened, exhaustion, frightened, poisoned
- **Senses** blindsight 60 ft, passive Perception 8
- **Challenge** 3 (700 XP) each

**Traits**

- **A Print, Not a Person.** There is nothing alive in it. If Ursa reaches out with the Mark of Handling he finds nothing at all, which is worse than finding something, and that line is his to deliver to the table.
- **Three Rounds.** Each Kept collapses into ordinary sand at the end of the third round after it rises, whatever its hit points are. This cap is what keeps the peak from becoming a wipe, and it is what makes ignoring them a real and defensible choice.
- **Anchored.** Each Kept is bound to the spent spike standing upright in the sand behind it. Those spikes are **ordinary objects** (AC 12, 10 hit points) and are fair targets, unlike Kyogre's. Knock one over, with any forced-movement effect aimed at it or with an Action and a DC 12 Strength (Athletics) check, and its Kept immediately has the **Prone** condition and can take no action on its next turn.
- **Cleansing Edge Frees It.** A **Bloodied** Kept that Stabby hits with Cleansing Edge lets go at once and collapses into sand, whatever its remaining hit points. This is the Hollowsong rule from Fight 3 coming back on a bigger creature, and it is the third thing competing for his one Cleansing Edge each turn.
- **The Star at Its Chest.** Each Kept carries a small dead star. Two of them burn black. The third burns red, and it is not dead at all. When that one collapses, the red star does not go out: it comes loose and drifts up through the water ceiling and away. Nobody says a word about any of this, ever.
- **Only What Fights Back.** It never attacks or targets a creature at 0 hit points. It only remembers fighting things that fight back.
- **Remembered Shapes.** **The Horned One** (black star): Speed 60 ft; if it moves at least 20 ft straight toward a creature before hitting it, the target makes a DC 15 Strength saving throw or is knocked Prone. **The Winged One** (black star): fly 40 ft, Remembered Blow has reach 10 ft, and it does not provoke Opportunity Attacks when it flies out of reach. **The Heavy One** (RED star): Speed 20 ft, 60 hit points, Resistance to bludgeoning, piercing and slashing damage, and on its first turn the sand cracks under it: each creature within 10 ft makes a DC 15 Dexterity saving throw or takes 10 (3d6) bludgeoning damage.

**Actions**

- **Remembered Blow.** *Melee Weapon Attack:* +8 to hit, reach 5 ft (10 ft for the Winged One). *Hit:* 13 (2d8 + 4) force damage.

**Reactions**

- **Glassfall.** When it drops to 0 hit points or collapses at the end of its three rounds, each creature within 5 ft makes a DC 13 Dexterity saving throw or takes 5 (2d4) slashing damage from the shards.

*Art brief:* Three figures of black volcanic glass standing up out of pale sand in a row, each an unfinished silhouette of a different enormous creature: one horned and long-legged, one broad-winged, one low and heavy and plated. Each has a single small star burning in the centre of its chest. Two of those stars are black voids; the third is a live ember red. Behind them, three scarred black spikes stand upright in the sand like fence posts.


---

## Session 9, Unda: the Crossing, the Board Procedure, the Tide Token, and the Road Between (eight events)

### Brinehound  
*Medium beast (corrupted), unaligned ✦ CR 3 (700 XP) ✦ random encounters only ✦ 3, and they came up the road ahead of the Tide*  
**Count:** 3  
**Role:** Skirmisher and anchor of the road fight. Fast, always closing, always in Stabby's reach, and it Drags people toward the walls, so the party never gets to stand still. It is the body the melee hero can always find.

- **AC** 15 (slick hide)  **HP** 38 (7d8 + 7)  **Speed** 50 ft, swim 60 ft
- **STR** 16  **DEX** 18  **CON** 13  **INT** 4  **WIS** 12  **CHA** 6
- **Resist** cold  **Imm.** (cond) frightened
- **Senses** blindsight 30 ft, passive Perception 13
- **Challenge** 3 (700 XP)

**Traits**

- **Pack Line.** At the start of the encounter each Brinehound picks a DIFFERENT target if three or more creatures are within reach of the pack, and it does not change target while that creature is still standing. Three of them can never converge on one hero in the first round.
- **Pack Sense.** It has Advantage on attack rolls against a creature that is within 5 ft of another Brinehound.
- **Wall-Runner.** Moving into or out of a water wall costs it no extra movement and does not provoke Opportunity Attacks. It arrives from whichever side is least convenient.
- **It Hunts Movement.** A creature at 0 hit points is instantly uninteresting to it. It never attacks a downed hero and never finishes one. It turns and looks for something that is still running.

**Actions**

- **Bite.** *Melee Weapon Attack:* +7 to hit, reach 5 ft. *Hit:* 11 (2d6 + 4) piercing damage.
- **Drag (Bonus Action, only after it hits with Bite this turn).** The target makes a DC 13 Strength saving throw or is pulled 10 ft toward the nearest water wall. Being pulled through a wall deals no damage: the next wave returns the creature to the sand within one round, and it loses its movement on its next turn.

**Reactions**

- **Slip.** When it is hit by an attack it can see, it may move up to 10 ft without provoking Opportunity Attacks. This does not reduce the damage. It simply refuses to be where it was hit.

*Art brief:* A long, low, four-legged sea hunter the size of a big dog, pouring out of a vertical wall of ocean water onto dry pale sand, its body slick and dark like poured oil, webbed feet splayed. Where its eyes should be there is only moving black water, and a thin trail of that black runs back from its muzzle into the wall behind it. Underroot's warm ochres are absent: this is gold sand, blue-green water light, and one wrong dark.

### Ghostbell  
*Large aberration (corrupted), unaligned ✦ CR 2 (450 XP) ✦ random encounters only ✦ 2, drifting down out of the wall*  
**Count:** 2  
**Role:** Ranged controller. It hangs back at reach 15 and makes ears ring, so the party has a target-priority argument every round even on the road. It is also the fight's clever line: it is full of held air, and popping one in the right place walls the pack off.

- **AC** 13  **HP** 22 (4d10)  **Speed** 0 ft, **fly 20 ft** (hover), swim 20 ft
- **STR** 6  **DEX** 12  **CON** 11  **INT** 2  **WIS** 12  **CHA** 8
- **Resist** cold, lightning  **Vuln.** thunder
- **Imm.** (cond) grappled, prone, restrained
- **Senses** blindsight 60 ft, passive Perception 11
- **Challenge** 2 (450 XP)

**Traits**

- **Drawn to Warmth.** It drifts toward the warmest creature it can sense and closes to within 10 ft of it. Any hero with a Speed of 30 or more can always reach a Ghostbell if they decide it is worth the movement, which is the clause that keeps a melee-only hero in this fight.
- **Full of Held Air.** When it drops to 0 hit points it bursts. Every creature within 10 ft is stung and blinking for a moment, and no Brinehound will voluntarily enter that 10-ft space until the start of its next turn.
- **Nothing on the Floor.** It hunts warmth, and a hero on the sand at 0 hit points goes cold in its senses at once. It never attacks a creature at 0 hit points.

**Actions**

- **Ringing Sting.** *Melee Weapon Attack:* +6 to hit, reach 15 ft. *Hit:* 7 (1d8 + 3) cold damage, and the target makes a DC 13 Constitution saving throw or has Disadvantage on its next attack roll as its ears ring.

*Art brief:* A pale jellyfish the size of a cartwheel, drifting through the air inside a dry sand gallery rather than through water, its dome faintly luminous and ribbed like a struck bell, tendrils trailing almost to the floor. Threads of the same wrong black that fills the Brinehounds' eyes run through its dome like ink in milk. It should read as beautiful first and dangerous second.

### Nabber Shoal  
*Medium swarm of Tiny beasts, unaligned ✦ CR 1/2 (100 XP) ✦ random encounters only ✦ 3 shoals, and every one of them wants something shiny*  
**Count:** 3  
**Role:** Small pressure and comic relief. It deals no damage and cannot: it takes things, and it teaches the party where to put their light. Not corrupted, just larcenous.

- **AC** 15  **HP** 18 (4d8)  **Speed** 5 ft, **swim 60 ft**, and it is only out of the water for a second at a time
- **STR** 4  **DEX** 20  **CON** 10  **INT** 3  **WIS** 12  **CHA** 10
- **Resist** bludgeoning, piercing, slashing
- **Imm.** (cond) charmed, frightened, grappled, prone, restrained
- **Senses** passive Perception 13
- **Challenge** 1/2 (100 XP)

**Traits**

- **Never Fights.** It deals no damage of any kind and has no attack that could. If cornered it leaves.
- **Brightest First.** It always goes for whoever is carrying the most light. A light set down on the sand is a brighter thing than any person holding one, and a party that puts its lantern on the floor and steps back loses nothing at all.
- **Will Not Touch the Sphere.** One of them tries exactly once, gets both fins under it, achieves nothing, and the entire shoal panics and hits the ceiling. The Sphere is never a legal target.
- **Not Actually Thieves.** Hold up anything that shines and the shoal returns everything it took, plus one item that was never theirs and that nobody wants to think about too hard.

**Actions**

- **Snatch.** One creature within 5 ft makes a DC 14 Dexterity saving throw. On a failure, one loose object goes through the wall with the shoal. Never an attuned item, never a weapon in hand, never the Essence Sphere. On a success the shoal takes a bootlace instead and is pleased with itself.

**Reactions**

- **Scatter.** When any Nabber Shoal is reduced to 0 hit points, every other shoal leaves at once and takes what it has. The party will not be getting their things back that way.

*Art brief:* A single flat sheet of hand-sized silver fish arriving through a vertical wall of ocean into a dry sand gallery, all at once, like a thrown blanket. Enormous cartoonish eyes, every fish looking at a different carried object. One of them is comically wrestling a glowing sphere it cannot lift. Bright, funny, weightless: this is the session's one laugh.

### The Black Thread  
*Tiny ooze (the Tide's scout), unaligned ✦ CR 1 (200 XP) ✦ Wild dot, even ✦ 1, and it is faster than you*  
**Count:** 1  
**Role:** The race made touchable. One round of pressure that moves the token on the printed board, with no damage risk at all. It is the clearest possible demonstration that the Tide is a thing the party can act on.

- **AC** 15  **HP** 30 (it behaves like an object with hit points; no Hit Dice worth printing)  **Speed** 60 ft, climb 60 ft
- **STR** 1  **DEX** 20  **CON** 10  **INT** 1  **WIS** 3  **CHA** 1
- **Imm.** poison, psychic  **Imm.** (cond) blinded, charmed, deafened, exhaustion, frightened, grappled, incapacitated, paralyzed, petrified, prone, restrained, stunned
- **Senses** blindsight 120 ft (blind beyond this), passive Perception 6
- **Challenge** 1 (200 XP)

**Traits**

- **It Does Not Fight.** It has no attacks and makes none, ever, under any circumstances. It is going somewhere and the party is in the way of nothing.
- **Under Everything.** Solid barriers, closed doors, walls and Web do not stop it. It goes underneath. It cannot be blocked or held, only broken.
- **Takes Everything Normally.** It has no damage resistances of any kind. Radiant, force, fire, cold, thunder, a sword: every hero at this table has an answer, and that is deliberate.
- **Two Rounds.** It leaves the gallery at the end of the second round of the encounter and cannot be pursued. Kill it before then or it is gone.
- **The Door It Was Going to Open.** If it is destroyed, MOVE THE TIDE TOKEN BACK ONE SPACE. If it escapes, move the Tide token FORWARD one space. As it dies it makes one low note, like a struck bell heard from a long way underwater, and every air-bell on the road behind the party rings faintly in answer. Explain nothing. They will hear that note again at the trench.

**Actions**

- **Run.** It takes the Dash action on every one of its turns, always, and moves toward the trench.

*Art brief:* A bootlace-thin line of black water running along the seam where a dry gold sand floor meets a curved wall of lit ocean, moving with obvious purpose. Behind it the sand is grey and the small pale ringed polyps on the wall above it have snapped shut; ahead of it the sand still glows. Almost abstract: one wrong dark line across a beautiful room.


---

## Session 9, Unda: the Professor's Advice (Part One) and the whole ending (the Way Home, the homecoming, Drowning Lull, and the Piplup epilogue)

### Piplup  
*Small beast (Water), unaligned. Water-rift companion, joins at the Session 9 homecoming.*  
**Count:** 1 (roster companion, one companion out in the world at a time)  
**Role:** NOT AN ENEMY. Roster lane: PREVENT and RESTORE. He is the healer and the mitigator, deliberately last in damage and last in control so he never squats on the Fire and Air lanes. What he makes the party decide: whether the day's bleeding is happening in the backline (field Piplup) or on Stabby at Speed 65 out past 30 feet, where Mistguard cannot reach him (field Sandshrew instead). Swapping is Lilly's Action, so that decision costs a turn mid-fight and is nearly free before one.

- **AC** 13  **HP** 45 (10d6 + 10)  **Speed** 25 ft., swim 50 ft.
- **STR** 6  **DEX** 16  **CON** 12  **INT** 10  **WIS** 16  **CHA** 14
- **Saves** Dex +6, Wis +6  **Skills** Medicine +6, Performance +5
- **Resist** cold
- **Senses** darkvision 60 ft., passive Perception 13
- **Languages** understands its handler; says only his own name, with total clarity

**Traits**

- **Proud Heart.** Piplup has Advantage on saving throws against being Frightened, and nothing can make him retreat while a friend is down.
- **Slipstream.** While swimming, Piplup doesn't provoke Opportunity Attacks.

**Actions**

- **Multiattack.** Piplup makes two Ice Beam attacks.
- **Ice Beam.** *Ranged Attack:* +8 to hit, range 60/120 ft., one target. *Hit:* 10 (2d6 + 3) Cold damage, and the target's Speed drops by 10 feet until the end of its next turn (the slow doesn't stack).
- **Heal Bubble (Bonus Action, 5/Short Rest).** A shimmering bubble drifts to one creature Piplup can see within 30 feet and pops into cool silver mist: it regains 14 (2d8 + 5) hit points and is cured of the Poisoned condition.
- **Sea Mist (2/Day).** Piplup breathes out a rolling bank of cool silver fog: a 20-foot-radius Sphere centered on a point he can see within 60 feet, lasting 1 round. His friends always know where each other are inside it and nothing else does, so while in the fog allies have Advantage on attack rolls, attacks against them have Disadvantage, and they can Disengage for free.

**Reactions**

- **Mistguard.** *Reaction.* When a creature Piplup can see within 30 feet is hit by an attack, cold haze closes over it: that creature gains +5 AC against that attack, which may turn the hit into a miss. Decide after the roll, the way Lilly's Shield works.

*Art brief:* A very small round seabird-creature with a two-lobed deep-blue cap over a white face, dark blue eyes, a short gold beak, deep-blue back and flippers, a pale belly with two white spots, and yellow feet, standing braced on a wooden stool in a dim lamplit workroom at night, chin up, absolutely immovable. One flipper rests flat on the ribs of a sleeping goblin lying on a long bench; a bubble of cold silver light gathers under that flipper. Warm brass-and-amber lamplight against deep blue shadow, in the Session 8 illustration style. Use assets/art_refs/REF_piplup.png as the likeness reference per the Pokemon-ref rule.


---

## Drowning Lull (Lilly's Water discharge, unlocked at this homecoming)

LOCKED PRINTED TEXT. This goes verbatim on Lilly's sheet, into the Aether Channeler block in templates/build_compendium.py (REPLACING the superseded sketch at lines 822-826), and into the Session 9 document at the Two Sockets Lit beat.

**Water / Unda, the Drowning Lull.** As a Magic action, expend 1 use of Mote Channeling to fill a 20-foot-radius Sphere centered on a point you can see within 120 feet with the shimmer of still, sunlit deep water. This is a **Lingering Discharge**: it lasts 1 minute, the Sphere sustains it so it does not require Concentration, and you can end it early (no action required). You can sustain only one Lingering Discharge at a time; starting another ends the first.

The water is the memory of an ocean, not an ocean. It does not block sight, douse fire, wet anything, or make the ground slick, and nothing in it can drown.

- **The Heavy Water.** When an enemy enters the Sphere for the first time on a turn or starts its turn there, it makes a Wisdom saving throw against your spell save DC. On a failed save, until the start of its next turn its Speed is halved, it cannot take Reactions, and it can make only one attack if it takes the Attack action. *A monster's Multiattack counts as the Attack action for this, so an affected monster makes one attack instead of its full routine. Legendary actions are not affected.*
- **The Still Water Mends.** When an ally enters the Sphere for the first time on a turn or starts its turn there, it regains 2d8 Hit Points. A creature can regain Hit Points this way only once per Lull.
- **Unda Does Not Let Its Guests Drown.** An ally at 0 Hit Points inside the Sphere is Stable while it remains there.

At level 7 that is a DC 16 Wisdom save, and Mote Channeling is a pool of 2 uses regained on a Short Rest, shared with Aether Ward and Tectonic Slam.

DM NOTES, NOT PRINTED ON THE SHEET.

Why it is not a strictly better Tectonic Slam. It deals no damage, kills nothing, moves nothing, and knocks nothing prone. Against a Glimmerfin sheet or a Needlemaw pack, Slam removes bodies from the board and the Lull removes none, and dead is still the best control in the game. The Lull's customers are the things Slam cannot kill: Pillarbacks, the Blackcask, the Quiet Hand, Kyogre. Two answers, two uses, and Aether Ward is still sitting there wanting one of them.

Why the enemy always gets a fresh save. The zone taxes, it does not lock. A creature that saves is completely fine, a creature that fails gets one round of it, and anything can walk out at half Speed. Nobody at this table ever loses a turn to a die they did not get to roll, which is why this replaced the earlier sketch (Wisdom save or Incapacitated plus Speed 0 for a minute, ending early on damage). That sketch was a hard lock with an anti-synergy clause, and it punished the party for attacking the thing they had just locked down, which is the wrong shape for an eight-year-old at the table.

How it changes her turn. On the turn she plants it she spends her Magic action, so no True Strike shot: roughly 20 damage given up to buy a zone. Her Bonus Action cannon fires as normal that turn and every turn after, and from the next turn on her routine is exactly what it always was. The real change is positional. Aether Ward goes wherever she is, Tectonic Slam goes wherever they are, and the Lull is a PLACE that stays for a minute, which makes Lilly the person who decides where the fight happens. Ursa wants to stand in it. Puff and the companion want to stand in it. Stabby, at Speed 65, will not be in it, and that honest gap is worth saying out loud once: her best zone does the least for the hero who bleeds most, and that is exactly the day to field Sandshrew instead.

Table numbers. Against a two-attack brute doing about 15 a swing, a failed save costs it roughly 15 to 20 damage that round; three rounds of a brute standing in the zone is 45 to 60 prevented, plus 18 to 27 restored across two or three allies. Aether Ward delivers 42 to 70 temporary hit points instantly with no positioning cost. Tectonic Slam deals 27 per body caught, so 27 against one target and 81 to 108 against a cluster of three or four, plus prone. All three land in the same band, and the Lull's variance is the highest of the three: near zero in a fight where nothing crosses a fixed point, and best in the game in a boss fight.

SOURCES. The per-round rider is a deliberate SUBSET of the 2024 Slow spell (Speed halved, cannot take Reactions, one attack if it takes the Attack action), read at dnd2024.wikidot.com/spell:slow on 2026-09-05 via the in-app browser. The three clauses Slow also carries, the -2 to AC and Dexterity saves, the action-or-Bonus-Action restriction, and the 25 percent somatic failure, are deliberately NOT included, and that is what keeps an unlimited-target no-Concentration zone in band. Slow does not appear in SRD 5.2.1, so cite the wiki and never the SRD for it. Every other term is glossary-defined: Stable (reference/srd/14_rules_glossary.md:956-958), Temporary Hit Points (1068-1070), Sphere as an area of effect, the Attack action, and Reactions. The feature grants NO condition, because there is no Slowed condition in the 2024 list.

SYNC LIST, all in one commit with the text: templates/build_compendium.py:822-826 (replace the sketch), reference/campaign/lilly_kit.md:97-98 and :136 (add the Lull to the shared pool and to the Door C line), characters/builders/build_lilly.py and her printed sheet (add it beside Tectonic Slam), memory/campaign_canon.md (record the Session 9 homecoming grant). This is a publish-affecting edit: the Compendium PDF changes.
