#!/usr/bin/env python3
"""
MW-Omega Cross-Document Reference Audit
Validates reference integrity across the document stack.

Usage:
    python cross_ref_audit.py          # Full audit
    python cross_ref_audit.py --ci     # CI mode (exit 1 on failure)
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
TRACKED_DIRS = ["docs", "skills"]


def collect_files() -> list:
    files = []
    for d in TRACKED_DIRS:
        dirpath = ROOT / d
        if dirpath.exists():
            for f in sorted(dirpath.rglob("*.md")):
                if f.is_file():
                    files.append(f)
    return files


def extract_references(filepath: Path) -> list:
    """Extract internal references (DOC-NNN, links to other docs)."""
    content = filepath.read_text(errors="replace")
    refs = []
    # Match DOC-NNN, BOOK-NNN, MUSIC-NNN, etc.
    asset_refs = re.findall(r'\b([A-Z]+-\d{3})\b', content)
    refs.extend(asset_refs)
    # Match relative markdown links
    link_refs = re.findall(r'\[.*?\]\(((?!http)[^)]+)\)', content)
    refs.extend(link_refs)
    return refs


def audit():
    files = collect_files()
    if not files:
        print("No documents found to audit.")
        return 0

    all_refs = {}
    errors = 0

    for f in files:
        rel = f.relative_to(ROOT)
        refs = extract_references(f)
        all_refs[str(rel)] = refs

    # Check relative link targets exist
    for doc, refs in all_refs.items():
        for ref in refs:
            if ref.startswith(("DOC-", "BOOK-", "MUSIC-", "ESSAY-")):
                continue  # Asset IDs checked separately
            target = ROOT / Path(doc).parent / ref
            if not target.exists() and not (ROOT / ref).exists():
                print(f"BROKEN LINK: {doc} -> {ref}")
                errors += 1

    if errors:
        print(f"\n{errors} reference error(s) found.")
    else:
        print(f"Audit complete. {len(files)} files checked. No errors.")

    return errors


if __name__ == "__main__":
    errors = audit()
    if "--ci" in sys.argv and errors > 0:
        sys.exit(1)
