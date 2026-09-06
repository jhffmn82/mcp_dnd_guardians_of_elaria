# s9_build_queue.py
# Turns the reconciled Session 9 art list (art_review/_s9_art_list.txt, one
# entry per blank-line-separated paragraph) into the runnable queue that
# templates/s9_art_queue.py holds and templates/batch_art_s9.py consumes.
#
# Each source entry already reads as a visual description, so the work here is
# slugging, deduping against what has already been generated, and deciding
# which character reference images to attach.
#
# Run: python templates/s9_build_queue.py
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SRC = "art_review/_s9_art_list.txt"
OUT = "templates/s9_art_queue.py"

# Entries already generated in the first locked batch, matched by slug.
DONE = {
    "s9_frontispiece", "s9_the_crossing", "s9_the_dive", "s9_aelwyn_and_the_reed",
    "s9_loc_brightshoal", "s9_loc_kelp_cathedral", "s9_loc_blackwater_seam",
    "s9_loc_guardians_trench",
}

# Piplup already has approved art at assets/companions/piplup.png.
SKIP_SLUGS = {"mon_piplup"}

# The auto-detector attaches a reference for every hero it sees named anywhere
# in the sentence, which over-attaches on plates where only one hero is in
# frame or where the mention is incidental ("the way the party came").
REF_OVERRIDE = {
    # No people in frame: sand, a cask, two Choristers.
    "s9_the_combed_sand": [],
    "s9_the_blackcask_comes_up": [],
    # One hero in frame, so only that hero's reference.
    "s9_two_sockets_lit": ["lilly"],
    "s9_the_first_freed_chorister": ["stabby"],
    "s9_the_notched_fin_chorister_comes_down": ["ursa"],
    # Heroes described by species or by pronoun rather than by name, which the
    # detector cannot see. Every one of these needs its reference or the plate
    # comes back off-model.
    "s9_the_bells": ["stabby"],                                    # "a goblin's bare hand"
    "s9_the_columns_turn_around": ["lilly", "stabby", "ursa"],     # "the party turning to look up"
    "s9_fomalhaut_and_who_is_looking": ["lilly", "stabby", "ursa"],  # "a gnome and a goblin"
    "s9_the_bell_buckles": ["lilly", "stabby"],                    # "one small figure with her hands up"
}

# Words that mean a person is in the shot even though no hero is named. The
# detector cannot tell WHICH hero from these, so they only raise a warning;
# the answer belongs in REF_OVERRIDE above.
PEOPLE_WORDS = ("a goblin", "a gnome", "the party", "small figure", "figures",
                "the druid", "the boy", "her hands", "his hands", "on him")

# Source lines that are instructions rather than plates.
SKIP_MARKERS = ("already exists and must NOT be respun",)

# Title -> slug overrides, where the generated slug would be ugly or would
# collide with something already in the repo.
SLUG = {
    "THE CROSSING": "s9_the_crossing",
    "THE DIVE": "s9_the_dive",
    "THE BRIGHTSHOAL, ARRIVAL": "s9_loc_brightshoal",
    "THE KELP CATHEDRAL": "s9_loc_kelp_cathedral",
    "THE BLACKWATER SEAM": "s9_loc_blackwater_seam",
    "THE GUARDIAN'S TRENCH": "s9_loc_guardians_trench",
    "THE CORNER TABLE": "s9_aelwyn_corner_table",
}

# Which reference sets to attach, keyed on words appearing in the entry.
# Monster portraits deliberately get NO references: they are new designs.
HERO_WORDS = ("the party", "three small figures", "three tiny figures",
              "the three", "lilly", "stabby", "ursa")


def slugify(title):
    if title in SLUG:
        return SLUG[title]
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    s = re.sub(r"^(monster_card_portrait|companion_card_portrait)_", "mon_", s)
    return "s9_" + s if not s.startswith("mon_") else s


def parse():
    raw = io.open(SRC, encoding="utf-8").read()
    out = []
    for para in [p.strip() for p in raw.split("\n\n") if p.strip()]:
        if any(m in para for m in SKIP_MARKERS):
            continue
        # "TITLE (parenthetical): body"  or  "Monster card portrait: Name, body"
        m = re.match(r"^(Monster card portrait|Companion card portrait):\s*(.+?)[,:]\s*(.+)$",
                     para, re.S)
        if m:
            name = m.group(2).strip().strip(".")
            name = re.sub(r"\s*\(.*?\)\s*", " ", name).strip()
            title = "Monster card portrait " + name
            body = m.group(3).strip()
            # strip a trailing editorial aside, e.g. "Chimewisp (RENAMED from ...)"
            body = re.sub(r"^RENAMED[^)]*\)\s*:?\s*", "", body).strip()
            name = name.split("(")[0].strip()
            slug = "mon_" + re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")
            out.append((slug, title, body, True))
            continue
        m = re.match(r"^([A-Z][A-Z'’,\- ]+?)\s*(?:\(([^)]*)\))?\s*:\s*(.+)$", para, re.S)
        if not m:
            print("  UNPARSED:", para[:90])
            continue
        title = m.group(1).strip().rstrip(",")
        note = (m.group(2) or "").strip()
        body = m.group(3).strip()
        out.append((slugify(title), title, body, False))
    return out


def refs_for(body, is_monster):
    if is_monster:
        return []
    low = body.lower()
    toks = []
    if any(w in low for w in HERO_WORDS):
        toks = ["lilly", "stabby", "ursa"]
    else:
        for h in ("lilly", "stabby", "ursa"):
            if h in low:
                toks.append(h)
    if "pangolin" in low or "sandshrew" in low:
        toks.append("sandshrew")
    if "aelwyn" in low or "scholar" in low or "professor" in low:
        toks.append("aelwyn")
    if "piplup" in low:
        toks.append("piplup")
    return toks


if __name__ == "__main__":
    items = parse()
    lines = [
        "# s9_art_queue.py",
        "# GENERATED by templates/s9_build_queue.py from the reconciled Session 9 art",
        "# list. Every entry lands in art_review/PENDING_<name>.png for DM approval;",
        "# nothing moves into assets/ until he approves it.",
        "#   (name, [reference tokens], scene line)",
        "QUEUE = [",
    ]
    n_new = 0
    for slug, title, body, is_mon in items:
        if slug in DONE or slug in SKIP_SLUGS:
            continue
        n_new += 1
        toks = REF_OVERRIDE.get(slug, refs_for(body, is_mon))
        scene = body.replace('"', "'").replace("\n", " ")
        scene = re.sub(r"\s+", " ", scene)
        lines.append(f'    ({slug!r}, {toks!r},')
        lines.append(f'     "Scene: {scene}"),')
    lines.append("]")
    io.open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")

    # Guard: a plate with a person in it and no character reference comes back
    # off-model, and that is the single most expensive kind of miss here.
    unref = []
    for slug, title, body, is_mon in items:
        if slug in DONE or slug in SKIP_SLUGS or is_mon:
            continue
        toks = REF_OVERRIDE.get(slug, refs_for(body, is_mon))
        if toks:
            continue
        low = body.lower()
        if any(w in low for w in PEOPLE_WORDS):
            unref.append(slug)
    if unref:
        print("\nWARNING: people in frame with no reference art attached.")
        print("Add each to REF_OVERRIDE naming the heroes actually shown:")
        for s in unref:
            print("   ", s)
    print(f"parsed {len(items)} entries, {n_new} new (skipped {len(items)-n_new} already generated)")
    print("wrote", OUT)
