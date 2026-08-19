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
SPIKE_HP = int(os.environ.get('S8_SPIKE_HP', '60'))
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
URSA_LINE = os.environ.get('S8_URSA_LINE', 'control')
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
        self.ghost = Actor('Ghostbloom', 'G', 'pc', 16, 62, (0, 0), 30, init_mod=4,
                           saves=dict(str=-1, dex=8, con=8, int=1, wis=6, cha=3),
                           resist={'necrotic', 'nm-bludgeoning', 'nm-piercing', 'nm-slashing'},
                           vuln={'fire', 'cold'},
                           cond_imm={'charmed', 'frightened'}, reach=15, fly=True)
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
        self.g_wail = True
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
    if tgt.temp and total > 0:
        ab = min(tgt.temp, total)
        tgt.temp -= ab
        total -= ab
        if ab:
            log(f"      * {tgt.name}'s ward soaks {ab}.")
    pre = tgt.hp
    tgt.hp -= total
    tgt.damaged_since = True
    if any(t in ('radiant', 'force') for _, t in parts) or is_ce:
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
    # Guardian's Light: reaction heal when a hero is hurt
    if tgt.side == 'pc' and total > 0 and tgt is not st.ghost and st.g_light > 0 \
            and st.ghost.alive and st.ghost.dist_ft(tgt) <= 30 \
            and (tgt.down or tgt.hp < tgt.hp_max * 0.4) and st.ghost.reaction:
        st.g_light -= 1
        st.ghost.reaction = False
        h = d(2, 8) + 3
        st.tally['healed']['Ghostbloom'] += h
        was_down = tgt.down
        tgt.hp = min(tgt.hp_max, tgt.hp + h)
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
    if getattr(tgt, 'entangled', 0) > 0:
        adv = True
    if attacker is not None and getattr(attacker, 'entangled', 0) > 0:
        dis = True
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
    # Lilly's Shield reaction
    if tgt is st.lilly and tgt.reaction and st.l_slot1 > 0 and not crit \
            and tgt.ac <= total < tgt.ac + 5:
        st.l_slot1 -= 1
        tgt.reaction = False
        log(f"      * Shield! Lilly flicks the attack aside ({total} vs AC 25). "
            f"[{st.l_slot1} first-level slots left]")
        return False, False, r
    return (total >= tgt.ac or crit), crit, r


def ursa_starry(st, again=False):
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


def ghost_lash(st, targets):
    g = st.ghost
    ts = [t for t in targets if t.hp > 0]
    if not ts:
        return
    for _ in range(2):
        ts = [t for t in targets if t.hp > 0]
        if not ts:
            return
        t = ts[0]
        if g.dist_ft(t) > 15:
            g.approach(t, 15, 30)
        if g.dist_ft(t) > 15:
            log(f"    Ghostbloom: drifts toward {t.name}.")
            return
        hit, crit, _ = attack_roll(st, 8, t, attacker=g)
        if hit:
            parts = [(d(2 if crit else 1, 8) + 6, 'slashing'), (d(1, 6), 'necrotic')]
            dmg = deal(st, t, parts, magical=False, attacker=g, credit='Ghostbloom')
            note = ''
            if 'frightened' not in t.cond_imm and not foe_save(t, t.saves.get('wis', 0), 16):
                t.fright = 2
                note = ' It recoils, frightened!'
            log(f"    Ghostbloom: spectral lash hits {t.name} for {dmg}.{note}")
            if t.hp <= 0:
                log(f"      {t.name} is destroyed.")
        else:
            log(f"    Ghostbloom: lash misses {t.name}.")


def summon_fey(st, pos=(9, 15)):
    """Summon Fey. 3rd: AC 15, HP 30, 2d6+6, one attack. Cast with a 4th-level
    slot (build_ursa.py:211-212): AC 16, HP 40, 2d6+7, and TWO attacks a turn."""
    lvl = 4 if (URSA_LINE == 'summon4' and st.u_slots[4] > 0) else 3
    if st.u_slots[lvl] <= 0:
        lvl = 3
        if st.u_slots[3] <= 0:
            return False
    st.u_slots[lvl] -= 1
    ac, hp = (16, 40) if lvl == 4 else (15, 30)
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
        st.conc = None
    elif st.fey is not None:
        log(f"      * Ursa loses concentration (DC {dc}): the fey spirit fades!")
        st.conc_lost += 1
        st.fey.hp = 0
        st.fey = None


def ursa_damage_line(st, targets, bonus_used):
    """The simple line: keep the summon up, then Guiding Bolt while the free
    Star Map casts last, then Starry Wisp forever."""
    live = [t for t in targets if t.hp > 0]
    if (st.fey is None or st.fey.hp <= 0) and st.u_slots[3] > 0:
        summon_fey(st, pos=tuple(st.ursa.pos))
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
        return
    if not ursa_close(st, target):
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
    mite_spots = [(15, 13), (16, 15), (15, 17), (17, 14), (16, 18), (17, 16),
                  (16, 12), (16, 19)]
    if BODIES:
        mite_spots += [(15, 14), (17, 18)]
    rots = []
    for i, p in enumerate(rot_spots):
        rots.append(Actor(f'Rotbloom-{i+1}', 'R', 'foe', 12, ehp(33), p, 25,
                          saves=dict(str=0, dex=1, con=2, wis=-1),
                          resist={'poison'}, cond_imm={'frightened'}))
    mites = []
    for i, p in enumerate(mite_spots):
        m = Actor(f'Mossmite-{i+1}', 'm', 'foe', 13, ehp(7), p, 40,
                  saves=dict(dex=3, con=1, wis=0))
        m.hidden = True
        mites.append(m)
    foes = rots + mites

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
    log("(The eight Mossmites are burrowed in the mid-field moss around x15-17 and")
    log(" boil out the moment the first Rotbloom is struck.)")

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
                bonus_used = ursa_triage(st)
                live_r = sorted([r for r in rots if r.hp > 0],
                                key=lambda r: st.ursa.dist_ft(r))
                live_m = [m for m in mites if m.hp > 0 and not m.hidden]
                if rnd == 1 and URSA_LINE != 'control':
                    if st.fey is None or st.fey.hp <= 0:
                        summon_fey(st)
                    if not bonus_used and ursa_starry(st):
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
                    if not bonus_used and ursa_starry(st):
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
                    summon_fey(st)
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
            elif name == 'Ghostbloom' and st.ghost.alive:
                if GHOST_SUPPORT:
                    log("    Ghostbloom: hangs back on triage, petals ready.")
                else:
                    gts = sorted([f for f in foes if f.hp > 0
                                  and not getattr(f, 'hidden', False)],
                                 key=lambda f: st.ghost.dist_ft(f))
                    ghost_lash(st, gts)
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
                             and h.hp < h.hp_max * 0.45
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
                bonus_used = ursa_triage(st)
                if rnd == 1 and not bonus_used and ursa_starry(st, again=True):
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
                    st.conc = 'the Entangle'
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
            elif name == 'Ghostbloom' and st.ghost.alive:
                if GHOST_SUPPORT:
                    log("    Ghostbloom: hangs back on triage, petals ready.")
                else:
                    gts = sorted([f for f in foes if f.hp > 0],
                                 key=lambda f: (f.aloft, not f.stunned,
                                                st.ghost.dist_ft(f)))
                    ghost_lash(st, gts)
            elif name == 'Shardwings':
                for wi, w in enumerate(wings):
                    if w.hp <= 0:
                        continue
                    if w.fright > 0:
                        w.fright -= 1
                    # They punish everyone, not just the front line: each wing
                    # picks its own hero and keeps the whole party moving.
                    marks = [h for h in st.pcs if h.alive]
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
    weeper = Actor('Glass Weeper', 'W', 'foe', 16, ehp(170), (15, 11), 20,
                   saves=dict(str=4, dex=-1, con=5, wis=1),
                   resist={'nm-bludgeoning', 'nm-piercing', 'nm-slashing'},
                   immune={'poison'},
                   cond_imm={'charmed', 'frightened', 'poisoned', 'prone'},
                   reach=15)
    roll_spots = [(27, 12), (27, 16), (28, 10), (28, 18)]
    rolls = [Actor(f'Cinderoll-{i+1}', 'o', 'foe', 15, ehp(18), p, 40,
                   saves=dict(str=1, dex=2, con=1, wis=-1),
                   immune={'fire', 'poison'},
                   cond_imm={'blinded', 'charmed', 'deafened', 'poisoned'})
             for i, p in enumerate(roll_spots)]
    arrived = rolls[:2]
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
            and any(h.alive for h in st.heroes) and rnd < 14:
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
                if weeper.hp > 0:
                    true_strike(st, weeper, adv=tended)
                elif live_rolls_now:
                    true_strike(st, live_rolls_now[0])
                    if live_rolls_now[0].hp <= 0:
                        burst(live_rolls_now[0])
                hurt_near = [h for h in st.pcs if h.alive
                             and h.hp < h.hp_max * 0.45
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
                bonus_used = ursa_triage(st)
                if rnd == 1 and not bonus_used and ursa_starry(st):
                    bonus_used = True
                if URSA_LINE != 'control':
                    pool = ([weeper] if weeper.hp > 0 else []) + [
                        c for c in arrived if c.hp > 0]
                    ursa_damage_line(st, pool, bonus_used)
                    fey_turn(st, pool)
                    continue
                if rnd == 1 and st.u_staff >= 2 and weeper.hp > 0:
                    st.u_staff -= 2
                    st.conc = 'the Moonbeam'
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
            elif name == 'Ghostbloom' and st.ghost.alive:
                live_rolls = [c for c in arrived if c.hp > 0]
                pack = [c for c in live_rolls if st.ghost.dist_ft(c) <= 15]
                if GHOST_SUPPORT:
                    log("    Ghostbloom: hangs back on triage, petals ready.")
                elif st.g_wail and len(pack) >= 2:
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
                    ghost_lash(st, sorted(live_rolls,
                                          key=lambda c: st.ghost.dist_ft(c)))
                    for c in live_rolls:
                        if c.hp <= 0:
                            burst(c)
                elif weeper.hp > 0:
                    ghost_lash(st, [weeper])
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
                    log("    Glass Weeper: the wounds stay OPEN (force, radiant and "
                        "the Nichirin have burned the glass).")
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
    spike = Actor('The Spike', 'x', 'foe', 17, SPIKE_HP, (14, 6), 0)
    spike.immune = {'slashing', 'bludgeoning', 'piercing', 'fire', 'cold',
                    'thunder', 'lightning', 'poison', 'necrotic', 'psychic',
                    'acid'}
    spike.is_spike = True
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
                bonus_used = ursa_triage(st)
                if rnd == 1 and not bonus_used and ursa_starry(st):
                    bonus_used = True
                if URSA_LINE != 'control':
                    if (st.fey is None or st.fey.hp <= 0) and st.u_slots[3] > 0:
                        summon_fey(st, pos=tuple(st.ursa.pos))
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
            elif name == 'Ghostbloom' and st.ghost.alive:
                lings = sorted([g for g in glasslings if g.hp > 0],
                               key=lambda g: st.ghost.dist_ft(g))
                if GHOST_SUPPORT:
                    log("    Ghostbloom: shields the casters, petals ready.")
                elif lings:
                    ghost_lash(st, lings)
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
                    log("    Ghostbloom: hovers guard over Lilly and Ursa.")
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
                bonus_used = ursa_triage(st)
                if rnd == 1 and not bonus_used:
                    bonus_used = ursa_starry(st)
                starry_wisp(st, tp)
                poked = True
                if not bonus_used and st.u_starry:
                    star_arrow(st, tp)
            elif name == 'Ghostbloom' and st.ghost.alive:
                if GHOST_SUPPORT:
                    log("    Ghostbloom: hangs back on triage, petals ready.")
                else:
                    ghost_lash(st, [tp])
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
                bonus_used = ursa_triage(st)
                if rnd == 1 and not bonus_used:
                    bonus_used = ursa_starry(st)
                t = next((sw for sw in swarms if sw.hp > 0), None)
                if t is not None:
                    starry_wisp(st, t)
                if not bonus_used and st.u_starry:
                    star_arrow(st, next((sw for sw in swarms if sw.hp > 0), None))
            elif name == 'Ghostbloom' and st.ghost.alive:
                if GHOST_SUPPORT:
                    log("    Ghostbloom: hangs back on triage, petals ready.")
                else:
                    ghost_lash(st, [s for s in swarms if s.hp > 0])
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


def revive_between(st):
    """Post-fight triage on the road: nobody walks on at 0."""
    st.conc = None      # a 1-minute spell does not survive the walk
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
