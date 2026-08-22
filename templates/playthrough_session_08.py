#!/usr/bin/env python3
"""Session 8 (Underroot) single-playthrough simulator on a 30x30 grid.

Unlike sim_session_08.py (3000-run Monte Carlo used to tune the numbers), this
runs ONE seeded playthrough with real positions, initiative, movement, action
economy and resource carryover, and logs every round for a table-style report.

Sources of record (recency rule):
  Enemies .... templates/build_session_08.py enemy cards (the retuned finals:
               Rotbloom AC12/22 x6, Mossmite x6, Chimestone AC16/52 x3,
               Shardwing AC14/22 x3, Weeper AC16/115 + 4 Cinderolls,
               Groudon AC18/230 with SPIKE AC17/60, Glassling spawn 1/round)
  Heroes ..... characters/builders/build_{lilly,stabby,ursa}.py (v3, L7)
  Ghostbloom . templates/build_bestiary.py level-7 card (AC16 HP62)
  Rules ...... memory/house_rules.md (Starseed not on star-arrow; Potent rides
               staff OR cantrip once/turn; 2024 Patient Defense etc.)

Run: LONG REST -> F1 Mosslight -> F2 Chime Reef -> SHORT REST -> F3 Gallery
     -> BOSS Groudon. Resources carry.

Table-relative tactics per the session doc: the party flails for a round, then
finds each fight's lever. Grid is 30x30, 5 ft per square, Chebyshev distance.
Declared simplifications: flying altitude abstracted to reach ("aloft" flag),
cones/lines resolved as nearest-N-in-arc, opportunity attacks only for the
cases the statblocks call out (Skitter/Glide exist to dodge them).
"""
import os
import random
import sys
from collections import Counter

SEED = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1] != '--sweep' else 20260818

# ---- pacing knobs (env vars, or exercised by --sweep) ----
# Baseline now matches the 2026-08-18 retuned doc: 8x Rotbloom 33 / 8x Mossmite,
# 4x Chimestone 78 / 4x Shardwing 33, Weeper 170, spike 60 WITH re-knit.
HPX = float(os.environ.get('S8_HPX', '1'))              # enemy HP multiplier
SPIKE_HP = int(os.environ.get('S8_SPIKE_HP', '160'))  # 80e0efd: 60 -> 160
SPIKE_REKNIT = os.environ.get('S8_SPIKE_REKNIT', '1') == '1'
#   Doc rule (2026-08-18): the spike regains 20 at the start of Groudon's turn
#   unless Cleansing Edge touched it since his last turn. Only Stabby makes
#   the damage STICK. Set S8_SPIKE_REKNIT=0 to compare without it.
BODIES = os.environ.get('S8_BODIES', '0') == '1'
#   The doc's own "too easy" scaling dials: mounds spend 2 more Mossmites,
#   2 more Shardwings drop from the spires on round 3, the second Cinderoll
#   pair arrives a round early, the spike drops 2 Glasslings a round.
GHOST_SUPPORT = os.environ.get('S8_GHOST_SUPPORT', '0') == '1'
#   Ghostbloom runs triage-only: Guardian's Light and guarding, no attacks.
NICHIRIN_RING = os.environ.get('S8_NICHIRIN_RING', '0') == '1'
FEY_HOUR = os.environ.get('S8_FEY_HOUR', 'carry')
#   Summon Fey runs ONE HOUR. 'carry' lets a spirit summoned at Mosslight
#   still be up at the Chime Reef (generous about the travel between
#   locations); 'onefight' expires it on the road, which is the honest
#   reading of a dungeon crawl with dot events between the landings.
WING_TARGET = os.environ.get('S8_WING_TARGET', 'weakest')
#   DM ruling 2026-08-20: the Shardwings hunt the WEAKEST party member, not
#   the nearest. They are flying predators and the doc's whole note on them
#   is 'nobody gets to stand still'. Everything else still targets nearest.
WING_PICKS_PUFF = os.environ.get('S8_WING_PICKS_PUFF', '0') == '1'
#   Open question for the DM: does a diving predator single out Puff (15 HP)?
ENGAGE = os.environ.get('S8_ENGAGE', 'far')
#   Where the enemies START. 'far' is the current staging (the doc supports it
#   for Mosslight, 'the grey holding the far rim', and for a stationary
#   Groudon); 'close' pulls every spawn 45% of the way toward the party, which
#   is what a DM does when they want the fight joined on round one.
BUBBLE_UNCAPPED = os.environ.get('S8_BUBBLE', 'capped') == 'uncapped'
#   Curl Up precedent: the Reaction itself is the limiter, no daily count.
MISTGUARD = int(os.environ.get('S8_MISTGUARD', '5'))
MG_MODE = os.environ.get('S8_MG_MODE', 'ac')   # damage | ac
#   'ac' (Justin, 2026-08-20): Mistguard becomes a Shield-style reaction
#   resolved AFTER the die, turning a hit into a miss rather than shaving it.
BEAM_HIT = int(os.environ.get('S8_BEAM_HIT', '8'))
MIST_ROUNDS = int(os.environ.get('S8_MIST_ROUNDS', '3'))
#   SEA MIST reborn (Justin, 2026-08-20): 1/day, a 20-ft-radius bank of fog.
#   Allies inside have ADVANTAGE on attacks; attacks against allies inside
#   have DISADVANTAGE. Lasts 2 rounds. This is his one big button.
BEAM_DIE = os.environ.get('S8_BEAM_DIE', '2d6')   # 2d6 | 1d8 | 1d10
PIPLUP_VER = os.environ.get('S8_PIPLUP', 'v4')   # v1 | v2 | v3 | v4
#   v4 (Justin, 2026-08-20): Action = Ice Beam with a 10-ft slow (a nudge,
#   not Air's 20-ft lane); BONUS = Heal Bubble, the deliberate choice;
#   REACTION = Mistguard, the reflex that shaves an incoming hit on an ally.
#   v3 (Justin, 2026-08-20): Action = one Ice Beam; BONUS = Mistguard, a
#   party-wide damage shave; REACTION = Heal Bubble, which always has a job
#   because damage always happens, and which he can turn on himself. Sea
#   Mist dropped: 1/day was doing nothing.
PIPLUP_V2 = PIPLUP_VER in ('v2', 'v3', 'v4')
BEAM_N = int(os.environ.get('S8_BEAM_N', '2'))   # Ice Beams per turn
#   Water re-scoped to PREVENT + RESTORE so it stops squatting on Fire's
#   damage lane and Air's control lane:
#     Ice Beam  -> ONE attack, no slow rider (the slow is Air's job)
#     Water Jet -> Disadvantage only, no damage
#     Bubble Shield (Action) -> 1d8+5 temp HP to one ally within 30 ft
#     Sea Mist (1/day) -> now actually modelled, his panic button
COMPANION = os.environ.get('S8_COMPANION', 'ghostbloom')
#   Only ONE companion is out at a time (roster rule). 'ghostbloom' is the
#   generalist; 'sandshrew' the Earth-rift tank; 'piplup' the Water-rift
#   healer. Stat blocks from templates/build_bestiary.py.
POLYMORPH = os.environ.get('S8_POLYMORPH', '0') == '1'
#   Cast EARLY (below 60%), not at the brink: it is an Action on his own turn,
#   not a Reaction, and temp HP do not revive a hero already at 0 (SRD
#   01_playing_the_game.md:831). Waiting for the brink measured no better than
#   never casting it at all.
#   Ursa's 4th-level slot on POLYMORPH, cast on a badly hurt ALLY, turning
#   them into a Giant Ape (SRD_CC_v5.2.1 p.348: CR 7, HP 168, AC 12, two
#   Fists at +9 for 3d10+6). The target gains Temporary Hit Points equal to
#   the beast's hit points, its stat block REPLACES theirs, and it cannot
#   speak or cast spells (SRD 12_spells_i-p.md:995-1020). Concentration.
PACK_TRIG = os.environ.get('S8_PACK_TRIG', 'both')   # move | both
URSA_LINE = os.environ.get('S8_URSA_LINE', 'pack')   # DM doctrine 2026-08-21
#   'control' = the tuned line (Plant Growth, Entangle, Moonbeam, Ice Storm).
#   'summon3' / 'summon4' = summon the Fey Spirit on turn 1 and then do
#   nothing but damage: Guiding Bolts while the free ones last, then
#   Starry Wisp. summon4 upgrades the spirit once (he has one 4th slot).
SHINE = os.environ.get('S8_SHINE', '0') == '1'
#   The suck-or-save shine pack: Groudon opens with Magma Vent, the drop
#   into the Hollow is a real DC 15 descent check, and heat-shear at the
#   spike makes the flyer check DC 15 Acrobatics each round (the climb
#   checks the doc wrote, restored against Air Dance).
#   DM-ruled a doc error 2026-08-18 (now fixed in the doc): Resonant Body
#   triggers on THUNDER damage and the Nichirin deals slashing/force.

rng = random.Random(SEED)
LOG = []


def ehp(n):
    return max(1, int(n * HPX))


def log(s):
    LOG.append(s)


def d(n, s):
    return sum(rng.randint(1, s) for _ in range(n))


def d20(adv=False, dis=False):
    r = rng.randint(1, 20)
    if adv and not dis:
        r2 = rng.randint(1, 20)
        return max(r, r2)
    if dis and not adv:
        r2 = rng.randint(1, 20)
        return min(r, r2)
    return r


def close_up(foes, party, frac=0.45):
    """Pull enemy starting positions toward the party by frac of the gap."""
    if ENGAGE != 'close' or not foes or not party:
        return
    cx = sum(h.pos[0] for h in party) / len(party)
    cy = sum(h.pos[1] for h in party) / len(party)
    for f in foes:
        f.pos[0] = int(round(f.pos[0] + (cx - f.pos[0]) * frac))
        f.pos[1] = int(round(f.pos[1] + (cy - f.pos[1]) * frac))


def cheb(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def ft(a, b):
    return cheb(a.pos, b.pos) * 5


class Actor:
    def __init__(self, name, ch, side, ac, hp, pos, speed, init_mod=0,
                 saves=None, resist=None, vuln=None, immune=None,
                 cond_imm=None, reach=5, fly=False, magical=True):
        self.name = name
        self.ch = ch
        self.side = side          # 'pc' or 'foe'
        self.ac = ac
        self.hp = self.hp_max = hp
        self.pos = list(pos)
        self.speed = speed
        self.init_mod = init_mod
        self.saves = saves or {}
        self.resist = resist or set()
        self.vuln = vuln or set()
        self.immune = immune or set()
        self.cond_imm = cond_imm or set()
        self.reach = reach
        self.fly = fly
        self.aloft = False        # out of melee reach of grounded creatures
        self.magical = magical    # weapon attacks count as magical
        self.temp = 0
        self.down = False
        self.drops = 0
        self.stunned = False
        self.prone = False
        self.fright = 0           # rounds of frightened (disadv on attacks)
        self.poisoned = 0
        self.damaged_since = False
        self.cleansed = False     # radiant/CE since its last turn
        self.reaction = True
        self.dodging = False      # Patient Defense: attackers at disadvantage
        self.entangled = 0        # restrained (Entangle) for N of its turns
        self.blinded = 0          # Blinded for N rounds
        self.slowed = 0           # Ice Beam -20 ft / Earthquake rubble
        self.cleanse_types = {'radiant', 'force'}   # per its own statblock
        self.restrained = False   # Roots Erupt / Entangle
        self.ape = False          # Polymorphed into a Giant Ape

    @property
    def alive(self):
        return self.hp > 0 and not self.down

    def dist_ft(self, other):
        return ft(self, other)

    def move_toward(self, dest, max_ft):
        steps = max_ft // 5
        x, y = self.pos
        while steps > 0 and (x, y) != tuple(dest):
            if x < dest[0]:
                x += 1
            elif x > dest[0]:
                x -= 1
            if y < dest[1]:
                y += 1
            elif y > dest[1]:
                y -= 1
            steps -= 1
        moved = (x, y) != tuple(self.pos)
        old = tuple(self.pos)
        self.pos = [x, y]
        return old, moved

    def approach(self, target, want_ft, max_ft):
        """Move toward target until within want_ft."""
        if self.slowed:
            max_ft = max(5, max_ft - 20)   # Ice Beam's slow / broken ground
            self.slowed = 0
        elif getattr(self, 'slowed_10', 0):
            max_ft = max(5, max_ft - 10)   # v4 Ice Beam's lighter chill
            self.slowed_10 = 0
        steps = max_ft // 5
        x, y = self.pos
        while steps > 0 and max(abs(x - target.pos[0]), abs(y - target.pos[1])) * 5 > want_ft:
            if x < target.pos[0]:
                x += 1
            elif x > target.pos[0]:
                x -= 1
            if y < target.pos[1]:
                y += 1
            elif y > target.pos[1]:
                y -= 1
            steps -= 1
        old = tuple(self.pos)
        self.pos = [x, y]
        return old, old != tuple(self.pos)


class State:
    """The whole run's shared resources."""
    def __init__(self):
        self.lilly = Actor('Lilly', 'L', 'pc', 20, 52, (0, 0), 25, init_mod=2,
                           saves=dict(str=-1, dex=2, con=5, int=8, wis=1, cha=-1))
        self.stabby = Actor('Stabby', 'S', 'pc', 18, 59, (0, 0), 55, init_mod=5,
                            saves=dict(str=2, dex=8, con=3, int=-1, wis=2, cha=-1))
        self.ursa = Actor('Ursa', 'U', 'pc', 18, 52, (0, 0), 30, init_mod=2,
                          saves=dict(str=-1, dex=2, con=2, int=4, wis=8, cha=-1))
        if COMPANION == 'sandshrew':
            self.ghost = Actor('Sandshrew', 'G', 'pc', 17, 78, (0, 0), 30, init_mod=2,
                               saves=dict(str=7, dex=2, con=5, int=-2, wis=1, cha=0),
                               resist={'nm-bludgeoning', 'nm-piercing', 'nm-slashing'},
                               vuln={'cold'}, reach=5)
        elif COMPANION == 'piplup':
            self.ghost = Actor('Piplup', 'G', 'pc', 13, 45, (0, 0), 25, init_mod=3,
                               saves=dict(str=-2, dex=6, con=1, int=0, wis=6, cha=2),
                               resist={'cold'}, reach=60)
        elif COMPANION in CANDIDATES:
            self.ghost = build_companion(COMPANION)
        else:
            self.ghost = Actor('Ghostbloom', 'G', 'pc', 16, 62, (0, 0), 30, init_mod=4,
                               saves=dict(str=-1, dex=8, con=8, int=1, wis=6, cha=3),
                               resist={'necrotic', 'nm-bludgeoning', 'nm-piercing', 'nm-slashing'},
                               vuln={'fire', 'cold'},
                               cond_imm={'charmed', 'frightened'}, reach=15, fly=True)
        self.ghost.kind = COMPANION
        self.heal_bubble = 5      # Piplup, 5/short rest
        self.sea_mist = DAILY_N   # Piplup, 2/day (DM 2026-08-22)
        self.challenged = None    # Sandshrew's Challenge target
        self.quake = None         # Sandshrew's broken ground: (x, y)
        self.mist_rounds = 0      # Piplup's Sea Mist
        self.mist_centre = (0, 0)
        # each candidate's showy ability. Togekiss's SING is 3/day (DM).
        self.big_left = AIR_SING if COMPANION == 'togekiss' else DAILY_N
        self.blessing = None
        self.blind_watch = []      # Togekiss
        self.quake_watch = []      # foes standing in the broken ground
        self.rage = 0             # Chimchar's Blaze
        self.burn_watch = []      # Growlithe's Burning targets
        self.puff = Actor('Puff', 'p', 'pc', 13, 15, (0, 0), 30, init_mod=4,
                          saves=dict(str=-1, dex=4, con=3, int=2, wis=2, cha=0),
                          immune={'poison'},
                          cond_imm={'poisoned', 'exhaustion'}, fly=True)
        self.puff.evasion = True
        self.cannon = Actor('Cannon', 'c', 'pc', 18, 35, (0, 0), 15)
        self.heroes = [self.lilly, self.stabby, self.ursa]
        self.pcs = [self.lilly, self.stabby, self.ursa, self.ghost, self.puff]

        # Lilly
        self.l_slot1, self.l_slot2 = 4, 3
        self.l_ward = 2
        self.l_fog = 5            # Flash of Genius
        self.mm_charges = 7       # Puff's Wand of Magic Missiles
        self.pipes = 3            # Pipes of Haunting, 3 charges
        # Stabby
        self.s_focus = 7
        self.s_metab = True
        self.s_fury = 3
        self.s_ignited = False
        self.s_airdance = True
        # Ursa
        self.u_slots = {1: 4, 2: 3, 3: 3, 4: 1}
        self.pack = None          # Conjure Animals: position, or None
        self.pack_lvl = 3
        self.u_wild = 3
        self.u_gbolt = 5          # Star Map free Guiding Bolts
        self.u_staff = 5          # staff charges (GB 1 each)
        self.u_omens = sorted([d20(), d20()], reverse=True)
        self.u_cosmic = 5
        self.u_aura = True        # Sigil-Stone Aura of Vitality 1/day
        self.aura_rounds = 0
        self.u_starry = False     # Starry Form up this fight
        self.resurgences = 0      # Wild Resurgence slot->Wild Shape swaps
        self.conc_lost = 0        # summons dropped by failed con saves
        self.fey_killed = 0       # summons beaten to 0 HP
        self.fey = None
        self.conc = None          # non-summon concentration (Moonbeam, Entangle)
        # Ghostbloom
        self.g_light = 3
        self.g_feystep = True
        self.g_wail = DAILY_N
        # bookkeeping
        self.gb_adv_target = None
        self.ward_pending = False
        self.omens_spent = 0
        self.cosmic_spent = 0
        self.tally = {'dealt': Counter(), 'taken': Counter(),
                      'healed': Counter(), 'kills': Counter(),
                      'prevented': Counter()}  # Guiding Bolt: next attack vs this has adv

    def spend_focus(self, n=1):
        if self.s_focus >= n:
            self.s_focus -= n
            return True
        return False

    def hero_save(self, hero, stat, dc, adv=False, tag=''):
        mod = hero.saves.get(stat, 0)
        if self.u_starry and hero is not self.ursa and not self.ursa.down:
            mod += 1              # Amulet of Guiding Light
        if stat == 'dex' and hero is self.stabby and self.s_ignited:
            adv = True
        roll = d20(adv=adv)
        # Omen dream: replace a dangerous roll before it counts
        if dc >= 16 and roll + mod < dc and self.u_omens and not self.ursa.down:
            best = self.u_omens[0]
            if best + mod >= dc:
                self.u_omens.pop(0)
                self.omens_spent += 1
                log(f"      * Ursa spends a dreamed omen ({best}) on {hero.name}'s save.")
                roll = best
        total = roll + mod
        ok = total >= dc
        if not ok and self.l_fog > 0 and not self.lilly.down \
                and self.lilly.reaction and self.lilly.dist_ft(hero) <= 30 \
                and total + 5 >= dc:
            self.l_fog -= 1
            self.lilly.reaction = False
            log(f"      * Flash of Genius! Lilly adds +5, {hero.name}'s "
                f"{stat.upper()} save {total}->{total + 5} vs DC {dc}: success. ({self.l_fog} left)")
            return True
        if not ok and self.u_cosmic > 0 and not self.ursa.down \
                and (dc >= 15 or tag == 'concentration') \
                and total + 3 >= dc:
            bump = d(1, 6) + 2
            self.u_cosmic -= 1
            self.cosmic_spent += 1
            if total + bump >= dc:
                log(f"      * Cosmic Omen (Weal +{bump}): {hero.name}'s save "
                    f"{total}->{total + bump} vs DC {dc}: success. ({self.u_cosmic} left)")
                return True
            log(f"      * Cosmic Omen (Weal +{bump}) not enough "
                f"({total}->{total + bump} vs DC {dc}). ({self.u_cosmic} left)")
            total += bump
        return total >= dc


def hero_check(st, hero, mod, dc, label):
    roll = d20()
    if dc >= 15 and roll + mod < dc and st.u_omens and not st.ursa.down:
        best = st.u_omens[0]
        if best + mod >= dc:
            st.u_omens.pop(0)
            st.omens_spent += 1
            log(f"      * Ursa saw this moment in a dream ({best}): he calls it "
                f"before {hero.name}'s {label} lands.")
            roll = best
    total = roll + mod
    if total < dc and st.l_fog > 0 and not st.lilly.down \
            and st.lilly.reaction and st.lilly.dist_ft(hero) <= 30 \
            and total + 5 >= dc:
        st.l_fog -= 1
        st.lilly.reaction = False
        log(f"      * FLASH OF GENIUS! Lilly shouts the trick: {hero.name}'s "
            f"{label} {total}->{total + 5} vs DC {dc}: success. [{st.l_fog} left]")
        return True
    if total < dc and st.u_cosmic > 0 and not st.ursa.down and total + 3 >= dc:
        bump = d(1, 6) + 2
        st.u_cosmic -= 1
        st.cosmic_spent += 1
        if total + bump >= dc:
            log(f"      * Cosmic Omen (Weal +{bump}): {hero.name}'s {label} "
                f"{total}->{total + bump} vs DC {dc}: success. [{st.u_cosmic} left]")
            return True
        log(f"      * Cosmic Omen (Weal +{bump}) is not enough on {hero.name}'s "
            f"{label}. [{st.u_cosmic} left]")
        total += bump
    return total >= dc


def deal(st, tgt, parts, magical=True, attacker=None, is_ce=False, credit=None):
    """parts: list of (amount, dtype). Returns damage actually dealt."""
    if is_ce and getattr(tgt, 'is_spike', False):
        # Cleansing Edge is one of the three things that can touch the spike.
        parts = [(amt, 'force') for amt, _ in parts]
        tgt.ce_touched = True
    if credit is None and attacker is not None:
        credit = attacker.name
    total = 0
    for amt, dtype in parts:
        if dtype in tgt.immune:
            continue
        if dtype in tgt.vuln:
            amt *= 2
        if dtype in tgt.resist:
            amt //= 2
        if not magical and ('nm-' + dtype) in tgt.resist:
            amt //= 2
        total += amt
    if tgt.stunned:
        total *= 2                # Resonant Body: double while stunned
    if tgt.side == 'pc' and tgt is st.stabby and tgt.reaction and total > 0 \
            and attacker is not None and any(
                t in ('bludgeoning', 'piercing', 'slashing') for _, t in parts):
        red = d(1, 10) + 12
        tgt.reaction = False
        cut = min(total, red)
        total -= cut
        st.tally['prevented']['Stabby (Deflect Attack)'] += cut
        log(f"      * Deflect Attack: Stabby swats {cut} off the hit"
            + (" (to 0!)" if total == 0 else f" ({total} gets through)"))
    if tgt.side == 'pc':
        st.tally['taken'][tgt.name] += total
    pre_kill = tgt.hp
    if tgt.side == 'foe' and credit:
        st.tally['dealt'][credit] += min(total, max(0, tgt.hp))
    # ---- candidate REACTIONS (boilerplate: each card has exactly one) ----
    if (tgt is st.ghost and total > 0 and tgt.reaction and attacker is not None
            and getattr(tgt, 'kind', '') in CANDIDATES):
        k = tgt.kind
        if k == 'chimchar':          # BACKDRAFT
            tgt.reaction = False
            burn = d(1, 6) + 3
            attacker.hp -= burn
            st.tally['dealt']['Chimchar'] += burn
            log(f"      * Backdraft: {attacker.name} takes {burn} fire for "
                "getting that close.")
        elif k == 'magmar':          # FLARE: it answers, it does not defend
            tgt.reaction = False
            burn = d(2, 6)
            attacker.hp -= burn
            st.tally['dealt']['Magmar'] += burn
            log(f"      * Flare: {attacker.name} takes {burn} fire for the trouble.")
        elif k == 'togekiss':        # CHARM (bespoke: not the Charmed condition)
            tgt.reaction = False
            if not foe_save(attacker, attacker.saves.get('wis', 0), 15):
                attacker.fright = 2      # sim: pure Disadvantage on its attacks
                st.tally['prevented']['Togekiss (charm)'] += 1
                log(f"      * Charm: {attacker.name} cannot bring itself to "
                    "swing properly at it.")
        elif k == 'pidgeot':         # SIDESTEP, it is never quite where you swung
            tgt.reaction = False
            cut = min(total, 6)
            total -= cut
            st.tally['prevented']['Pidgeot (sidestep)'] += cut
            log(f"      * Sidestep: Pidgeot rolls with it and {cut} never lands.")
    # GUARD DOG / WISH: reactions that trigger on an ALLY being hit
    if (tgt.side == 'pc' and tgt is not st.ghost and total > 0
            and st.ghost.alive and st.ghost.reaction
            and getattr(st.ghost, 'kind', '') in CANDIDATES):
        k = st.ghost.kind
        if k == 'growlithe' and st.ghost.dist_ft(tgt) <= 10 and attacker is not None:
            st.ghost.reaction = False
            hit2, crit2, _ = attack_roll(st, 8, attacker, attacker=st.ghost)
            if hit2:
                bite = d(2 if crit2 else 1, 8) + 4
                attacker.hp -= bite
                st.tally['dealt']['Growlithe'] += bite
                log(f"      * Guard Dog: Growlithe puts {bite} into "
                    f"{attacker.name} for touching one of hers.")
    # CURL UP: Sandshrew tucks behind its plates, reducing the hit by 10.
    if (tgt is st.ghost and getattr(tgt, 'kind', '') == 'sandshrew'
            and tgt.reaction and total > 0 and attacker is not None):
        tgt.reaction = False
        cut = min(total, 10)
        total -= cut
        st.tally['prevented']['Sandshrew (Curl Up)'] += cut
        log(f"      * Curl Up: Sandshrew tucks and {cut} skids off the plates"
            + (" (to 0!)" if total == 0 else f" ({total} gets through)"))
    # MISTGUARD. v3: a bonus-action aura, first hit on each ally each round.
    # v4: a REACTION, once per round, on whoever is being hit right now.
    if (PIPLUP_VER == 'v3' and total > 0 and tgt.side == 'pc'
            and getattr(tgt, 'mistguard', False)):
        tgt.mistguard = False
        cut = min(total, MISTGUARD)
        total -= cut
        st.tally['prevented']['Piplup (Mistguard)'] += cut
    elif (MG_MODE == 'damage' and PIPLUP_VER == 'v4' and total > 0
            and tgt.side == 'pc'
            and st.ghost.alive and st.ghost.kind == 'piplup'
            and st.ghost.reaction and st.ghost.dist_ft(tgt) <= 30):
        st.ghost.reaction = False
        cut = min(total, MISTGUARD)
        total -= cut
        st.tally['prevented']['Piplup (Mistguard)'] += cut
        log(f"      * Mistguard: cold haze closes over {tgt.name} and {cut} of it "
            "never lands.")
    if tgt.temp and total > 0:
        ab = min(tgt.temp, total)
        tgt.temp -= ab
        total -= ab
        if ab:
            log(f"      * {tgt.name}'s ward soaks {ab}.")
    pre = tgt.hp
    tgt.hp -= total
    if tgt.side == 'foe' and tgt.hp < 0:
        st.tally['prevented']['_overkill'] += min(-tgt.hp, total)
    if tgt.side == 'foe':
        st.tally['prevented']['_useful'] += min(pre, total)
    tgt.damaged_since = True
    if any(t in tgt.cleanse_types for _, t in parts) or is_ce:
        tgt.cleansed = True
    if tgt.side == 'foe' and credit and pre_kill > 0 and tgt.hp <= 0:
        st.tally['kills'][credit] += 1
    if tgt.hp <= 0:
        tgt.hp = 0
        if tgt is st.fey:
            st.fey_killed += 1
        if tgt.side == 'pc':
            if not tgt.down:
                tgt.down = True
                tgt.drops += 1
                log(f"      *** {tgt.name} DROPS to 0 HP! ***")
        # foes handle death in caller
    # HEAL BUBBLE as a REACTION (v3): damage always happens, so it always has
    # a job, and he can turn it on himself, which is his whole survivability.
    if (PIPLUP_VER == 'v3' and tgt.side == 'pc' and total > 0
            and st.ghost.alive and st.ghost.kind == 'piplup'
            and (BUBBLE_UNCAPPED or st.heal_bubble > 0) and st.ghost.reaction
            and st.ghost.dist_ft(tgt) <= 30
            and (tgt.down or tgt.hp < tgt.hp_max * 0.65)):
        st.heal_bubble -= 1
        st.ghost.reaction = False
        h = d(2, 8) + 5
        was = tgt.down
        tgt.hp = min(tgt.hp_max, tgt.hp + h)
        if tgt.hp > 0:
            tgt.down = False
        tgt.poisoned = 0
        st.tally['healed']['Piplup'] += h
        log(f"      * Heal Bubble: it pops over {tgt.name} for {h}"
            + (" and they are back up" if was else "")
            + f". [{st.heal_bubble} left]")
    # Guardian's Light: reaction heal when a hero is hurt
    if tgt.side == 'pc' and total > 0 and tgt is not st.ghost and st.g_light > 0 \
            and st.ghost.alive and not st.ghost.ape \
            and st.ghost.kind == 'ghostbloom' \
            and st.ghost.dist_ft(tgt) <= 30 \
            and (tgt.down or tgt.hp < tgt.hp_max * GLIGHT_AT) and st.ghost.reaction:
        st.g_light -= 1
        st.ghost.reaction = False
        st.tally['prevented']["Ghostbloom (guardian's light)"] += 1
        h = d(2, 8) + 3
        tgt.fright = 0          # the card ends charmed or frightened too
        was_down = tgt.down
        _before = tgt.hp
        tgt.hp = min(tgt.hp_max, tgt.hp + h)
        st.tally['healed']['Ghostbloom'] += tgt.hp - _before
        if tgt.hp > 0:
            tgt.down = False
        log(f"      * Guardian's Light: Ghostbloom heals {tgt.name} {h}"
            + (" (back on their feet!)" if was_down else "")
            + f" [{st.g_light} left]")
    return total


def attack_roll(st, bonus, tgt, adv=False, dis=False, attacker=None):
    if tgt.stunned:
        adv = True
    if (st.gb_adv_target is tgt and attacker is not None
            and attacker.side == 'pc'):
        adv = True
        st.gb_adv_target = None
    if tgt.dodging:
        dis = True
    if attacker is not None and attacker.side == 'foe' and tgt.side == 'pc':
        st.tally['prevented']['_enemy_swings'] += 1
    if getattr(tgt, 'entangled', 0) > 0 or getattr(tgt, 'restrained', False):
        adv = True
    if getattr(tgt, 'blinded', 0) > 0:
        adv = True
        st.tally['prevented']['_blind_adv_for_us'] += 1
    if getattr(attacker, 'smoked', 0):
        attacker.smoked = 0
        dis = True
    if st.blessing is attacker:
        adv = True
    if getattr(st, 'mist_rounds', 0) > 0:
        mc = st.mist_centre
        if (tgt.side == 'pc' and attacker is not None and attacker.side == 'foe'
                and max(abs(tgt.pos[0] - mc[0]), abs(tgt.pos[1] - mc[1])) * 5 <= 20):
            dis = True
        if (attacker is not None and attacker.side == 'pc'
                and max(abs(attacker.pos[0] - mc[0]),
                        abs(attacker.pos[1] - mc[1])) * 5 <= 20):
            adv = True
    # Sand Veil: attacks on Sandshrew from beyond 15 ft are at Disadvantage.
    if (tgt is st.ghost and tgt.kind == 'sandshrew' and attacker is not None
            and attacker.dist_ft(tgt) > 15):
        dis = True
    # Sandshrew's Challenge: the dared enemy swings at anyone else at Disadvantage.
    if (attacker is st.challenged and tgt is not st.ghost
            and st.ghost.alive and st.ghost.kind == 'sandshrew'):
        dis = True
        st.tally['prevented']['Sandshrew (Challenge bites)'] += 1
    # Piplup's Water Jet: a needle of water spoils an attack on a friend.
    if (PIPLUP_VER in ('v1', 'v2')
            and tgt.side == 'pc' and attacker is not None and attacker.side == 'foe'
            and st.ghost.alive and st.ghost.kind == 'piplup' and tgt is not st.ghost
            and st.ghost.reaction and st.ghost.dist_ft(attacker) <= 30):
        st.ghost.reaction = False
        dis = True
        if PIPLUP_V2:
            log(f"      * Water Jet: a needle of water crosses {attacker.name}'s "
                "eyeline and the swing goes wide.")
        else:
            jet = d(2, 6)
            attacker.hp -= jet
            st.tally['dealt']['Piplup'] += jet
            log(f"      * Water Jet: Piplup snaps a needle of water at "
                f"{attacker.name} ({jet} damage) and the swing goes wide.")
    if attacker is not None and (getattr(attacker, 'entangled', 0) > 0
                                 or getattr(attacker, 'restrained', False)):
        dis = True
    if attacker is not None and getattr(attacker, 'blinded', 0) > 0:
        dis = True
        st.tally['prevented']['_blind_dis_on_them'] += 1
    if tgt.prone and attacker is not None and attacker.dist_ft(tgt) <= 5:
        adv = True
    if attacker is not None and attacker.fright > 0:
        dis = True
    if (st.u_starry and attacker is not None and attacker.side == 'pc'
            and attacker is not st.ursa and not st.ursa.down
            and attacker.dist_ft(st.ursa) <= 30):
        bonus += 1              # Amulet of Guiding Light, allies only
    r = d20(adv=adv, dis=dis)
    crit = (r == 20)
    if r == 1:
        return False, False, r
    total = r + bonus
    # Reader of Omens, Woe: he reads the moment AFTER the die is rolled and
    # pulls an enemy's swing off line. Held for the swings that would hurt.
    if (attacker is not None and attacker.side == 'foe' and tgt.side == 'pc'
            and not crit and total >= tgt.ac and st.u_cosmic > 0
            and not st.ursa.down and st.ursa.dist_ft(tgt) <= 30
            and (tgt.hp <= tgt.hp_max * 0.5 or tgt.hp_max >= 200
                 or (tgt is st.ursa
                     and ((st.fey is not None and st.fey.hp > 0) or st.conc)))):
        bump = d(1, 6) + 2
        st.u_cosmic -= 1
        st.cosmic_spent += 1
        if total - bump < tgt.ac:
            log(f"      * COSMIC OMEN (Woe -{bump}): Ursa reads the swing and "
                f"{attacker.name}'s attack on {tgt.name} slides wide "
                f"({total}->{total - bump} vs AC {tgt.ac}). [{st.u_cosmic} left]")
            return False, False, r
        log(f"      * Cosmic Omen (Woe -{bump}) is not enough: it lands anyway. "
            f"[{st.u_cosmic} left]")
        total -= bump
    if (getattr(tgt, 'blessed_ac', 0) and attacker is not None
            and attacker.side == 'foe' and not crit
            and tgt.ac <= total < tgt.ac + 2):
        st.tally['prevented']['Togekiss (blessing)'] += 1
        log(f"      * Blessing: the blow slides off {tgt.name}.")
        return False, False, r
    # MISTGUARD (ac mode): the fog thickens and the blow goes wide.
    if (MG_MODE == 'ac' and PIPLUP_VER == 'v4' and tgt.side == 'pc' and not crit
            and st.ghost.alive and st.ghost.kind == 'piplup' and st.ghost.reaction
            and st.ghost.dist_ft(tgt) <= 30
            and tgt.ac <= total < tgt.ac + MISTGUARD):
        st.ghost.reaction = False
        st.tally['prevented']['Piplup (Mistguard)'] += 1
        log(f"      * Mistguard: the fog thickens over {tgt.name} and the blow "
            f"goes wide ({total} vs AC {tgt.ac + MISTGUARD}).")
        return False, False, r
    # Lilly's Shield reaction
    if tgt is st.lilly and tgt.reaction and st.l_slot1 > 0 and not crit \
            and tgt.ac <= total < tgt.ac + 5:
        st.l_slot1 -= 1
        tgt.reaction = False
        log(f"      * Shield! Lilly flicks the attack aside ({total} vs AC 25). "
            f"[{st.l_slot1} first-level slots left]")
        return False, False, r
    return (total >= tgt.ac or crit), crit, r


def ursa_starry(st, again=False, targets=None):
    """Starry Form (Archer), a Bonus Action costing one Wild Shape use.

    WILD RESURGENCE (SRD 04_classes_druid_fighter_monk.md:148): once on each of
    his turns, and ONLY if he has no uses of Wild Shape left, he can spend a
    spell slot (no action) to give himself one. His 2nd-level slots are the
    natural fuel: Summon Beast and Spike Growth both want the concentration
    his summon is already holding, so they would otherwise go unspent.
    """
    if st.u_starry or st.ursa.down:
        return False
    if st.u_wild <= 0:
        for lvl, ordinal in ((2, '2nd'), (1, '1st'), (3, '3rd')):
            if st.u_slots[lvl] > 0:
                st.u_slots[lvl] -= 1
                st.u_wild += 1
                st.resurgences += 1
                log(f"    Ursa: WILD RESURGENCE, no action, no uses left: he "
                    f"spends a {ordinal}-level slot and the starlight comes "
                    f"back to him. [slots {st.u_slots[1]}/{st.u_slots[2]}/"
                    f"{st.u_slots[3]}/{st.u_slots[4]}]")
                break
    if st.u_wild <= 0:
        log("    Ursa: no Wild Shape and no slot to burn; he fights unlit.")
        return False
    st.u_wild -= 1
    st.u_starry = True
    log(f"    Ursa: STARRY FORM (Archer){' again' if again else ''}; the Amulet "
        f"wakes, +1 to allies' attacks and saves. [Wild Shape {st.u_wild}]")
    # Archer fires ON ACTIVATION as well as on later turns (verified
    # dnd2024.wikidot.com/druid:circle-of-the-stars, 2026-08-21): "When you
    # activate this form AND as a Bonus Action on your subsequent turns".
    if targets:
        alive = [t for t in targets if t.hp > 0]
        if alive:
            star_arrow(st, alive[0])
    return True


def cast_polymorph(st):
    """Polymorph a hurt ally into a Giant Ape. Costs his only 4th-level slot
    AND his concentration, so the summon has to go."""
    if not POLYMORPH or st.u_slots[4] <= 0 or st.ursa.down:
        return False
    # Stabby is excluded on purpose: as an ape he loses Cleansing Edge, which is
    # the only thing that stops Re-Bloom, Glassbound and the spike re-knitting.
    cands = [h for h in (st.ghost, st.lilly) if h.alive and not h.ape
             and h.hp < h.hp_max * 0.60 and st.ursa.dist_ft(h) <= 60]
    if not cands:
        return False
    t = min(cands, key=lambda h: h.hp / h.hp_max)
    st.u_slots[4] -= 1
    if st.fey is not None:
        log("    (The fey spirit fades: he cannot hold both.)")
        st.fey = None
    ursa_take_conc(st, 'the Polymorph')
    t.ape = True
    t.temp = max(t.temp, 168)          # temp HP equal to the beast's hit points
    t.ape_ac, t.ac = t.ac, 12
    log(f"    Ursa: POLYMORPH. {t.name} comes apart and reassembles as a GIANT "
        f"APE: 168 temporary hit points, AC 12, two fists at +9 for 3d10+6. "
        f"[4th slots left {st.u_slots[4]}]")
    log("      (No speech, no spells, and it ends the moment those 168 run out.)")
    return True


def ape_turn(st, h, targets):
    """Two Fist attacks, +9 for 3d10+6 bludgeoning."""
    live = [t for t in targets if t.hp > 0]
    if not live:
        return
    for _ in range(2):
        live = [t for t in targets if t.hp > 0]
        if not live:
            return
        t = live[0]
        if h.dist_ft(t) > 10:
            h.approach(t, 10, 40)
        if h.dist_ft(t) > 10:
            log(f"    {h.name} (ape): lopes toward {t.name}.")
            return
        hit, crit, _ = attack_roll(st, 9, t, attacker=h)
        if hit:
            dmg = deal(st, t, [(d(6 if crit else 3, 10) + 6, 'bludgeoning')],
                       magical=False, attacker=h, credit='Ursa')
            log(f"    {h.name} (ape): FIST on {t.name} for {dmg}.")
            if t.hp <= 0:
                log(f"      {t.name} is destroyed.")
        else:
            log(f"    {h.name} (ape): fist crashes down beside {t.name}.")


def end_polymorph(st, h):
    if h.ape and h.temp <= 0:
        h.ape = False
        h.ac = getattr(h, 'ape_ac', h.ac)
        st.conc = None
        log(f"    The ape shape comes apart: {h.name} is themself again.")


# =====================================================================
# CANDIDATES for the two open lanes. FIRE must top damage (>14%, Ghostbloom's
# share) and lose on its own survival; AIR must top control (>18/day,
# Sandshrew's Challenge rate) and lose on damage. Every card carries the same
# boilerplate as the built three: two traits, an Action, a Bonus Action, a
# Reaction, and one showy 1/day.
AIR_DIE = tuple(int(x) for x in os.environ.get('S8_AIR_DIE', '2,6,2').split(','))
AIR_BLESS = os.environ.get('S8_AIR_BLESS', '1') == '1'
AIR_RIDER = os.environ.get('S8_AIR_RIDER', 'blind')   # stun | blind
AIR_DC = int(os.environ.get('S8_AIR_DC', '15'))
AIR_RIDER_N = int(os.environ.get('S8_AIR_RIDER_N', '2'))
AIR_SING = int(os.environ.get('S8_AIR_SING', '3'))
AIR_PICK = os.environ.get('S8_AIR_PICK', 'asis')  # near|fresh|big|hitter
FIRE_WHEEL = tuple(int(x) for x in os.environ.get('S8_FIRE_WHEEL', '2,6').split(','))
FIRE_SWINGS = int(os.environ.get('S8_FIRE_SWINGS', '2'))
FIRE_RADIUS = int(os.environ.get('S8_FIRE_RADIUS', '20'))
FIRE_BLITZ = os.environ.get('S8_FIRE_BLITZ', '1') == '1'
FIRE_BLAZE_AT = float(os.environ.get('S8_FIRE_BLAZE_AT', '0.5'))
FIRE_BLITZ_DICE = int(os.environ.get('S8_FIRE_BLITZ_DICE', '5'))
SHREW_MODE = os.environ.get('S8_SHREW', 'guard')   # guard | brawl
DAILY_N = int(os.environ.get('S8_DAILY_N', '2'))   # showpiece uses per day
GHOST_MODE = os.environ.get('S8_GHOST', 'guard')   # guard | chase
GLIGHT_AT = float(os.environ.get('S8_GLIGHT_AT', '1.01'))  # card: ANY damage
# The CARD has no hit-point threshold: Piplup may bubble anyone. 0.85 is a PLAY
# heuristic, not a rule - do not spend a charge on a scratch. Measured slightly
# better than spamming at 0.99 (knockdowns 0.04 vs 0.05, floor 77% vs 73%),
# because the charges are there when they matter.
BUBBLE_AT = float(os.environ.get('S8_BUBBLE_AT', '0.85'))
QUAKE_DICE = int(os.environ.get('S8_QUAKE_DICE', '3'))
QUAKE_NEED = int(os.environ.get('S8_QUAKE_NEED', '2'))
FIRE_SHROUD = os.environ.get('S8_FIRE_SHROUD', 'dodge')  # temp | dodge | off
FIRE_GATE = os.environ.get('S8_FIRE_GATE', '1') == '1'   # only while Blaze is lit

CANDIDATES = {
    # ---- FIRE: three different ways to be the striker ----
    'chimchar': dict(  # MELEE STRIKER: stands in it and burns it down
        ac=16, hp=70, speed=40, reach=5, fly=False, init=3,
        saves=dict(str=2, dex=6, con=4, int=-1, wis=1, cha=1),
        immune={'fire'}, vuln={'cold'}, resist=set()),
    'growlithe': dict(  # MELEE STRIKER alt: fewer, heavier bites + burn
        ac=16, hp=66, speed=50, reach=5, fly=False, init=4,
        saves=dict(str=4, dex=5, con=4, int=-2, wis=3, cha=2),
        immune={'fire'}, vuln={'cold'}, resist=set()),
    'magmar': dict(  # artillery: sets the room on fire from 60 ft
        ac=13, hp=46, speed=30, reach=60, fly=False, init=2,
        saves=dict(str=3, dex=3, con=5, int=0, wis=2, cha=1),
        immune={'fire'}, vuln={'cold'}, resist=set()),
    # ---- AIR: three different ways to be the denier ----
    'pidgeot': dict(  # positional denial: nothing stands where it wants to
        ac=16, hp=55, speed=60, reach=10, fly=True, init=5,
        saves=dict(str=4, dex=7, con=3, int=-1, wis=3, cha=2),
        immune=set(), vuln=set(), resist=set()),
    'togekiss': dict(  # AIR: ranged, fragile, buffs allies and debuffs foes
        ac=14, hp=50, speed=40, reach=60, fly=True, init=4,
        saves=dict(str=-1, dex=3, con=4, int=1, wis=4, cha=7),
        immune={'radiant'}, vuln={'necrotic'}, resist=set()),
}


def build_companion(kind):
    c = CANDIDATES[kind]
    a = Actor(kind.capitalize(), 'G', 'pc', c['ac'], c['hp'], (0, 0), c['speed'],
              init_mod=c['init'], saves=c['saves'], resist=c['resist'],
              vuln=c['vuln'], immune=c['immune'], reach=c['reach'], fly=c['fly'])
    a.kind = kind
    return a


def break_free(st, h, athletics):
    """Restrained by the glassed roots: an ACTION for a DC 14 Str (Athletics)
    check, per The Roots Erupt in build_session_08.py."""
    if not h.restrained:
        return False
    if hero_check(st, h, athletics, 14, 'Athletics to tear free'):
        h.restrained = False
        log(f"    {h.name}: rips free of the roots, and that was the whole turn.")
    else:
        log(f"    {h.name}: heaves against the glassed roots and stays caught.")
    return True


def cast_ward(st, where='before they close'):
    """Aether Ward: a Magic action with NO duration, so she spends it out of
    initiative and the action costs her nothing. One use of the Sphere's pool.
    Temp HP do not stack, so she holds the use if the shell is still good."""
    st.ward_pending = False
    if st.l_ward <= 0 or st.lilly.down:
        return False
    live = [h for h in st.pcs if not h.down]
    if live and min(h.temp for h in live) >= 9:
        log(f"    Lilly checks the Sphere and holds the use: the shell from "
            f"last time is still up. [{st.l_ward} left]")
        return False
    st.l_ward -= 1
    t = d(2, 8) + 5
    n = 0
    for h in st.pcs:
        if not h.down and h.dist_ft(st.lilly) <= 30:
            h.temp = max(h.temp, t)
            n += 1
    st.tally['prevented']['Lilly (Aether Ward temp)'] += t * n
    log(f"  Lilly: AETHER WARD {where}, out of initiative. The Sphere flares and "
        f"{t} temp HP settles over {n} of them within 30 ft. [{st.l_ward} left]")
    return True


def foe_save(foe, stat_mod, dc, adv=False):
    return d20(adv=adv) + stat_mod >= dc


def render_map(actors, terrain=None, size=30):
    grid = [['.' for _ in range(size)] for _ in range(size)]
    for (x, y), chs in (terrain or {}).items():
        if 0 <= x < size and 0 <= y < size:
            grid[y][x] = chs
    for a in actors:
        if a.hp > 0 or a.side == 'pc':
            x, y = a.pos
            if 0 <= x < size and 0 <= y < size:
                grid[y][x] = a.ch
    lines = ['    ' + ''.join(f'{i % 10}' for i in range(size))]
    for y in range(size):
        lines.append(f'{y:>3} ' + ''.join(grid[y]))
    return '\n'.join(lines)


def initiative(st, groups):
    """groups: list of (label, actors, mod). Heroes individually."""
    order = []
    for h, m in ((st.stabby, 5), (st.lilly, 2), (st.ursa, 2), (st.ghost, 4)):
        order.append((d20() + m, h.name, [h]))
    for label, actors, mod in groups:
        order.append((d20() + mod, label, actors))
    order.sort(key=lambda t: -t[0])
    log('  Initiative: ' + ', '.join(f'{n} {r}' for r, n, _ in order))
    return order


def ursa_triage(st):
    """Healing Word (bonus) on a downed friend; returns True if bonus used."""
    downed = [h for h in [st.lilly, st.stabby, st.ursa, st.ghost] if h.down]
    if not downed and st.u_slots[2] > 0:
        sick = [h for h in [st.stabby, st.lilly, st.ursa] if h.poisoned > 0]
        if sick:
            st.u_slots[2] -= 1
            sick[0].poisoned = 0
            log(f"    Ursa: LESSER RESTORATION (2nd, bonus action) scrubs the "
                f"spores out of {sick[0].name}. [{st.u_slots[2]} 2nd slots left]")
            return True
    if downed and st.u_slots[1] > 0:
        st.u_slots[1] -= 1
        h = d(2, 4) + 5
        st.tally['healed']['Ursa'] += h
        t = downed[0]
        t.hp = min(t.hp_max, t.hp + h)
        t.down = False
        log(f"    Ursa: HEALING WORD on {t.name}, back up with {t.hp} HP. "
            f"[{st.u_slots[1]} 1st slots left]")
        return True
    if downed and st.u_aura:
        st.u_aura = False
        st.aura_rounds = 10
        t = downed[0]
        h = d(2, 6)
        st.tally['healed']['Ursa'] += h
        t.hp = min(t.hp_max, t.hp + h)
        t.down = False
        log(f"    Ursa: lights ASH'S SIGIL-STONE, Aura of Vitality washes over "
            f"{t.name}: back up with {t.hp} HP.")
        return True
    return False


def aura_tick(st):
    if st.aura_rounds > 0:
        st.aura_rounds -= 1
        pool = [h for h in [st.lilly, st.stabby, st.ursa, st.ghost] if h.hp < h.hp_max]
        if pool:
            t = min(pool, key=lambda h: h.hp / h.hp_max)
            h = d(2, 6)
            st.tally['healed']['Ursa'] += h
            t.hp = min(t.hp_max, t.hp + h)
            if t.down and t.hp > 0:
                t.down = False
            log(f"    (Aura of Vitality: {t.name} heals {h}.)")


def start_round(st, rnd):
    log(f"  --- Round {rnd} ---")
    for a in st.pcs + [st.cannon]:
        a.reaction = True
        a.fright = max(0, a.fright - 1)
    if getattr(st, 'mist_rounds', 0) > 0:
        st.mist_rounds -= 1
    for _f in getattr(st, 'burn_watch', []):
        if _f.hp > 0 and getattr(_f, 'burning', 0) > 0:
            _f.burning -= 1
            _b = d(1, 6)
            _f.hp -= _b
            st.tally['dealt']['Growlithe'] += _b
            log(f"    {_f.name} is still burning: {_b}.")
    # BROKEN GROUND: anything standing in Sandshrew's quake wades.
    if getattr(st, 'quake', None) is not None:
        for _f in getattr(st, 'quake_watch', []):
            if _f.hp > 0 and max(abs(_f.pos[0] - st.quake[0]),
                                 abs(_f.pos[1] - st.quake[1])) <= 2:
                _f.slowed = 1
                st.tally['prevented']['Sandshrew (broken ground)'] += 1
    for _f in getattr(st, 'blind_watch', []):
        if getattr(_f, 'blinded', 0) > 0:
            _f.blinded -= 1
    aura_tick(st)


def katana_hit_dmg(st, crit=False):
    n = 2 if crit else 1
    parts = [(d(n, 10) + 7, 'slashing')]
    if st.s_ignited:
        parts.append((2, 'force'))
    return parts


def stabby_attack_routine(st, targets, rnd, fury_ok=True, devour=True,
                          chime_ring=False, no_bonus=False):
    """Two katana swings + Devour (or MA punch). targets = ordered kill list."""
    s = st.stabby
    live = lambda: [t for t in targets if t.hp > 0]
    for swing in range(2):
        ts = live()
        if not ts:
            return
        t = ts[0]
        if s.dist_ft(t) > 5:
            old, _ = s.approach(t, 5, st.s_speed_left)
        hit, crit, _ = attack_roll(st, 10, t, attacker=s)
        if hit:
            parts = katana_hit_dmg(st, crit)
            if fury_ok and st.s_fury > 0 and t.ch in 'CWDT':  # bigger than him
                parts.append((3, 'force'))
                st.s_fury -= 1
                fury_ok = False
            dmg = deal(st, t, parts, magical=True, attacker=s, is_ce=True)
            extra = ''
            if chime_ring and t.ch == 'C' and not t.stunned and t.hp > 0:
                t.stunned = True
                extra = ' The crystal RINGS: stunned!'
            log(f"    Stabby: katana {'CRIT ' if crit else ''}hits {t.name} for {dmg}."
                f" Cleansing Edge burns.{extra}")
            if t.hp <= 0:
                log(f"      {t.name} is destroyed.")
        else:
            log(f"    Stabby: katana misses {t.name}.")
    ts = live()
    if not ts or no_bonus:
        return
    t = ts[0]
    if devour and st.s_focus > 0:
        st.s_focus -= 1
        if s.dist_ft(t) > 5:
            s.approach(t, 5, 15)
        hit, crit, _ = attack_roll(st, 10, t, attacker=s)
        if hit:
            parts = [(d(6 if crit else 3, 8) + 9, 'force')]
            dmg = deal(st, t, parts, magical=True, attacker=s, is_ce=True)
            note = ''
            if t.hp <= 0:
                st.s_focus += 1
                note = ' It drops: Focus refunded!'
            log(f"    Stabby: FIRST FORM: DEVOUR {'CRIT ' if crit else ''}hits "
                f"{t.name} for {dmg}.{note} [Focus {st.s_focus}]")
        else:
            log(f"    Stabby: Devour misses {t.name}. [Focus {st.s_focus}]")
    else:
        hit, crit, _ = attack_roll(st, 10, t, attacker=s)
        if hit:
            dmg = deal(st, t, [(d(2 if crit else 1, 8) + 7, 'force')],
                       attacker=s, is_ce=True)
            log(f"    Stabby: bonus punch hits {t.name} for {dmg} force.")
        else:
            log(f"    Stabby: bonus punch misses {t.name}.")


def stabby_defensive(st, pool):
    """Low HP: swing at what is already in reach, then Patient Defense
    (1 Focus: Disengage + Dodge) and fall back on his speed."""
    s = st.stabby
    adj = [f for f in pool if f.hp > 0 and s.dist_ft(f) <= 5]
    if adj and s.hp >= 12:
        for _ in range(2):
            if adj[0].hp <= 0:
                break
            hit, crit, _ = attack_roll(st, 10, adj[0], attacker=s)
            if hit:
                dmg = deal(st, adj[0], katana_hit_dmg(st, crit), magical=True,
                           attacker=s, is_ce=True)
                log(f"    Stabby: (falling back) katana hits {adj[0].name} for {dmg}.")
                if adj[0].hp <= 0:
                    log(f"      {adj[0].name} is destroyed.")
            else:
                log(f"    Stabby: (falling back) katana misses {adj[0].name}.")
    rally = (st.lilly.pos[0], min(29, st.lilly.pos[1] + 4))
    if st.s_focus > 0:
        st.s_focus -= 1
        s.dodging = True
        old, _ = s.move_toward(rally, 65)
        log(f"    Stabby: PATIENT DEFENSE (1 Focus), Disengage and Dodge, falling "
            f"back {old}->{tuple(s.pos)} behind the line. [Focus {st.s_focus}]")
    else:
        old, _ = s.move_toward(rally, 65)
        log(f"    Stabby: Nimble Escape, Disengages and falls back "
            f"{old}->{tuple(s.pos)}.")


def puff_pipes(st, foes):
    """Pipes of Haunting (build_lilly.py:226): Magic action, 1 charge, each
    creature she chooses within 30 ft, Wis save DC 15 or Frightened 1 minute.
    A creature that SAVES is immune to the pipes for 24 hours."""
    if st.puff.down or st.pipes <= 0:
        return False
    pool = [f for f in foes if f.hp > 0 and not getattr(f, 'pipes_immune', False)
            and 'frightened' not in f.cond_imm and f.fright <= 0
            and st.puff.dist_ft(f) <= 30]
    if len(pool) < 3:
        return False
    st.pipes -= 1
    log(f"    Puff: PIPES OF HAUNTING, a thin ugly tune over {len(pool)} of them. "
        f"[{st.pipes} charges left]")
    for f in pool:
        if foe_save(f, f.saves.get('wis', 0), 15):
            f.pipes_immune = True
            log(f"      {f.name} shrugs the tune off for good.")
        else:
            f.fright = 4
            log(f"      {f.name} is FRIGHTENED: disadvantage on everything it swings.")
    return True


def puff_turn(st, target, use_mm, overload=False):
    if st.puff.down:
        return
    if use_mm and st.mm_charges > 0 and target is not None and target.hp > 0:
        # 1 charge = 3 darts; each extra charge adds one dart, up to 3/5 darts.
        n_ch = 3 if (overload and st.mm_charges >= 3) else 1
        darts = 3 + (n_ch - 1)
        st.mm_charges -= n_ch
        dmg = deal(st, target, [(d(darts, 4) + darts, 'force')], credit='Puff')
        log(f"    Puff: Wand of Magic Missiles at {n_ch} charge"
            f"{'s' if n_ch > 1 else ''}, {darts} darts that never miss "
            f"{target.name}: {dmg} force. [{st.mm_charges} charges left]")
        if target.hp <= 0 and target.side == 'foe':
            log(f"      {target.name} is destroyed.")
    elif target is not None and target.hp > 0 and st.puff.dist_ft(target) <= 30:
        hit, crit, _ = attack_roll(st, 8, target, attacker=st.puff)
        if hit:
            dmg = deal(st, target, [(d(2 if crit else 1, 6) + 2, 'force')],
                       credit='Puff')
            log(f"    Puff: Force Strike hits {target.name} for {dmg}.")
        else:
            log(f"    Puff: Force Strike misses {target.name}.")


def cannon_fire(st, mode, targets=None, center=None, dis=False):
    c = st.cannon
    if mode == 'ballista' and targets:
        t = targets[0]
        hit, crit, _ = attack_roll(st, 8, t, dis=dis, attacker=c)
        if hit:
            dmg = deal(st, t, [(d(4 if crit else 2, 8) + 2, 'force')],
                       credit='Cannon')
            log(f"    Cannon (Force Ballista): slams {t.name} for {dmg} force.")
            if t.hp <= 0 and t.side == 'foe':
                log(f"      {t.name} is destroyed.")
        else:
            log(f"    Cannon (Force Ballista): misses {t.name}.")
    elif mode == 'flame' and targets:
        hits = [t for t in targets if t.hp > 0][:3]
        for t in hits:
            dmg_roll = d(2, 8) + 2
            if foe_save(t, t.saves.get('dex', 0), 16):
                dmg = deal(st, t, [(dmg_roll // 2, 'fire')], credit='Cannon')
                log(f"    Cannon (Flamethrower): {t.name} ducks, {dmg} fire.")
            else:
                dmg = deal(st, t, [(dmg_roll, 'fire')], credit='Cannon')
                log(f"    Cannon (Flamethrower): scorches {t.name} for {dmg} fire.")
    elif mode == 'protector':
        t_hp = d(1, 8) + 5
        n = 0
        for h in st.pcs:
            if not h.down and h.dist_ft(c) <= 10:
                h.temp = max(h.temp, t_hp)
                n += 1
        log(f"    Cannon (Protector): {t_hp} shield-points to {n} friends.")


def companion_turn(st, targets):
    """One companion is out at a time. Branch on which."""
    g = st.ghost
    if not g.alive:
        return
    if g.kind == 'sandshrew':
        return sandshrew_turn(st, targets)
    if g.kind == 'piplup':
        return piplup_turn(st, targets)
    if g.kind in CANDIDATES:
        return candidate_turn(st, targets)
    return ghost_lash(st, targets)


def _swing(st, g, t, bonus, dice, flat, dtype, label, adv=False, rider=None,
           extra=None):
    hit, crit, _ = attack_roll(st, bonus, t, adv=adv, attacker=g)
    if not hit:
        log(f"    {g.name}: {label} misses {t.name}.")
        return False
    n, f = dice
    parts = [(d(n * (2 if crit else 1), f) + flat, dtype)]
    if extra and extra[0]:
        en, ef, et = extra
        parts.append((d(en * (2 if crit else 1), ef), et))
    if st.rage and g.kind == 'chimchar':
        parts.append((d(1, 6) + 3, 'fire'))
    dmg = deal(st, t, parts, magical=False, attacker=g, credit=g.name)
    extra = rider(st, g, t) if rider else ''
    log(f"    {g.name}: {label} hits {t.name} for {dmg}.{extra}")
    if t.hp <= 0:
        log(f"      {t.name} is destroyed.")
    return True


def _blast(st, g, live, rng, dice, dc, stat, dtype, name, on_fail=None):
    """One showy AoE. Returns True if it fired."""
    pool = [t for t in live if g.dist_ft(t) <= rng]
    if st.big_left <= 0 or len(pool) < 3:
        return False
    st.big_left -= 1
    log(f"    {g.name}: {name}")
    for t in pool[:5]:
        roll = d(*dice)
        ok = foe_save(t, t.saves.get(stat, 0), dc)
        dmg = deal(st, t, [(roll // 2 if ok else roll, dtype)], credit=g.name)
        note = ''
        if not ok and on_fail:
            note = on_fail(st, t)
        log(f"      {t.name} takes {dmg}.{note}")
        if t.hp <= 0:
            log(f"      {t.name} is destroyed.")
    return True


def _melee_routine(st, g, targets, swings, bonus, dice, flat, dtype, label,
                   adv=False, rider=None, reach=5):
    for _ in range(swings):
        live = [x for x in targets if x.hp > 0]
        if not live:
            return
        t = live[0]
        if g.dist_ft(t) > reach:
            g.approach(t, reach, g.speed)
        if g.dist_ft(t) > reach:
            log(f"    {g.name}: closes on {t.name}.")
            return
        _swing(st, g, t, bonus, dice, flat, dtype, label, adv=adv, rider=rider)


def candidate_turn(st, targets):
    g = st.ghost
    live = [t for t in targets if t.hp > 0]
    if not live:
        return
    k = g.kind

    # ============ FIRE: three ways to be the striker ============
    if k == 'chimchar':
        was = st.rage
        st.rage = 1 if g.hp <= g.hp_max * FIRE_BLAZE_AT else 0
        st.tally['prevented']['_turns'] += 1
        if st.rage:
            st.tally['prevented']['_blaze_turns'] += 1
        if st.rage and not was:
            log("    Chimchar: BLAZE catches. Everything it does carries an "
                "extra 1d6+3 now, it swings with advantage, and the boiling air "
                "makes it hard to hit.")
        # 1/DAY, the showy one: it becomes a comet and runs the whole line.
        if FIRE_BLITZ and _blast(st, g, live, 40, (FIRE_BLITZ_DICE, 6), 15, 'dex', 'fire',
                  "FLARE BLITZ. It takes a run-up and becomes a comet."):
            return
        # ACTION (Multiattack): ONE claw and ONE Fire Wheel, two claws once
        # Blaze is lit. The wheel is the routine now, not a cooldown: this is
        # the lane, and it is not here to duel Stabby.
        _melee_routine(st, g, targets, FIRE_SWINGS, 8, (1, 10), 5, 'fire',
                       'ember claw', adv=bool(st.rage))
        # BLAZE also boils the air around it: no separate Bonus Action.
        if st.rage:
            g.dodging = True
            st.tally['prevented']['Chimchar (blaze haze)'] += 1
        near = [t for t in live if t.hp > 0 and g.dist_ft(t) <= FIRE_RADIUS]
        if near:
            _n, _f = FIRE_WHEEL
            log(f"    Chimchar: FIRE WHEEL, it tucks and spins burning through "
                f"{len(near)} of them.")
            for t in near[:6]:
                roll = d(_n, _f) + (d(1, 6) + 3 if st.rage else 0)
                ok = foe_save(t, t.saves.get('dex', 0), 15)
                dmg = deal(st, t, [(roll // 2 if ok else roll, 'fire')],
                           credit='Chimchar')
                log(f"      {t.name} takes {dmg}.")
                if t.hp <= 0:
                    log(f"      {t.name} is destroyed.")
        return

    if k == 'growlithe':
        if _blast(st, g, live, 30, (6, 6), 15, 'dex', 'fire',
                  "FLAMETHROWER, a thirty-foot cone of white fire."):
            return
        t = min(live, key=lambda x: x.hp)
        pounced = False
        if g.dist_ft(t) > 5:
            g.approach(t, 5, g.speed)
            pounced = True
            log(f"    Growlithe: POUNCE, fifty feet of dog at {t.name}.")
        if g.dist_ft(t) > 5:
            return
        pack = any(h.alive and h is not g and h.dist_ft(t) <= 5 for h in st.pcs)

        def burn(st_, g_, t_):
            if not foe_save(t_, t_.saves.get('con', 0), 14):
                t_.burning = 2
                if t_ not in st_.burn_watch:
                    st_.burn_watch.append(t_)
                return " It is set BURNING."
            return ''
        _melee_routine(st, g, targets, 2, 8, (2, 10), 5, 'fire', 'fire fang',
                       adv=(pounced or pack), rider=burn)
        return

    if k == 'magmar':
        if _blast(st, g, live, 60, (8, 6), 15, 'dex', 'fire',
                  "FIRE BLAST, the air itself goes white."):
            return
        clump = [x for x in live if g.dist_ft(x) <= 60]
        if len(clump) >= 3:
            log("    Magmar: LAVA PLUME, it stamps and the floor spits.")
            for x in clump[:4]:
                roll = d(3, 6)
                ok = foe_save(x, x.saves.get('dex', 0), 14)
                dmg = deal(st, x, [(roll // 2 if ok else roll, 'fire')],
                           credit=g.name)
                log(f"      {x.name} takes {dmg} fire.")
                if x.hp <= 0:
                    log(f"      {x.name} is destroyed.")
        else:
            for _ in range(2):
                live = [x for x in targets if x.hp > 0]
                if not live:
                    break
                t = live[0]
                if g.dist_ft(t) > 60:
                    g.approach(t, 60, g.speed)
                if g.dist_ft(t) <= 60:
                    _swing(st, g, t, 7, (2, 6), 3, 'fire', 'ember volley')
        live = [x for x in targets if x.hp > 0]
        if live:
            big = max(live, key=lambda x: x.hp)
            big.smoked = 1
            st.tally['prevented']['Magmar (smoke screen)'] += 1
            log(f"    Magmar: SMOKE SCREEN over {big.name}; it swings blind.")
        return

    # ============ AIR: three ways to be the denier ============
    if k == 'pidgeot':
        def flung(st_, t_):
            t_.prone = True
            t_.slowed = 1
            st_.tally['prevented']['Pidgeot (hurricane)'] += 1
            return " It is flung down."
        if _blast(st, g, live, 40, (3, 6), 15, 'str', 'bludgeoning',
                  "HURRICANE, it climbs and drops a wall of wind.", on_fail=flung):
            return

        def push(st_, g_, t_):
            if not foe_save(t_, t_.saves.get('str', 0), 14):
                t_.slowed = 1
                st_.tally['prevented']['Pidgeot (buffet)'] += 1
                return " It is buffeted back."
            return ''
        _melee_routine(st, g, targets, 2, 7, (1, 8), 3, 'slashing',
                       'wing strike', rider=push)
        live = [x for x in targets if x.hp > 0]
        if live:
            far = max(live, key=lambda x: x.hp)
            if not foe_save(far, far.saves.get('str', 0), 14):
                far.prone = True
                far.slowed = 1
                st.tally['prevented']['Pidgeot (gust)'] += 1
                log(f"    Pidgeot: GUST slams {far.name} flat.")
            else:
                log(f"    Pidgeot: GUST, and {far.name} leans into it.")
        return

    if k == 'togekiss':
        def serene_grace():
            """BONUS ACTION. Fires on a Sing turn too: Sing is an Action."""
            if not AIR_BLESS:
                return
            cands = [h for h in (st.stabby, st.lilly, st.ursa)
                     if h.alive and g.dist_ft(h) <= 60]
            if cands:
                pick = cands[0]
                for _h in st.pcs:          # the old one ends as this one begins
                    _h.blessed_ac = 0
                st.blessing = pick
                pick.blessed_ac = 1
                st.tally['prevented']['Togekiss (serene grace)'] += 1
                log(f"    Togekiss: SERENE GRACE settles over {pick.name}: their "
                    "swing is guided, and blows slide off them.")

        if st.big_left > 0 and len([x for x in live if g.dist_ft(x) <= 30]) >= 3:
            st.big_left -= 1
            log("    Togekiss: SING. It settles on the air and begins to hum.")
            for x in [x for x in live if g.dist_ft(x) <= 30][:6]:
                if 'charmed' in x.cond_imm:
                    log(f"      {x.name} cannot hear it.")
                elif foe_save(x, x.saves.get('wis', 0), 15):
                    log(f"      {x.name} shakes it off.")
                else:
                    x.entangled = 3
                    st.tally['prevented']['Togekiss (sing)'] += 1
                    log(f"      {x.name} FALLS ASLEEP where it stands.")
            serene_grace()
            return

        def disable(st_, g_, t_):
            if foe_save(t_, t_.saves.get('wis', 0), AIR_DC):
                return ''
            st_.tally['prevented']['Togekiss (rider)'] += 1
            if AIR_RIDER == 'blind':
                t_.blinded = 2
                if t_ not in st_.blind_watch:
                    st_.blind_watch.append(t_)
                return " Its eyes are FULL OF LIGHT and it cannot see."
            t_.entangled = 2          # stun: it loses the turn outright
            t_.reaction = False
            return " It is STUNNED, and the moment is gone."
        _n, _f, _fl = AIR_DIE
        # MULTIATTACK: two gleams, both carrying the rider. DM doctrine
        # (2026-08-21): Togekiss plays DEFENSIVELY. It keeps the two BIGGEST
        # THREATS blinded rather than shooting whatever is nearest, because a
        # blinded enemy swings at Disadvantage and the WHOLE PARTY has
        # Advantage against it. So: threat order, and never waste a gleam
        # re-blinding something already blind while a live threat can see.
        reach = [t for t in live if g.dist_ft(t) <= 60] or live
        if AIR_PICK == 'big':            # biggest max HP
            key = lambda t: (getattr(t, 'blinded', 0) > 0, -t.hp_max, -t.hp)
        elif AIR_PICK == 'fresh':        # don't double-blind; else nearest
            key = lambda t: (getattr(t, 'blinded', 0) > 0, g.dist_ft(t))
        elif AIR_PICK == 'hitter':       # whoever swings hardest at us
            key = lambda t: (getattr(t, 'blinded', 0) > 0,
                             -getattr(t, 'threat', t.hp_max))
        elif AIR_PICK == 'near':         # plain nearest two
            key = lambda t: g.dist_ft(t)
        else:                            # 'asis': the caller's own priority
            key = None
        marks = live[:2] if key is None else sorted(reach, key=key)[:2]
        for _i, t in enumerate(marks):
            if g.dist_ft(t) > 60:
                g.approach(t, 60, g.speed)
            if g.dist_ft(t) > 60:
                continue
            _swing(st, g, t, 8, (_n, _f), _fl, 'radiant', 'dazzling gleam',
                   rider=(disable if _i < AIR_RIDER_N else None))
        serene_grace()
        return



class _Spot:
    """A bare coordinate that Actor.approach can walk toward."""
    def __init__(self, xy):
        self.pos = list(xy)


def sandshrew_turn(st, targets):
    """DM doctrine (2026-08-21): Sandshrew is not a brawler. Its job is to stand
    BETWEEN the enemies and the squishies and break the ground they must cross."""
    g = st.ghost
    live = [t for t in targets if t.hp > 0]
    if not live:
        return
    if SHREW_MODE == 'guard':
        # the ward: whoever is least able to take a hit
        ward = min([h for h in (st.lilly, st.ursa, st.stabby) if h.alive],
                   key=lambda h: (h.hp / h.hp_max, h.ac), default=None)
        if ward is not None:
            ex = sum(t.pos[0] for t in live) / len(live)
            ey = sum(t.pos[1] for t in live) / len(live)
            # two thirds of the way from the ward toward the enemy mass: close
            # enough to break their ground, in front of the one being guarded
            spot = _Spot((round(ward.pos[0] + 0.66 * (ex - ward.pos[0])),
                          round(ward.pos[1] + 0.66 * (ey - ward.pos[1]))))
            g.approach(spot, 0, 30)
    # Challenge whatever most endangers the ward, not simply the fattest thing.
    mark = max(live, key=lambda t: t.hp)
    st.challenged = mark
    log(f"    Sandshrew: CHALLENGE, rears up and dares {mark.name} to try it.")
    # Earthquake: the card says "each creature of Sandshrew's CHOICE", so allies
    # are never caught and there is no reason to hold it because they are near.
    cube = [t for t in live if g.dist_ft(t) <= 20]
    need = QUAKE_NEED if SHREW_MODE == 'guard' else 3
    friends_in = [] if SHREW_MODE == 'guard' else [
        h for h in st.pcs if h.alive and h is not g and g.dist_ft(h) <= 20]
    if len(cube) >= need and not friends_in:
        log("    Sandshrew: EARTHQUAKE, both forefeet down and the floor splits.")
        for t in cube[:6]:
            roll = d(QUAKE_DICE, 6)
            if foe_save(t, t.saves.get('dex', 0), 15):
                dmg = deal(st, t, [(roll // 2, 'bludgeoning')], credit='Sandshrew')
                log(f"      {t.name} rides it out: {dmg}.")
            else:
                dmg = deal(st, t, [(roll, 'bludgeoning')], credit='Sandshrew')
                log(f"      {t.name} is thrown down for {dmg}.")
            t.slowed = 1
            if t.hp <= 0:
                log(f"      {t.name} is destroyed.")
        st.quake = tuple(g.pos)
        for t in live:
            if t not in st.quake_watch:
                st.quake_watch.append(t)
        log("      The broken ground is difficult terrain until its next turn.")
        return
    for _ in range(2):
        live = [t for t in targets if t.hp > 0]
        if not live:
            return
        t = live[0]
        if g.dist_ft(t) > 5:
            g.approach(t, 5, 30)
        if g.dist_ft(t) > 5:
            log(f"    Sandshrew: digs forward at {t.name}.")
            return
        hit, crit, _ = attack_roll(st, 8, t, attacker=g)
        if hit:
            dmg = deal(st, t, [(d(2 if crit else 1, 10) + 5, 'slashing')],
                       magical=False, attacker=g, credit='Sandshrew')
            log(f"    Sandshrew: claw rakes {t.name} for {dmg}.")
            if t.hp <= 0:
                log(f"      {t.name} is destroyed.")
        else:
            log(f"    Sandshrew: claw scrapes past {t.name}.")


def piplup_turn(st, targets):
    """Heal Bubble (bonus action) then Ice Beams at range."""
    g = st.ghost
    if PIPLUP_VER == 'v3':
        n = 0
        for h in st.pcs:
            if h.alive and g.dist_ft(h) <= 30:
                h.mistguard = True
                n += 1
        log(f"    Piplup: MISTGUARD, cold silver haze settles over {n} of them; "
            "the next blow each takes lands lighter.")
    elif PIPLUP_V2 and st.sea_mist and (g.hp < g.hp_max * 0.5 or any(
            h.alive and h.hp < h.hp_max * 0.35 for h in (st.lilly, st.stabby, st.ursa))):
        st.sea_mist -= 1
        st.mist_rounds = 10
        log("    Piplup: SEA MIST, a rolling bank of cool silver fog. His friends "
            "know where each other are inside it; nothing else does.")
    hurt = [h for h in st.pcs if h.alive and h is not st.cannon
            and (h.down or h.hp < h.hp_max * BUBBLE_AT) and g.dist_ft(h) <= 30]
    if hurt and st.heal_bubble > 0:
        st.heal_bubble -= 1
        t = min(hurt, key=lambda h: h.hp / h.hp_max)
        heal = d(2, 8) + 5
        was = t.down
        _before = t.hp
        t.hp = min(t.hp_max, t.hp + heal)
        if t.hp > 0:
            t.down = False
        t.poisoned = 0
        st.tally['healed']['Piplup'] += t.hp - _before
        log(f"    Piplup: HEAL BUBBLE drifts to {t.name} and pops: {heal} back"
            + (" and back on their feet" if was else "")
            + f". [{st.heal_bubble} left]")
    if PIPLUP_VER == 'v4' and st.sea_mist and st.mist_rounds <= 0:
        near = [t for t in targets if t.hp > 0 and any(
            h.alive and h.dist_ft(t) <= 30 for h in (st.lilly, st.stabby, st.ursa))]
        allies = [h for h in st.pcs if h.alive]
        if len(near) >= 2 and len(allies) >= 3:
            xs = [h.pos[0] for h in allies]; ys = [h.pos[1] for h in allies]
            st.mist_centre = (sum(xs) // len(xs), sum(ys) // len(ys))
            st.mist_rounds = MIST_ROUNDS
            st.sea_mist -= 1
            log(f"    Piplup: SEA MIST, a rolling bank of cool silver fog "
                f"{MIST_ROUNDS} rounds deep. His friends know where each other are "
                "inside it. Nothing else does.")
            log("      (Allies inside swing with ADVANTAGE; everything swinging at "
                "them does so at DISADVANTAGE.)")
            return
    live = [t for t in targets if t.hp > 0]
    if PIPLUP_VER == 'v2':
        # BUBBLE SHIELD: prevention beats a heal when nobody is hurt yet.
        naked = [h for h in st.pcs if h.alive and h.temp <= 0
                 and g.dist_ft(h) <= 30 and h is not st.cannon]
        if naked:
            t = min(naked, key=lambda h: h.hp / h.hp_max)
            shield = d(1, 8) + 5
            t.temp = max(t.temp, shield)
            st.tally['prevented']['Piplup (Bubble Shield)'] += shield
            log(f"    Piplup: BUBBLE SHIELD closes around {t.name}: {shield} "
                "temporary hit points.")
            return
    for _ in range(BEAM_N):
        live = [t for t in targets if t.hp > 0]
        if not live:
            return
        t = live[0]
        if g.dist_ft(t) > 60:
            g.approach(t, 60, 25)
        if g.dist_ft(t) > 60:
            log(f"    Piplup: waddles into range of {t.name}.")
            return
        hit, crit, _ = attack_roll(st, BEAM_HIT, t, attacker=g)
        if hit:
            _n, _f = (2, 6) if BEAM_DIE == '2d6' else (1, int(BEAM_DIE[2:]))
            dmg = deal(st, t, [(d(_n * (2 if crit else 1), _f) + 3, 'cold')],
                       magical=False, attacker=g, credit='Piplup')
            if PIPLUP_VER == 'v1':
                t.slowed = 1          # -20 ft
            elif PIPLUP_VER == 'v4':
                t.slowed_10 = 1       # -10 ft, a nudge
            log(f"    Piplup: ICE BEAM hits {t.name} for {dmg} cold"
                + ("." if PIPLUP_V2 else "; it slows."))
            if t.hp <= 0:
                log(f"      {t.name} is destroyed.")
        else:
            log(f"    Piplup: ice beam splashes past {t.name}.")


def ghost_lash(st, targets):
    # GHOSTLY WAIL, 1/long rest: a 15-ft cone. Spend it on the biggest cluster
    # of the day, wherever that happens, not only in the Gallery.
    if st.g_wail:
        pack = [t for t in targets if t.hp > 0 and st.ghost.dist_ft(t) <= 15
                and 'frightened' not in t.cond_imm]
        if len(pack) >= 3:
            st.g_wail -= 1
            st.tally['prevented']['Ghostbloom (wail)'] += 1
            log("    Ghostbloom: GHOSTLY WAIL, a cry that cracks the air!")
            for t in pack[:4]:
                roll = d(5, 6)
                if foe_save(t, t.saves.get('wis', 0), 16):
                    dmg = deal(st, t, [(roll // 2, 'necrotic')], credit='Ghostbloom')
                    log(f"      {t.name} takes {dmg} necrotic.")
                else:
                    dmg = deal(st, t, [(roll, 'necrotic')], credit='Ghostbloom')
                    t.fright = 2
                    log(f"      {t.name} takes {dmg} necrotic and quails!")
                if t.hp <= 0:
                    log(f"      {t.name} is destroyed.")
            return
    # FEY STEP, 1/short rest: blink 20 ft, and her next attack has Advantage.
    if st.g_feystep and any(t.hp > 0 and st.ghost.dist_ft(t) > 15 for t in targets):
        st.g_feystep = False
        st.ghost.fey_adv = True
        st.tally['prevented']['Ghostbloom (fey step)'] += 1
        t = next(t for t in targets if t.hp > 0)
        st.ghost.approach(t, 15, 20)
        log("    Ghostbloom: FEY STEP, she blinks across the gap and comes up "
            "behind them.")
    g = st.ghost
    ts = [t for t in targets if t.hp > 0]
    if not ts:
        return
    for _ in range(2):
        ts = [t for t in targets if t.hp > 0]
        if not ts:
            return
        # She has FIFTEEN feet of reach. Take whatever is already inside it, and
        # only chase if nothing is: swinging at the list's first entry made her
        # walk past adjacent enemies toward a distant one.
        inreach = [x for x in ts if g.dist_ft(x) <= 15]
        t = min(inreach, key=lambda x: g.dist_ft(x)) if inreach             else min(ts, key=lambda x: g.dist_ft(x))
        if g.dist_ft(t) > 15 and GHOST_MODE == 'guard':
            # GUARD DOCTRINE: she is the generalist who covers the party. Her
            # reaction heal only reaches 30 ft, so she stays inside that of the
            # ward and uses her FIFTEEN feet of reach from there, instead of
            # chasing whatever is nearest across the board.
            ward = min([h for h in (st.lilly, st.ursa, st.stabby) if h.alive],
                       key=lambda h: (h.hp / h.hp_max, h.ac), default=None)
            if ward is not None:
                near_ward = [x for x in ts if ward.dist_ft(x) <= 40]
                if near_ward:
                    t = min(near_ward, key=lambda x: ward.dist_ft(x))
        if g.dist_ft(t) > 15:
            g.approach(t, 15, 30)
        if g.dist_ft(t) > 15:
            log(f"    Ghostbloom: drifts toward {t.name}.")
            return
        adv = getattr(g, 'fey_adv', False)
        g.fey_adv = False
        hit, crit, _ = attack_roll(st, 8, t, adv=adv, attacker=g)
        if hit:
            parts = [(d(2 if crit else 1, 8) + 6, 'slashing'), (d(1, 6), 'necrotic')]
            dmg = deal(st, t, parts, magical=False, attacker=g, credit='Ghostbloom')
            note = ''
            if 'frightened' not in t.cond_imm and not foe_save(t, t.saves.get('wis', 0), 16):
                t.fright = 2
                st.tally['prevented']['Ghostbloom (fear)'] += 1
                note = ' It recoils, frightened!'
            log(f"    Ghostbloom: spectral lash hits {t.name} for {dmg}.{note}")
            if t.hp <= 0:
                log(f"      {t.name} is destroyed.")
        else:
            log(f"    Ghostbloom: lash misses {t.name}.")


def fey_drop(st, target):
    """Where to manifest the spirit: beside its target if that is inside the
    spell's 90 ft, otherwise next to Ursa."""
    if target is not None and st.ursa.dist_ft(target) <= 90:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)):
            sp = (target.pos[0] + dx, target.pos[1] + dy)
            if 0 <= sp[0] < 30 and 0 <= sp[1] < 30:
                return sp
    return tuple(st.ursa.pos)


def summon_fey(st, pos=(9, 15)):
    """Summon Fey. 3rd: AC 15, HP 30, 2d6+6, one attack. Cast with a 4th-level
    slot (build_ursa.py:211-212): AC 16, HP 40, 2d6+7, and TWO attacks a turn."""
    if ursa_holding(st):
        return False
    lvl = 4 if (URSA_LINE == 'summon4' and st.u_slots[4] > 0) else 3
    if st.u_slots[lvl] <= 0:
        lvl = 3
        if st.u_slots[3] <= 0:
            return False
    st.u_slots[lvl] -= 1
    ac, hp = (16, 40) if lvl == 4 else (15, 30)
    ursa_take_conc(st, 'the fey spirit')
    st.fey = Actor('Fey spirit', 'f', 'pc', ac, hp, pos, 30,
                   saves=dict(dex=3, con=2, wis=2), fly=True)
    st.fey.lvl = lvl
    log(f"    Ursa: SUMMON FEY at {'4th' if lvl == 4 else '3rd'} level, a silver-antlered spirit steps "
        f"out of the light (AC {ac}, HP {hp}"
        f"{', TWO attacks a turn' if lvl == 4 else ''}). "
        f"[slots {st.u_slots[1]}/{st.u_slots[2]}/{st.u_slots[3]}/{st.u_slots[4]}]")
    return True


def fey_turn(st, targets):
    if st.fey is None or st.fey.hp <= 0:
        return
    f = st.fey
    lvl = getattr(f, 'lvl', 3)
    bonus_dmg = 7 if lvl == 4 else 6
    for _ in range(2 if lvl == 4 else 1):
        ts = [t for t in targets if t.hp > 0]
        if not ts:
            return
        t = ts[0]
        if f.dist_ft(t) > 5:
            f.approach(t, 5, 30)
        if f.dist_ft(t) > 5:
            log(f"    Fey spirit: closes on {t.name}.")
            return
        hit, crit, _ = attack_roll(st, 8, t, attacker=f)
        if hit:
            dmg = deal(st, t, [(d(4 if crit else 2, 6) + bonus_dmg, 'force')],
                       credit='Fey spirit')
            log(f"    Fey spirit: fey blade hits {t.name} for {dmg} force.")
            if t.hp <= 0:
                log(f"      {t.name} is destroyed.")
        else:
            log(f"    Fey spirit: fey blade misses {t.name}.")


def ursa_holding(st):
    """What Ursa is concentrating on right now, or None. Summon Fey is tracked
    as a creature rather than in st.conc, so it has to be checked separately."""
    if st.fey is not None and st.fey.hp > 0:
        return 'the fey spirit'
    return st.conc


def ursa_take_conc(st, what):
    """Take concentration on `what`, dropping whatever he was already holding.
    A creature can concentrate on only one spell at a time."""
    had = ursa_holding(st)
    if had and had != what:
        log(f"      (Ursa lets go of {had} to hold {what}.)")
        if st.fey is not None:
            st.fey.hp = 0
            st.fey = None
        st.pack = None
    st.conc = what if what != 'the fey spirit' else None


def ursa_conc_check(st, dmg):
    """One concentration slot, shared by the summon, Moonbeam and Entangle."""
    holding = (st.fey is not None and st.fey.hp > 0) or st.conc
    if not holding or dmg <= 0:
        return
    dc = max(10, dmg // 2)
    # Flash of Genius and a dreamed omen or Weal can all rescue this: it is an
    # ordinary Constitution saving throw. hero_save owns those hooks.
    if st.hero_save(st.ursa, 'con', dc, tag='concentration'):
        return
    if st.conc:
        log(f"      * Ursa loses concentration (DC {dc}): {st.conc} winks out!")
        if st.conc == 'the Conjure Animals':
            st.pack = None
        st.conc = None
    elif st.fey is not None:
        log(f"      * Ursa loses concentration (DC {dc}): the fey spirit fades!")
        st.conc_lost += 1
        st.fey.hp = 0
        st.fey = None


def conjure_animals(st, pos, targets=None):
    """SRD 5.2.1: Action, 3rd level, Concentration 10 min. A Large pack of
    spectral animals. It is an EFFECT, not a creature: nothing can attack it,
    and only a lost concentration check ends it."""
    if ursa_holding(st):
        return False
    lvl = 4 if (URSA_LINE == 'pack4' and st.u_slots[4] > 0) else 3
    if st.u_slots[lvl] <= 0:
        lvl = 3
        if st.u_slots[3] <= 0:
            return False
    st.u_slots[lvl] -= 1
    st.pack = list(pos)
    st.pack_lvl = lvl
    ursa_take_conc(st, 'the Conjure Animals')
    log(f"    Ursa: CONJURE ANIMALS at {lvl}th level, a Large pack of spectral "
        f"wolves boils up out of nothing ({lvl + 0}d10 on a failed DC 16 Dex). "
        f"[slots {st.u_slots[1]}/{st.u_slots[2]}/{st.u_slots[3]}/{st.u_slots[4]}]")
    # He casts it up to 60 ft away and then MOVES on the same turn, so the pack
    # moves its 30 ft immediately and can bite on the turn it appears.
    if targets:
        pack_tick(st, targets, phase='move')
    return True


def pack_tick(st, targets, phase='both'):
    """Free with Ursa's move: shove the pack up to 30 ft onto the biggest
    cluster, then every creature within 10 ft saves. Once per turn each."""
    if st.pack is None or st.conc != 'the Conjure Animals':
        return
    live = [t for t in targets if t.hp > 0]
    if not live:
        return

    def bite(pool, why):
        dice = 3 if st.pack_lvl == 3 else 4
        pool = [t for t in pool if t.hp > 0]
        if not pool:
            return
        log(f"    Ursa: the pack {why} {len(pool)} of them.")
        for t in pool[:6]:
            roll = d(dice, 10)
            if foe_save(t, t.saves.get('dex', 0), 16):
                log(f"      {t.name} throws itself clear.")
                continue
            dmg = deal(st, t, [(roll, 'slashing')], magical=True, credit='Ursa')
            log(f"      {t.name} takes {dmg}.")
            if t.hp <= 0:
                log(f"      {t.name} is destroyed.")

    # TRIGGER 1 (RAW): creatures that ENDED THEIR TURN within 10 ft of the pack.
    # Resolved here for timing convenience; it is a different turn from Ursa's,
    # so the once-per-turn cap does not merge it with the move trigger below.
    if PACK_TRIG == 'both' and phase == 'both':
        bite([t for t in live
              if max(abs(t.pos[0] - st.pack[0]),
                     abs(t.pos[1] - st.pack[1])) <= 2], 'closes over')
        live = [t for t in live if t.hp > 0]
        if not live:
            return
    # DM doctrine (2026-08-21): park it on as many bodies as possible AND
    # INTERPOSED, between them and the party, so anything walking at the group
    # has to come through the 10-ft ring and eat the save on its own turn too.
    friends = [h for h in (st.lilly, st.stabby, st.ursa) if h.alive]
    if friends:
        cx = sum(h.pos[0] for h in friends) / len(friends)
        cy = sum(h.pos[1] for h in friends) / len(friends)
    else:
        cx, cy = st.ursa.pos

    def cheb(a, b):
        return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

    best, best_score = None, -1
    for dx in range(-6, 7):                    # every square within its 30 ft
        for dy in range(-6, 7):
            cand = (st.pack[0] + dx, st.pack[1] + dy)
            if not (0 <= cand[0] < 30 and 0 <= cand[1] < 30):
                continue
            if cheb(cand, st.pack) > 6:
                continue
            touched = [x for x in live if cheb(x.pos, cand) <= 2]
            if not touched:
                continue
            # interposed = the pack sits on the party's side of that enemy, so
            # closing on the group means entering the ring
            d_pack = max(abs(cand[0] - cx), abs(cand[1] - cy))
            blocking = sum(1 for x in touched
                           if max(abs(x.pos[0] - cx),
                                  abs(x.pos[1] - cy)) > d_pack)
            score = len(touched) * 10 + blocking * 3
            if score > best_score:
                best, best_score = cand, score
    if best is not None:
        st.pack = list(best)
    caught = [t for t in live
              if max(abs(t.pos[0] - st.pack[0]), abs(t.pos[1] - st.pack[1])) <= 2]
    bite(caught, 'surges through')


def ursa_damage_line(st, targets, bonus_used):
    """The simple line: keep the summon up, then Guiding Bolt while the free
    Star Map casts last, then Starry Wisp forever."""
    live = [t for t in targets if t.hp > 0]
    if URSA_LINE in ('pack', 'pack4'):
        if st.pack is None and st.u_slots[3] > 0:
            conjure_animals(st, tuple(live[0].pos) if live else tuple(st.ursa.pos),
                            targets=live)
        else:
            if live:
                if st.u_gbolt > 0 or st.u_staff > 0:
                    guiding_bolt(st, live[0])
                else:
                    starry_wisp(st, live[0])
        # re-target: his Action may have just killed live[0], and the arrow
        # should not be loosed at a corpse
        still = [t for t in targets if t.hp > 0]
        if not bonus_used and st.u_starry and still:
            star_arrow(st, still[0])
            bonus_used = True
        return bonus_used
    if (st.fey is None or st.fey.hp <= 0) and st.u_slots[3] > 0:
        summon_fey(st, pos=fey_drop(st, live[0] if live else None))
    elif live:
        if st.u_gbolt > 0 or st.u_staff > 0:
            guiding_bolt(st, live[0])
        else:
            starry_wisp(st, live[0])
    if not bonus_used and st.u_starry and live:
        star_arrow(st, live[0])
        bonus_used = True
    return bonus_used


def ursa_close(st, target, want_ft=55):
    """Ursa spends movement to get his 60-ft powers in range."""
    if target is not None and st.ursa.dist_ft(target) > want_ft:
        old, moved = st.ursa.approach(target, want_ft, 30)
        if moved:
            log(f"    Ursa: steps up {old}->{tuple(st.ursa.pos)}.")
    return target is not None and st.ursa.dist_ft(target) <= 60


def star_arrow(st, target, dis=False):
    if target is None or target.hp <= 0:
        st.tally['prevented']['_arrow_notarget'] += 1
        return
    if not ursa_close(st, target):
        st.tally['prevented']['_arrow_outofrange'] += 1
        return
    hit, crit, _ = attack_roll(st, 10, target, dis=dis, attacker=st.ursa)
    if hit:
        dmg = deal(st, target, [(d(2 if crit else 1, 8) + 5, 'radiant')],
                   credit='Ursa')
        log(f"    Ursa: star-arrow streaks into {target.name} for {dmg} radiant.")
        if target.hp <= 0:
            log(f"      {target.name} is destroyed.")
    else:
        log(f"    Ursa: star-arrow misses {target.name}.")


def guiding_bolt(st, target, dis=False):
    src = None
    if st.u_gbolt > 0:
        st.u_gbolt -= 1
        src = f"Star Map, {st.u_gbolt} free left"
    elif st.u_staff > 0:
        st.u_staff -= 1
        src = f"staff charge, {st.u_staff} left"
    else:
        return False
    adv = (st.gb_adv_target is target)
    hit, crit, _ = attack_roll(st, 10, target, adv=adv, dis=dis, attacker=st.ursa)
    if hit:
        dmg = deal(st, target, [(d(8 if crit else 4, 6), 'radiant'),
                                (d(2 if crit else 1, 8), 'radiant')],
                   credit='Ursa')
        st.gb_adv_target = target
        log(f"    Ursa: GUIDING BOLT ({src}) blazes into {target.name} for {dmg} "
            f"radiant; it glows, next attack has advantage.")
        if target.hp <= 0:
            log(f"      {target.name} is destroyed.")
    else:
        log(f"    Ursa: Guiding Bolt ({src}) misses {target.name}.")
    return True


def starry_wisp(st, target):
    if not ursa_close(st, target):
        return guiding_bolt(st, target)     # 120-ft fallback when out of range
    hit, crit, _ = attack_roll(st, 10, target, attacker=st.ursa)
    if hit:
        dmg = deal(st, target, [(d(4 if crit else 2, 8) + 5, 'radiant'),
                                (d(2 if crit else 1, 8), 'radiant')],
                   credit='Ursa')
        log(f"    Ursa: Starry Wisp burns {target.name} for {dmg} radiant.")
        if target.hp <= 0:
            log(f"      {target.name} is destroyed.")
    else:
        log(f"    Ursa: Starry Wisp misses {target.name}.")


def true_strike(st, target, dis=False, radiant=False, adv=False):
    if st.gb_adv_target is target:
        adv = True
        st.gb_adv_target = None
    # Boomstick is a pistol: 30/90, disadvantage past its short range.
    long_shot = st.lilly.dist_ft(target) > 30
    if long_shot:
        dis = True
    hit, crit, _ = attack_roll(st, 10, target, adv=adv, dis=dis, attacker=st.lilly)
    if hit:
        m = 2 if crit else 1
        if radiant:
            parts = [(d(m, 10) + 7, 'radiant'), (d(m, 6), 'radiant'), (d(m, 8), 'radiant')]
        else:
            parts = [(d(m, 10) + 7, 'thunder'), (d(m, 6), 'radiant'), (d(m, 8), 'thunder')]
        dmg = deal(st, target, parts, credit='Lilly')
        note = ''
        if not radiant and target.ch == 'C' and not target.stunned and target.hp > 0:
            target.stunned = True
            note = ' The thunder makes it RING: stunned, everything hits double!'
        log(f"    Lilly: True Strike (Boomstick) {'CRIT ' if crit else ''}hits "
            f"{target.name} for {dmg}{' radiant' if radiant else ''}"
            f"{' (long shot)' if long_shot else ''}.{note}")
        if target.hp <= 0:
            log(f"      {target.name} is destroyed.")
    else:
        log(f"    Lilly: Boomstick misses {target.name}"
            f"{' (long shot, disadvantage)' if long_shot else ''}.")


def shatter(st, targets, label='Shatter'):
    if st.l_slot2 <= 0:
        return False
    st.l_slot2 -= 1
    log(f"    Lilly: SHATTER detonates ({len(targets)} caught). "
        f"[{st.l_slot2} 2nd slots left]")
    base = d(3, 8)
    rider = d(1, 8)
    first = True
    for t in targets:
        if t.hp <= 0:
            continue
        roll = base + (rider if first else 0)
        first = False
        if foe_save(t, t.saves.get('con', 0), 16):
            dmg = deal(st, t, [(roll // 2, 'thunder')], credit='Lilly')
            log(f"      {t.name} braces: {dmg} thunder.")
        else:
            dmg = deal(st, t, [(roll, 'thunder')], credit='Lilly')
            log(f"      {t.name} takes {dmg} thunder.")
        if t.ch == 'C' and t.hp > 0 and not t.stunned:
            t.stunned = True
            log(f"      {t.name} RINGS itself apart: stunned!")
        if t.hp <= 0:
            log(f"      {t.name} is destroyed.")
    return True


# --------------------------------------------------------------------------
# FIGHT 1: Mosslight Landing. 8 Rotblooms + 8 Mossmites.
# --------------------------------------------------------------------------
def fight1(st):
    log("=" * 72)
    log("FIGHT 1: MOSSLIGHT LANDING (8 Rotblooms, 8 Mossmites)")
    log("=" * 72)
    st.lilly.pos = [5, 15]
    st.stabby.pos = [6, 14]
    st.ursa.pos = [5, 16]
    st.ghost.pos = [6, 16]
    st.puff.pos = [4, 14]
    st.cannon.pos = [4, 15]
    rot_spots = [(23, 12), (24, 14), (25, 16), (23, 17), (24, 18), (25, 13),
                 (26, 15), (26, 12)]
    # They come out of the mounds the party is standing among: a ring at 5-15 ft.
    mite_spots = [(3, 13), (8, 13), (3, 17), (8, 17), (2, 15), (9, 15),
                  (5, 12), (6, 18)]
    if BODIES:
        mite_spots += [(4, 11), (7, 19)]
    rots = []
    for i, p in enumerate(rot_spots):
        r = Actor(f'Rotbloom-{i+1}', 'R', 'foe', 12, ehp(33), p, 25,
                  saves=dict(str=0, dex=1, con=2, wis=-1),
                  resist={'poison'}, cond_imm={'frightened'})
        r.cleanse_types = set()   # 80e0efd: Cleansing Edge alone stops Re-Bloom
        rots.append(r)
    mites = []
    for i, p in enumerate(mite_spots):
        m = Actor(f'Mossmite-{i+1}', 'm', 'foe', 13, ehp(7), p, 40,
                  saves=dict(dex=3, con=1, wis=0))
        m.hidden = True
        mites.append(m)
    foes = rots + mites
    close_up(foes, [st.lilly, st.stabby, st.ursa])

    plant_growth = [False]     # Ursa's 3rd-level slot, no concentration

    def mv(base):
        """Plant Growth: 4 ft of movement per 1 ft travelled, and he leaves
        clear lanes for his friends, so only the enemies wade."""
        return max(5, base // 4) if plant_growth[0] else base

    terrain = {}
    for x in range(21, 28):
        for y in range(10, 20):
            terrain[(x, y)] = ','          # the grey, wrong moss
    log("Starting map (5 ft squares; , = grey corrupted moss; L Lilly, S Stabby,")
    log("U Ursa, G Ghostbloom, p Puff, c cannon, R Rotbloom, m Mossmite [hidden]):")
    log(render_map([a for a in st.pcs + [st.cannon] + rots], terrain))
    log("(The eight Mossmites are burrowed in the warm mounds the party is standing")
    log(" among, and boil out AROUND them the moment the first Rotbloom is struck.)")

    # Stabby: Uncanny Metabolism + ignite at initiative
    heal = 7 + d(1, 8)
    st.stabby.hp = min(st.stabby.hp_max, st.stabby.hp + heal)
    st.s_focus = 7
    st.s_metab = False
    st.spend_focus()
    st.s_ignited = True
    log("  Stabby rolls initiative: UNCANNY METABOLISM (Focus to 7, heals to full)")
    log("  and IGNITES THE BREATH (1 Focus): katana +2 force, speed 65, adv on Dex saves. [Focus 6]")
    cast_ward(st, 'while they are still counting the grey caps')

    order = initiative(st, [('Mossmites', mites, 3), ('Rotblooms', rots, 1)])
    mites_out = False
    rnd = 0
    while any(f.hp > 0 for f in foes) and any(h.alive for h in st.heroes) and rnd < 12:
        rnd += 1
        start_round(st, rnd)
        for _, name, actors in order:
            if name == 'Stabby' and st.stabby.alive:
                st.s_speed_left = 65
                st.stabby.dodging = False
                kill_list = sorted([r for r in rots if r.hp > 0],
                                   key=lambda r: st.stabby.dist_ft(r))
                if st.stabby.hp < 25:
                    stabby_defensive(st, kill_list + [m for m in mites
                                                      if m.hp > 0 and not m.hidden])
                    continue
                if rnd == 1:
                    old, _ = st.stabby.approach(rots[0], 5, 65)
                    if st.stabby.dist_ft(rots[0]) > 5:
                        st.stabby.approach(rots[0], 5, 65)
                        log(f"    Stabby: Step of the Wind, {old}->{tuple(st.stabby.pos)}, "
                            f"a 130-ft sprint across the hollow to the grey moss.")
                        mites_out = True
                        for m in mites:
                            m.hidden = False
                        log("      The moss BOILS: Mossmites pour out of the mounds in a wave!")
                        continue
                stabby_attack_routine(st, kill_list or sorted(
                    [m for m in mites if m.hp > 0], key=lambda r: st.stabby.dist_ft(r)),
                    rnd, fury_ok=False)
                if not mites_out and any(r.damaged_since for r in rots):
                    mites_out = True
                    for m in mites:
                        m.hidden = False
                    log("      The moss BOILS: Mossmites pour out of the mounds in a wave!")
            elif name == 'Lilly' and st.lilly.alive:
                near_mites = sorted([m for m in mites if m.hp > 0 and not m.hidden],
                                    key=lambda m: st.lilly.dist_ft(m))
                clump = [m for m in near_mites
                         if near_mites and cheb(m.pos, near_mites[0].pos) <= 4]
                # no Shatter centered on a friend: the sphere is 10 ft around
                if any(h.alive and any(cheb(h.pos, m.pos) <= 2 for m in clump)
                       for h in st.pcs):
                    clump = []
                live_r = sorted([r for r in rots if r.hp > 0],
                                key=lambda r: st.lilly.dist_ft(r))
                if rnd >= 2 and len(clump) >= 3 and st.l_slot2 > 0:
                    shatter(st, clump[:4])
                elif live_r and st.lilly.dist_ft(live_r[0]) <= 90:
                    true_strike(st, live_r[0])
                elif live_r:
                    hit, crit, _ = attack_roll(st, 8, live_r[0], attacker=st.lilly)
                    if hit:
                        dmg = deal(st, live_r[0], [(d(4 if crit else 2, 10), 'fire'),
                                                   (d(1, 8), 'thunder')])
                        log(f"    Lilly: Fire Bolt scorches {live_r[0].name} for {dmg}.")
                    else:
                        log(f"    Lilly: Fire Bolt misses {live_r[0].name}.")
                elif near_mites:
                    true_strike(st, near_mites[0])
                # cannon bonus action
                tgt_pool = [f for f in foes if f.hp > 0 and not getattr(f, 'hidden', False)]
                if tgt_pool:
                    in_cone = [f for f in tgt_pool if st.cannon.dist_ft(f) <= 15]
                    if len(in_cone) >= 2:
                        cannon_fire(st, 'flame', in_cone)
                    else:
                        cannon_fire(st, 'ballista',
                                    sorted(tgt_pool, key=lambda f: st.cannon.dist_ft(f)))
                if not puff_pipes(st, [f for f in foes
                                       if not getattr(f, 'hidden', False)]):
                    puff_turn(st, next((m for m in mites if m.hp > 0 and not m.hidden
                                        and st.puff.dist_ft(m) <= 30), None),
                              use_mm=False)
            elif name == 'Ursa' and st.ursa.alive:
                _pk = [r for r in rots if r.hp > 0] + [x for x in mites if x.hp > 0 and not x.hidden]
                pack_tick(st, _pk)
                bonus_used = ursa_triage(st)
                live_r = sorted([r for r in rots if r.hp > 0],
                                key=lambda r: st.ursa.dist_ft(r))
                live_m = [m for m in mites if m.hp > 0 and not m.hidden]
                if rnd == 1 and URSA_LINE != 'control':
                    if st.fey is None or st.fey.hp <= 0:
                        (conjure_animals(st, tuple(st.ursa.pos), targets=_pk)
                         if URSA_LINE in ('pack', 'pack4') else summon_fey(st))
                    if not bonus_used and ursa_starry(st, targets=_pk):
                        bonus_used = True
                elif URSA_LINE != 'control':
                    tgt = live_r[0] if live_r else (live_m[0] if live_m else None)
                    if tgt is not None:
                        if st.u_gbolt > 0:
                            guiding_bolt(st, tgt)
                        else:
                            starry_wisp(st, tgt)
                    if not bonus_used and st.u_starry:
                        star_arrow(st, live_r[0] if live_r else
                                   (live_m[0] if live_m else None))
                elif rnd == 1 and st.u_slots[3] > 0:
                    # Underroot is made of growing things: Plant Growth always
                    # has something to work on, needs no concentration, and he
                    # can leave his own friends clear lanes.
                    st.u_slots[3] -= 1
                    plant_growth[0] = True
                    log("    Ursa: PLANT GROWTH. He puts one hand flat on the "
                        "warm ground and the whole landing ANSWERS: moss ropes "
                        "up into waist-high thickets for a hundred feet, with "
                        "clean lanes left open where his friends are standing. "
                        f"[3rd slots left {st.u_slots[3]}]")
                    log("      Everything that wants to reach them now wades at "
                        "a quarter speed. No save, no concentration.")
                    if not bonus_used and ursa_starry(st, targets=_pk):
                        bonus_used = True
                elif rnd == 2 and st.u_slots[4] > 0 and len(
                        [r for r in live_r
                         if sum(1 for o in live_r if cheb(o.pos, r.pos) <= 4) >= 4
                         and all(not h.alive or cheb(h.pos, r.pos) > 5
                                 for h in st.pcs)]) >= 4:
                    # they are strung out in the open and WADING. Hail them.
                    clump = [r for r in live_r
                             if sum(1 for o in live_r if cheb(o.pos, r.pos) <= 4) >= 4
                             and all(not h.alive or cheb(h.pos, r.pos) > 5
                                     for h in st.pcs)]
                    st.u_slots[4] -= 1
                    log("    Ursa: ICE STORM into the thicket, while they are "
                        f"still stuck in the open. [4th slots left {st.u_slots[4]}]")
                    for r in clump[:6]:
                        bl, cd = d(2, 10), d(4, 6)
                        if foe_save(r, r.saves.get('dex', 0), 16):
                            dmg = deal(st, r, [(bl // 2, 'bludgeoning'),
                                               (cd // 2, 'cold')], credit='Ursa')
                            log(f"      {r.name} weathers it: {dmg}.")
                        else:
                            dmg = deal(st, r, [(bl, 'bludgeoning'), (cd, 'cold')],
                                       credit='Ursa')
                            log(f"      {r.name} is hammered flat for {dmg}!")
                        if r.hp <= 0:
                            log(f"      {r.name} is destroyed.")
                    log("      Ice over thorns: the survivors slog worse than before.")
                    if not bonus_used and st.u_starry:
                        star_arrow(st, live_r[0] if live_r else
                                   (live_m[0] if live_m else None))
                elif st.fey is None and st.u_slots[3] > 0 and rnd <= 3:
                    (conjure_animals(st, tuple(st.ursa.pos), targets=_pk)
                     if URSA_LINE in ('pack', 'pack4') else summon_fey(st))
                    if not bonus_used and st.u_starry:
                        star_arrow(st, live_r[0] if live_r else
                                   (live_m[0] if live_m else None))
                else:
                    tgt = live_r[0] if live_r else (live_m[0] if live_m else None)
                    if tgt is not None:
                        starry_wisp(st, tgt)
                    if not bonus_used and st.u_starry:
                        t2 = next((r for r in rots if r.hp > 0), None) or \
                             next((m for m in mites if m.hp > 0 and not m.hidden), None)
                        star_arrow(st, t2)
                fey_targets = sorted([f for f in foes if f.hp > 0
                                      and not getattr(f, 'hidden', False)],
                                     key=lambda f: (0 if f.ch == 'R' else 1,
                                                    st.fey.dist_ft(f) if st.fey else 0))
                fey_turn(st, fey_targets)
            elif name == st.ghost.name and st.ghost.alive:
                if GHOST_SUPPORT:
                    log(f"    {st.ghost.name}: hangs back on triage.")
                else:
                    gts = sorted([f for f in foes if f.hp > 0
                                  and not getattr(f, 'hidden', False)],
                                 key=lambda f: st.ghost.dist_ft(f))
                    companion_turn(st, gts)
            elif name == 'Mossmites':
                if not mites_out:
                    continue
                for m in mites:
                    if m.hp <= 0:
                        continue
                    if m.stunned:
                        m.stunned = False
                        continue
                    packs = [o for o in mites if o is not m and o.hp > 0
                             and cheb(o.pos, m.pos) <= 1]
                    tgt = min([h for h in st.pcs + ([st.fey] if st.fey else [])
                               if h is not None and h.alive],
                              key=lambda h: m.dist_ft(h), default=None)
                    if tgt is None:
                        break
                    m.approach(tgt, 5,
                               mv(m.speed * (2 if m.dist_ft(tgt) > m.speed + 5 else 1)))
                    if m.dist_ft(tgt) <= 5:
                        hit, crit, _ = attack_roll(st, 5, tgt, adv=bool(packs), attacker=m)
                        if hit:
                            dmg = deal(st, tgt, [(d(2 if crit else 1, 4) + 3, 'piercing')],
                                       magical=False, attacker=m)
                            log(f"    {m.name}: nips {tgt.name} for {dmg}."
                                + (' (pack advantage)' if packs else ''))
                            if tgt is st.ursa:
                                ursa_conc_check(st, dmg)
                        else:
                            log(f"    {m.name}: darts at {tgt.name} and misses.")
                    else:
                        log(f"    {m.name}: skitters toward {tgt.name}.")
            elif name == 'Rotblooms':
                for r in rots:
                    if r.hp <= 0:
                        continue
                    # Re-Bloom
                    if r.damaged_since and not r.cleansed and r.hp < r.hp_max:
                        r.hp = min(r.hp_max, r.hp + 5)
                        log(f"    {r.name}: its cap swells, RE-BLOOMS 5 (now {r.hp}).")
                    r.damaged_since = False
                    r.cleansed = False
                    tgt = min([h for h in st.pcs + ([st.fey] if st.fey else [])
                               if h is not None and h.alive],
                              key=lambda h: r.dist_ft(h), default=None)
                    if tgt is None:
                        break
                    r.approach(tgt, 5, mv(25))
                    close = [h for h in st.pcs + ([st.fey] if st.fey else [])
                             if h is not None and h.alive and r.dist_ft(h) <= 10]
                    if len(close) >= 2 and rng.randint(1, 6) >= 4:
                        log(f"    {r.name}: SPORE PUFF over "
                            + ' and '.join(h.name for h in close[:3]) + "!")
                        for h in close[:3]:
                            roll = d(2, 6)
                            if h.side == 'pc' and h in st.pcs:
                                ok = st.hero_save(h, 'con', 12)
                            else:
                                ok = foe_save(h, 2, 12)
                            if ok:
                                dmg = deal(st, h, [(roll // 2, 'poison')], attacker=r)
                                log(f"      {h.name} holds their breath: {dmg} poison.")
                            else:
                                dmg = deal(st, h, [(roll, 'poison')], attacker=r)
                                h.poisoned = 1
                                log(f"      {h.name} takes {dmg} poison and is poisoned!")
                                if h is st.ursa:
                                    ursa_conc_check(st, dmg)
                    elif r.dist_ft(tgt) <= 5:
                        hit, crit, _ = attack_roll(st, 3, tgt, attacker=r)
                        if hit:
                            dmg = deal(st, tgt, [(d(4 if crit else 2, 4) + 1, 'bludgeoning')],
                                       magical=False, attacker=r)
                            log(f"    {r.name}: cap-slams {tgt.name} for {dmg}.")
                            if tgt is st.ursa:
                                ursa_conc_check(st, dmg)
                        else:
                            log(f"    {r.name}: cap-slams at {tgt.name}, misses.")
                    else:
                        log(f"    {r.name}: sways closer, still smiling.")
        for h in st.pcs:
            h.poisoned = max(0, h.poisoned - 1)
    log(f"  FIGHT 1 ENDS after round {rnd}.")
    party_state(st, "after Fight 1")
    return rnd


def party_state(st, when):
    log(f"  Party {when}: " + '; '.join(
        f"{h.name} {h.hp}/{h.hp_max}" + (f" (+{h.temp} temp)" if h.temp else '')
        for h in [st.lilly, st.stabby, st.ursa, st.ghost, st.puff]))
    log(f"  Resources: Focus {st.s_focus} | Lilly slots {st.l_slot1}/{st.l_slot2}, "
        f"Ward {st.l_ward}, Genius {st.l_fog}, MM {st.mm_charges} | "
        f"Ursa slots {st.u_slots[1]}/{st.u_slots[2]}/{st.u_slots[3]}/{st.u_slots[4]}, "
        f"Wild {st.u_wild}, free GB {st.u_gbolt}, omens {st.u_omens}, cosmic {st.u_cosmic} | "
        f"Guardian's Light {st.g_light}")


# --------------------------------------------------------------------------
# FIGHT 2: Chime Reef. 4 Chimestones + 4 Shardwings.
# --------------------------------------------------------------------------
def fight2(st):
    log("=" * 72)
    log("FIGHT 2: CHIME REEF (4 Chimestones, 4 Shardwings)")
    log("=" * 72)
    st.lilly.pos = [14, 26]
    st.stabby.pos = [15, 25]
    st.ursa.pos = [16, 26]
    st.ghost.pos = [15, 27]
    st.puff.pos = [13, 26]
    st.cannon.pos = [13, 27]
    if st.fey:
        st.fey.pos = [16, 24]
    chime_spots = [(12, 20), (15, 19), (18, 21), (21, 20)]
    wing_spots = [(9, 14), (15, 11), (21, 13), (12, 10)]
    chimes = []
    for i, p in enumerate(chime_spots):
        chimes.append(Actor(f'Chimestone-{i+1}', 'C', 'foe', 16, ehp(78), p, 25,
                            saves=dict(str=4, dex=-1, con=3, wis=1),
                            resist={'piercing', 'slashing'}, vuln={'thunder'},
                            immune={'poison'},
                            cond_imm={'charmed', 'frightened', 'poisoned'}))

    def make_wing(i, p):
        w = Actor(f'Shardwing-{i+1}', 'w', 'foe', 14, ehp(33), p, 50,
                  saves=dict(str=-1, dex=4, con=1, wis=1),
                  vuln={'thunder'}, immune={'poison'},
                  cond_imm={'poisoned', 'prone'}, fly=True)
        w.aloft = True
        return w
    wings = [make_wing(i, p) for i, p in enumerate(wing_spots)]
    foes = chimes + wings
    close_up(foes, [st.lilly, st.stabby, st.ursa])
    terrain = {(11, 18): '#', (16, 16): '#', (20, 19): '#', (13, 13): '#',
               (18, 12): '#', (8, 17): '#', (23, 16): '#'}
    log("Starting map (# = great crystal spires; C Chimestone, w Shardwing aloft;")
    log("black pool shallows through the middle):")
    log(render_map(st.pcs + [st.cannon] + foes + ([st.fey] if st.fey else []), terrain))

    st.spend_focus()
    st.s_ignited = True
    log("  Stabby ignites again at initiative (1 Focus). [Focus "
        f"{st.s_focus}]")
    cast_ward(st, 'at the edge of the black water')
    order = initiative(st, [('Shardwings', wings, 4), ('Chimestones', chimes, -1)])
    rnd = 0
    while any(f.hp > 0 for f in foes) and any(h.alive for h in st.heroes) and rnd < 12:
        rnd += 1
        start_round(st, rnd)
        if BODIES and rnd == 3:
            extra = [make_wing(len(wings), (13, 12)),
                     make_wing(len(wings) + 1, (18, 11))]
            wings.extend(extra)
            foes.extend(extra)
            log("    Two more Shardwings drop out of the high spires!")
        for _, name, actors in order:
            if name == 'Stabby' and st.stabby.alive:
                st.s_speed_left = 65
                st.stabby.dodging = False
                stunned_first = sorted([c for c in chimes if c.hp > 0],
                                       key=lambda c: (not c.stunned,
                                                      st.stabby.dist_ft(c)))
                pool = stunned_first + sorted(
                    [w for w in wings if w.hp > 0 and not w.aloft],
                    key=lambda w: st.stabby.dist_ft(w))
                if st.stabby.hp < 25:
                    stabby_defensive(st, pool)
                elif pool:
                    stabby_attack_routine(st, pool, rnd, fury_ok=True,
                                          chime_ring=NICHIRIN_RING)
            elif name == 'Lilly' and st.lilly.alive:
                live_c = sorted([c for c in chimes if c.hp > 0],
                                key=lambda c: (c.stunned, st.lilly.dist_ft(c)))
                live_w = [w for w in wings if w.hp > 0]
                clump = []
                for f in foes:
                    if f.hp <= 0:
                        continue
                    near = [g for g in foes if g.hp > 0 and cheb(g.pos, f.pos) <= 2]
                    if any(h.alive and any(cheb(h.pos, g.pos) <= 2 for g in near)
                           for h in st.pcs + ([st.fey] if st.fey else [])):
                        continue          # would catch a friend in the sphere
                    if len(near) > len(clump):
                        clump = near
                if rnd >= 2 and len(clump) >= 2 and st.l_slot2 > 0:
                    shatter(st, clump)
                elif live_c:
                    tgt = next((c for c in live_c if not c.stunned), live_c[0])
                    true_strike(st, tgt)
                elif live_w:
                    true_strike(st, live_w[0])
                hurt_near = [h for h in st.pcs if h.alive
                             and h.hp < h.hp_max * 0.60
                             and h.dist_ft(st.cannon) <= 10]
                pool = sorted([f for f in foes if f.hp > 0],
                              key=lambda f: (not f.stunned, st.cannon.dist_ft(f)))
                if hurt_near:
                    cannon_fire(st, 'protector')
                elif pool:
                    cannon_fire(st, 'ballista', pool)
                mm_t = next((f for f in foes if f.hp > 0 and f.stunned), None)
                if mm_t is not None or not puff_pipes(st, foes):
                    puff_turn(st, mm_t or next((f for f in foes if f.hp > 0), None),
                              use_mm=(mm_t is not None))
            elif name == 'Ursa' and st.ursa.alive:
                _pk = [f for f in foes if f.hp > 0]
                pack_tick(st, _pk)
                bonus_used = ursa_triage(st)
                if rnd == 1 and not bonus_used and ursa_starry(st, again=True, targets=_pk):
                    bonus_used = True
                if URSA_LINE != 'control':
                    ursa_damage_line(st, sorted(
                        [f for f in foes if f.hp > 0],
                        key=lambda f: (not f.stunned, st.ursa.dist_ft(f))),
                        bonus_used)
                    fey_turn(st, sorted([f for f in foes if f.hp > 0],
                                        key=lambda f: (not f.stunned, f.aloft)))
                    continue
                adj = [c for c in chimes if c.hp > 0 and st.ursa.dist_ft(c) <= 10]
                live = sorted([f for f in foes if f.hp > 0],
                              key=lambda f: (not f.stunned, st.ursa.dist_ft(f)))
                # Entangle: worth a 1st slot only when he is not already holding
                # something and the wall is still bunched at a distance.
                ent_pack = []
                for c in [x for x in chimes if x.hp > 0]:
                    near = [o for o in chimes if o.hp > 0 and cheb(o.pos, c.pos) <= 3]
                    if len(near) > len(ent_pack):
                        ent_pack = near
                if (len(ent_pack) >= 3 and st.u_slots[1] > 0 and st.conc is None
                        and (st.fey is None or st.fey.hp <= 0) and not adj):
                    st.u_slots[1] -= 1
                    ursa_take_conc(st, 'the Entangle')
                    log(f"    Ursa: ENTANGLE, weed-ropes burst out of the shallows "
                        f"under the wall. [{st.u_slots[1]} 1st slots left]")
                    for c in ent_pack:
                        if d20() + c.saves.get('str', 0) >= 16:
                            log(f"      {c.name} tears straight through it.")
                        else:
                            c.entangled = 2
                            log(f"      {c.name} is RESTRAINED, held fast in the weed.")
                elif len(adj) >= 2 and st.u_slots[1] > 0:
                    st.u_slots[1] -= 1
                    log(f"    Ursa: THUNDERWAVE! [{st.u_slots[1]} 1st slots left]")
                    roll = d(2, 8)
                    for c in adj:
                        if foe_save(c, c.saves.get('con', 0), 16):
                            dmg = deal(st, c, [(roll // 2, 'thunder')], credit='Ursa')
                            log(f"      {c.name} holds: {dmg} thunder.")
                        else:
                            dmg = deal(st, c, [(roll, 'thunder')], credit='Ursa')
                            log(f"      {c.name} is blasted for {dmg} thunder!")
                        if c.hp > 0 and not c.stunned:
                            c.stunned = True
                            log(f"      {c.name} RINGS: stunned!")
                        if c.hp <= 0:
                            log(f"      {c.name} shatters.")
                elif live:
                    starry_wisp(st, live[0])
                if not bonus_used and st.u_starry:
                    t2 = next((f for f in foes if f.hp > 0 and f.stunned), None) \
                        or next((f for f in foes if f.hp > 0), None)
                    star_arrow(st, t2)
                fey_turn(st, sorted([f for f in foes if f.hp > 0],
                                    key=lambda f: (not f.stunned, f.aloft)))
            elif name == st.ghost.name and st.ghost.alive:
                if GHOST_SUPPORT:
                    log(f"    {st.ghost.name}: hangs back on triage.")
                else:
                    gts = sorted([f for f in foes if f.hp > 0],
                                 key=lambda f: (f.aloft, not f.stunned,
                                                st.ghost.dist_ft(f)))
                    companion_turn(st, gts)
            elif name == 'Shardwings':
                for wi, w in enumerate(wings):
                    if w.hp <= 0:
                        continue
                    if w.fright > 0:
                        w.fright -= 1
                    # DM ruling: they hunt the WEAKEST thing on the field.
                    marks = [h for h in st.pcs if h.alive
                             and (WING_PICKS_PUFF or h is not st.puff)]
                    if WING_TARGET == 'weakest' and marks:
                        tgt = min(marks, key=lambda h: (h.hp, h.ac))
                    else:
                        tgt = marks[wi % len(marks)] if marks else None
                    if tgt is None:
                        break
                    if rnd % 2 == 1 and w.dist_ft(tgt) >= 30:
                        w.aloft = False
                        w.approach(tgt, 5, 50)
                        hit, crit, _ = attack_roll(st, 6, tgt, attacker=w)
                        if hit:
                            dmg = deal(st, tgt, [(d(4 if crit else 2, 6) + 2, 'slashing'),
                                                 (d(1, 6), 'slashing')],
                                       magical=False, attacker=w)
                            log(f"    {w.name}: DIVES on {tgt.name} for {dmg}!")
                            if tgt is st.ursa:
                                ursa_conc_check(st, dmg)
                        else:
                            log(f"    {w.name}: dives at {tgt.name} and shears past.")
                    else:
                        if w.dist_ft(tgt) <= 10:
                            w.aloft = True
                            old, _ = w.move_toward((w.pos[0], max(2, w.pos[1] - 8)), 50)
                            log(f"    {w.name}: glides up and away.")
                        if w.dist_ft(tgt) <= 60:
                            hit, crit, _ = attack_roll(st, 6, tgt, attacker=w)
                            if hit:
                                dmg = deal(st, tgt, [(d(2 if crit else 1, 10) + 2,
                                                      'piercing')],
                                           magical=False, attacker=w)
                                log(f"    {w.name}: spits shards at {tgt.name} for {dmg}.")
                                if tgt is st.ursa:
                                    ursa_conc_check(st, dmg)
                            else:
                                log(f"    {w.name}: shard spit misses {tgt.name}.")
            elif name == 'Chimestones':
                for c in chimes:
                    if c.hp <= 0:
                        continue
                    if c.stunned:
                        log(f"    {c.name}: stands RINGING, stunned, and loses its turn.")
                        c.stunned = False
                        continue
                    tgt = min([h for h in st.pcs + ([st.fey] if st.fey else [])
                               if h is not None and h.alive and not h.aloft],
                              key=lambda h: c.dist_ft(h), default=None)
                    if tgt is None:
                        break
                    if c.entangled > 0:
                        c.entangled -= 1
                        if d20() + 4 >= 16:
                            c.entangled = 0
                            log(f"    {c.name}: spends its whole turn tearing free "
                                "of the weed.")
                        else:
                            log(f"    {c.name}: heaves against the weed-ropes and "
                                "stays stuck, and it cannot reach anybody.")
                        continue
                    c.approach(tgt, 5, 25)
                    if c.dist_ft(tgt) <= 5:
                        for _ in range(2):
                            if not tgt.alive:
                                break
                            hit, crit, _ = attack_roll(st, 6, tgt, attacker=c)
                            if hit:
                                dmg = deal(st, tgt, [(d(4 if crit else 2, 6) + 4,
                                                      'bludgeoning')],
                                           magical=False, attacker=c)
                                log(f"    {c.name}: crystal ram slams {tgt.name} for {dmg}.")
                                if tgt is st.ursa:
                                    ursa_conc_check(st, dmg)
                            else:
                                log(f"    {c.name}: crystal ram misses {tgt.name}.")
                    elif c.dist_ft(tgt) <= 40:
                        hit, crit, _ = attack_roll(st, 6, tgt, attacker=c)
                        if hit:
                            dmg = deal(st, tgt, [(d(4 if crit else 2, 8), 'piercing')],
                                       magical=False, attacker=c)
                            log(f"    {c.name}: shard volley hits {tgt.name} for {dmg}.")
                            if tgt is st.ursa:
                                ursa_conc_check(st, dmg)
                        else:
                            log(f"    {c.name}: shard volley misses {tgt.name}.")
                    else:
                        log(f"    {c.name}: grinds forward through the shallows.")
    log(f"  FIGHT 2 ENDS after round {rnd}.")
    party_state(st, "after Fight 2")
    return rnd


def short_rest(st):
    log("=" * 72)
    log("SHORT REST at the edge of the quiet reef")
    log("=" * 72)
    for h, die, cmod in ((st.lilly, 8, 2), (st.stabby, 8, 3), (st.ursa, 8, 2)):
        spent = 0
        healed = 0
        while h.hp < h.hp_max * 0.85 and spent < 4:
            spent += 1
            healed += d(1, die) + cmod
        h.hp = min(h.hp_max, h.hp + healed)
        if spent:
            log(f"  {h.name} spends {spent} Hit Dice, heals {healed}, now {h.hp}/{h.hp_max}.")
    st.ghost.hp = st.ghost.hp_max
    st.puff.hp = st.puff.hp_max
    st.s_focus = 7
    st.l_ward = 2
    st.u_wild = min(3, st.u_wild + 1)
    st.g_light = 3
    st.heal_bubble = 5
    st.mist_rounds = 0
    st.g_feystep = True
    st.u_starry = False
    st.conc = None
    if st.fey is not None:
        log("  The fey spirit bows and fades; the hour is long past.")
        st.fey = None
    log("  Focus 7, Aether Ward 2, one Wild Shape back, Guardian's Light 3.")


# --------------------------------------------------------------------------
# FIGHT 3: The Glassed Gallery. Glass Weeper + 4 Cinderolls (2 at a time).
# --------------------------------------------------------------------------
def fight3(st):
    log("=" * 72)
    log("FIGHT 3: THE GLASSED GALLERY (Glass Weeper, 4 Cinderolls in pairs)")
    log("=" * 72)
    st.lilly.pos = [14, 24]
    st.stabby.pos = [15, 23]
    st.ursa.pos = [16, 24]
    st.ghost.pos = [15, 25]
    st.puff.pos = [13, 24]
    st.cannon.pos = [13, 25]
    weeper = Actor('Glass Weeper', 'W', 'foe', 16, ehp(340), (15, 11), 20,
                   saves=dict(str=4, dex=-1, con=5, wis=1),
                   resist={'nm-bludgeoning', 'nm-piercing', 'nm-slashing'},
                   immune={'poison'},
                   cond_imm={'charmed', 'frightened', 'poisoned', 'prone'},
                   reach=15)
    weeper.cleanse_types = set()   # 80e0efd: Glassbound yields to Cleansing Edge only
    roll_spots = [(27, 12), (27, 16), (28, 10), (28, 18)]
    rolls = [Actor(f'Cinderoll-{i+1}', 'o', 'foe', 15, ehp(18), p, 40,
                   saves=dict(str=1, dex=2, con=1, wis=-1),
                   immune={'fire', 'poison'},
                   cond_imm={'blinded', 'charmed', 'deafened', 'poisoned'})
             for i, p in enumerate(roll_spots)]
    arrived = rolls[:2]
    close_up([weeper] + rolls, [st.lilly, st.stabby, st.ursa])
    terrain = {}
    for x in range(12, 19):
        for y in range(8, 15):
            terrain[(x, y)] = '~'      # glassed roots
    log("Starting map (~ = glassed roots the Weeper tends, W Weeper, o Cinderoll;")
    log("two more Cinderolls roll in from the east tunnel on round 3):")
    log(render_map(st.pcs + [st.cannon, weeper] + arrived, terrain))

    st.spend_focus()
    st.s_ignited = True
    log(f"  Stabby ignites at initiative (1 Focus). [Focus {st.s_focus}]")
    cast_ward(st, 'reading the gallery before they step into it')
    order = initiative(st, [('Cinderolls', rolls, 2), ('Glass Weeper', [weeper], -1)])
    burst_done = set()
    tended = False
    rnd = 0

    def burst(c):
        if c.name in burst_done:
            return
        burst_done.add(c.name)
        near = [h for h in st.pcs + ([st.fey] if st.fey else [])
                if h is not None and h.alive and c.dist_ft(h) <= 10]
        others = [o for o in rolls if o is not c and o.hp > 0 and c.dist_ft(o) <= 10]
        if near or others:
            log(f"      {c.name} BURSTS!")
        for h in near:
            roll = d(2, 6)
            if st.hero_save(h, 'dex', 12, adv=(h is st.stabby and st.s_ignited)):
                if h is st.stabby or h is st.puff:
                    log(f"        {h.name} evades entirely (Evasion).")
                else:
                    dmg = deal(st, h, [(roll // 2, 'fire')])
                    log(f"        {h.name} ducks: {dmg} fire.")
            else:
                dmg = deal(st, h, [(roll, 'fire')])
                log(f"        {h.name} is scorched for {dmg} fire!")
        for o in others:
            if not foe_save(o, o.saves.get('dex', 0), 12):
                o.hp -= d(2, 6)   # fire-immune actually; chain via impact? keep 0
            # Cinderolls are fire-immune; the chain is narrative only.

    while (weeper.hp > 0 or any(c.hp > 0 for c in arrived)) \
            and any(h.alive for h in st.heroes) and rnd < 20:
        rnd += 1
        start_round(st, rnd)
        if rnd == (2 if BODIES else 3) and len(arrived) < 4:
            arrived.extend(rolls[2:4])
            log("    Two more Cinderolls come rolling out of the dark, eyes furious.")
        for _, name, actors in order:
            live_rolls_now = [c for c in arrived if c.hp > 0]
            if name == 'Stabby' and st.stabby.alive:
                st.s_speed_left = 65
                st.stabby.dodging = False
                if break_free(st, st.stabby, 2):
                    continue
                pool = [weeper] if weeper.hp > 0 else sorted(
                    live_rolls_now, key=lambda c: st.stabby.dist_ft(c))
                if st.stabby.hp < 25:
                    stabby_defensive(st, pool + live_rolls_now)
                elif pool:
                    stabby_attack_routine(st, pool, rnd, fury_ok=(weeper.hp > 0))
                    for c in live_rolls_now:
                        if c.hp <= 0:
                            burst(c)
            elif name == 'Lilly' and st.lilly.alive:
                if break_free(st, st.lilly, -1):
                    continue
                if weeper.hp > 0 and st.lilly.dist_ft(weeper) > 30:
                    old, moved = st.lilly.approach(weeper, 30, 25)
                    if moved:
                        st.cannon.approach(weeper, 40, 15)
                        st.puff.approach(weeper, 35, 30)
                        log(f"    Lilly: walks it in {old}->{tuple(st.lilly.pos)}, "
                            "inside Boomstick's short range and outside the fronds.")
                if weeper.hp > 0:
                    true_strike(st, weeper, adv=tended)
                elif live_rolls_now:
                    true_strike(st, live_rolls_now[0])
                    if live_rolls_now[0].hp <= 0:
                        burst(live_rolls_now[0])
                hurt_near = [h for h in st.pcs if h.alive
                             and h.hp < h.hp_max * 0.60
                             and h.dist_ft(st.cannon) <= 10]
                pool = [c for c in arrived if c.hp > 0 and st.cannon.dist_ft(c) <= 120]
                if hurt_near:
                    cannon_fire(st, 'protector')
                elif pool:
                    cannon_fire(st, 'ballista',
                                sorted(pool, key=lambda f: st.cannon.dist_ft(f)))
                    for c in pool:
                        if c.hp <= 0:
                            burst(c)
                elif weeper.hp > 0:
                    cannon_fire(st, 'ballista', [weeper])
                if weeper.hp > 0 and not puff_pipes(
                        st, ([weeper] if weeper.hp > 0 else []) + arrived):
                    puff_turn(st, weeper, use_mm=True)
                else:
                    puff_turn(st, next((c for c in arrived if c.hp > 0), None),
                              use_mm=False)
            elif name == 'Ursa' and st.ursa.alive:
                _pk = [x for x in [weeper] + rolls if x.hp > 0]
                pack_tick(st, _pk)
                bonus_used = ursa_triage(st)
                if rnd == 1 and not bonus_used and ursa_starry(st, targets=_pk):
                    bonus_used = True
                if break_free(st, st.ursa, -1):
                    continue
                if cast_polymorph(st):
                    continue
                if URSA_LINE != 'control':
                    pool = ([weeper] if weeper.hp > 0 else []) + [
                        c for c in arrived if c.hp > 0]
                    ursa_damage_line(st, pool, bonus_used)
                    fey_turn(st, pool)
                    continue
                if rnd == 1 and st.u_staff >= 2 and weeper.hp > 0:
                    st.u_staff -= 2
                    ursa_take_conc(st, 'the Moonbeam')
                    ursa_close(st, weeper, want_ft=115)
                    log("    Ursa: MOONBEAM from the staff (2 charges), a cold pillar "
                        "of light drops onto the Weeper. It is Rooted; it cannot "
                        f"leave the beam. [{st.u_staff} charges left]")
                    log("      (Concentration: a hard enough hit on Ursa puts it out.)")
                elif rnd >= 2 and weeper.hp > 0:
                    roll = d20() + 5
                    if roll >= 14:
                        tended = True
                        weeper.cleansed = True
                        log(f"    Ursa: TENDS THE ROOTS (Medicine {roll} vs DC 14): the "
                            f"glass greys, the Weeper's Glassbound is stripped and "
                            f"everyone has ADVANTAGE against it!")
                    else:
                        tended = False
                        log(f"    Ursa: tries to tend the roots (Medicine {roll} vs DC 14) "
                            f"and cannot find live wood.")
                else:
                    w_tgt = weeper if weeper.hp > 0 else next(
                        (c for c in arrived if c.hp > 0), None)
                    if w_tgt is not None:
                        starry_wisp(st, w_tgt)
                        if w_tgt is not weeper and w_tgt.hp <= 0:
                            burst(w_tgt)
                if not bonus_used and st.u_starry:
                    t2 = next((c for c in arrived if c.hp > 0
                               and st.ursa.dist_ft(c) <= 60), None)
                    if t2 is None and weeper.hp > 0:
                        t2 = weeper
                    if t2 is not None:
                        star_arrow(st, t2)
                        if t2 is not weeper and t2.hp <= 0:
                            burst(t2)
            elif name == st.ghost.name and st.ghost.alive:
                end_polymorph(st, st.ghost)
                if st.ghost.ape:
                    ape_turn(st, st.ghost, ([weeper] if weeper.hp > 0 else [])
                             + [c for c in arrived if c.hp > 0])
                    continue
                live_rolls = [c for c in arrived if c.hp > 0]
                pack = [c for c in live_rolls if st.ghost.dist_ft(c) <= 15]
                if GHOST_SUPPORT:
                    log(f"    {st.ghost.name}: hangs back on triage.")
                elif st.ghost.kind == 'ghostbloom' and st.g_wail and len(pack) >= 2:
                    st.g_wail = False
                    log("    Ghostbloom: GHOSTLY WAIL, a cry that cracks the glass!")
                    for c in pack[:3]:
                        roll = d(5, 6)
                        if foe_save(c, c.saves.get('wis', 0), 16):
                            dmg = deal(st, c, [(roll // 2, 'necrotic')], credit='Ghostbloom')
                            log(f"      {c.name} takes {dmg} necrotic.")
                        else:
                            dmg = deal(st, c, [(roll, 'necrotic')], credit='Ghostbloom')
                            c.fright = 2
                            log(f"      {c.name} takes {dmg} necrotic and quails!")
                        if c.hp <= 0:
                            log(f"      {c.name} cracks apart.")
                            burst(c)
                elif live_rolls:
                    companion_turn(st, sorted(live_rolls,
                                          key=lambda c: st.ghost.dist_ft(c)))
                    for c in live_rolls:
                        if c.hp <= 0:
                            burst(c)
                elif weeper.hp > 0:
                    companion_turn(st, [weeper])
            elif name == 'Cinderolls':
                for c in arrived:
                    if c.hp <= 0:
                        continue
                    if c.fright > 0:
                        c.fright -= 1
                    tgt = min([h for h in st.pcs if h.alive],
                              key=lambda h: c.dist_ft(h), default=None)
                    if tgt is None:
                        break
                    far = c.dist_ft(tgt) >= 20
                    c.approach(tgt, 5, 40 if c.dist_ft(tgt) <= 45 else 80)
                    if c.dist_ft(tgt) <= 5:
                        hit, crit, _ = attack_roll(st, 4, tgt, attacker=c)
                        if hit:
                            parts = [(d(4 if crit else 2, 4) + 2, 'bludgeoning'),
                                     (d(1, 6), 'fire')]
                            if far:
                                parts.append((d(1, 6), 'bludgeoning'))
                            dmg = deal(st, tgt, parts, magical=False, attacker=c)
                            msg = f"    {c.name}: rolling charge slams {tgt.name} for {dmg}!"
                            if far and not st.hero_save(tgt, 'str', 12):
                                tgt.prone = True
                                msg += " Knocked prone!"
                            log(msg)
                            if tgt is st.ursa:
                                ursa_conc_check(st, dmg)
                        else:
                            log(f"    {c.name}: careens past {tgt.name}.")
                    else:
                        log(f"    {c.name}: rolls in fast.")
            elif name == 'Glass Weeper':
                if weeper.hp <= 0:
                    continue
                # THE ROOTS ERUPT (80e0efd): start of its turn, one creature it
                # can see within 60 ft, DC 15 Dex, 3d8 piercing + Restrained.
                # Suppressed on a turn when Tend the Roots stripped Glassbound.
                if not tended:
                    pool = [h for h in st.pcs if h.alive and not h.restrained
                            and weeper.dist_ft(h) <= 60]
                    if pool:
                        soft = [h for h in pool if not (h is st.stabby
                                or getattr(h, 'evasion', False))]
                        v = max(soft or pool, key=lambda h: h.hp)
                        roll = d(3, 8)
                        if st.hero_save(v, 'dex', 15):
                            if v is st.stabby or getattr(v, 'evasion', False):
                                log("    THE ROOTS ERUPT under "
                                    f"{v.name}, who is already gone (Evasion).")
                            else:
                                dmg = deal(st, v, [(roll // 2, 'piercing')],
                                           magical=False)
                                log(f"    THE ROOTS ERUPT under {v.name}: {dmg}, "
                                    "and they cannot hold on.")
                        else:
                            dmg = deal(st, v, [(roll, 'piercing')], magical=False)
                            v.restrained = True
                            log(f"    THE ROOTS ERUPT under {v.name} for {dmg} "
                                "and close around them: RESTRAINED.")
                            if v is st.ursa:
                                ursa_conc_check(st, dmg)
                if st.conc == 'the Moonbeam':
                    roll = d(2, 10) + d(1, 8)
                    if foe_save(weeper, weeper.saves.get('con', 0), 16):
                        dmg = deal(st, weeper, [(roll // 2, 'radiant')],
                                   credit='Ursa')
                        log(f"    The Moonbeam sears the Weeper for {dmg} radiant "
                            "(it braces).")
                    else:
                        dmg = deal(st, weeper, [(roll, 'radiant')], credit='Ursa')
                        log(f"    The Moonbeam sears the Weeper for {dmg} radiant.")
                    if weeper.hp <= 0:
                        log("      Glass Weeper is destroyed.")
                        continue
                if weeper.damaged_since and not weeper.cleansed:
                    weeper.hp = min(weeper.hp_max, weeper.hp + 10)
                    log(f"    Glass Weeper: glass knits closed, REGENERATES 10 (now {weeper.hp}).")
                elif weeper.damaged_since:
                    log("    Glass Weeper: the wounds stay OPEN, because the "
                        "Nichirin burned the glass. Nothing else would have.")
                weeper.damaged_since = False
                weeper.cleansed = False
                in_reach = [h for h in st.pcs if h.alive and weeper.dist_ft(h) <= 15]
                cone = [h for h in st.pcs if h.alive and weeper.dist_ft(h) <= 30]
                if len(cone) >= 3 and rng.randint(1, 6) >= 5:
                    log("    Glass Weeper: KEENING, a cone of grief-noise!")
                    for h in cone[:4]:
                        roll = d(6, 6)
                        if st.hero_save(h, 'con', 15):
                            dmg = deal(st, h, [(roll // 2, 'psychic')])
                            log(f"      {h.name} grits through it: {dmg} psychic.")
                        else:
                            dmg = deal(st, h, [(roll, 'psychic')])
                            h.fright = 2
                            log(f"      {h.name} takes {dmg} psychic and is frightened!")
                            if h is st.ursa:
                                ursa_conc_check(st, dmg)
                else:
                    if not in_reach:
                        tgt = min([h for h in st.pcs if h.alive],
                                  key=lambda h: weeper.dist_ft(h), default=None)
                        if tgt:
                            weeper.approach(tgt, 15, 15)  # rooted: 15 ft leash
                            in_reach = [h for h in st.pcs
                                        if h.alive and weeper.dist_ft(h) <= 15]
                    for i in range(3):
                        if not in_reach:
                            break
                        tgt = in_reach[i % len(in_reach)]
                        if not tgt.alive:
                            continue
                        hit, crit, _ = attack_roll(st, 7, tgt, attacker=weeper)
                        if hit:
                            dmg = deal(st, tgt, [(d(4 if crit else 2, 6) + 5,
                                                  'slashing')],
                                       magical=False, attacker=weeper)
                            log(f"    Glass Weeper: frond lash rakes {tgt.name} for {dmg}.")
                            if tgt is st.ursa:
                                ursa_conc_check(st, dmg)
                        else:
                            log(f"    Glass Weeper: frond lash misses {tgt.name}.")
        for c in arrived:
            if c.hp <= 0:
                burst(c)
        for h in st.pcs:
            if h.prone and h.alive:
                h.prone = False   # they stand at the start of their next turn
    log(f"  FIGHT 3 ENDS after round {rnd}.")
    log("  The Weeper shatters. Curled where its heart would be is a small,")
    log("  ordinary creature that has been dead for two years.")
    party_state(st, "after Fight 3")
    return rnd


# --------------------------------------------------------------------------
# BOSS: Groudon's Hollow.
# --------------------------------------------------------------------------
def boss(st):
    log("=" * 72)
    log("BOSS: GROUDON'S HOLLOW (Groudon, the Spike, Glasslings every round)")
    log("=" * 72)
    st.lilly.pos = [13, 26]
    st.stabby.pos = [15, 25]
    st.ursa.pos = [17, 26]
    st.ghost.pos = [15, 27]
    st.puff.pos = [12, 26]
    st.cannon.pos = [12, 27]
    groudon = Actor('Groudon', 'D', 'foe', 18, 230, (14, 8), 40,
                    saves=dict(str=8, dex=-2, con=7, wis=2),
                    resist={'nm-bludgeoning', 'nm-piercing', 'nm-slashing'},
                    immune={'fire', 'poison'},
                    cond_imm={'charmed', 'frightened', 'prone', 'restrained'},
                    reach=15)
    spike = Actor('The Spike', 'x', 'foe', 17, ehp(SPIKE_HP), (14, 6), 0)
    spike.immune = {'slashing', 'bludgeoning', 'piercing', 'fire', 'cold',
                    'thunder', 'lightning', 'poison', 'necrotic', 'psychic',
                    'acid'}
    spike.is_spike = True
    close_up([groudon, spike], [st.lilly, st.stabby, st.ursa])
    spike.ce_touched = False
    glasslings = []
    terrain = {}
    for x in range(12, 18):
        for y in range(6, 12):
            terrain[(x, y)] = 'D'
    terrain[(14, 6)] = 'x'
    log("Starting map (D = Groudon, a mountain filling the north of the hollow;")
    log("x = the black glass SPIKE at his shoulder, 25 ft up):")
    log(render_map(st.pcs + [st.cannon], terrain))

    st.spend_focus()
    st.s_ignited = True
    log(f"  Stabby ignites at initiative (1 Focus). [Focus {st.s_focus}]")
    cast_ward(st, 'on the lip of the hollow')
    if SHINE:
        log("  THE DROP. The tunnel ends and there is no floor: forty feet of "
            "broken shelf down into the hollow (DC 15 to descend well).")
        for h, mod, lbl in ((st.stabby, 8, 'Acrobatics'), (st.lilly, 2, 'Acrobatics'),
                            (st.ursa, 2, 'Acrobatics')):
            if hero_check(st, h, mod, 15, f'{lbl} descent'):
                log(f"    {h.name} picks a clean line down.")
            else:
                dmg = deal(st, h, [(d(2, 6), 'bludgeoning')], magical=False)
                log(f"    {h.name} loses the shelf and clatters down for {dmg}.")
        log("    Ghostbloom and Puff drift down; the cannon walks the wall.")
    order = initiative(st, [('Groudon', [groudon], -2)])
    vent_ready = True
    stabby_at_spike = False
    n_spawned = 0
    for _i in range(4):
        n_spawned += 1
        glasslings.append(Actor(f'Glassling-{n_spawned}', 'g', 'foe', 14, ehp(10),
                                (12 + _i, 13), 30, saves=dict(dex=3, con=1, wis=-2),
                                immune={'poison', 'psychic'},
                                cond_imm={'blinded', 'charmed', 'deafened',
                                          'frightened', 'poisoned'}))
    log("  Four Glasslings are ALREADY LOOSE on the hollow floor, picking over the "
        "stone, and they look up all at once.")
    rnd = 0
    while spike.hp > 0 and any(h.alive for h in st.heroes) and rnd < 14:
        rnd += 1
        start_round(st, rnd)
        for _, name, actors in order:
            if spike.hp <= 0:
                break
            if name == 'Stabby' and st.stabby.alive:
                st.s_speed_left = 65
                sotw = False
                if not stabby_at_spike:
                    if st.s_airdance:
                        st.s_airdance = False
                        st.stabby.fly = True
                        st.stabby.aloft = True
                        log("    Stabby: AIR DANCE! The Sash catches him and he goes "
                            "UP the mountainside like a red spark.")
                    old, _ = st.stabby.approach(spike, 5, 65)
                    if st.stabby.dist_ft(spike) > 5:
                        sotw = True
                        st.stabby.approach(spike, 5, 65)
                        log(f"    Stabby: Step of the Wind, {old}->{tuple(st.stabby.pos)}, "
                            "closing on the spike (bonus action spent).")
                    if st.stabby.dist_ft(spike) <= 5:
                        stabby_at_spike = True
                        log("    Stabby reaches the SPIKE at Groudon's shoulder.")
                if stabby_at_spike and SHINE and st.stabby.aloft and rnd > 1:
                    if not hero_check(st, st.stabby, 8, 15, 'Acrobatics vs the '
                                      'heat-shear'):
                        st.stabby.pos[1] += 3
                        stabby_at_spike = False
                        log("    The updraft off the magma seams SLAMS Stabby off "
                            "the shoulder; the Sash catches him below. He spends "
                            "the round fighting back up.")
                if stabby_at_spike:
                    pre = spike.hp
                    # Step of the Wind used his bonus action: no Devour and no
                    # Martial Arts punch on that turn.
                    stabby_attack_routine(st, [spike], rnd, fury_ok=False,
                                          devour=(not sotw), no_bonus=sotw)
                    if spike.hp < pre and spike.hp > 0:
                        log("      Groudon THRASHES; Stabby is flying, and the Sash "
                            "holds him just off the plates.")
            elif name == 'Lilly' and st.lilly.alive:
                if st.lilly.dist_ft(spike) > 90:
                    old, _ = st.lilly.approach(spike, 90, 25)
                    st.cannon.approach(spike, 100, 15)
                    st.puff.approach(spike, 100, 30)
                    log(f"    Lilly: hustles forward {old}->{tuple(st.lilly.pos)}, "
                        "Puff and the cannon trundling with her.")
                if st.lilly.dist_ft(spike) <= 90:
                    true_strike(st, spike, dis=True, radiant=True)
                cannon_fire(st, 'ballista', [spike], dis=True)  # called shot
                puff_turn(st, spike, use_mm=True, overload=True)
                if spike.hp <= 0:
                    break
            elif name == 'Ursa' and st.ursa.alive:
                _pk = [x for x in (groudon, spike) if x.hp > 0]
                pack_tick(st, _pk)
                bonus_used = ursa_triage(st)
                if rnd == 1 and not bonus_used and ursa_starry(st, targets=_pk):
                    bonus_used = True
                if cast_polymorph(st):
                    continue
                if URSA_LINE != 'control':
                    if (st.fey is None or st.fey.hp <= 0) and st.u_slots[3] > 0:
                        (conjure_animals(st, tuple(st.ursa.pos), targets=_pk)
                         if URSA_LINE in ('pack', 'pack4') else summon_fey(st, pos=fey_drop(st, spike)))
                    else:
                        guiding_bolt(st, spike, dis=True)
                    if not bonus_used and st.u_starry:
                        star_arrow(st, spike, dis=True)
                    if st.fey is not None and st.fey.hp > 0:
                        st.fey.aloft = True
                        fey_turn(st, [spike])
                    if spike.hp <= 0:
                        break
                    continue
                lings = [g for g in glasslings if g.hp > 0
                         and st.ursa.dist_ft(g) <= 10]
                if len(lings) >= 3 and st.u_slots[1] > 0:
                    st.u_slots[1] -= 1
                    log(f"    Ursa: THUNDERWAVE scatters the glass! "
                        f"[{st.u_slots[1]} 1st slots left]")
                    roll = d(2, 8)
                    for g in lings:
                        dmg = roll if not foe_save(g, 1, 16) else roll // 2
                        st.tally['dealt']['Ursa'] += min(dmg, max(0, g.hp))
                        if g.hp > 0 and g.hp - dmg <= 0:
                            st.tally['kills']['Ursa'] += 1
                        g.hp -= dmg
                        if g.hp <= 0:
                            log(f"      {g.name} shatters.")
                else:
                    guiding_bolt(st, spike, dis=True)
                if not bonus_used and st.u_starry:
                    star_arrow(st, spike, dis=True)
                if spike.hp <= 0:
                    break
            elif name == st.ghost.name and st.ghost.alive:
                end_polymorph(st, st.ghost)
                if st.ghost.ape:
                    ape_turn(st, st.ghost,
                             sorted([g for g in glasslings if g.hp > 0],
                                    key=lambda g: st.ghost.dist_ft(g)))
                    continue
                lings = sorted([g for g in glasslings if g.hp > 0],
                               key=lambda g: st.ghost.dist_ft(g))
                if GHOST_SUPPORT:
                    log(f"    {st.ghost.name}: shields the casters.")
                elif lings:
                    companion_turn(st, lings)
                    for g in lings:
                        if g.hp <= 0 and not getattr(g, 'burst', False):
                            g.burst = True
                            near = [h for h in st.pcs
                                    if h.alive and g.dist_ft(h) <= 5]
                            for h in near:
                                if not st.hero_save(h, 'dex', 12):
                                    dmg = deal(st, h, [(d(2, 4), 'slashing')])
                                    log(f"      Shatterburst catches {h.name} for {dmg}.")
                else:
                    log(f"    {st.ghost.name}: holds position by Lilly and Ursa.")
            elif name == 'Groudon':
                # Re-knit (knob): the corruption closes unless the Nichirin
                # touched it since Groudon's last turn.
                if SPIKE_REKNIT and spike.hp > 0:
                    if spike.ce_touched:
                        log("    The spike stays CRACKED where the Nichirin burned it.")
                    elif spike.hp < SPIKE_HP:
                        spike.hp = min(SPIKE_HP, spike.hp + 20)
                        log(f"    The spike RE-KNITS, black glass flowing closed "
                            f"(back to {spike.hp}).")
                    spike.ce_touched = False
                # Agony
                groudon.hp -= 10
                new_lings = []
                for _ in range(2 if BODIES else 1):
                    n_spawned += 1
                    g = Actor(f'Glassling-{n_spawned}', 'g', 'foe', 14, ehp(10),
                              (groudon.pos[0] + rng.randint(-2, 3), groudon.pos[1] + 4),
                              30, saves=dict(dex=3, con=1, wis=-2),
                              immune={'poison', 'psychic'},
                              cond_imm={'blinded', 'charmed', 'deafened',
                                        'frightened', 'poisoned'})
                    glasslings.append(g)
                    new_lings.append(g.name)
                log(f"    The spike pulses (Groudon takes 10 Agony, {groudon.hp} HP); "
                    f"{' and '.join(new_lings)} drop{'s' if len(new_lings) == 1 else ''} "
                    "off his back and scuttles.")
                for h in st.pcs:
                    if h.alive and groudon.dist_ft(h) <= 20:
                        if not st.hero_save(h, 'dex', 16,
                                            adv=(h is st.stabby and st.s_ignited)):
                            dmg = deal(st, h, [(d(3, 6), 'bludgeoning')])
                            log(f"      Agony shockwave hits {h.name} for {dmg}.")
                        elif h is st.stabby or getattr(h, 'evasion', False):
                            log(f"      {h.name} rides the shockwave "
                                "(Evasion: nothing).")
                        else:
                            log(f"      {h.name} keeps their feet.")
                # Action
                if rnd == 1 and SHINE and vent_ready:
                    vent_ready = False
                    ground = [h for h in st.pcs if h.alive and not h.aloft]
                    ground.sort(key=lambda h: groudon.dist_ft(h))
                    in_line = ground[:2] if len(ground) >= 2 else ground
                    log("    Groudon: his first act is MAGMA VENT, a white-orange "
                        f"line under {' and '.join(h.name for h in in_line)}!")
                    for h in in_line:
                        roll = d(10, 6)
                        if st.hero_save(h, 'dex', 17):
                            if h is st.stabby or getattr(h, 'evasion', False):
                                log(f"      {h.name} is simply not there when it "
                                    "lands (Evasion).")
                                continue
                            dmg = deal(st, h, [(roll // 2, 'fire')])
                            log(f"      {h.name} dives aside: {dmg} fire.")
                        else:
                            if h is st.stabby or getattr(h, 'evasion', False):
                                roll //= 2
                            dmg = deal(st, h, [(roll, 'fire')])
                            log(f"      {h.name} is caught in it for {dmg} fire!")
                elif rnd == 1:
                    log("    Groudon: CONTINENTAL STEP. The floor of the world moves.")
                    groudon.pos[1] += 2
                    spike.pos[1] += 2
                    for h in st.pcs:
                        if h.alive and not h.aloft and groudon.dist_ft(h) <= 30:
                            if not st.hero_save(h, 'dex', 16):
                                dmg = deal(st, h, [(d(2, 10), 'bludgeoning')])
                                h.prone = True
                                log(f"      {h.name} is thrown down for {dmg}.")
                            else:
                                log(f"      {h.name} rides the ground-swell.")
                elif vent_ready:
                    vent_ready = False
                    ground = [h for h in st.pcs if h.alive and not h.aloft]
                    ground.sort(key=lambda h: groudon.dist_ft(h))
                    in_line = ground[:2] if len(ground) >= 2 else ground
                    log("    Groudon: MAGMA VENT, a white-orange line splits the floor "
                        f"under {' and '.join(h.name for h in in_line)}!")
                    for h in in_line:
                        roll = d(10, 6)
                        if st.hero_save(h, 'dex', 17):
                            if h is st.stabby or getattr(h, 'evasion', False):
                                log(f"      {h.name} is simply not there when it "
                                    "lands (Evasion).")
                                continue
                            dmg = deal(st, h, [(roll // 2, 'fire')])
                            log(f"      {h.name} dives aside: {dmg} fire.")
                        else:
                            if h is st.stabby or getattr(h, 'evasion', False):
                                roll //= 2
                            dmg = deal(st, h, [(roll, 'fire')])
                            log(f"      {h.name} is caught in it for {dmg} fire!")
                else:
                    vent_ready = rng.randint(1, 6) >= 4
                    tgt = min([h for h in st.pcs
                               if h.alive and groudon.dist_ft(h) <= 15],
                              key=lambda h: groudon.dist_ft(h), default=None)
                    if tgt is not None:
                        hit, crit, _ = attack_roll(st, 12, tgt, attacker=groudon)
                        if hit:
                            dmg = deal(st, tgt, [(d(6 if crit else 3, 10) + 8,
                                                  'slashing')],
                                       magical=False, attacker=groudon)
                            log(f"    Groudon: CLAW catches {tgt.name} for {dmg}!")
                            if tgt is st.ursa:
                                ursa_conc_check(st, dmg)
                        else:
                            log(f"    Groudon: claw crashes down beside {tgt.name}.")
                    else:
                        near = min([h for h in st.pcs if h.alive and not h.aloft],
                                   key=lambda h: groudon.dist_ft(h), default=None)
                        if near is not None:
                            log("    Groudon: CONTINENTAL STEP, heaving himself "
                                "toward the party; the floor bucks.")
                            dx = 1 if near.pos[0] > groudon.pos[0] else -1 \
                                if near.pos[0] < groudon.pos[0] else 0
                            dy = 1 if near.pos[1] > groudon.pos[1] else -1 \
                                if near.pos[1] < groudon.pos[1] else 0
                            for _ in range(8):
                                groudon.pos[0] += dx
                                groudon.pos[1] += dy
                                spike.pos[0] += dx
                                spike.pos[1] += dy
                            for h in st.pcs:
                                if h.alive and not h.aloft and groudon.dist_ft(h) <= 30:
                                    if not st.hero_save(h, 'dex', 16):
                                        dmg = deal(st, h, [(d(2, 10), 'bludgeoning')])
                                        h.prone = True
                                        log(f"      {h.name} is thrown down for {dmg}.")
                                    else:
                                        log(f"      {h.name} rides the ground-swell.")
                # Glasslings
                for g in glasslings:
                    if g.hp <= 0:
                        continue
                    tgt = min([h for h in st.pcs if h.alive and not h.aloft],
                              key=lambda h: g.dist_ft(h), default=None)
                    if tgt is None:
                        continue
                    g.approach(tgt, 5, 60 if g.dist_ft(tgt) > 35 else 30)
                    if g.dist_ft(tgt) <= 5:
                        hit, crit, _ = attack_roll(st, 5, tgt, attacker=g)
                        if hit:
                            dmg = deal(st, tgt, [(d(2 if crit else 1, 6) + 3,
                                                  'slashing')],
                                       magical=False, attacker=g)
                            log(f"    {g.name}: glass bite on {tgt.name} for {dmg}.")
                            if tgt is st.ursa:
                                ursa_conc_check(st, dmg)
                        else:
                            log(f"    {g.name}: snaps at {tgt.name} and misses.")
                    else:
                        log(f"    {g.name}: scuttles at {tgt.name}.")
        for h in st.pcs:
            if h.prone and h.alive:
                h.prone = False
    if spike.hp <= 0:
        log("  >>> THE SPIKE BREAKS. It comes apart like a held breath let go. <<<")
        alive_lings = sum(1 for g in glasslings if g.hp > 0)
        if alive_lings:
            log(f"  Every Glassling on the board ({alive_lings} of them) collapses "
                "into ordinary sand in the same heartbeat.")
        log(f"  Groudon goes still at {groudon.hp}/230 HP; nobody ever had to chew "
            "through him. The Mote of Terra drifts to the Sphere.")
    log(f"  BOSS ENDS after round {rnd}.")
    party_state(st, "after the Hollow")
    st.spike_ok = spike.hp <= 0
    return rnd


# --------------------------------------------------------------------------
# THE ROAD BETWEEN: the board walk. Sequence extracted from build_rift_board's
# actual geometry (19 spaces; even/odd of the movement die picks the outcome).
# --------------------------------------------------------------------------
ROAD = [
    ('the Gate to Mosslight Landing', ['trav', 'enc', 'trav', 'boon', 'wild']),
    ('Mosslight to the Chime Reef', ['haz', 'trav', 'enc', 'trav']),
    ('the Reef to the Glassed Gallery', ['enc', 'trav', 'enc', 'wild', 'haz']),
    ("the Gallery to Groudon's Hollow", ['trav', 'enc', 'trav', 'boon', 'trav']),
]


def thumpaw_fight(st):
    log("  " + "-" * 60)
    log("  ROAD FIGHT: THUMPAW (garnet, even). A boulder unfolds in the way.")
    st.lilly.pos = [14, 21]
    st.stabby.pos = [15, 20]
    st.ursa.pos = [16, 21]
    st.ghost.pos = [15, 22]
    st.puff.pos = [13, 21]
    st.cannon.pos = [13, 22]
    tp = Actor('Thumpaw', 'T', 'foe', 14, ehp(76), (15, 12), 30,
               saves=dict(str=5, dex=-1, con=4, wis=1), reach=10)
    log("  (If Ursa thinks of his Mark, DC 15 Animal Handling at +8 with "
        "advantage moves it aside. This table came here to fight.)")
    st.spend_focus()
    st.s_ignited = True
    log(f"  Stabby ignites (1 Focus). [Focus {st.s_focus}]")
    order = initiative(st, [('Thumpaw', [tp], -1)])
    rnd = 0
    poked = False
    while tp.hp > 0 and any(h.alive for h in st.heroes) and rnd < 8:
        rnd += 1
        start_round(st, rnd)
        for _, name, actors in order:
            if tp.hp <= 0:
                break
            if name == 'Stabby' and st.stabby.alive:
                st.s_speed_left = 65
                st.stabby.dodging = False
                if st.stabby.hp < 25:
                    stabby_defensive(st, [tp])
                else:
                    stabby_attack_routine(st, [tp], rnd, fury_ok=True)
                    poked = True
            elif name == 'Lilly' and st.lilly.alive:
                true_strike(st, tp)
                poked = True
                cannon_fire(st, 'ballista', [tp])
                puff_turn(st, tp, use_mm=False)
            elif name == 'Ursa' and st.ursa.alive:
                _pk = [x for x in ([tp] if tp is not None else []) if x.hp > 0]
                pack_tick(st, _pk)
                bonus_used = ursa_triage(st)
                if rnd == 1 and not bonus_used:
                    bonus_used = ursa_starry(st, targets=_pk)
                starry_wisp(st, tp)
                poked = True
                if not bonus_used and st.u_starry:
                    star_arrow(st, tp)
            elif name == st.ghost.name and st.ghost.alive:
                if GHOST_SUPPORT:
                    log(f"    {st.ghost.name}: hangs back on triage.")
                else:
                    companion_turn(st, [tp])
            elif name == 'Thumpaw':
                if tp.hp <= 0:
                    continue
                if not poked:
                    log("    Thumpaw: stands in the tunnel, patient, in the way.")
                    continue
                tgt = min([h for h in st.pcs if h.alive and not h.aloft],
                          key=lambda h: tp.dist_ft(h), default=None)
                if tgt is None or tp.dist_ft(tgt) > 10:
                    log("    Thumpaw: plants itself and waits. It never pursues.")
                    continue
                for _ in range(2):
                    if not tgt.alive:
                        break
                    hit, crit, _ = attack_roll(st, 7, tgt, attacker=tp)
                    if hit:
                        dmg = deal(st, tgt, [(d(4 if crit else 2, 8) + 5,
                                              'bludgeoning')],
                                   magical=False, attacker=tp)
                        log(f"    Thumpaw: shovel slam flattens {tgt.name} for {dmg}.")
                        if tgt is st.ursa:
                            ursa_conc_check(st, dmg)
                    else:
                        log(f"    Thumpaw: shovel slam misses {tgt.name}.")
    log(f"  Thumpaw goes down after {rnd} rounds, grumbling to the last.")
    st.s_ignited = False
    return rnd


def gleamoth_fight(st):
    log("  " + "-" * 60)
    log("  ROAD FIGHT: THE GLEAMOTH (garnet, odd). Forty pale sparks round the "
        "corner, and they want the Sphere.")
    st.lilly.pos = [15, 21]
    st.stabby.pos = [14, 20]
    st.ursa.pos = [16, 21]
    st.ghost.pos = [15, 22]
    st.puff.pos = [14, 22]
    st.cannon.pos = [16, 22]
    swarms = [Actor(f'Gleamoth swarm-{i+1}', 'g', 'foe', 12, ehp(26), p, 40,
                    saves=dict(str=-3, dex=2, con=2, wis=0),
                    resist={'bludgeoning', 'piercing', 'slashing'},
                    vuln={'fire', 'thunder'},
                    cond_imm={'charmed', 'frightened', 'grappled', 'prone',
                              'restrained', 'stunned'}, fly=True)
              for i, p in enumerate([(14, 10), (15, 9), (16, 10)])]
    order = initiative(st, [('Gleamoths', swarms, 2)])
    rnd = 0
    while any(s.hp > 0 for s in swarms) and any(h.alive for h in st.heroes) and rnd < 8:
        rnd += 1
        start_round(st, rnd)
        for _, name, actors in order:
            live = [s for s in swarms if s.hp > 0]
            if not live:
                break
            if name == 'Stabby' and st.stabby.alive:
                st.stabby.dodging = False
                for _ in range(2):
                    live = [s for s in swarms if s.hp > 0]
                    if not live:
                        break
                    t = min(live, key=lambda s: st.stabby.dist_ft(s))
                    if st.stabby.dist_ft(t) > 5:
                        st.stabby.approach(t, 5, 55)
                    hit, crit, _ = attack_roll(st, 10, t, attacker=st.stabby)
                    if hit:
                        dmg = deal(st, t, [(d(2 if crit else 1, 8) + 7, 'force')],
                                   attacker=st.stabby)
                        log(f"    Stabby: force-wrapped fist scatters "
                            f"{t.name} for {dmg}.")
                        if t.hp <= 0:
                            log(f"      {t.name} disperses in a drift of lights.")
                    else:
                        log(f"    Stabby: swats through {t.name}, moths part around it.")
            elif name == 'Lilly' and st.lilly.alive:
                on_her = [s for s in swarms if s.hp > 0
                          and s.dist_ft(st.lilly) <= 5]
                if len(on_her) >= 2 and st.l_slot1 > 0:
                    st.l_slot1 -= 1
                    log(f"    Lilly: THUNDERWAVE, the boom rolls through the cloud! "
                        f"[{st.l_slot1} 1st slots left]")
                    base, rider = d(2, 8), d(1, 8)
                    first = True
                    for s in on_her:
                        r2 = base + (rider if first else 0)
                        first = False
                        if foe_save(s, s.saves.get('con', 0), 16):
                            dmg = deal(st, s, [(max(1, r2) // 2, 'thunder')], credit='Lilly')
                            log(f"      {s.name} holds together: {dmg} thunder.")
                        else:
                            dmg = deal(st, s, [(max(1, r2), 'thunder')], credit='Lilly')
                            log(f"      {s.name} is blasted apart for {dmg} thunder!")
                        if s.hp <= 0:
                            log(f"      {s.name} disperses in a drift of lights.")
                else:
                    t = min([s for s in swarms if s.hp > 0],
                            key=lambda s: st.lilly.dist_ft(s))
                    true_strike(st, t)
                pool = [s for s in swarms if s.hp > 0]
                if pool:
                    cannon_fire(st, 'ballista', pool)
                puff_turn(st, next((s for s in swarms if s.hp > 0), None),
                          use_mm=False)
            elif name == 'Ursa' and st.ursa.alive:
                _pk = [sw for sw in swarms if sw.hp > 0]
                pack_tick(st, _pk)
                bonus_used = ursa_triage(st)
                if rnd == 1 and not bonus_used:
                    bonus_used = ursa_starry(st, targets=_pk)
                t = next((sw for sw in swarms if sw.hp > 0), None)
                if t is not None:
                    starry_wisp(st, t)
                if not bonus_used and st.u_starry:
                    star_arrow(st, next((sw for sw in swarms if sw.hp > 0), None))
            elif name == st.ghost.name and st.ghost.alive:
                if GHOST_SUPPORT:
                    log(f"    {st.ghost.name}: hangs back on triage.")
                else:
                    companion_turn(st, [s for s in swarms if s.hp > 0])
            elif name == 'Gleamoths':
                for s in swarms:
                    if s.hp <= 0:
                        continue
                    s.approach(st.lilly, 0, 40)
                    if s.dist_ft(st.lilly) > 0:
                        log(f"    {s.name}: drifts toward the Sphere's light.")
                        continue
                    hit, crit, _ = attack_roll(st, 4, st.lilly, attacker=s)
                    if hit:
                        n = 2 if s.hp <= s.hp_max // 2 else 4
                        dmg = deal(st, st.lilly, [(d(n * (2 if crit else 1), 4),
                                                   'piercing')],
                                   magical=False, attacker=s)
                        st.lilly.fright = 2
                        log(f"    {s.name}: smothers Lilly for {dmg}; she is "
                            "BLINDED by wings until her next turn.")
                    else:
                        log(f"    {s.name}: swirls over Lilly, wings everywhere, "
                            "and cannot get through her armor.")
    log(f"  The last lights scatter after {rnd} rounds.")
    return rnd


def road_walk(st, seg, stats):
    label, seq = ROAD[seg]
    log("=" * 72)
    log(f"THE ROAD: {label} ({len(seq)} spaces)")
    log("=" * 72)
    pos = -1
    while True:
        roll = d(1, 6)
        pos += roll
        if pos >= len(seq):
            log(f"  Move {roll}: the token reaches the stop; the beat plays.")
            break
        dot = seq[pos]
        even = (roll % 2 == 0)
        if dot == 'trav':
            log(f"  Move {roll}: a slate-blue space. Nothing; keep going.")
            continue
        stats.setdefault('events', []).append((dot, even))
        if dot == 'enc' and even:
            log(f"  Move {roll}: GARNET, even.")
            stats['road_rounds'] = stats.get('road_rounds', 0) + thumpaw_fight(st)
            revive_between(st)
        elif dot == 'enc':
            log(f"  Move {roll}: GARNET, odd.")
            stats['road_rounds'] = stats.get('road_rounds', 0) + gleamoth_fight(st)
            revive_between(st)
        elif dot == 'boon' and even:
            log(f"  Move {roll}: MOSS, even. THE DEEPWATER SPRING, forty feet of "
                "impossible clarity.")
            for h, die, cm in ((st.lilly, 8, 2), (st.stabby, 8, 3), (st.ursa, 8, 2)):
                if h.alive and h.hp < h.hp_max:
                    heal = d(1, die) + cm
                    h.hp = min(h.hp_max, h.hp + heal)
                    log(f"    {h.name} drinks a Hit Die back: +{heal}, now {h.hp}.")
            log("    Ghostbloom glows brighter for an hour and is insufferable.")
        elif dot == 'boon':
            log(f"  Move {roll}: MOSS, odd. THE SHORTCUT: something small and "
                "yellow-brown digs a tunnel exactly the right way. Advance 3.")
            pos += 3
            if pos >= len(seq):
                log("    The shortcut opens right onto the stop ahead.")
                break
        elif dot == 'haz' and even:
            log(f"  Move {roll}: OCHRE, even. SINKLOAM, the floor stops being floor.")
            for h in (st.lilly, st.stabby, st.ursa):
                if not h.alive:
                    continue
                dis = (h is st.lilly)
                r = d20(dis=dis) + h.saves['str']
                if r < 13:
                    log(f"    {h.name} sinks to the waist ({r} vs DC 13) and has "
                        "to be hauled out.")
                else:
                    log(f"    {h.name} keeps to the firm ground ({r} vs DC 13).")
        elif dot == 'haz':
            log(f"  Move {roll}: OCHRE, odd. THE CEILING LETS GO.")
            for h in (st.lilly, st.stabby, st.ursa, st.ghost):
                if not h.alive:
                    continue
                roll_d = d(2, 10)
                ok = st.hero_save(h, 'dex', 14)
                if h in (st.stabby, st.puff) and ok:
                    log(f"    {h.name} flows between the falling stones (Evasion).")
                    continue
                dmg = deal(st, h, [((roll_d // 2) if ok else roll_d, 'bludgeoning')],
                           magical=False)
                log(f"    {h.name} takes {dmg} under the rockfall.")
            log("    The way back is shut. Nobody was going back anyway.")
        elif dot == 'wild' and even:
            log(f"  Move {roll}: AMETHYST, even. THE REEF ANSWERS: the whole "
                "tunnel rings one enormous chord.")
            t = d(2, 8)
            for h in st.pcs:
                if not h.down:
                    h.temp = max(h.temp, t)
            log(f"    Everyone gains {t} temporary hit points. Ghostbloom sings "
                "back, badly, at the top of her voice.")
        else:
            log(f"  Move {roll}: AMETHYST, odd. THE GUARDIAN'S DREAM: an empty "
                "sea, and something patient walking through it, making land.")
            if len(st.u_omens) < 2:
                new = d20()
                st.u_omens.append(new)
                st.u_omens.sort(reverse=True)
                log(f"    Something spoke to Ursa: he regains a spent omen ({new}).")
            else:
                log("    Ursa holds both his omens already; the dream just stays "
                    "with him.")


def aura_of_vitality_walk(st, last_chance=False):
    """Ursa burns the free Aura of Vitality on the road: ten ticks of 2d6.
    He holds it until the party is actually hurt, because it is 1/long rest."""
    if not st.u_aura or st.ursa.down:
        return
    pool = [h for h in (st.lilly, st.stabby, st.ursa, st.ghost) if h.alive]
    if not pool:
        return
    frac = sum(h.hp for h in pool) / sum(h.hp_max for h in pool)
    # It is free and it does not carry to tomorrow, so the only real question is
    # whether a better moment is still coming. Before the Hollow, there is not.
    if frac > (0.95 if last_chance else 0.72):
        return
    st.u_aura = False
    total = 0
    for _ in range(10):             # 1 minute of concentration on the walk
        hurt = [h for h in pool if h.hp < h.hp_max]
        if not hurt:
            break
        t = min(hurt, key=lambda h: h.hp / h.hp_max)
        heal = d(2, 6)
        before = t.hp
        t.hp = min(t.hp_max, t.hp + heal)
        total += t.hp - before
    log(f"  Ursa spends the walk on AURA OF VITALITY from Ash's Sigil-Stone "
        f"(free, 1/long rest): {total} hit points back across the party.")


def revive_between(st):
    """Post-fight triage on the road: nobody walks on at 0."""
    st.conc = None      # a 1-minute spell does not survive the walk
    st.pack = None
    for _h in st.pcs:
        _h.restrained = False
    st.u_starry = False  # Starry Form runs 10 minutes, not all day
    if FEY_HOUR == 'onefight' and st.fey is not None:
        log("  (The hour runs out on the road: the fey spirit bows and goes.)")
        st.fey = None
    for h in [st.lilly, st.stabby, st.ursa, st.ghost]:
        if h.down:
            amt = d(2, 4) + 5
            if st.u_slots[1] > 0 and not st.ursa.down:
                st.u_slots[1] -= 1
            h.hp = min(h.hp_max, max(h.hp + amt, 8))
            h.down = False
            log(f"  (Between fights, {h.name} is patched back up to {h.hp} HP.)")
    aura_of_vitality_walk(st)


def spike_breaker():
    try:
        i = LOG.index("      The Spike is destroyed.")
    except ValueError:
        return None
    for j in range(i - 1, -1, -1):
        ln = LOG[j]
        if ln.startswith('    ') and not ln.startswith('      ') and ':' in ln:
            return ln.strip().split(':')[0].split(' (')[0]
    return None


def run_day(seed):
    global rng
    rng = random.Random(seed)
    LOG.clear()
    st = State()
    log(f"Ursa's Omen Dreams for the day: {st.u_omens}")
    stats = {}

    def dcount():
        return sum(h.drops for h in [st.lilly, st.stabby, st.ursa, st.ghost])

    def hp_pct():
        return 100.0 * sum(h.hp for h in st.heroes) / sum(
            h.hp_max for h in st.heroes)
    stats['road_rounds'] = 0
    road_walk(st, 0, stats)
    stats['f1'] = fight1(st)
    stats['drops_f1'] = dcount()
    stats['hp_f1'] = hp_pct()
    if not any(h.alive for h in st.heroes):
        stats['wipe'] = 'f1'
        return st, stats
    revive_between(st)
    # walk to the reef: fey persists (< 1 hr)
    road_walk(st, 1, stats)
    stats['f2'] = fight2(st)
    stats['drops_f2'] = dcount() - stats['drops_f1']
    stats['hp_f2'] = hp_pct()
    if not any(h.alive for h in st.heroes):
        stats['wipe'] = 'f2'
        return st, stats
    revive_between(st)
    short_rest(st)
    road_walk(st, 2, stats)
    stats['f3'] = fight3(st)
    stats['drops_f3'] = dcount() - stats['drops_f1'] - stats['drops_f2']
    stats['hp_f3'] = hp_pct()
    if not any(h.alive for h in st.heroes):
        stats['wipe'] = 'f3'
        return st, stats
    revive_between(st)
    aura_of_vitality_walk(st, last_chance=True)
    road_walk(st, 3, stats)
    stats['boss'] = boss(st)
    stats['drops_boss'] = dcount() - stats['drops_f1'] - stats['drops_f2'] \
        - stats['drops_f3']
    stats['hp_boss'] = hp_pct()
    if not any(h.alive for h in st.heroes):
        stats['wipe'] = 'boss'
    stats['spike_ok'] = getattr(st, 'spike_ok', False)
    stats['breaker'] = spike_breaker()
    stats['drops'] = sum(h.drops for h in [st.lilly, st.stabby, st.ursa, st.ghost])
    stats['fog'] = 5 - st.l_fog
    stats['omen'] = st.omens_spent
    stats['cosmic'] = st.cosmic_spent
    stats['resurge'] = st.resurgences
    stats['wild_left'] = st.u_wild
    stats['slot2_left'] = st.u_slots[2]
    stats['tally'] = st.tally
    return st, stats


def print_tally(tally, runs=1, header='CHARACTER CONTRIBUTIONS'):
    dealt = tally['dealt']
    total = sum(dealt.values()) or 1
    print(header + (f' (mean per run over {runs} runs)' if runs > 1 else ''))
    order = ['Stabby', 'Lilly', 'Cannon', 'Puff', 'Ursa', 'Fey spirit', 'Ghostbloom']
    for k in order + [k for k in dealt if k not in order]:
        if k not in dealt:
            continue
        print(f"  {k:12s} dealt {dealt[k] / runs:6.1f}  ({100 * dealt[k] / total:4.1f}%)"
              f"   kills {tally['kills'].get(k, 0) / runs:4.1f}")
    print("  damage taken: " + ', '.join(
        f"{k} {v / runs:.1f}" for k, v in tally['taken'].most_common()))
    print("  healing given: " + (', '.join(
        f"{k} {v / runs:.1f}" for k, v in tally['healed'].most_common()) or 'none'))
    print("  prevented: " + (', '.join(
        f"{k} {v / runs:.1f}" for k, v in tally['prevented'].most_common()) or 'none'))
    print()
    print('  BY PLAYER SEAT (a summon or construct counts for whoever fields it)')
    seats = [
        ('Stabby', ['Stabby']),
        ('Lilly + cannon + Puff', ['Lilly', 'Cannon', 'Puff']),
        ('Ursa + fey spirit', ['Ursa', 'Fey spirit']),
        ('Ghostbloom (DM companion)', ['Ghostbloom']),
    ]
    for label, members in seats:
        dd = sum(dealt.get(mname, 0) for mname in members)
        kk = sum(tally['kills'].get(mname, 0) for mname in members)
        tk = sum(tally['taken'].get(mname, 0) for mname in members)
        print(f"  {label:30s} dealt {dd / runs:6.1f} ({100 * dd / total:4.1f}%)"
              f"  kills {kk / runs:5.1f}  taken {tk / runs:5.1f}")


def sweep(seeds=range(1, 21)):
    global HPX, SPIKE_HP, SPIKE_REKNIT, BODIES, GHOST_SUPPORT, NICHIRIN_RING, SHINE
    base = (HPX, SPIKE_HP, SPIKE_REKNIT, BODIES, GHOST_SUPPORT, NICHIRIN_RING, SHINE)
    configs = [
        ('baseline (retuned doc: 8/8, 4/4, W170, re-knit)', {}),
        ('no re-knit (what the rule buys)', {'SPIKE_REKNIT': False}),
        ('doc "too easy" dials on', {'BODIES': True}),
        ('Ghostbloom support-only (no attacks)', {'GHOST_SUPPORT': True}),
        ('enemy HP x1.25 on top', {'HPX': 1.25}),
        ('spike 110 for reference', {'SPIKE_HP': 110}),
        ('FoG + omen shine pack', {'SHINE': True}),
    ]
    hdr = f"{'config':46s} {'F1':>4} {'F2':>4} {'F3':>4} {'Boss':>4} {'drops':>5} {'wipe':>4} {'no-brk':>6}  spike broken by"
    print(hdr)
    print('-' * len(hdr))
    for label, kv in configs:
        HPX, SPIKE_HP, SPIKE_REKNIT, BODIES, GHOST_SUPPORT, NICHIRIN_RING, SHINE = base
        for k, v in kv.items():
            globals()[k] = v
        rows = []
        for s in seeds:
            _, stats = run_day(s)
            rows.append(stats)

        def m(key):
            vals = [r[key] for r in rows if key in r]
            return sum(vals) / len(vals) if vals else 0.0
        wipes = sum(1 for r in rows if r.get('wipe'))
        nobrk = sum(1 for r in rows if r.get('spike_ok') is False)
        brk = Counter(r['breaker'] for r in rows if r.get('breaker'))
        who = ', '.join(f"{k} {v}" for k, v in brk.most_common())
        dd = (f"[{m('drops_f1'):.1f}/{m('drops_f2'):.1f}/"
              f"{m('drops_f3'):.1f}/{m('drops_boss'):.1f}]")
        print(f"{label:46s} {m('f1'):4.1f} {m('f2'):4.1f} {m('f3'):4.1f} "
              f"{m('boss'):4.1f} {m('drops'):5.2f} {dd} {wipes:4d} {nobrk:6d}  {who}")
        ev = Counter()
        for r in rows:
            ev.update(r.get('events', []))
        evname = {('enc', True): 'Thumpaw', ('enc', False): 'Gleamoth',
                  ('boon', True): 'Spring', ('boon', False): 'Shortcut',
                  ('haz', True): 'Sinkloam', ('haz', False): 'Ceiling',
                  ('wild', True): 'ReefAnswers', ('wild', False): 'Dream'}
        n_ev = sum(ev.values())
        tally = ', '.join(f"{evname[k]} {v}" for k, v in ev.most_common())
        print(f"{'':46s} road: {n_ev / max(1, len(rows)):.1f} events/run, "
              f"{m('road_rounds'):.1f} extra rounds/run ({tally})")
        print(f"{'':46s} shine: Flash of Genius {m('fog'):.1f}/day, dreamed "
              f"omens {m('omen'):.1f}/day, Cosmic Omens {m('cosmic'):.1f}/day")
        print(f"{'':46s} Ursa: Wild Resurgence {m('resurge'):.1f} swaps/day, "
              f"ends on {m('wild_left'):.1f} Wild Shape and "
              f"{m('slot2_left'):.1f}/3 second-level slots")
        print(f"{'':46s} hero HP pool left after each fight: "
              f"{m('hp_f1'):.0f}% / {m('hp_f2'):.0f}% / {m('hp_f3'):.0f}% / "
              f"{m('hp_boss'):.0f}%")
        if label.startswith('baseline'):
            agg = {'dealt': Counter(), 'taken': Counter(), 'healed': Counter(),
                   'kills': Counter(), 'prevented': Counter()}
            for r in rows:
                for key in agg:
                    agg[key].update(r['tally'][key])
            print()
            print_tally(agg, runs=len(rows))
            print()
    HPX, SPIKE_HP, SPIKE_REKNIT, BODIES, GHOST_SUPPORT, NICHIRIN_RING, SHINE = base


if __name__ == '__main__':
    if '--sweep' in sys.argv:
        sweep()
    else:
        _, stats = run_day(SEED)
        print('\n'.join(LOG))
        print()
        print_tally(stats['tally'])
        print(f"  shine: Flash of Genius {stats['fog']}, dreamed omens "
              f"{stats['omen']}, Cosmic Omens {stats['cosmic']}")
