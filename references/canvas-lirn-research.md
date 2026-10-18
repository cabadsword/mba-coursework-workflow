# Canvas And LIRN Research

Use this reference when an assignment requires Canvas intake, LIRN/library research, or peer-reviewed article validation.

## Canvas Intake

- Use BrowserOS first when authenticated Canvas access is required and the BrowserOS MCP is configured. Typical setup command supplied by the user may look like:

```bash
codex mcp add browseros http://127.0.0.1:9000/mcp
```

- If BrowserOS tools are not visible, use the available Browser or Chrome skills/tools for authenticated browsing. If no authenticated browser is available, ask the user to provide screenshots, copied instructions, or downloaded files.
- Start from the user's Canvas dashboard or direct assignment URL. For CIAM Canvas, the dashboard URL used in prior work was `https://ciam.instructure.com/`.
- Capture the assignment title, course, due date, points, submission type, rubric, required word count or duration, and citation/source requirements.
- Save a paraphrased requirements artifact under `source/`.
- If the assignment has discussion replies, record both original-post and reply requirements.
- Do not submit or post in Canvas unless explicitly instructed.

## BrowserOS Canvas Browsing Pattern

Use BrowserOS for live Canvas/LIRN work when available:

1. Confirm BrowserOS is reachable or that BrowserOS MCP tools are listed. If not, remind the user of the setup command and fall back to Browser/Chrome or user-provided screenshots.
2. Open the Canvas dashboard.
3. Identify the relevant course card, module, assignment, or discussion link.
4. Open the assignment page and capture requirements, rubric, due dates, points, submission type, and reply requirements.
5. For module/textbook links, open the linked page and extract only assignment-relevant content needed for a paraphrased source artifact.
6. For discussion assignments, check whether replies are required and whether the original post is already submitted.
7. For LIRN/library research, enter LIRN from the Canvas course/module link when possible so authentication carries through.
8. Record what was inspected and any URLs/titles needed to re-open the path later.

Safety boundaries:

- Do not click final submit/post/upload buttons unless the user explicitly says to submit.
- If a page includes personal grades, messages, or unrelated courses, do not summarize unrelated private information.
- If BrowserOS can see only search results but not full article text, do not treat that as full-text validation.

Troubleshooting:

- If Canvas asks for login or MFA, pause and ask the user to complete authentication in the browser.
- If a new provider tab opens outside BrowserOS visibility, switch to Chrome/Browser if that is where the authenticated tab lives.
- If downloads are blocked, use the provider's PDF/full-text export, print, or copyable article view only when permitted.
- If a tool cannot access BrowserOS despite setup, continue with available browser tooling and note that BrowserOS was unavailable.

## LIRN Search Workflow

- Enter LIRN from the Canvas course link when possible so access/authentication carries through.
- In BrowserOS, keep the provider/full-text tab open long enough to confirm whether the article can actually be read, downloaded, or exported.
- Start broad, then narrow. Record search strings and filters in `research/`.
- Prefer filters:
  - Peer reviewed
  - Full text
  - Scholarly journals
  - English, unless the assignment allows otherwise
- Avoid using news, book reviews, dissertations, magazines, or non-peer-reviewed sources as the main scholarly article unless the assignment permits them.

## Article Validation

Validate candidates beyond the search-result abstract:

- Open the provider page or PDF/full-text page.
- Use BrowserOS to capture the ProQuest/EBSCO/provider URL and visible metadata when available.
- Confirm full text is available.
- Confirm peer-reviewed or scholarly journal status.
- Capture authors, year, article title, journal, volume, issue, pages, DOI, and database/provider.
- For ProQuest, look for source type such as "Scholarly Journal" and page metadata showing full text/PDF availability.
- For EBSCO, look for peer-reviewed/full-text indicators and a journal/source record rather than only database subject tags.
- If a DOI is present, keep it in the APA citation; if the DOI is missing or suspicious, optionally verify with Crossref or the publisher page when web access is available.
- Download or export the PDF/text into `research/` when permitted.
- Extract enough text to verify the article truly supports the assignment claim.
- Keep APA 7 reference and in-text citation notes.

## Research Output

For each usable article, produce:

- APA 7 reference
- APA 7 in-text citation
- 3-5 sentence paraphrase of the core finding
- Explanation of how it supports the assignment
- Any limitations or fit concerns

If full text cannot be read, mark the source as rejected or pending; do not rely on it.
