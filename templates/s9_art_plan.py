# s9_art_plan.py
# The source of truth for Session 9 art: every plate declares WHERE it happens
# and WHO is in it, and the runner turns that into reference images.
#
# This exists because the first pass did neither. 41 of 54 plates went out with
# no character reference at all, so every person in them was a stranger, and
# the monster plates carried no setting, so they came back looking like they
# belonged to another plane. assets/character_refs.md line 12 already warned
# about exactly this ("Describing them in the prompt is not a substitute").
#
# TWO STAGES:
#   1. Generate the LOCATION plates. Nothing else runs until the DM approves
#      them, because everything else uses them as its setting reference.
#   2. Generate every other plate with refs = [its location] + [its people].
#
# The API takes about five reference images per request, so a plate is capped
# at one location plus four characters.

# ---------------------------------------------------------------- locations
# Unda locations are generated in stage 1 and land in assets/session_09/.
# Gearhaven is not a new place: Sessions 7 and 8 already have approved plates
# of these rooms, so those ARE the reference and nothing is regenerated.
LOCATIONS = {
    "brightshoal":      "assets/session_09/s9_loc_brightshoal.png",
    "kelp_cathedral":   "assets/session_09/s9_loc_kelp_cathedral.png",
    "blackwater_seam":  "assets/session_09/s9_loc_blackwater_seam.png",
    "guardians_trench": "assets/session_09/s9_loc_guardians_trench.png",
    "rift_gate":        "assets/session_09/s9_loc_rift_gate.png",
    "open_water":       "assets/session_09/s9_loc_open_water.png",
    # already approved, do not regenerate
    "guild":            "assets/session_07/beat_3/guild_interior.png",
    "tavern":           "assets/session_07/beat_1/tavern.png",
    "rift_hall":        "assets/session_08/A_the_finished_ring.png",
}

STAGE1 = ["brightshoal", "kelp_cathedral", "blackwater_seam",
          "guardians_trench", "rift_gate", "open_water"]

# ------------------------------------------------------------------- people
CHARACTER_REFS = {
    "lilly":     "assets/art_refs/REF_lilly_6_level7.png",
    "stabby":    "assets/art_refs/REF_stabby_4_level7.png",
    "ursa":      "assets/art_refs/REF_ursa_4_level7.png",
    "sandshrew": "assets/characters/sandshrew.png",
    "piplup":    "assets/companions/piplup.png",
    "aelwyn":    "assets/art_refs/REF_aelwyn.webp",
    "puff":      "assets/art_refs/REF_homunculus.png",
}

# ---------------------------------------------------- plate -> (where, who)
PLAN = {
    # cover
    "s9_frontispiece":                       (None, []),

    # the crossing and the road
    "s9_the_crossing":                       ("rift_gate", ["lilly", "stabby", "ursa", "sandshrew"]),
    "s9_the_bells":                          ("brightshoal", ["stabby"]),
    "s9_the_wrong_colour_at_the_far_end":    ("brightshoal", []),
    "s9_road_rail_plate":                    ("brightshoal", []),
    "s9_the_bell_that_went_out":             ("brightshoal", []),
    "s9_the_sounder":                        ("brightshoal", []),
    "s9_the_black_thread":                   ("brightshoal", []),
    "s9_the_smoker":                         ("guardians_trench", []),
    "s9_the_bell_buckles":                   ("kelp_cathedral", ["lilly", "stabby"]),

    # 1 the Brightshoal
    "s9_the_combed_sand":                    ("brightshoal", []),
    "s9_the_herd_hits":                      ("brightshoal", ["lilly", "stabby", "ursa"]),
    "s9_the_blackfroth_arrives":             ("brightshoal", []),

    # 2 the Kelp Cathedral
    "s9_the_notched_fin_chorister_comes_down": ("kelp_cathedral", ["ursa"]),
    "s9_the_columns_turn_around":            ("kelp_cathedral", ["lilly", "stabby", "ursa"]),
    "s9_the_bells_open":                     ("kelp_cathedral", ["lilly"]),

    # 3 the Blackwater Seam
    "s9_the_man_pouring_the_cask":           ("blackwater_seam", []),
    "s9_the_blackcask_comes_up":             ("blackwater_seam", []),
    "s9_the_tanglehands":                    ("blackwater_seam", []),
    "s9_the_notched_fin_surfacing":          ("blackwater_seam", []),
    "s9_the_first_freed_chorister":          ("blackwater_seam", ["stabby"]),
    "s9_the_empty_gallery":                  ("blackwater_seam", []),

    # the dive and 4 the Guardian's Trench
    "s9_the_dive":                           ("open_water", ["lilly", "stabby", "ursa", "sandshrew"]),
    "s9_what_kyogre_dreams":                 ("open_water", []),
    "s9_the_case":                           ("guardians_trench", []),
    "s9_the_kept_rise":                      ("guardians_trench", []),
    "s9_stabby_on_the_whale_s_back":         ("guardians_trench", ["stabby"]),
    "s9_the_hammer_stops":                   ("guardians_trench", []),
    "s9_kyogre_in_colour":                   ("guardians_trench", ["lilly", "stabby", "ursa"]),
    "s9_what_the_guardian_went_and_got":     ("guardians_trench", []),
    "s9_the_road_up":                        ("open_water", ["lilly", "stabby", "ursa"]),

    # Gearhaven: Part One and the homecoming
    "s9_aelwyn_and_the_reed":                ("guild", ["aelwyn", "ursa"]),
    "s9_aelwyn_corner_table":                ("tavern", ["aelwyn", "lilly", "stabby", "ursa"]),
    "s9_fomalhaut_and_who_is_looking":       ("rift_hall", ["lilly", "stabby", "ursa"]),
    "s9_two_sockets_lit":                    ("guild", ["lilly"]),
    "s9_piplup_steps_out_already_walking":   ("guild", ["piplup"]),
    "s9_the_watch":                          ("guild", ["piplup"]),
}

# Monster portraits: the setting reference matters, the cast does not.
MONSTER_LOCATION = {
    "mon_glimmerfin": "brightshoal", "mon_surgehorn": "brightshoal",
    "mon_inkmantle": "brightshoal", "mon_blackfroth": "brightshoal",
    "mon_pillarback": "kelp_cathedral", "mon_needlemaw": "kelp_cathedral",
    "mon_quillfrond": "kelp_cathedral", "mon_gullet_bell": "kelp_cathedral",
    "mon_the_blackcask": "blackwater_seam", "mon_hollowsong": "blackwater_seam",
    "mon_lancefin": "blackwater_seam", "mon_tanglehand": "blackwater_seam",
    "mon_the_notched_fin": "blackwater_seam",
    "mon_kyogre_the_deep_that_holds_the_world": "guardians_trench",
    "mon_the_quiet_hand": "guardians_trench", "mon_brine_thing": "guardians_trench",
    "mon_drownbell": "guardians_trench", "mon_the_kept": "guardians_trench",
    "mon_brinehound": "brightshoal", "mon_ghostbell": "kelp_cathedral",
    "mon_nabber_shoal": "brightshoal", "mon_the_black_thread": "brightshoal",
}


# The approved board map is the plane's colour language: the palette, the light
# and the geography the players will have in front of them all night. Every
# location plate is generated against it so the art and the map agree.
BOARD = "assets/session_09/unda_board.png"


def refs_for_plate(name):
    """Location reference first, then each person in frame. Capped at five."""
    if name.startswith("s9_loc_"):
        # The Rift Gate is the one place in Unda with something built in it, and
        # the party built it: Vane's brass ring, carried through from Gearhaven.
        # Reference the approved Session 8 plate so the ring is the same ring.
        if name == "s9_loc_rift_gate":
            return [BOARD, "assets/session_08/A_the_finished_ring.png"]
        return [BOARD]
    if name in MONSTER_LOCATION:
        where, who = MONSTER_LOCATION[name], []
    elif name in PLAN:
        where, who = PLAN[name]
    else:
        return []
    out = []
    if where:
        out.append(LOCATIONS[where])
    out += [CHARACTER_REFS[c] for c in who if c in CHARACTER_REFS]
    return out[:5]


def banked_path(name):
    """Where an approved plate lives once the DM has signed it off, or None."""
    import os
    for d in ("assets/session_09", "assets/monsters"):
        p = os.path.join(d, name + ".png")
        if os.path.exists(p):
            return p
    return None


def missing_locations():
    """Stage-1 plates that have not been approved into assets/ yet."""
    import os
    return [k for k in STAGE1 if not os.path.exists(LOCATIONS[k])]
