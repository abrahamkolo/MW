#!/usr/bin/env python3
"""
MW-Omega Document Hash Verification
SHA3-512 hashing for canonical document sealing.

Usage:
    python hash-verify.py                 # Generate hashes for all docs
    python hash-verify.py --check         # Verify against MASTER_INDEX.json
    python hash-verify.py --file path     # Hash a single file
"""

import hashlib
import json
import sys
import os
from pathlib import Path
from datetime import datetime, timezone

MASTER_INDEX = "MASTER_INDEX.json"
TRACKED_DIRS = ["docs", "skills"]


def sha3_512(filepath: str) -> str:
    """Compute SHA3-512 hash of a file after normalization."""
    with open(filepath, "rb") as f:
        content = f.read()
    # Normalize: strip BOM, convert CRLF to LF
    if content.startswith(b"\xef\xbb\xbf"):
        content = content[3:]
    content = content.replace(b"\r\n", b"\n")
    return hashlib.sha3_512(content).hexdigest()


def collect_files() -> list:
    """Collect all trackable files from TRACKED_DIRS."""
    root = Path(__file__).parent.parent
    files = []
    for d in TRACKED_DIRS:
        dirpath = root / d
        if dirpath.exists():
            for f in sorted(dirpath.rglob("*")):
                if f.is_file() and not f.name.startswith("."):
                    files.append(str(f.relative_to(root)))
    return files


def generate_index():
    """Generate MASTER_INDEX.json with hashes for all tracked files."""
    root = Path(__file__).parent.parent
    files = collect_files()
    index = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "algorithm": "SHA3-512",
        "documents": {}
    }
    for f in files:
        filepath = root / f
        index["documents"][f] = {
            "hash": sha3_512(str(filepath)),
            "size": filepath.stat().st_size,
            "sealed": datetime.now(timezone.utc).isoformat()
        }
    index_path = root / MASTER_INDEX
    with open(index_path, "w") as out:
        json.dump(index, out, indent=2)
    print(f"Generated {MASTER_INDEX} with {len(index['documents'])} documents.")
    # Hash the index itself
    index_hash = sha3_512(str(index_path))
    print(f"Index hash (SHA3-512): {index_hash}")


def verify_index():
    """Verify current files against MASTER_INDEX.json."""
    root = Path(__file__).parent.parent
    index_path = root / MASTER_INDEX
    if not index_path.exists():
        print(f"ERROR: {MASTER_INDEX} not found. Run without --check first.")
        sys.exit(1)
    with open(index_path) as f:
        index = json.load(f)
    errors = 0
    for doc, meta in index["documents"].items():
        filepath = root / doc
        if not filepath.exists():
            print(f"MISSING: {doc}")
            errors += 1
            continue
        current_hash = sha3_512(str(filepath))
        if current_hash != meta["hash"]:
            print(f"MODIFIED: {doc}")
            print(f"  Expected: {meta['hash'][:32]}...")
            print(f"  Got:      {current_hash[:32]}...")
            errors += 1
        else:
            print(f"OK: {doc}")
    if errors:
        print(f"\n{errors} verification failure(s).")
        sys.exit(1)
    else:
        print(f"\nAll {len(index['documents'])} documents verified.")


def hash_single(filepath: str):
    """Hash a single file."""
    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)
    h = sha3_512(filepath)
    print(f"SHA3-512: {h}")
    print(f"File:     {filepath}")


if __name__ == "__main__":
    if "--check" in sys.argv:
        verify_index()
    elif "--file" in sys.argv:
        idx = sys.argv.index("--file")
        if idx + 1 < len(sys.argv):
            hash_single(sys.argv[idx + 1])
        else:
            print("Usage: hash-verify.py --file <path>")
            sys.exit(1)
    elif "--ci" in sys.argv:
        verify_index()
    else:
        generate_index()
