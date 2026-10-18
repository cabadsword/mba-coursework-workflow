# Workspace Organization

Use this reference when starting, cleaning, or resuming MBA coursework in a shared workspace.

## Standard Layout

Create one assignment folder per course task:

```text
assignments/<COURSE>/<assignment-slug>/
  source/
  research/
  drafts/
  design/
  final/
```

Use these meanings consistently:

- `source/`: Canvas instructions, rubrics, textbook/module notes, source artifacts, assignment screenshots, due-date notes.
- `research/`: PDFs, exported article text, citation notes, LIRN search notes, source validation evidence.
- `drafts/`: discussion posts, peer replies, outlines, scripts, working prose.
- `design/`: Open Design projects, HTML slide sources, preview images, layout JSON, build manifests.
- `final/`: submission-ready files only.

## Shared Workspace Areas

- `assignments/_inbox/`: temporary files before sorting.
- `workspace-notes/`: cross-assignment trackers, plans, and checklists.
- `tools/open-design/`: reusable documentation or notes about the Open Design service.
- `archive/`: superseded files worth keeping but not actively used.

## Operating Rules

- Inspect existing structure before creating folders.
- Do not move user files if their purpose is unclear; place a note in the tracker instead.
- Keep root clean. Root may contain a README, tracker, and convenience symlinks to final deliverables.
- Keep generated build output under `design/` unless it is the final submission file.
- Update or create `workspace-notes/assignment-tracker.md` with course, assignment, status, and key final file path.

## Helper Script

Use:

```bash
scripts/init_assignment_workspace.py --root <workspace> --course GB501 --assignment oral-presentation
```

The script creates the standard tree and is safe to re-run.
