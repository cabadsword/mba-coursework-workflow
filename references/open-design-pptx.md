# Open Design And PPTX Workflow

Use this reference for slide decks, oral presentations, and PowerPoint deliverables.

## Source First

Before designing slides, create a source artifact under `source/` or `design/` containing:

- Assignment requirements and rubric.
- Required questions or learning objectives.
- Textbook/module source notes in paraphrased form.
- Proposed slide structure.
- Speaker flow or draft script.
- Citation/reference notes.

Do not paste long textbook excerpts into reusable skill files.

## Open Design Flow

- Confirm the local Open Design web UI and daemon if needed.
- Create or update a Deck project with a clear name.
- Use the assignment source artifact as input.
- Favor professional, readable classroom/video-recording design.
- Keep slide text concise and audience-facing.
- Put full narration in speaker notes, not visible slide text.
- Keep HTML source, preview images, and build output under `design/`.

## PPTX Build And Verification

When using the Presentations skill or another PPTX builder:

- Generate an editable PPTX.
- Verify the file opens.
- Confirm exact slide count.
- Extract visible text to check required assignment topics are covered.
- Confirm speaker notes exist and have enough words for the required presentation duration.
- Run Open Design `pptx-html-fidelity-audit` rail verifier when available.
- Inspect preview/contact sheet for visible overlap, cropped content, or unreadable text.

Use `scripts/verify_pptx_ready.py` for repeatable checks.

## Speaker Notes

- For oral assignments, write notes as read-aloud script unless the user requests cue notes.
- Estimate timing from word count:
  - 390-650 words: about 3-5 minutes at moderate speaking speed.
  - 650-750 words: near the upper edge of 5 minutes depending on delivery.
- Keep the final slide shorter if the speaker needs a clean closing.

## Final Deliverables

- Place submission-ready PPTX files in `final/`.
- Keep editable design sources and generated previews in `design/`.
- Report the final PPTX path, slide count, notes word count, and verification results.
