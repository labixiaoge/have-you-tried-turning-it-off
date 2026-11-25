"""make.fun entry: Have You Tried Turning It Off?

Writes a single funny line, under 200 characters, that a hopeless tech
support agent says to a desperate customer, to /output/entry.txt.
The program ships the line itself: it reads nothing from the network,
no secrets, no git history, only this file.
"""

import os

LINE = (
    "Have you tried turning it off and on again? I just did \u2014 "
    "now neither of us has internet, but at least we are in this together."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def _validate(line: str) -> None:
    # Gate: the line must be 1-199 characters (the competition's entry rule).
    chars = len(line)
    if chars < 1 or chars > 199:
        raise SystemExit(f"entry must be 1-199 characters, got {chars}")
    if line != line.strip():
        raise SystemExit("entry must not start or end with whitespace")


def main() -> None:
    _validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
