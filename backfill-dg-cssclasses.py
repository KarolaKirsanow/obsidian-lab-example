#!/usr/bin/env python3
"""
Backfill cssclasses frontmatter into existing Discourse Graph node files.

Usage:
    python backfill-dg-cssclasses.py           # preview only (dry run)
    python backfill-dg-cssclasses.py --apply   # write changes

Run from the vault root.
"""

import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).parent
DG_FOLDER = VAULT_ROOT / "DiscourseGraph"

# Maps filename prefix → cssclass added by templates
PREFIX_MAP = {
    "QUE": "dg-que",
    "CLM": "dg-clm",
    "EVD": "dg-evd",
    "EXP": "dg-exp",
    "RES": "dg-res",
    "CON": "dg-con",
    "ISS": "dg-iss",
    "HYP": "dg-hyp",
    "@":   "dg-src",
}


def cssclass_for(filename: str) -> str | None:
    stem = Path(filename).stem
    for prefix, cls in PREFIX_MAP.items():
        if prefix == "@":
            if stem.startswith("@"):
                return cls
        elif stem.startswith(f"{prefix} -") or stem.startswith(f"{prefix}-"):
            return cls
    return None


def patch(path: Path, cssclass: str, apply: bool) -> str:
    text = path.read_text(encoding="utf-8")

    if "cssclasses:" in text:
        return "already-set"

    if not text.startswith("---"):
        return "no-frontmatter"

    close = text.find("\n---", 3)
    if close == -1:
        return "malformed"

    if apply:
        patched = text[:close] + f"\ncssclasses: {cssclass}" + text[close:]
        path.write_text(patched, encoding="utf-8")

    return "patched"


def main():
    apply = "--apply" in sys.argv
    if not apply:
        print("DRY RUN — no files will be changed. Pass --apply to write.\n")

    counts = {"patched": 0, "already-set": 0, "skipped": 0}

    for md in sorted(DG_FOLDER.glob("*.md")):
        cls = cssclass_for(md.name)
        if not cls:
            print(f"  UNKNOWN  {md.name}")
            counts["skipped"] += 1
            continue

        result = patch(md, cls, apply)
        tag = f"[{cls}]".ljust(10)

        if result == "patched":
            verb = "PATCHED " if apply else "WOULD PATCH"
            print(f"  {verb} {tag} {md.name}")
            counts["patched"] += 1
        elif result == "already-set":
            print(f"  SKIP     {tag} {md.name}  (cssclasses already present)")
            counts["already-set"] += 1
        else:
            print(f"  SKIP     {tag} {md.name}  ({result})")
            counts["skipped"] += 1

    print(f"\n{counts['patched']} {'patched' if apply else 'to patch'}, "
          f"{counts['already-set']} already set, "
          f"{counts['skipped']} skipped.")


if __name__ == "__main__":
    main()
