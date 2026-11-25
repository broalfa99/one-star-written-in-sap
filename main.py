#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes the one-line 1-star review from a houseplant to
/output/entry.txt. The competition gate requires UTF-8 text of
1-279 characters, not only whitespace, so the program refuses to
write anything outside that gate.

The line: a plant misnamed Fern watches its owner water the
succulent beside it, then wonders why it droops — grievance,
plant's-eye detail (succulent, tag, droop) and a twist ending.
132 characters, one line.
"""

import os

LINE = (
    "One star: she named me Fern, waters the succulent beside me, "
    "and wonders why I droop. I am not Fern. I never was Fern. "
    "Read the tag."
)


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 279:
        raise SystemExit(f"entry must be 1-279 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    # The grader sandbox provides /output, but create it when it is
    # missing so the program also runs cleanly anywhere else.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Round-trip check: what the grader reads must be exactly this line.
    back = open("/output/entry.txt", encoding="utf-8").read().rstrip("\n")
    if back != line:
        raise SystemExit("round-trip mismatch")
    print(f"wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
