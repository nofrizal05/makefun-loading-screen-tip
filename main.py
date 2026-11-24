"""Loading Screen Gold: one tip in at most 200 characters.

Writes the tip to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt),
as a single line of UTF-8 with no trailing newline.
"""

import os

TIP = (
    "Tip: walking beats respawning. Sprint past a ledge and you will spend "
    "longer staring at the death screen than the shortcut ever saved \u2014 "
    "and yes, the loading bar is judging you."
)


def main() -> None:
    tip = TIP.strip()
    assert len(tip) <= 200, f"tip is {len(tip)} characters, over the 200 limit"
    assert "\n" not in tip, "tip must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(tip)


if __name__ == "__main__":
    main()
