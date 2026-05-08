#!/usr/bin/env python3
"""
Add article entries to LOCAL_ARTICLES in index.html.
Avoids reading the full 300-line index.html into agent context.

Usage:
  python tools/add_to_index.py 21
  python tools/add_to_index.py 21 22 23
"""
import re, sys
from pathlib import Path

INDEX = Path(__file__).parent.parent / "index.html"


def add_articles(nums: list[int]):
    content = INDEX.read_text(encoding="utf-8")

    added = []
    for num in sorted(nums):
        entry_key = f"{num}:"
        if entry_key in content:
            print(f"  SKIP {num} (already in LOCAL_ARTICLES)")
            continue
        entry = f"  {num}:'./articles/article_{num:03d}.html',"
        # Insert before the closing }; of LOCAL_ARTICLES
        content = re.sub(r"(\n\};)", f"\n{entry}\\1", content, count=1)
        added.append(num)
        print(f"  ADD  {num}")

    if added:
        INDEX.write_text(content, encoding="utf-8")
        print(f"Updated index.html: added {added}")
    else:
        print("No changes made.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: add_to_index.py <num> [num2 ...]")
        sys.exit(1)
    nums = [int(x) for x in sys.argv[1:]]
    add_articles(nums)
