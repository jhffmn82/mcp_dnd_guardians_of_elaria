# approve_art.py
# Bank approved plates from the review board. The DM approves by LETTER, using
# the codes printed on art_review/review.html (and on the published Artifact),
# so this reads the letter map written alongside the board and moves only what
# he named.
#
# Nothing here decides anything: approval is the DM's, and a plate stays in
# art_review/ until he says a letter out loud.
#
#   python templates/approve_art.py A B C
#   python templates/approve_art.py --list
import io, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
RD = "art_review"
MAP = os.path.join(RD, "_letter_map.json")
MANIFEST = "assets/image_manifest.md"


def dest_for(stem):
    """Where an approved plate is banked, by name prefix."""
    if stem.startswith("s9_"):
        return os.path.join("assets/session_09", stem + ".png")
    if stem.startswith("S8mon_"):
        return os.path.join("assets/monsters", stem[len("S8"):] + ".png")
    if stem.startswith("S8_"):
        return os.path.join("assets/session_08", stem[len("S8_"):] + ".png")
    if stem.startswith("mon_"):
        return os.path.join("assets/monsters", stem + ".png")
    return os.path.join("assets/session_09", stem + ".png")


def load_map():
    if not os.path.exists(MAP):
        sys.exit("no letter map; rebuild the board first (review_gallery.build())")
    return json.load(io.open(MAP, encoding="utf-8"))


def main(letters):
    m = load_map()
    if not letters:
        for c in sorted(m, key=lambda s: (len(s), s)):
            print(f"  {c:>3}  {m[c]}")
        return

    moved, missing = [], []
    for raw in letters:
        c = raw.strip().upper().rstrip(",")
        label = m.get(c)
        if not label:
            missing.append(c)
            continue
        stem = label.replace(" ", "_")
        src = os.path.join(RD, f"PENDING_{stem}.png")
        if not os.path.exists(src):
            missing.append(f"{c} ({stem}: no pending file)")
            continue
        dst = dest_for(stem)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.move(src, dst)
        moved.append((c, stem, dst))

    if moved:
        prompts = "assets/gen_prompts"
        with io.open(MANIFEST, "a", encoding="utf-8") as f:
            for c, stem, dst in moved:
                p = os.path.join(prompts, stem + ".txt")
                pref = p.replace("\\", "/") if os.path.exists(p) else "(prompt not recorded)"
                f.write(f"| `{dst.replace(os.sep, '/')}` (DM-approved as **{c}**) | `{pref}` |\n")
        print(f"BANKED {len(moved)}:")
        for c, stem, dst in moved:
            print(f"   {c}  {stem}  ->  {dst}")
        print(f"\nAppended {len(moved)} row(s) to {MANIFEST}.")
    if missing:
        print("\nNOT FOUND:", ", ".join(missing))


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--list"]
    main(args)
