#!/usr/bin/env python3
"""
ingest.py — track which raw/ files have been processed into the wiki.

State file : .ingest/state.json  (not markdown, invisible to wiki tools)
Unique key : filename:sha256     (directory is ignored)

Changing even one byte in a file produces a new hash, so the file will
appear unprocessed again even though it carries the same name.
"""

import argparse
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

STATE_FILE = Path(".ingest/state.json")
RAW_DIR = Path("raw")
ASSETS_DIR = RAW_DIR / "assets"


# ---------------------------------------------------------------------------
# State helpers
# ---------------------------------------------------------------------------

def load_state() -> dict:
    if not STATE_FILE.exists():
        return {"version": 1, "processed": {}}
    with STATE_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(exist_ok=True)
    with STATE_FILE.open("w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# File helpers
# ---------------------------------------------------------------------------

def file_hash(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def make_key(filename: str, hash_: str) -> str:
    return f"{filename}:{hash_}"


def all_raw_files() -> list[Path]:
    if not RAW_DIR.exists():
        return []
    assets = str(ASSETS_DIR)
    return sorted(
        p for p in RAW_DIR.rglob("*")
        if p.is_file() and not str(p).startswith(assets)
    )


def is_processed(path: Path, state: dict) -> bool:
    h = file_hash(path)
    return make_key(path.name, h) in state["processed"]


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_add(args, state: dict) -> None:
    paths = [Path(p) for p in args.paths]
    added, skipped, missing = [], [], []

    for path in paths:
        if not path.exists():
            missing.append(str(path))
            continue

        filename = path.name
        h = file_hash(path)
        key = make_key(filename, h)

        # Warn about filename collisions with other raw files
        same_name = [
            f for f in all_raw_files()
            if f.name == filename and f != path
        ]
        if same_name:
            print(
                f"  warning: another file with the same name exists: "
                f"{same_name[0]}",
                file=sys.stderr,
            )

        if key in state["processed"]:
            skipped.append(str(path))
        else:
            state["processed"][key] = {
                "filename": filename,
                "path": str(path),
                "hash": h,
                "processed_at": str(date.today()),
            }
            added.append(str(path))

    save_state(state)

    parts = []
    if added:
        parts.append(f"added: {len(added)}")
    if skipped:
        parts.append(f"already processed: {len(skipped)}")
    if missing:
        parts.append(f"not found: {len(missing)}")
    print("  " + "   ".join(parts) if parts else "  nothing to do")

    if missing:
        for p in missing:
            print(f"  not found: {p}", file=sys.stderr)
        sys.exit(1)


def cmd_next(args, state: dict) -> None:
    n = args.n
    files = all_raw_files()

    unprocessed = [f for f in files if not is_processed(f, state)]

    if not unprocessed:
        print("  all files are processed")
        return

    for f in unprocessed[:n]:
        print(str(f))


def cmd_status(args, state: dict) -> None:
    files = all_raw_files()
    processed, unprocessed = [], []

    for f in files:
        (processed if is_processed(f, state) else unprocessed).append(f)

    total = len(files)
    print(f"  total:       {total}")
    print(f"  processed:   {len(processed)}")
    print(f"  unprocessed: {len(unprocessed)}")


def cmd_clean(args, state: dict) -> None:
    existing_names = {f.name for f in all_raw_files()}

    before = len(state["processed"])
    state["processed"] = {
        k: v
        for k, v in state["processed"].items()
        if v["filename"] in existing_names
    }
    after = len(state["processed"])

    save_state(state)
    print(f"  removed {before - after} stale entries ({after} remaining)")


def cmd_check(args, state: dict) -> None:
    path = Path(args.path)

    if not path.exists():
        print(f"  error: file not found: {path}", file=sys.stderr)
        sys.exit(1)

    h = file_hash(path)
    key = make_key(path.name, h)

    if key in state["processed"]:
        entry = state["processed"][key]
        print(f"  status:       processed")
        print(f"  processed_at: {entry['processed_at']}")
        print(f"  hash:         {h[:16]}...")
    else:
        older = [
            v for k, v in state["processed"].items()
            if v["filename"] == path.name
        ]
        if older:
            last = older[-1]
            print(f"  status:       not processed  (file has changed)")
            print(f"  last run:     {last['processed_at']}  hash {last['hash'][:16]}...")
        else:
            print(f"  status:       not processed")


def cmd_help(*_) -> None:
    print("""
ingest.py — raw/ file processing tracker for second-brain vaults

USAGE
  python tools/ingest.py <command> [args]

COMMANDS

  add <file> [file ...]
      Mark one or more files as processed.
      Records filename + SHA-256 content hash as the unique key.
      If the file content changes later, it will appear unprocessed again.

  next [n]
      Print paths of the next N unprocessed files (default: 1).
      Output is one path per line — suitable for scripting.

  status
      Summary: total / processed / unprocessed counts,
      plus a list of every unprocessed file with its path.

  clean
      Remove state entries for files that no longer exist in raw/.
      Stale hash entries for files that still exist are kept.

  check <file>
      Check whether a specific file is currently processed.
      If the file has changed since last ingest, reports "file has changed".

  help
      Show this message.

STATE FILE
  .ingest/state.json
  Not a markdown file — invisible to wiki glob patterns and LLM tools.

UNIQUE KEY
  Each entry is stored as  filename:sha256  (directory path is ignored).
  This means you can reorganise files inside raw/ without losing state.
  Changing even one byte produces a new hash, triggering reprocessing.
""")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

COMMANDS = {
    "add": cmd_add,
    "next": cmd_next,
    "status": cmd_status,
    "clean": cmd_clean,
    "check": cmd_check,
    "help": cmd_help,
}


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="ingest.py",
        description="Track which raw/ files have been processed into the wiki.",
        add_help=False,
    )
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add")
    p_add.add_argument("paths", nargs="+", help="files to mark as processed")

    p_next = sub.add_parser("next")
    p_next.add_argument("n", nargs="?", type=int, default=1, help="how many files to return")

    sub.add_parser("status")
    sub.add_parser("clean")

    p_check = sub.add_parser("check")
    p_check.add_argument("path", help="file to check")

    sub.add_parser("help")

    args = parser.parse_args()

    if args.command is None or args.command == "help":
        cmd_help()
        return

    if args.command not in COMMANDS:
        parser.print_usage()
        sys.exit(1)

    state = load_state()
    COMMANDS[args.command](args, state)


if __name__ == "__main__":
    main()
