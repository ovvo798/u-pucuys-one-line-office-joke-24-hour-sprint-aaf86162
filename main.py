#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes a single-line joke about office life (at most 200 characters)
to /output/entry.txt.
"""

import os

JOKE = (
    "The meeting that should have been an email just spawned a follow-up "
    "meeting, a recap email, and a calendar invite to discuss the recap."
)


def main() -> None:
    text = JOKE.strip()
    assert text, "joke must not be blank"
    assert "\n" not in text, "joke must be a single line"
    assert 1 <= len(text) <= 200, f"joke must be 1-200 characters, got {len(text)}"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
