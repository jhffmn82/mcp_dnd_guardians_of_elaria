# Campaign 2: The AI-Run Table (Vision and Architecture)

Captured 2026-07-29 from a design conversation between Justin and Claude. This is the
design of record for the campaign 2 project. Target timeframe: late 2027, after the
Guardians of Elaria finale. Status: vision locked at the architecture level; open
dials listed at the bottom. Nothing here is built yet.

## The dream (Justin's original six items)

1. An open world: world map, area maps, key-location maps (cities, dungeons, districts).
2. A populated world: NPCs, monsters, magic items, loot tables, quest hooks.
3. A light table (or TV) and an AI GM running sessions for the family in real time.
4. Push-to-talk speech input; NPCs answer with AI-generated voice lines.
5. Storyboards generated at the end of each session.
6. The storyboards compiled into a publishable book at campaign end.

## The two decisions that shape everything

**Justin is a hybrid GM/player; the AI is a performer, not an author.** Justin writes
the campaign (the "score"); the AI executes it: voices, pacing, rules, screen. Its
creative authority is limited to improvising inside the authored world when the kids
go off-script (they will). The score format is what makes that survivable: scenes with
goals rather than lines, NPCs as motivations rather than scripts, an explicit hard-canon
versus soft-canvas boundary, and pre-authored tripwires for predictable derailments.
The worldbuilding (items 1 and 2) is not reference material; it is the program the
engine runs.

**The AI never runs the interface.** Three layers, strictly separated:

- **Engine** (deterministic code, no AI): state store plus rules functions. HP, spell
  slots, initiative, token positions, conditions, inventory, dice math. The only thing
  that owns game state.
- **View** (the TV app): subscribes to engine state, redraws on change. A broadcast
  graphics package, not a game engine: React-style compositor in a fullscreen browser.
- **AI** (a client, like a player is): receives speech events, reads state by query,
  acts only through narrow tool calls (request_roll, apply_damage, set_mode, speak_as).
  Illegal calls are rejected by the engine. Decision and execution never live in the
  same component.

This is the same architecture as modern AI coding agents (model + narrow tools +
deterministic system + human review), wearing a wizard hat.

## Event sourcing is the spine

- **The journal** is an append-only event log and the sole ground truth: every
  declaration, roll, state change, and line of narration, in order. Nothing writes to
  any projection except through the log. DM overrides are privileged events
  ("DM ruling: the duke survived"), logged like everything else.
- **Everything else is a projection**, rebuildable from the log: the live game state
  table, every entity's current state, per-NPC knowledge.
- Payoffs: time travel (world-as-of-session-3), retcon detection (proposed memory
  contradicts an established projection and gets flagged, never silently overwritten),
  generated "previously on" openers, and desync as a formal, countable metric.
- The journal is also the raw manuscript: storyboards (item 5) and the book (item 6)
  are a summarization-and-illustration pass over a lossless session record.

## Three layers of state, three homes

| Layer | Holds | Store | Written by |
|---|---|---|---|
| Engine state | Mechanical truth right now (HP, positions, slots) | SQLite on the laptop | Engine, via tool calls |
| The score | Authored canon (world bible, NPCs, maps, loot, quests) | Git repo | Justin, between sessions |
| The memory tree | Accumulated narrative truth from play | Entity directories + manifest | The chronicler agent, DM-reviewed |

## The memory tree is the era/topic/leaf architecture, re-rooted

Direct transplant of the claude-archive memory system to a fictional world. Every item,
NPC, and location gets an entity directory:

```
world/npcs/marla_the_innkeeper/
  canon.md        authored score: motivations, secret, voice notes, never-does
  portrait.png    canonical ref image (plus derived grid token)
  state.json      projection: disposition_toward_party, location, alive, knows_X
  history/        leaves: s03_caught-stabby-pickpocketing.md, ...
```

Rules that keep it honest:

- **Authored versus derived, never blurred.** canon.md is Justin's; state.json and
  history/ are chronicler-written projections, rebuildable from the journal.
- **Write cadence: draft during a scene, commit at scene close, reconcile at session
  close.** Wet ink lies (the duke who looked dead gets revivified); truth is committed
  only when a scene resolves. Scene-grain commits mean same-session returns to a
  location find the tree current.
- **DM review gate as a git diff.** The chronicler commits post-session memory writes
  on a branch; Justin approves/edits/vetoes the diff. Nothing becomes world-truth
  without DM eyes. ("Never invent campaign events," enforced at the memory layer.)
- **Improvised entities are born structured**: auto-scaffolded directory at scene
  close, canon.md stub flagged provenance:improvised, first-generation portrait becomes
  the canonical ref (campaign 1's reference-registry habit, automated).
- **Subjective memory is derived, not stored**: "what does Marla know" is a witness
  filter over the event log. One log, many truths. Enables secrets, rumors, and
  dramatic irony as queryable state.
- RAG retrieval chunks along entity-directory boundaries; a manifest indexes it
  (manifest-index is load-bearing; do not rely on glob/grep over big trees).

## Agents: one performer, many stagehands

- **Foreground (one voice at a time):** a single conversational agent whose prompt and
  toolset swap with the mode. Never split the table-facing conversation across
  multiple talking agents; the seams become audible.
- **Background stagehands (async, invisible):** cartographer (scene graphs for
  on-the-fly battlemaps), illustrator (portraits for improvised NPCs), rules clerk
  (SRD lookups with citations), chronicler (journal to memory leaves). Each is a
  bolt-on that removes a job from the foreground prompt; each fails soft (cartographer
  down = theater of the mind for that fight).
- **Modes are a finite state machine** (combat, dialogue, exploration, downtime). Mode
  lives in the engine; the AI switches it by tool call; the switch swaps BOTH the
  screen layout and the foreground agent's toolset/prompt. An agent that cannot call
  apply_damage during a heart-to-heart cannot misuse it. Transitions are cheap
  production value (initiative sting, cards sliding in).

## Input architecture

Every input becomes a tagged event: who, what channel, what content. One event queue.

1. **Voice, push-to-talk, per kid.** Hold-to-talk gives speaker attribution for free,
   crosstalk immunity, and a privacy boundary: the AI only ever hears button-held
   speech, never ambient table audio. STT to {speaker, text} events. The brain
   classifies: dialogue / action declaration / question.
2. **Roll button.** The brain calls for rolls; a kid physically triggers them; dice
   animate on the TV (dddice-class 3D physics, arbitrary expressions like 3d8+1d6+4).
   The brain never both calls for and executes a roll.
   Hardware: one small box per kid: PTT button, roll button, LED ring in their accent
   color (hot mic / your turn). ESP32 build, or fallback to old phones running a
   two-button web app.
3. **Spatial.** Start voice-with-veto ("I move behind the cart"; brain places, kid
   corrects); add touch later only if missed. Avoids multi-user touch on a shared
   screen entirely.
4. **DM console: the universal escape hatch.** Correct mishears, type missed intent,
   approve/veto parsed actions (approval gate is a per-scene dial: up for boss fights,
   off for roleplay), veto maps, pause the brain, review memory diffs. If one
   interface gets hand-crafted design energy, it is this one.

## Physical setup

One laptop runs everything; the TV is an extended display (view fullscreen on monitor
2, DM console on monitor 1). No network, no server, no second machine. Kids' devices
talk to the laptop; NPC voices out the TV speakers. A light table later is still just
monitor 2. This is the proven Foundry-at-a-physical-table ergonomic.

Build-versus-buy note: evaluate Foundry VTT as engine/view substrate (it has the API,
dice, grid, sheets) versus custom compositor. The custom presentation Justin wants
(portraits beside location art, speaker highlight, scrolling dialogue band, combat log,
turn-order cards) exceeds stock Foundry; the likely answer is Foundry-as-engine or
fully custom view over a small bespoke engine. Decide at prototype time, not now.

## Art and maps

- **Environments: license, do not generate.** Forgotten Adventures / 2-Minute Tabletop
  style prop and texture libraries. Programmer energy goes into the composer, not
  the assets.
- **On-the-fly maps: LLM as art director, renderer as pixels.** Foreground agent emits
  a structured scene graph (backdrop, dimensions, props with positions/rotations/tags);
  a deterministic compositor draws it. Authored set-piece maps for the ~20 locations
  that matter; generation for everywhere else. Never hand-author 4-5 maps per
  environment; the kids will still go somewhere else.
- **Characters, items, monsters: generate**, governed by an explicit versioned style
  bible (palette, rendering style, line weight, lighting) so two years of model
  upgrades do not drift the art mid-campaign. Every significant creature gets a
  portrait AND a derived token (crop, accent ring, transparent background: a script).
  Canonical reference image per recurring character (campaign 1 registry, formalized).
- Placement quality bar is table-relative: score maps for what the kids actually do
  tactically, not RAW-optimal play.

## The grad project tie-in (the merge)

The memory tree IS the consistency engine, so campaign 2 and the IT 494 project are
one research program, two deployments:

- **Part 1 (IT 494, 2026-2027, unchanged scope):** productize the claude-archive
  memory backend into an installable suite for Claude Desktop (memory MCP server,
  journaling, chronicler write policy, review gate, scan-QR setup). Deployment domain:
  a real human life. Deliverables: symposium poster, preprint (the PhD-application
  publications fix).
- **Part 2 (late 2027, first PhD year if that lands):** re-root the same servers to a
  fictional world, add the deterministic game engine, view, voice loop, and table
  hardware. Deployment domain: the family campaign.

Research framing that elevates it beyond stack bingo: **fiction-state consistency in
interactive narrative agents.** The reconciler (prose in, schema-conformant state
deltas out), the autonomous memory-write policy (what is leaf-worthy, when is truth
settled), and desync as a measurable metric (narration contradicts projection,
projection contradicts log; count per session, show improvement). Ground truth exists
because the journal is lossless; adversarial input is generated free of charge by
children. The PhD narrative: external structured memory keeps agents truthful to a
persistent world, demonstrated on a human life and a fictional one.

## v0.1: the tavern test

The only question that threatens the project: does the magic survive contact with the
actual kids? Test it for a weekend of effort, not a year:

- One laptop, the living-room TV, ONE USB mic passed like a talking stick.
- No engine, no compositor, no hardware: the foreground agent, STT, one TTS voice,
  a static location image on monitor 2.
- Content: one authored tavern scene with a goal, a secret, and a tripwire.
- Run it inside campaign 1 as a low-stakes one-shot (dream sequence or tavern night)
  sometime in the remaining sessions. The kids get a gimmick night; the project gets
  data on latency, mishears, off-script recovery, and whether the kids talk to it.
- Pass criterion: the illusion holds while a kid leaves the script and the agent vamps
  inside the authored world for ninety seconds, then hands back to the plot.

## Open dials (decided later, listed so they are not forgotten)

1. Touch tokens on the table/TV versus voice-with-veto (starting voice; revisit).
2. Enemy tactics dial: kid-fair theatrical versus RAW-optimal (table-relative; likely
   theatrical with behavior notes authored per monster).
3. Foundry-as-substrate versus fully custom view+engine (decide at prototype).
4. TTS voice casting: per-NPC voices, consistency across sessions, kid-safe latency.
5. Hardware boxes (ESP32, accent-color LED rings) versus phone web-app fallback.
6. Always-listening ambient mode versus strict PTT (current call: strict PTT for
   privacy, attribution, and fewer misfires).
7. Light table hardware, if ever (changes nothing upstream; it is monitor 2).

## Relationship to campaign 1

Campaign 1 (Guardians of Elaria) finishes as planned: finale plus keepsake books by
Christmas 2027. It also serves as the pilot program: the art style bible and reference
registry are campaign 2 disciplines running at manual scale, the session log and canon
files are the memory tree at manual scale, and one of its remaining sessions hosts the
v0.1 tavern test.
