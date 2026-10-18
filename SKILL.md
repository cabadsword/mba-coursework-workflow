---
name: mba-coursework-workflow
description: Use when Codex helps with MBA or graduate coursework workflows, including Canvas assignment intake, LIRN/library peer-reviewed research, discussion posts and peer replies, source artifacts, Open Design slide decks, PPTX speaker notes and verification, final submission files, and ongoing workspace organization across multiple classes.
---

# MBA Coursework Workflow

Use this skill to move an MBA assignment from Canvas intake to final-ready work product while keeping research, drafts, design sources, and submission files organized.

## Core Rules

- Start by inspecting the workspace, existing assignment tracker, and source artifacts before asking for input.
- Use BrowserOS first for authenticated Canvas/LIRN browsing when its MCP is configured. If BrowserOS is unavailable, use Browser or Chrome when appropriate, or explain the blocker and work from user-provided materials.
- Do not submit, post, upload, or modify Canvas content unless the user explicitly asks for that action.
- Preserve user-owned files and edits. Do not overwrite final deliverables unless the user requested an update.
- Keep private course content, textbook excerpts, downloaded articles, and PDFs inside the current assignment workspace; do not bundle them into this skill.
- Prefer existing specialized skills/plugins when relevant: Presentations for PPTX/decks, Documents for DOCX, Browser/Chrome for web tasks, and local PDF/text tools for source extraction.

## Workflow

1. **Organize the assignment workspace.** Read `references/workspace-organization.md`. Use `scripts/init_assignment_workspace.py` when creating a course/assignment folder.
2. **Capture requirements.** For Canvas or dashboard browsing, read `references/canvas-lirn-research.md`. Save Canvas instructions, rubric details, textbook/module links, due dates, and required deliverable formats under `source/`.
3. **Research and validate sources.** For LIRN or peer-reviewed work, read `references/canvas-lirn-research.md`. Validate full text, scholarly status, citation fields, and PDF/text access before using an article.
4. **Draft written coursework.** For discussion posts and peer replies, read `references/discussion-writing.md`. Ask for personal background only when the assignment requires personal reflection.
5. **Build slide or deck assignments.** For oral presentations or PPTX work, read `references/open-design-pptx.md`. Create a source artifact first, then design, export, and verify the deck.
6. **Finish and record state.** Put submission-ready files in `final/`, keep editable design artifacts in `design/`, update trackers, and summarize verification results.

## Output Defaults

- Use concise assignment-specific file names with course code and assignment topic.
- Put final files in `assignments/<COURSE>/<assignment>/final/`.
- Keep working drafts in `drafts/`, research evidence in `research/`, assignment instructions in `source/`, and generated deck/build assets in `design/`.
- When creating a deck, keep the visible slides concise and put the full read-aloud script in speaker notes.
- Report exact file paths and verification results in the final response.

## Scripts

- `scripts/init_assignment_workspace.py --root <workspace> --course <COURSE> --assignment <slug>`
  creates the standard assignment folder tree without overwriting files.
- `scripts/verify_pptx_ready.py <pptx> --expected-slides <n> --min-notes-words <n>`
  checks that a PPTX opens, has the expected slide count, has sufficient speaker notes, and optionally passes an Open Design rail verifier.
