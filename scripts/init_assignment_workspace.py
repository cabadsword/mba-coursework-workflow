#!/usr/bin/env python3
"""Create the standard MBA assignment workspace tree without overwriting files."""

from __future__ import annotations

import argparse
from pathlib import Path


SUBDIRS = ("source", "research", "drafts", "design", "final")


def normalize_course(course: str) -> str:
    value = course.strip().replace(" ", "-")
    if not value:
        raise ValueError("course must not be empty")
    return value.upper()


def normalize_assignment(assignment: str) -> str:
    value = assignment.strip().lower().replace(" ", "-").replace("_", "-")
    value = "".join(ch for ch in value if ch.isalnum() or ch == "-")
    value = "-".join(part for part in value.split("-") if part)
    if not value:
        raise ValueError("assignment must not be empty")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path, help="Workspace root")
    parser.add_argument("--course", required=True, help="Course code, such as GB501")
    parser.add_argument("--assignment", required=True, help="Assignment slug or title")
    args = parser.parse_args()

    root = args.root.expanduser().resolve()
    course = normalize_course(args.course)
    assignment = normalize_assignment(args.assignment)
    base = root / "assignments" / course / assignment

    created: list[Path] = []
    for subdir in SUBDIRS:
        path = base / subdir
        before = path.exists()
        path.mkdir(parents=True, exist_ok=True)
        if not before:
            created.append(path)

    tracker_dir = root / "workspace-notes"
    before = tracker_dir.exists()
    tracker_dir.mkdir(parents=True, exist_ok=True)
    if not before:
        created.append(tracker_dir)

    inbox = root / "assignments" / "_inbox"
    before = inbox.exists()
    inbox.mkdir(parents=True, exist_ok=True)
    if not before:
        created.append(inbox)

    print(f"assignment_dir={base}")
    print(f"created={len(created)}")
    for path in created:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
