# The Rift Run: Design Document for the Pokemon-Themed Back Half (Sessions 8 to 14)

*The Guardians of Elaria, a family D&D campaign on 2024 revised 5e. This document is the runnable design for the collecting-and-battling rift arc: the reusable game loop, the companion-catching system, a fully built Session 8 (the Earth Rift), a reskin guide for the other planes, and the open questions still owed to the DM.*

Built on `memory/campaign_canon.md` and `lore/world_history.md`. No canon is contradicted here and no table events are invented. This is a design layer that sits on top of the chronicle; where an older draft disagreed with the balance decisions below, the decisions below win.

---

## 1. Overview and the Core Loop

### 1.1 What a rift run is

The back half of the campaign is built on a single repeatable engine. After the one-year timeskip the party returns at level 7, and Guildmaster Vane's finished Rift Portal (Vane's Folly) lets them step through, one plane at a time, into the living worlds that hang around the Material world like the gears of a great clock. Each plane is anchored by a star that is going dark; each holds a corrupted guardian; freeing that guardian closes the rift and lets Ursa's Staff of Waking Constellations relight the star. That is the mission spine the kids already know from Session 7 and the Grand Custodian.

Layered over that spine is the heart of the back half: **collecting creatures.** Every plane is a living world themed by a Pokemon type family, teeming with wondrous creatures, most of them frightened rather than fierce. The party gathers essence across a run, and at the climax they spend it through Lilly's Essence Sphere to **catch** one of those creatures, adding it to a growing roster. The kids accrue a team over Sessions 8 through 12, field one companion at a time in battle, and in the finale (Session 14) the whole accrued roster manifests at once. Collecting is not a side activity. It is the point.

The five type-planes:

| Plane | Type family | Feel | Anchor-star |
|---|---|---|---|
| **Earth (Terra)** | Ground, Rock, Grass, Bug | Teeming stone-and-moss cathedral, warm and green | Antares (dimming) |
| **Water (Unda)** | Water, Ice, Poison | Drowned reefs and cold currents | Fomalhaut |
| **Air (Aer)** | Flying, Electric, Fairy | Sky-islands and storm-light | Vega (going dark) |
| **Fire (Ignis)** | Fire, Fighting, Steel | Volcanic forge-world | Aldebaran |
| **Shadow (Umbra)** | Ghost, Dark, Psychic | The climax plane, Nyxthid's own element | Algol (dark) |

The home world is **Normal** type. **Dragon** is reserved for legendary and boss tier only. Earth is Session 8, the tutorial rift; the others follow in order.

### 1.2 Shared-token, d6, co-op play

A rift run plays out on a printed **gameboard** (fully specified in Section 3). The rules of motion are deliberately simple so a seven-year-old can run them:

- The party is **one shared token** on a single winding path. There is no splitting, ever. Everyone advances together and resolves each tile together. This is pure co-op.
- What rotates is only the **honor of the roll.** Going around the table, players take turns being the **Pathfinder** for one turn. The youngest player (Stabby's player, age 7) rolls first, then it passes to the next seat.
- The Pathfinder rolls the **d6**, physically moves the shared token that many tiles, and reads aloud the name of the tile the party lands on. Then the whole party resolves that tile. Then the chair passes.

Rotating the roller rather than the mover means every child gets the dice-and-token moment on a fair cycle, and because there is only one token, no one's creature is ever left behind. The party stops **on** the tile the roll lands them on and resolves only that tile; they do not resolve tiles they pass over. A roll that would overshoot the boss lair simply arrives at the lair (you cannot overshoot the end).

**Anatomy of a turn:**

| Step | Who | What happens |
|---|---|---|
| 1. Roll | Pathfinder | d6 for movement |
| 2. Move | Pathfinder | Advance the shared token that many tiles |
| 3. Reveal | Pathfinder | Name the tile the party landed on |
| 4. Resolve | Whole party | Play out the tile together |
| 5. Bank | Essence-keeper | Slide the shared essence pip up by whatever dropped |
| 6. Pass | (table) | The Pathfinder chair moves one seat |

### 1.3 The locked essence economy

Essence is a **single shared pool.** Every creature the party defeats or calms sheds essence into it, tracked by one physical pip sliding along a numbered track printed along the board's bottom margin. The target is fixed: the party banks roughly **100 essence by the time they stand at the boss**, then spends it through the Sphere to catch a companion. The counter resets to zero for the next rift.

The single most important design decision in this whole document is that **reaching 100 by the boss is guaranteed by the structure of the board, not by luck.** Early drafts let the math float on random rolls, which risks a kid grinding for essence or, worse, arriving at the boss unable to catch. That is now locked:

**The locked drop values (pre-print these on the tiles so a kid can add them):**

| Source | Essence dropped |
|---|---|
| Each of the **4 Location tiles** | **exactly +20** |
| Small **Encounter tile** | **+8 to +10** (pre-set per encounter; see the Session 8 list) |
| The **Boss Lair Location** (the 4th) | its +20 is the chunk that tips the bar to or past 100 |

The four Location tiles alone guarantee a floor of **80 essence** (4 x 20). Three of them come before the boss; the fourth Location **is** the boss lair, and its +20 is deliberately the piece that carries the bar over the line. So the three pre-boss Locations give a guaranteed 60, the scripted small encounters between them add the rest, and the boss lair's own +20 tips it past 100. No dice roll can take the floor away and nothing grinds, because there is no random essence source in Session 8 at all (encounters are pre-assigned, not rolled on a table; see Section 3).

### 1.4 A worked example (sums past 100 at the boss)

Here is a full tile-by-tile trace of the Session 8 tutorial run, so the math is visible. The Location backbone (bold) is fixed regardless of the dice; the small encounters are the pre-set list from Section 3.7.

| Beat | Tile | What happens | Essence | Running total |
|---|---|---|---|---|
| 1 | **L1: Mosslight Landing** | Arrival, idol goes ice-cold, first tutorial beat | **+20** | **20** |
| 2 | Encounter | Quartzback Beetle (standard) | +10 | 30 |
| 3 | **L2: Chime Reef** | The singing-crystal puzzle | **+20** | **50** |
| 4 | Encounter | Root Lasher (standard) | +10 | 60 |
| 5 | **L3: Glassed Gallery** | Rescue fight, idol callback | **+20** | **80** |
| 6 | Encounter | Thornhopper Swarm (standard) | +8 | 88 |
| 7 | Encounter | Bramblehorn Bull leftovers, calmed | +8 | 96 |
| 8 | **L4: Heartroot Hollow (BOSS)** | Free Terranox; the lair's cache lands | **+20** | **116** |

The party crosses the 100 notch as the boss lair resolves, exactly on cue. Even a leaner run that skipped an encounter or two still banks the guaranteed 80 from the four Locations plus at least one or two scripted encounters, landing in the 96 to 116 band. **The economy cannot soft-lock the catch**, and it cannot be ground past its ceiling either, because the essence sources in Session 8 are all fixed rather than rolled.

> **Note on later sessions:** Sessions 9 onward add Event tiles, a risk-fork shortcut, and full type-based random-encounter tables (Section 4). Those introduce a small amount of essence variance, but the four-Location +20 floor of 80 is a permanent structural guarantee across every rift, so the same "guaranteed by structure" property holds for the whole arc.

---

## 2. The Pokemon Companion System

*A reusable rules module for the whole rift arc. Built on 2024 5e, the campaign house rules, and the Ghostbloom v3 power budget (AC ~15, HP 52, one reliable action, one 3-per-rest special). Designed to run at a table with a seven-year-old, an eleven-year-old, and an adult.*

### 2.1 What a companion is

A companion is a creature the party has caught in a rift and can now summon to fight alongside them. Ghostbloom is the first roster member; every creature caught after her joins the same list. Mechanically a fielded companion behaves like a summoned ally (think the 2024 Summon spells or a Ranger's Primal Companion): it has its own statblock and its own turn, it shares the party's fate, but it is never a full extra PC and must never outshine the kids' own heroes.

The roster is a **shared party resource**, not any one player's pet. This matters at this table: both children get a say, and no one feels they own the cool creature while a sibling is stuck with a dud. The party decides together.

### 2.2 How a catch joins the roster

Catching happens through **Lilly's Essence Sphere**, which is canonically a gatherer. When the shared essence counter reaches roughly 100 and the party defeats or frees the rift's boss, the Sphere is charged and a catch is offered:

1. The DM presents the catchable creature. In Session 8 this is a single young stone-shelled creature, **Cindershell** (Section 3.9). From Session 9 on, present a **choose-1-of-3** offer (echoing Aelwyn's original three creatures in Session 3); the party picks one and the others slip back into the rift as it closes.
2. Lilly's player rolls the Sphere's **Gathering check:** a flat d20, DC 10, with **advantage** if the party freed the guardian peacefully rather than only bludgeoning it. This roll is theater more than gate. A kid who has earned a creature across a whole session should not lose it to one bad d20. On a failure the creature wriggles free but stays nearby; the party gets one more roll at advantage, and the catch should essentially always land within two tries, so the session ends on triumph. It is never lost forever.
3. On success the creature is drawn into the Sphere and added to the roster permanently. Narrate the creature **choosing to come**, not being trapped. These are friends, not prisoners.

> **DM note:** The catch is an emotional beat, not a mechanical tax. Let the child who bonded with the creature during the session be the one to name it and welcome it. A kid-chosen name is worth more than any statblock.

### 2.3 Handler ownership (command of caught creatures)

To keep the roster fair and to head off sibling arguments before they start, each caught creature is assigned a **permanent kid "handler" in catch order.** The order is fixed and simple:

- **Catch #1 (Ghostbloom):** shared / auto-fielded in Session 8 (see below).
- **Catch #2:** handler is the **7-year-old** (Stabby's player).
- **Catch #3:** handler is the **11-year-old** (Ursa's player).
- **Catch #4:** back to the 7-year-old. And so on, alternating.

The handler is the player who runs that creature on its turn in combat and who gets first say in welcoming and naming it. Alternating in fixed catch order means the assignment is never up for negotiation, so there is nothing to argue about: the game decided, not a parent. Each caught creature also gets a **physical "active creature" card** (a half-page: AC, HP, speed, one attack, one special move, and a field note). That card is what the handler holds during a fight; it is all a young player needs.

In **Session 8 specifically**, the roster is just Ghostbloom, so she is simply auto-fielded in every fight and there is no selection step yet. The moment the **second** creature (Cindershell) is caught at the end of Session 8, the select step (below) switches on for Session 9.

### 2.4 Selecting who to field

At the **start of each battle**, before initiative, the party selects **ONE** companion from the roster to field. Only one companion is active at a time. This is the core Pokemon-flavored decision and it belongs to the whole table:

- Look at the enemies (type, resistances, the terrain) and pick the companion whose kit fits best. This is a real, kid-legible choice: "the bug guys are on fire tiles, so maybe not Cindershell, his moss doesn't grow on hot metal."
- Let the kids debate it for about thirty seconds, then call it. Keep it snappy.
- The fielded companion is summoned at the start of the first round (no action cost the first time; it appears with the party) and stays until the battle ends, it drops to 0 HP, or the party swaps it.

**Swapping mid-battle** is deliberately a little costly so the opening pick matters. Any hero can spend their **Bonus Action** to recall the fielded companion and field a different one; the new companion appears within 5 feet and acts on that hero's initiative for the rest of the fight (it does not get a turn the round it is swapped in, keeping it from being a free extra action; it can still take reactions). Ghostbloom is a full roster member and swaps by the exact same rule; she is simply the companion the party started with.

**A companion at 0 HP is not dead.** It is recalled to the Sphere, dazed, and cannot be fielded again until the party finishes a short or long rest. No death, ever. Creatures faint and recover, they do not die. (Death stakes are saved for the finale, and even there it is a heroic sacrifice, not gore.)

### 2.5 Who runs the companion, and the action-economy guardrail

The fielded companion's **handler** runs it, and it acts on the handler's turn, immediately after their own action, using the creature's card. The DM keeps a light hand on the reins: the DM decides nothing about the companion's turn except to gently steer an obviously self-destructive move ("are you sure you want to run into the lava?"). This keeps the adult free to run the monsters and the board. Do not have the DM run the companion; it doubles the DM's load and steals agency from the kids. The companion is a gift to the players; let them play it.

> **Action-economy guardrail:** one fielded companion, one turn per round, tied to a hero's initiative. That is the balance valve. It is roughly one extra "beast," never a second party. If a fight ever feels swingy because of the companion, the DM can rule a given enemy "too strong-willed" for a companion to easily land on, but this should be rare.

### 2.6 Keeping companions relevant from level 7 to 10

The party climbs from 7 to 10 across Sessions 8 to 14. Companions grow with the bond on a simple, no-bookkeeping track keyed to **party level, not XP:**

| Party level | Tier | What changes |
|---|---|---|
| 7 to 8 | **Sprout** | Base statblock as written. |
| 9 | **Bloom** | +15 HP; attacks deal +1 die of damage; attack and save-DC numbers +1. |
| 10 (finale) | **Radiant** | As Bloom, plus the Signature move recharges on a 5-6 instead of 6, and one flavorful "grown-up" perk in its statblock. |

Every statblock lists Sprout numbers with a **Growth** line giving the exact Bloom and Radiant deltas, so the DM upgrades the whole roster in about a minute before a session. Every companion is assumed to be at the party's current tier, so a creature caught late is never weaker than one caught early. The bond, not the calendar, sets the power.

### 2.7 The reusable companion statblock template

Copy this for every future plane's catch. The power budget is anchored to Ghostbloom v3 and to the 2024 Summon spells scaled for a level 7 to 10 ally.

> **Power budget (Sprout tier, for a level-7 party):**
> - **AC 14 to 16. HP 45 to 60** (Ghostbloom sits at 52). **Speed** 30 baseline, adjust for theme.
> - **One attack action:** one hit for ~2d6+4 (avg ~11) or two hits for ~1d6+3 each. Do not exceed ~14 average damage per turn at Sprout.
> - **One Signature move** on a **Recharge 6**, roughly the strength of a 3rd-level spell, usually with a rider (a small heal, a control effect, a battlefield trick), NOT big raw damage.
> - **One passive** that expresses the plane's type and gives the field-selection choice teeth.
> - **One thematic weakness** (Ghostbloom is vulnerable to fire and cold). This is the friendly-fire and tactics hook.
> - Proficient in **two** relevant saves and **one or two** skills. Keep it lean.

```
[NAME]  ("[Type tag, e.g. Rock/Bug companion]")
[Size] [creature type], loyal to the party

Look (one line): [vivid, kid-delightful visual]
Personality (one line): [why the table will love it]

AC    [14 to 16]
HP    [45 to 60]   (Growth: Bloom +15, Radiant +15)
Speed [30 ft., + any special mode]

STR [ ]  DEX [ ]  CON [ ]  INT [ ]  WIS [ ]  CHA [ ]

Saving Throws  [two]
Skills         [one or two]
Resistances / Immunities  [thematic, 1 to 2]
Vulnerability  [one thematic weakness]
Senses  [as fits], passive Perception [ ]
Languages  understands the party; communicates in [feelings / chimes / etc.]
Type-fit  [Earth / Water / Air / Fire / Shadow, for field-selection]

TRAITS
- [Passive #1, the type-expressing aura or trick.]
- [Optional passive #2, small flavor.]

ACTIONS
- [Attack]: Melee/Ranged, +[hit], reach/range, one target.
  Hit: [~2d6+4] [type] damage.   (Growth: Bloom +1 die, Radiant +1 die)

- SIGNATURE [Name] (Recharge 6; Radiant: Recharge 5-6):
  [One 3rd-level-ish effect with a rider. Save DC = 8 + prof + key mod.]

REACTIONS (zero or one)
- [One small reaction if the theme demands it.]

FIELD NOTE (for the handler card): [One sentence on when to pick this
companion over the others.]
```

That is the whole cost of a future catch: a name, a look, a personality, six ability scores, one attack, one Signature, one passive, one weakness. A DM can build a plane's companion in ten minutes.

### 2.8 What the roster builds toward: the finale sacrifice

Seed this expectation from Session 8 and never let it go: **every catch is a future finale hero.** In Session 14 the whole accrued roster manifests at once, and each companion spends its stored essence to reach the sleeping Elaria and restore the downed party. The kids should understand, in their bones, that the little creature they name at the end of the Earth Rift will one day stand in that final circle. Collecting is the point precisely because the collection is what saves everyone at the end.

Cindershell, the first catch, should be the one that plants itself in front of the fallen party one last time and pours out its little glowing garden to shield them, calm and unafraid, because being the brave little bodyguard was the only thing it ever wanted to be, and this time it finally gets it right.

---

## 3. Session 8: The Earth Rift

*The first rift run. One year after Gearhaven. A tutorial, scoped to be genuinely runnable in one family session of about three to three and a half hours.*

Session 8 teaches the entire engine while telling a complete homecoming-to-triumph story. It is deliberately lean: the crawl is a spine of about seven resolved tiles (four Locations plus three small Encounters), the cold open is time-boxed, and every fiddly system that would bloat a first session (Event tiles, the risk fork, random-encounter tables) is deferred to Session 9. What ships in Session 8 is the emotional shape of the whole back half: reunite, step through, gather, free the guardian, relight the star, catch a friend.

### 3.1 Cold open: "The Year the Star Went Thin" (time-boxed, ~15 minutes)

The session opens on a reunion at Vane's finished Rift Portal, one year after Gearhaven. Keep it to about fifteen minutes: this is a homecoming, not a briefing, and because the timeskip Door picks are not locked, the Door fallout is **narrated softly** rather than mechanically resolved at the table.

**The beats to hit:**

- **The three heroes return, one year older and changed.** Land level 7 through behavior, not numbers. Lilly is a builder now, sure-handed with her tools. Stabby has gone quiet and still, Master Kaelon's lesson finally rooted ("when the whole world is screaming, get still"), his hand resting near the idol he never asked for. Ursa carries a quiet, enormous weight behind her eyes, a year of the road worn into her like rings in a tree. Ask each player, in character, one thing their hero did during the year apart. If a player has decided their Door, invite them to color it in ("You spent the year at the Monastery / with Poots / on your father's trail"); if not, keep it soft ("You went somewhere and came back changed"). Do not force a Door reveal.
- **Ghostbloom's welcome is the emotional anchor.** She stayed with Vane the whole year (canon). Play her overjoyed, like a beloved pet reunited with her family, spinning once around each hero. She is also "Elaria's voice," and will be the first to feel the plane on the other side.
- **Vane reveals the finished portal.** Ten years of his work: a ring of dark iron and darker glass, tall as a house, empty in the center, waiting. The Essence Sphere sits cradled at its foot. "The Guild calls it the Rift Portal. Everyone else calls it Vane's Folly. A folly is just a hope that hasn't happened yet." That line is the thesis of the whole arc.
- **The clock:** Antares, the star that holds the world of stone and root steady, is going thin. When it goes out the crack it leaves will not close on its own, and nothing on our side can reach through to mend it (canon: rifts cannot be closed from our side). The Sphere is the key Vane was missing. The party has to go first.

> **Sample read-aloud (Vane, at the ring):** "The star is going out. Antares. When it goes, the crack it leaves behind will not close on its own. Nothing here can reach through and mend it. But you can. The Sphere is the key I was missing. It always was. And you three are the hands that turn it. One year I asked you to grow. You grew. Now I have to ask you for something harder. I have to ask you to go first."

**Two canon must-dos, woven into the threshold (do not skip):**

1. **Stabby's idol goes ice-cold.** The moment the party steps toward the ring, the little bundle at Stabby's ribs goes cold, the deep aching cold of a stone pulled from a winter river, so sudden he gasps. Read it small and private, to Stabby's player. He has felt it once before, a year ago, near Vane's unfinished door. No explanation (Door C seed, the Idol's Dreams). Ghostbloom's petals turn toward him, as if she almost hears something in it too.

2. **The companion offer is planted.** Before they go through, Vane presses the Sphere into Lilly's hands. "The Sphere gathers. The world you are going to is alive. It has creatures in it, frightened ones, hurting ones. Some of them can be helped. And a thing you help, sometimes, decides to come home with you. Gather enough, and the Sphere can hold a friend the way it has held Pikachu's spark all these years." This reframes the essence track as rescuing, not looting, and it echoes Aelwyn's choose-1-of-3 offer from Session 3. Ghostbloom stands right there as living proof it works.

### 3.2 The living Earth world: the Underroot

When the party steps through, they do not fall into a cave. They arrive on a **balcony of living stone**, high on the inner wall of a world that grew instead of being built. This is the **Underroot**: a cathedral-sized hollow world where the ground is the sky and the sky is more ground, a sphere of mossy rock cupped around a warm green glow that rises from below like a buried sunrise.

**What it looks like.** Boulders the size of houses hang furred in emerald moss and slow rivers of ivy. Crystal reefs grow sideways out of the walls, amber and rose and honey-gold, catching the underlight and throwing it around the hollow so the whole place shimmers like the inside of a geode. Mushroom groves taller than oak trees fan out in shelves and terraces, caps glowing soft blue and lantern-orange, and between them drift lazy motes of spore-light like slow snow that floats up instead of down. Nothing here is barren. The Underroot is the world's root cellar, the deep green place where growing things go to keep growing when the surface forgets them.

**What it sounds like.** A low, contented humming comes up through the soles of your boots, the sound of stone that is not quite asleep. Beetles the size of ponies click and burr in the ivy. Water drips somewhere, always, into pools that chime because they are full of crystal grit.

**Who lives here.** The **Mycoid** (say "MY-koyd"): gentle mushroom-people, knee-high to waist-high, who tend the glowing groves the way shepherds tend a flock, kindling and hooding their own caps to signal one another across the dark. They are close cousins of the Shroomytes the party already knows, and the kids should feel that echo. Around them live stone-shelled life of every size (pebble-beetles that roll into geodes when startled, reef-crawlers with backs of living crystal, moss-oxen, dinner-plate glimmer-moths) and, beneath it all, **Terranox's kin**, the great stone serpents that garden the deep. One of them has grown into something far larger and older, and it is sick.

**Where the sickness shows.** Antares is dimming, so the corruption creeps in a **direction**, and the party watches it thicken as they descend. Near the landing the moss is lush and the Mycoid only nervous. The closer the path winds toward the deep heart, the more the living rock goes wrong: a hard black glass-crust spreads over the moss like a frost that kills what it touches; the warm underlight curdles to bruised violet; crystal reefs crack and weep dark sap. The corruption is not the world. It is a wound in the world, and the kids are walking toward it to close it.

### 3.3 The four Location tiles

Each Location has bespoke art, a scripted beat, and a guaranteed **+20 essence** (locked, per Section 1.3).

#### L1: The Mosslight Landing (arrival, tutorial, idol beat)

**Art:** A wide balcony of rounded, moss-furred stone jutting into the hollow, railed by natural crystal spurs glowing warm gold. Behind the party, the shimmering circle of Vane's Folly hangs in the rock like a coin of daylight. Ahead and below, the whole green cathedral of the Underroot falls away, with a single darker smudge far down in the haze where the light goes wrong. Spore-motes drift upward.

**The beat (arrival + idol + companion tease):**
- The party lands together. Ghostbloom reacts to the plane as "Elaria's voice," her petals chiming brighter the moment her feet touch living stone: *this world can still be saved.*
- A frightened Mycoid elder, **Cap Umbrel**, creeps out from under a glowing toadstool. He first mistakes the heroes for corrupted "hard-shell walkers," then weeps with relief. In the plainest kid-facing terms he explains what has gone wrong: the deep-gardener, the great stone serpent who keeps the Underroot growing, has "gone hard and angry," and the killing black crust spreads a little farther every day. He points the way down.
- **MUST-DO, the idol:** the instant the party arrives on the Earth plane, **Stabby's mystery idol goes ice-cold**, cold enough to bite through the leather of his bag, and the corruption-crust visibly recoils in a small ring wherever Stabby stands. Cap Umbrel stares and whispers that it "smells of the deep-dark, but it keeps the rot back." No answers. Just the chill and the flinch. Anchoring the idol beat to the very first tile foreshadows early, before any fight. (Door C seed.)
- **The companion tease:** Cap Umbrel shows how the Essence Sphere drinks the loose light the corrupted creatures shed when they are calmed, and points to the essence track: *fill it, and the deep will let you keep one of its own.* This plants the essence economy and the end-of-rift catch in-world.

This is also the tutorial tile: teach the roll-move-resolve loop here on gentle ground before the first real fight.

**Guaranteed essence: +20.**

#### L2: The Chime Reef (puzzle set-piece, great for the 7-year-old)

**Art:** A sideways forest of enormous singing crystals, amber and rose and honey-gold, growing out of the wall in fans and pipes like a cave organ. Waterfalls of glittering crystal-grit pour between them into chiming pools. Glimmer-moths drift through beams of refracted light. On the far side, one great crystal has gone dark and cracked, leaking a thread of violet corruption, and the music around it is sour.

**The beat (a puzzle, low-combat):**
- The Chime Reef is a living instrument, and the path forward is blocked by a fall of grit that only stops when the reef sings its true chord. A cluster of glimmer-moths and a shy Reef-crawler shelter here, terrified silent by the sour dark crystal.
- **The puzzle:** four great crystal pipes ring the pool, each humming a different note (the Mycoid painted simple colored marks on them ages ago). Corruption has knocked one pipe out of tune. The kids strike the pipes (any character, no roll needed to try), listen, and figure out which one is wrong. A successful check (Perception, Performance, or Arcana; DC 13, and Ursa's star-sense or Lilly's tinkering both grant advantage in-fiction) identifies the soured pipe. Cleansing it spotlights a relic: Ursa's Staff, Lilly's cannon, or simply a well-described idea.
- **The reward:** when the true chord rings, the grit-fall stops, the dark crystal's thread of corruption snaps, and the sheltering Reef-crawler creeps out, calmed. The kids get their first taste of the loop: a frightened creature soothed rather than slain, shedding light into the Sphere.

**Guaranteed essence: +20.**

#### L3: The Glassed Gallery (rescue fight, the plane's real teeth, idol callback)

**Art:** A collapsed terrace of mushroom groves where the corruption has truly taken hold. Once-glowing toadstool trees are frozen under black mote-glass, their light trapped and flickering inside like fireflies in ice. The underlight has curdled to bruised violet. Stone-beetles stand fused and jagged, shells grown over with glassy spikes. A crust-bridge of black glass arches over a chasm, cracking underfoot. In the far shadows, a huddle of un-glassed Mycoid crouches behind a fallen cap, trapped and pleading.

**The beat (a rescue fight):**
- A band of corrupted stone-shelled creatures (glass-fused pebble-beetles and a larger Crag-brute, all Ground/Rock/Bug flavor) has cornered a family of Mycoid against the chasm. The heroes fight through to reach them before the crust-bridge gives way. The enemies are **sick, not evil**: describe them flinching from the light, hurting, lashing out. The kids are curing a fever, not slaughtering monsters. Kid-safe, real stakes.
- **The idol callback:** the corruption-crust recoils near Stabby again, more strongly this time, opening a safe lane across the crust-bridge wherever he leads. The idol is becoming a tool the party half-understands. Still no explanation.
- **The rescue payoff:** free the trapped Mycoid, and an old grove-keeper among them gives the party a boon (a one-use trinket or a free short-rest's worth of Hit Dice) and reframes the boss: the deep-gardener is "not a monster, it is our grandfather, and it is screaming." This tells the kids the boss is a rescue, not a kill, before they ever see it.

**Guaranteed essence: +20.**

#### L4: The Heartroot Hollow (the guardian's lair, the boss)

**Art:** The deep heart of the Underroot, a vast circular chamber where every root, vein of crystal, and river of moss converges like the spokes of a wheel. At the center, coiled around the **Heartroot** (a colossal pillar of living stone that is the world's spine), sleeps **Terranox**, the Earth-guardian: a mountain-huge serpent of living stone, scales like slabs of moss-veined granite, spine a ridge of enormous crystals gone violet-black and cracked. Jagged mote-glass has grown over its eyes and jaws like a muzzle of frozen tar. Overhead, through a natural oculus, the anchor-star **Antares** shows as a dim, guttering red ember, almost out. The chamber pulses with the serpent's pain.

The full boss design is Section 3.8. The lair's guaranteed **+20** essence is the chunk that tips the shared bar to or past 100 (Section 1.3), and it lands as Terranox is freed, so the catch becomes possible in the same breath.

### 3.4 The two-sheet gameboard (17 x 11)

**The spread.** Two US Letter sheets, **portrait**, butt together side by side to make one 17-wide by 11-tall landscape board, with a vertical seam down the exact center (the 8.5-inch mark). The background is one continuous high-res illustration of the Underroot hollow, painted so the seam falls through open haze and drifting spore-light, never across a Location tile or a key path junction.

**Two layers.** The art is clean background only: no grid, no numbers, no tile frames baked in. The winding path, tiles, Location frames, icons, and the numbered essence track all live on a **separate clean vector overlay** printed over the art. This lets the art be reprinted or reused and the overlay be corrected independently.

**The path (the journey down).** A single descending S-curve from top-left to bottom-center, tracing the party's descent from the balcony to the deep heart. It reads as "walking down into the world," and it drifts from lush green (top) toward corrupted violet-black (bottom) so the board itself shows the sickness thickening.

```
  LEFT SHEET          |          RIGHT SHEET
                      seam
 [L1] MOSSLIGHT LANDING (top-left, on the balcony)
     \                 |
      \__ travel/enc __|__
                        \  [L2] CHIME REEF (upper-mid, right sheet)
                        /  |
      __ travel/enc ___/   |
     /                     |
 [L3] GLASSED GALLERY      |
 (lower-mid, left sheet)   |
     \__ travel/enc ___    |
                       \___|___
                       [L4] HEARTROOT HOLLOW
                       (bottom-center, boss lair)
```

**Seam discipline (locked rules):**
- **No Location tile and no key junction sits on the seam.** L1 is top-left clear of the seam; L2 sits in the right sheet; L3 in the left sheet; L4 is bottom-center, framed wide so the seam passes through the dark haze around the lair, not across the lair art or its entrance.
- **The path crosses the seam only on plain TRAVEL segments,** through open haze: once between L1 and L2 (crossing right), once between L3 and L2's return (crossing back left). Never a fight or a decision on the seam.
- **The numbered essence track lives entirely on ONE sheet.** Print it as a horizontal row of pips along the bottom margin of the **right** sheet, running 0 to 100+, with the ~100 "CATCH" threshold clearly marked near the Heartroot end, directly beneath the boss lair, so the visual promise is obvious: *fill the bar, reach the boss, earn the catch.* Keeping the whole track on one sheet means the sliding pip never has to cross the seam.

**Margins:**
- **Title** in the top margin, spanning the seam (where it does no gameplay harm): "THE EARTH RIFT: The Underroot."
- **Legend/key** tucked into the top-left corner of the left sheet: tile-type icons, the d6-rotation reminder, "one active companion at a time."
- **Companion-roster strip** in the top-right corner of the right sheet: slots to note which creatures the party has caught and which is currently fielded. Ghostbloom occupies slot 1 at the start of Session 8.

### 3.5 Trackability: whose job is what

Assign these jobs out loud at the start, so nothing runs on mental math:

- **Essence-keeper (one person's explicit job):** the 11-year-old or the adult. This person, and only this person, slides the physical essence pip along the track every time a tile drops essence. Never mental math, never "I think we're around ninety." The pip is the truth.
- **Pathfinder:** rotates each turn (Section 1.2). Rolls, moves the shared token, names the tile.
- **Companion handler:** in Session 8, Ghostbloom is auto-fielded and the whole table can voice her; from Session 9 the fixed catch-order handler runs the fielded creature (Section 2.3).

### 3.6 Tutorial scope and timing

Session 8 uses only **Encounter, Location, and Travel** tiles. Event tiles, the risk fork, and the full random-encounter table are all **deferred to Session 9.** Encounters are **pre-assigned**, not rolled on a table live, so the pacing and the essence math are both predictable.

The resolved spine is about **seven tiles**: the four Locations plus about three small Encounters, connected by Travel steps. No dead time: every tile gives all three players something to do. On a Travel tile, hand the table one of these each time so nobody is idle:
- a line of banter to voice (Ghostbloom chimes, a Mycoid calls a greeting, Stabby mutters about the cold idol),
- a quick "spot the hidden essence mote" Perception check for a small flavor bonus (a shimmer in the moss; success is a nice description moment, not a grind),
- or a companion beat (Ghostbloom notices something, reacts to the plane).

**Wall-clock estimate (one family session, ~3 to 3.5 hours):**

| Segment | Time |
|---|---|
| Cold-open reunion at Vane's Folly + step-through | ~15 min |
| L1 Mosslight Landing (arrival, idol, tutorial of the loop) | ~20 min |
| Travel + first Encounter, leg to L2 | ~15 min |
| L2 Chime Reef (puzzle) | ~20 min |
| Travel + Encounter, leg to L3 | ~15 min |
| L3 Glassed Gallery (rescue fight) | ~25 min |
| Travel + final Encounter, leg to L4 | ~15 min |
| L4 Heartroot Hollow: the Terranox fight | ~30 to 40 min |
| Antares relights + the catch + tag scene | ~15 to 20 min |
| **Total** | **~3 to 3.5 hours** |

Pressure valves if running long: convert a planned Encounter to a Travel tile on the fly, or trim an enemy from a pack. If running short, add one of the deferred creatures as an extra Encounter.

### 3.7 The pre-set encounter list (Session 8)

Do not roll a table live in Session 8. Pre-assign these three encounters to the three small Encounter tiles, in this order (easy to hard), and pre-print each tile's essence value on the overlay. The full Earth random-encounter table is introduced in Session 9 (Section 4).

| Order | Encounter | Tier | Essence |
|---|---|---|---|
| 1st Encounter | Quartzback Beetle | standard | +10 |
| 2nd Encounter | Root Lasher | standard | +10 |
| 3rd Encounter | Thornhopper Swarm | standard | +8 |

All three creatures are drawn from the Earth bestiary below. They fight **reluctantly**: corruption makes them lash out, and kindness (a calm word, Ursa's Mark of Handling, a good roll) can end almost any fight early. Establish that gentle theme here so the boss's "free it, don't break it" turn lands as a promise kept, not a twist.

**Earth bestiary (Session 8 subset + the full roster for later reskins):**

**Quartzback Beetle** (standard, +10 essence): *A knee-high stag beetle whose back is a single slab of rose quartz; its horns spark faint pink when it charges.*
- AC 17 (crystal carapace), HP 42, Speed 25 ft., burrow 10 ft.
- **Gore:** Melee, +6, 5 ft. Hit: 2d6+4 piercing.
- **Crystal Flare** (Recharge 5-6): 15-ft. cone; DC 13 Dex save, 3d6 radiant on a fail (half on success), blinded until end of target's next turn on a fail.
- **Gemshell (passive):** the first time it takes damage each turn, reduce that damage by 3. Teaches the kids to burst it, not chip it.

**Root Lasher** (standard, +10 essence): *A wad of animate briar and grasping root, faceless but for a knot like a squinting eye; it erupts from the trail to grab an ankle.*
- AC 14, HP 38, Speed 10 ft. (burrows 15 ft. to reposition).
- **Root Grab:** Melee, +6, 15 ft. reach. Hit: 1d8+3 bludgeoning and grappled (escape DC 13). Holds two creatures.
- **Constrict** (only vs. a grappled creature): 2d6+3 bludgeoning, no roll.
- **Rooted Vigor (passive):** regains 5 HP at the start of its turn if grappling anyone. Fire damage stops the regen for a round. Cutting a friend loose is the smart play, a great teaching beat for Stabby's speed.

**Thornhopper Swarm** (standard, +8 essence): *A chittering wave of thumb-sized grasshoppers armored in rose-thorns; alone they are cute, together a problem with a thousand tiny knees.*
- AC 12, HP 30 (swarm), Speed 20 ft., climb 20 ft.
- **Prickle Storm:** Melee, +4, 5 ft. Hit: 3d4 piercing (half if the swarm is below half HP). Resistant to bludgeoning/piercing/slashing; vulnerable to area effects (Lilly's cannon, moonbeam, thunderwave).
- **Scatter and Reform (passive):** if reduced to 0 by a single-target attack, it instead drops to 5 HP and scatters 15 ft. (dies only to an area effect or a second 0). Teaches area-attack combos. Kid-safe: they hop off, they are not squashed.

*The rest of the Earth roster, for Session 9+ reskins and any extra Encounter needed: Pebblchurl (trash, catch-adjacent, +3), Mossback Trundler (trash, +4), Glowmoth Drifter (trash, catch-adjacent, +5), Geckalodon (elite, +16), Bramblehorn Bull (elite, +18, can be calmed to end the fight early: a rehearsal for the boss). Full statblocks live in the campaign bestiary; two entries, Pebblchurl and Glowmoth, can be calmed instead of fought for the first taste of the catch loop.*

### 3.8 The boss: Terranox (legendary-flavored, not a by-the-book legendary)

*Deep under a ceiling of dead-black crystal, the guardian sleeps in agony: a serpent of living stone the length of a village street, scales seamed with moss and ore, eyes two dimming embers the exact fading red of Antares overhead. Corruption has driven black crystal spikes down its spine like nails, and where they bite, the stone goes wrong. It does not roar. It groans, a sound like a mountain trying to say a name. This is Terranox. It is not your enemy. It is a friend in pain, and the black crystal is the thing you have come to break.*

This is the corrupted Earth-guardian, a legendary-**flavored** boss echoing the Large stone serpent the party first glimpsed in Session 2, now grown vast and sick. It is tuned as an effective CR 8 to 9 fight for three level-7 PCs plus one companion (Ghostbloom in Session 8). Crucially, it is **not** a by-the-book legendary monster: no legendary action economy, no lair-action gauntlet, no stacked legendary resistances. It fights like a cornered, grieving animal, and the win condition is **freeing** it, echoing the Grand Custodian in Session 7.

> **DM framing (say this to the table):** "You do not have to destroy Terranox. You have to free it. Every black crystal you shatter is one less nail in a good creature's back. When the last one falls, the guardian wakes up, and the rift begins to close."

**TERRANOX, the Undermountain Warden**, *Huge celestial (corrupted earth-guardian), boss-tier*

| | |
|---|---|
| **Armor Class** | 17 (living granite) |
| **Hit Points** | ~200 (a 3 to 4 round fight; do NOT tell the kids the number) |
| **Speed** | 40 ft., burrow 40 ft., climb 30 ft. |
| **Saving Throws** | Str +8, Con +7, Wis +5 |
| **Save DCs** | ~15 (single value, easy to remember) |
| **Resistances** | bludgeoning, piercing, slashing from nonmagical attacks |
| **Immunities** | poison; conditions poisoned, frightened (too sad to be scared) |
| **Senses** | tremorsense 60 ft., darkvision 120 ft., passive Perception 14 |
| **Corruption Vulnerability** | the black crystal nodes take double damage from radiant damage and from Ursa's Staff of Waking Constellations. Tell the kids this early. Ursa is the key. |

**The win condition: break the crystals, free the Warden.** Terranox has **four black corruption crystals** (spine, left flank, right flank, brow), each **AC 15, 20 HP,** a separate target. The fight is a race to shatter all four, not to drain the guardian's HP. Terranox's own ~200 HP is a "sadness meter": it never reaches 0 by the party's hand, and the kids should be told that. Bringing the guardian low only makes it groan and slow; the crystals are the objective. When the last crystal breaks, the guardian simply opens clear golden eyes. **No death, no final blow.**

**Balance decisions locked into this fight (from playtest review):**

- **Single-hit damage capped ~20 to 25.** Terranox's attacks knock heroes around, never one-shot them. Crush does 2d10+5 (avg 16, max 25); Boulder Toss does 2d8+5 (avg 14). Scary, never lethal in one blow to a level-7 PC.
- **One telegraphed big move on a timer.** Terranox **rears** on one turn (visibly, narrate it: "the whole serpent gathers itself and lifts"), and only on its **next** turn does it slam: **Sunder Tunnel**, each creature within 30 ft. makes a DC 15 Dex save for 4d6 bludgeoning (half on success) as the stone heaves. The rear gives the kids a full turn to spread out or take cover. It also opens a new tunnel for cover and can dislodge a crystal (dropping one crystal to 10 HP: the guardian fighting the corruption alongside them).
- **At most one legendary-resistance-style save,** used once, so Ursa's control still matters. Reserve it for a single dramatic moment (Terranox shrugging off one hold or one banishment attempt) and never again. Ursa's moonbeam, faerie fire, and battlefield control should otherwise land normally; the whole point of the Staff's double-damage rule is that her control is central, not fought against.
- **Fail-forward on a dropped PC.** A hero who hits 0 is **"knocked breathless,"** not dying: Terranox's own corruption recoils from hurting them (it does not want to), leaving them at 1 HP and prone, or Ghostbloom's Guardian's Light (1d8+3, 3/short rest) tops them up, or the fielded companion can rouse them. Nobody sits out the finale of the first rift. No death saves at this table in Session 8.

**Ordinary actions (no legendary action block):**
- **Multiattack:** one Crush and one Boulder Toss, OR Sunder Tunnel (after rearing) in place of both.
- **Crush:** Melee, +8, 15 ft. reach. Hit: 2d10+5 bludgeoning; a Medium-or-smaller target is pushed 10 ft. and must succeed on a DC 15 Str save or be knocked prone.
- **Boulder Toss:** Ranged, +7, 60 ft. Hit: 2d8+5 bludgeoning. On a miss, the boulder shatters into difficult terrain (scree) in a 10-ft. square (terrain, not extra damage).
- **Bonus Action, Groan of the Deep:** Terranox strains against a crystal from within. Roll d6; on 5-6 a random crystal takes 5 damage. The guardian is helping. Narrate it.

**Phases (three, a clean 3 to 4 round shape):**
- **Phase 1, four crystals:** Terranox lashes out unwillingly, always with the push/prone effects that knock heroes down rather than truly hurt them. Establish the pattern: hit the crystals, ride out the tail.
- **Phase 2, two crystals remain:** *"The great serpent's groan changes. It is fighting the corruption now, and it is fighting on your side."* Groan of the Deep now triggers on 4-6. Sunder Tunnel now always dislodges a crystal (drops one to 10 HP). Terranox stops targeting whoever last hit a crystal and starts cracking the crystals itself.
- **Phase 3, one crystal remains (the last nail):** the final crystal glows and grows to AC 15, 30 HP. Stage this so the whole team breaks the last nail together, and let **Ursa land the finishing hit with the Staff** whenever natural (the double damage makes it easy). If a younger player is itching, let Stabby's speed set it up and Ursa land it.

**Waking the Warden (the win, read aloud):**

> *The black crystal bursts like ice off a spring branch, and for one held breath the whole cavern is silent. Then Terranox lifts its enormous head, and its eyes, which were dying embers, kindle clear and gold. The wrongness drains out of the stone. Moss greens. Ore glints. The guardian looks down at three small heroes who came all this way to pull the nails from its back, and it lowers its great brow to the floor before you, the way a mountain might bow if a mountain could be grateful.*

- **The essence payoff:** the Heartroot Hollow's guaranteed +20 lands here (Section 1.3), tipping the shared counter to or past 100. This is the moment the catch becomes possible. Cue Lilly's Sphere.
- **The rift closes:** with the guardian freed, the cracks in Terra seal, exactly as they did for the Grand Custodian in Session 7. The living world is safe.
- **MUST-DO, relighting Antares (Ursa's spotlight):** Ursa raises the Staff of Waking Constellations to the oculus. She does not speak a spell; the Staff draws a line of pale fire from the guardian's golden eyes to the dimming red star, and **Antares relights**, flaring back to a steady, warm coal. The Underroot's underlight surges from bruised violet back to living green. If Ursa is not at the table, the Staff is the party's shared relic and any hero can raise it, but this is Ursa's moment by design.
- **MUST-DO, the idol beat closes:** at the moment the last crystal breaks, Stabby's idol goes ice-cold in his bag one last time (a callback to the Landing), radiating chill while the corruption recoils, then goes quiet and merely cool as Terranox wakes. No explanation. *"The idol has been ice-cold since you entered this place, Stabby. The moment the guardian wakes, it stops fighting you and rests in your hand, cool as a river stone. It knew something was wrong here. It seems glad it is over, too."*

**Safety valves:** Too easy? Add a fifth crystal, or have a broken crystal reform at 10 HP once in Phase 1. Too hard? Skip Boulder Toss, or let every crystal-hit also chip a neighbor for 5. Runtime flagging? Jump to Phase 3 after the second crystal; the emotional beat is the wake-up, not the grind. Aim for 3 to 4 rounds.

### 3.9 The first catch: Cindershell

With the guardian freed and the Sphere brimming, the deep keeps its promise from the Landing. In Session 8 this is a **single** creature, not a choose-1-of-3 (the three-way offer begins in Session 9). Deep in the plane, on the tumbled moss-furred boulders, the party had earlier found what looked like one more mossy rock, until it sneezed, rolled over, and looked up with two enormous hopeful eyes. It had been rolling itself downhill after the guardian's tremors knocked its family's nest apart, and it is very brave about being very lost. It decided, wordlessly, that the party is its family now.

> **Anchoring the catch to a specific board moment:** Cindershell is first *seen* as a scripted background creature during the leg between L3 (Glassed Gallery) and L4 (the boss), so the kids meet it before they catch it. The actual **catch resolves in the tag scene**, right after Antares relights and the Sphere fires. It pours out of the Sphere onto the Guild gallery floor at session's end (Section 3.10).

**CINDERSHELL**, *Small elemental (living stone), loyal to the party. Earth / Rock companion.*

- **Look:** A round, dome-shelled little tortoise-beetle of living gray stone, mossy green fuzz growing along the seams of its back like a tiny garden, with two big amber eyes and stubby stone feet that click when it walks.
- **Personality:** The party's clumsy, fearless little bodyguard. It plants itself between the heroes and danger every single time, whether or not that is a good idea, and it makes a happy pebbly rumble like a purr when someone is kind to it. The moss on its back has glowing seed-embers that brighten when it is happy and go dark when it is scared, so the kids read its mood by how brightly its little garden glows.

| | |
|---|---|
| **AC** | 16 (that shell is no joke) |
| **HP** | 54 (Growth: Bloom 69, Radiant 84) |
| **Speed** | 25 ft., burrow 15 ft. |
| **STR** 16 (+3) | **DEX** 8 (-1) |
| **CON** 16 (+3) | **INT** 6 (-2) |
| **WIS** 12 (+1) | **CHA** 12 (+1) |
| **Saving Throws** | Con +5, Str +5 |
| **Skills** | Athletics +5, Perception +3 |
| **Resistances** | bludgeoning, piercing, slashing from nonmagical attacks (the stone shell) |
| **Vulnerability** | thunder (a hard ringing note rattles it right out of its shell: the tactics and friendly-fire hook) |
| **Senses** | darkvision 60 ft., tremorsense 30 ft., passive Perception 13 |
| **Type-fit** | EARTH (Ground/Rock) |

**Traits:**
- **Little Bodyguard (passive):** while within 5 ft. of a downed or bloodied ally, that ally has half cover (+2 AC). It cannot help planting itself in the way; that is the whole point of it.
- **Mossy Mend (passive):** at the end of each of its turns, if it stands on natural ground (stone, soil, moss, most outdoor tiles), it regains 3 HP (Growth: Bloom 5, Radiant 7). Almost always on across the Earth board; off on a metal Fire-forge floor, a nice type-matchup wrinkle for later planes.

**Actions:**
- **Shell Bash:** Melee, +5, 5 ft. Hit: 2d6+3 bludgeoning (avg 10) (Growth: Bloom 3d6+3, Radiant 4d6+3). If it moved at least 10 ft. straight toward the target first, the target must succeed on a DC 13 Str save or be knocked prone. It gets a running start and just... bonks. It is very proud of this.
- **SIGNATURE, Curl and Roll!** (Recharge 6; Radiant: Recharge 5-6): Cindershell tucks in and rolls a 15-ft. line. Each creature in the line makes a DC 13 Dex save (DC = 8 + prof + CON). Fail: 2d8+3 bludgeoning (avg 12) and knocked prone. Success: half, not prone (Growth: Bloom 3d8+3, Radiant 4d8+3). It ends at the far end of the line so pleased that one ally it ends within 5 ft. of gains 5 temporary HP. It rolled all that way to come stand next to a friend. That was always the plan.

**Reactions:**
- **Take the Hit** (recharge after a short or long rest): when an ally it can see within 5 ft. is hit by an attack, Cindershell throws its shell in the way and becomes the target instead (its resistances still apply). It will do this every time it is allowed to; you may have to tell it to stop.

**Field note:** pick Cindershell when the party expects to get hit hard and wants a wall that heals itself on the ground. Shines on Earth, Water-ice, and outdoor boards; weakest on metal Fire-forge floors (no Mossy Mend) and against thunder-users (its one true fear).

*Balance check: AC 16 / HP 54 sits right on the Ghostbloom-anchored line (HP 52). Average damage ~10 per Shell Bash, ~12 on a recharged Signature, both under the ~14 Sprout ceiling. One 3rd-level-ish Signature on Recharge 6, one thematic passive (Mossy Mend), one support passive (Little Bodyguard), one clean weakness (thunder). It is a tank/protector, deliberately not a striker, so it complements Ghostbloom's healer role and never competes with the PCs for the big-damage spotlight.*

**Command ownership:** as catch #2, Cindershell's permanent handler is the **7-year-old** (Stabby's player), per the fixed catch-order rule (Section 2.3). A young kid running a big friendly creature that plants itself in front of danger is pure joy. Hand Stabby's player Cindershell's card. From Session 9 on, the party must **select** which of Ghostbloom or Cindershell to field at the start of each battle.

### 3.10 The tag scene: "What Came Back Through"

Runs after the win, the relight, and the idol beat. The party falls backward through the ring into the cool brass quiet of the Guild gallery, Vane's hands catching their shoulders, Ghostbloom spinning delirious circles, the Sphere blazing full and heavy in Lilly's arms.

Then Ghostbloom goes still, and Elaria's voice speaks through her (the voice they learned aboard a sinking ship and beneath a foggy town means *listen*):

> *"One star lit. Four still dark. And the one who is putting them out has noticed you now. He was there, at the edge of the stone world. You did not see him. He saw you. He is not troubled. He is pleased. He wanted to know what you could do. There was a mark on the far mountains of that world, burned into the rock in a hand you would know, Ursa. A word. It said: the pattern leads on. Following the dark. Your father stood in that world once. And the next star, the little one, the water-star, the thing that guards it is not sleeping and gentle like the serpent was. It is awake. And it is afraid of nothing."*

Then the weight lifts and Ghostbloom is just Ghostbloom again. The Sphere pulses, insistent, something inside pressing outward like a chick at an egg. Lilly opens her hands, and **Cindershell pours out and stands on the brass floor**, blinking, brand new to the world, the creature they chose to help instead of harm. It does not run. It came home with them.

> *"Well," said Ursa, kneeling to its level with a smile the whole year had not quite managed to put on her face. "Hello, you. Let's find out your name."*

**End the session on the name.** Hand the naming to the table; the 7-year-old (Cindershell's handler) should do the honors.

**DM notes on the tag scene:**
- The party won cleanly, and the tag immediately complicates it: Nyxthid (unnamed, "he") saw the whole thing and was *pleased*. The victory was a test he set, and they passed, which is worse. This keeps the arc from feeling like a checklist of five easy rifts.
- Three finale threads pulled at once, all soft: the **Ash breadcrumb** (a burned mark in Ash's own hand, echoing the canonical logbook line, "the pattern leads east, following the dark"; a private jolt for Ursa's player, slow-drip toward the Session 12 clue); the **Nyxthid glimpse** (named only as "he" until the Shadow Rift; unbothered and curious, the most unsettling thing an enemy can be); and **the next star is worse** (explicit on-ramp to Session 9 Water: its guardian is awake and unafraid, unlike the gentle Earth serpent).
- The catch is the joy note to end on. After the dread, the session closes warm.

### 3.11 Foreshadow tracker (Session 8 plants)

| Thread | Planted in S8 as | Pays off |
|---|---|---|
| **Ash Catchum** | A word burned into the far mountains in Ash's hand: "the pattern leads on, following the dark." Ursa's private jolt: her father stood in a rift world. | Major clue S12 (Shadow); Ash's fate decided before S12. Echoes the canonical Guild log. Resonates with Ursa's Door B if taken. |
| **Elaria** | Speaks through Ghostbloom: "One star lit, four still dark." Antares relit is the first of her lights rekindled. | Culminates S14: the built roster manifests at once and spends its essences to reach the sleeping Elaria and restore the downed party. |
| **Pikachu** | The Sphere "has held Pikachu's spark all these years"; the caught companion pours from the same Sphere, proving the mechanism. | Pikachu's full return S13. The catch mechanic is the dry-run for the spark's release. |
| **Companions-as-finale-army** | Vane's pre-transit promise; the first catch (Cindershell) walks out at session's end. Ghostbloom (#1) + Cindershell (#2). | S14 climax: the whole built team manifests together and sacrifices essences. Set the expectation now: collecting is the point. |
| **Nyxthid** | Unnamed "he" who watched the run and was pleased, treating the win as a test the party passed. | Named at the Shadow Rift (S12); first glimpsed as the Dark Figure at Stormwatch Cliffs (S3). His approval now = his ambush later. |
| **Stabby's idol** | Goes ice-cold at the threshold, at L1, and at the boss; corruption recoils from it; Ghostbloom almost hears something in it. | Door C seed (the Idol's Dreams / Shadow Breathing). Unexplained by design. Watch it at every future rift. |
| **The next guardian is worse** | Elaria's warning: the Water-star's guardian is "awake, and afraid of nothing." | Direct on-ramp to S9 (Water/Fomalhaut). Each rift's guardian harder to free than the last. |

---

## 4. Reskinning the Template for Water, Fire, and Air

The Session 8 build is a template. To spin up any later plane, keep the fixed frame and swap the type-flavored contents.

### 4.1 What stays fixed (every plane)

- **The board:** two-sheet 17 x 11 portrait spread, one continuous background + a separate vector overlay, one shared token, rotating d6 Pathfinder, pure co-op. Same seam discipline (no Location or junction on the seam; essence track on one sheet; path crosses the seam only on Travel).
- **The four-Location backbone at +20 each,** with the fourth being the boss lair whose +20 tips the bar past 100. The guaranteed floor of 80 essence is permanent across every rift.
- **The loop:** gather essence to ~100, free the corrupted guardian to close the rift, relight the anchor-star with Ursa's Staff, feed the Sphere, catch a companion, reset the counter.
- **The catch-and-roster system** (Section 2): fixed catch-order handlers, the select-at-battle step, the growth tiers, the companion statblock template, the finale-sacrifice payoff.
- **The boss philosophy:** legendary-flavored not by-the-book, effective CR scaling with party level, one telegraphed timed move, at most one legendary-resistance-style save, fail-forward "knocked breathless" instead of death, win by freeing not only killing.
- **The kid-safety rails:** creatures faint rather than die; enemies are sick or frightened rather than evil; single-hit damage never one-shots a PC; the catch essentially always lands within two tries.

### 4.2 What changes per plane (the type map)

| Plane | Type family | World feel (replace the Underroot) | Anchor-star to relight | Guardian & catch flavor |
|---|---|---|---|---|
| **Water (Unda), S9** | Water, Ice, Poison | Drowned reef-halls, cold currents, sunken light; its guardian is **awake and afraid of nothing** (per S8's tag warning) | Fomalhaut | A restless, defensive water-guardian; catch options lean tanky/control (an ice-shell, a healing tide, a poison-warding eel) |
| **Fire (Ignis), S10** | Fire, Fighting, Steel | A volcanic forge-world of ember-rivers and clanging metal terraces; **note:** metal floors switch OFF ground-based passives like Cindershell's Mossy Mend | Aldebaran | A forge-guardian; catch options lean striker/steel (Cindershell is weakest here, so the plane rewards fielding a fire-immune or metal creature) |
| **Air (Aer), S11** | Flying, Electric, Fairy | Sky-islands and storm-light, wind-bridges between floating stones; verticality is the tactical theme | Vega (going dark) | A tempest-guardian; catch options lean fast/flying/electric, rewarding mobility |

**Systems that switch on after Session 8 (all deferred out of the tutorial):**
- **Event tiles:** breathers and spice (essence caches, a traveler's boon, a lore whisper, a hazard save, a shortcut sign). Add these from Session 9.
- **Type-based random-encounter tables:** each plane rolls on its own d8 of type-appropriate creatures, replacing Session 8's pre-set list. Two or three entries per table should be **catch-adjacent** (calmable), so the catch loop is felt tile by tile.
- **The risk fork:** an optional harder shortcut on the leg before the boss, worth bonus essence, a genuine push-your-luck choice the kids make together. It is also the catch-up valve if a run is running low on essence.
- **The choose-1-of-3 catch offer:** from Session 9 on, present three catch candidates at the boss and let the party pick one (echoing Aelwyn). Alternate the handler by fixed catch order.

The **Shadow plane (Umbra, S12, Algol)** is the climax rift and Nyxthid's own element; it should break the comfortable template on purpose (a guardian that resists freeing, the idol's fullest reaction yet, the major Ash clue) and is out of scope for this document beyond the reskin frame above.

---

## 5. Open Questions and Decisions Still Needed From the DM

None of these block Session 8; they are choices that sharpen the arc.

1. **Door picks and their small buffs.** The Door picks are not locked, and Session 8 runs fine without them, but two picks would deepen the companion system if chosen:
   - **Ursa Door C (Beast Handler / Living World):** if chosen, Ursa's player becomes a natural co-runner for fielded companions, and you may grant a small buff (e.g. Ursa spends her own Bonus Action to let the fielded companion take Dash/Disengage/Dodge, mirroring 2024 companion handling). Does this change the fixed catch-order handler rule, or layer on top of it?
   - **Lilly Door C (Awakened Essence Sphere):** if chosen, consider dropping the Gathering-check DC from 10 to auto-success, or granting permanent advantage on catch rolls, since the Sphere is now sentient and eager. Confirm which.
2. **Catch-order vs. favorites.** The fixed catch-order handler rule (Section 2.3) is designed to prevent sibling arguments. Do you want a release valve where the kids may **trade** handler assignments by mutual agreement, or is the fixed order strictly better for your table?
3. **The choose-1-of-3 from Session 9.** Section 4 begins the three-way catch offer at Water. Confirm you want Session 8 to stay a single guaranteed catch (Cindershell) with the three-way offer starting in Session 9, versus offering three even in Session 8.
4. **Terranox HP and the crystal count.** The boss is written at ~200 HP with four crystals for a 3 to 4 round fight. If your table burst-damages hard, four crystals may fall in two rounds; if they are cautious, consider whether the fifth-crystal safety valve should be default-on. A quick gut-check against your kids' actual damage output would let me pin the exact number.
5. **Ash's fate.** Canon says Ash Catchum's fate is decided before Session 12. The Session 8 tag scene plants the breadcrumb but commits to nothing. Flagging only so the plant and the eventual reveal stay consistent; no decision needed yet.
6. **The idol's eventual answer.** The idol is unexplained by design (Door C seed). Its Session 8 reactions (ice-cold at the threshold, at L1, and at the boss; corruption recoils) are all consistent with any of the three eventual explanations. No decision needed now; noting so future rifts keep its behavior consistent.
```