#!/usr/bin/env python3
"""Update slide-titles.md while preserving timing notes and comments."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "slides" / "index.qmd"
OUTPUT = ROOT / "slide-titles.md"
ENTRY_RE = re.compile(r"^## (?P<number>\d+)\. .*?(?=^## \d+\. |\Z)", re.MULTILINE | re.DOTALL)
TITLE_RE = re.compile(r"^## (?P<title>.*?)(?:\s+\{[^{}]*\})?\s*$", re.MULTILINE)


def slide_titles() -> list[str]:
    titles = []
    for line in SOURCE.read_text().splitlines():
        if line.startswith("## "):
            title = re.sub(r"\s+\{[^{}]*\}\s*$", "", line[3:]).strip()
            titles.append(title)
    return titles


def existing_entries() -> dict[int, str]:
    if not OUTPUT.exists():
        return {}
    entries = {}
    for match in ENTRY_RE.finditer(OUTPUT.read_text()):
        entries[int(match.group("number"))] = match.group(0).split("\n", 1)[1]
    return entries


def main() -> None:
    old_text = OUTPUT.read_text() if OUTPUT.exists() else (
        "# Slide timing\n\n"
        "<!-- Add times after `Time:` and comments below each slide. "
        "The generator preserves slide bodies. -->\n\n"
    )
    old_entries = existing_entries()
    preamble = ENTRY_RE.split(old_text, maxsplit=1)[0].rstrip() + "\n\n"

    blocks = []
    for number, title in enumerate(slide_titles(), start=1):
        body = old_entries.get(number, "Time: \n")
        blocks.append(f"## {number}. {title}\n{body.rstrip()}\n")

    OUTPUT.write_text(preamble + "\n".join(blocks).rstrip() + "\n")


if __name__ == "__main__":
    main()
