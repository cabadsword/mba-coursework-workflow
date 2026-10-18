#!/usr/bin/env python3
"""Verify a PPTX is ready for MBA presentation submission."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import zipfile
from pathlib import Path

try:
    from pptx import Presentation
except ImportError:
    print("python-pptx is required: pip install python-pptx", file=sys.stderr)
    raise SystemExit(2)


def notes_text(path: Path, slide_index: int) -> str:
    name = f"ppt/notesSlides/notesSlide{slide_index}.xml"
    try:
        with zipfile.ZipFile(path) as archive:
            if name not in archive.namelist():
                return ""
            xml = archive.read(name).decode("utf-8", "replace")
    except zipfile.BadZipFile:
        return ""
    return " ".join(re.findall(r"<a:t>(.*?)</a:t>", xml))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--expected-slides", type=int)
    parser.add_argument("--min-notes-words", type=int, default=0)
    parser.add_argument("--rail-verifier", type=Path, help="Optional Open Design verify_layout.py")
    args = parser.parse_args()

    pptx = args.pptx.expanduser().resolve()
    if not pptx.exists():
        print(f"FAIL file not found: {pptx}", file=sys.stderr)
        return 1

    try:
        presentation = Presentation(str(pptx))
    except Exception as exc:
        print(f"FAIL cannot open PPTX: {exc}", file=sys.stderr)
        return 1

    slide_count = len(presentation.slides)
    print(f"slides={slide_count}")
    print(f"bytes={pptx.stat().st_size}")

    failures: list[str] = []
    if args.expected_slides is not None and slide_count != args.expected_slides:
        failures.append(f"expected {args.expected_slides} slides, found {slide_count}")

    counts: list[int] = []
    for index in range(1, slide_count + 1):
        text = notes_text(pptx, index)
        count = len(text.split())
        counts.append(count)
        print(f"notes_slide_{index}_words={count}")
        if args.min_notes_words and count < args.min_notes_words:
            failures.append(
                f"slide {index} notes have {count} words; minimum is {args.min_notes_words}"
            )
    print(f"notes_total_words={sum(counts)}")

    if args.rail_verifier:
        verifier = args.rail_verifier.expanduser().resolve()
        if not verifier.exists():
            failures.append(f"rail verifier not found: {verifier}")
        else:
            result = subprocess.run(
                [sys.executable, str(verifier), str(pptx)],
                text=True,
                capture_output=True,
                check=False,
            )
            if result.stdout:
                print(result.stdout, end="")
            if result.stderr:
                print(result.stderr, end="", file=sys.stderr)
            if result.returncode != 0:
                failures.append(f"rail verifier failed with exit code {result.returncode}")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}", file=sys.stderr)
        return 1

    print("OK pptx ready")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
