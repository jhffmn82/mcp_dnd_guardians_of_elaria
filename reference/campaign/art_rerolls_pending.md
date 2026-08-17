# Session 8 art: queued re-rolls

Blocked 2026-08-17 on `credit_balance_exhausted`. Every prompt below is written
and committed. Add API credits and run these from the repo root, in order.

Lickgloom has no reference image yet, so **build his first**: plates B and any
future scene with him need it.

```bash
# 1. Lickgloom's canonical reference (must come first)
GENART_SIZE=1024x1024 python templates/genart.py \
  assets/art_refs/REF_lickgloom.png assets/gen_prompts/REF_lickgloom.txt

# 2. B: Aelwyn arrives, now with Lickgloom on the luggage and no assistant
GENART_SIZE=1536x1024 python templates/genart.py \
  art_review/PENDING_S8_B_aelwyn_arrives.png assets/gen_prompts/s8_B_aelwyn_arrives.txt \
  assets/art_refs/REF_aelwyn.webp assets/art_refs/REF_lickgloom.png

# 3. I: the briefing, correct Ghostbloom, Puff added, no assistant
GENART_SIZE=1536x1024 python templates/genart.py \
  art_review/PENDING_S8_I_aelwyns_briefing.png assets/gen_prompts/s8_I_the_briefing.txt \
  assets/art_refs/REF_ghostbloom.png assets/art_refs/REF_aelwyn.webp \
  assets/art_refs/REF_vane.png assets/art_refs/REF_homunculus.png

# 4. Q: the purge, correct two-handed grip and edge orientation
GENART_SIZE=1536x1024 python templates/genart.py \
  art_review/PENDING_S8_Q_the_purge.png assets/gen_prompts/s8_S3_the_purge.txt \
  assets/art_refs/REF_stabby_4_level7.png assets/items/nichirin_katana.png

# 5. J: in-place edit, fix Lilly's malformed goggles only
GENART_SIZE=1536x1024 python templates/genart.py \
  art_review/PENDING_S8_J_the_threshold.png assets/gen_prompts/_fix_j_goggles.txt \
  art_review/PENDING_S8_J_the_threshold.png

# 6. rebuild the board
python templates/lettered_board.py
```

## What the DM asked for, plate by plate

| Plate | Verdict | Action |
|---|---|---|
| **B** | creature is wrong, assistant unwanted | Replace with **Lickgloom**, drop Tamsin. Needs the new ref. |
| **I** | Ghostbloom wrong, assistant unwanted | Correct Ghostbloom, drop Tamsin, add Puff to Lilly's shoulder. |
| **Q** | grip wrong | Two hands on the hilt, tip up, glow on the OUTER convex edge. |
| **J** | Ghostbloom fine, Lilly's goggles malformed | **Edit in place**, do not re-roll: Ghostbloom is correct here and worth keeping. |
| **V** | approved as-is | None. |

## Why B and I went wrong

Same failure as the earrings, the Boomstick chamber and the katana grip: **a
vague description in the prompt beats an accurate reference image**. Ghostbloom's
reference was attached to both plates, but the prompt called her "a small
translucent teal fey creature made of soft glowing light," and the generator
followed the words. The rewritten prompts now describe her explicitly as a
four-legged spirit-beast and list what she is NOT.

Add Ghostbloom and Lickgloom to the standing design rules in
`assets/character_refs.md` when the refs land.

## Tamsin

Cut from Session 8 entirely, in art and in text. She remains canon as Aelwyn's
assistant from Session 3; she simply does not travel to Gearhaven. Lickgloom now
rides the luggage and gets the reunion beat instead.
