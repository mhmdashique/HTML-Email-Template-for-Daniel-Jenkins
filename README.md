# Better Web Digest — Responsive HTML Email

Responsive, email-compatible HTML newsletter for the **Better Web Digest — The Accessibility Issue (November 2026)** campaign (Job ID: `88owrQecuP7DRHL7Ug3h`).

## Overview

This repository contains a single-column, table-based HTML email built with inline CSS for broad email-client compatibility. The primary deliverable is `deliverables/newsletter.html`, with supporting assets, evidence, and compatibility documentation.

## Repository Structure

- `deliverables/` — Final submission package
  - `newsletter.html` — Completed responsive HTML email
  - `images/` — Optimized PNG assets used by the email
  - `CLIENT_TEST_MATRIX.csv` — Client/viewport test matrix
  - `technical_compatibility_report.md` — Implementation and compatibility report
  - `COMPLETION_NOTE.txt` — Completion summary and deployment notes
  - `evidence/` — Viewport screenshots and static check output
- `Better_Web_Digest_Deliverable/` — Earlier deliverable snapshot
- `INPUT_FILES/` — Source brief, design references, starter HTML, image assets, and templates
- `START_HERE.txt` — Original task instructions
- `SUBMISSION_CHECKLIST.txt` — Submission checklist
- `check_header.py` — Local helper script

## Key Implementation Notes

- **Layout:** Nested `<table role="presentation">` structure, max width `600px`
- **Styling:** Inline CSS only; no `<style>` blocks, external stylesheets, scripts, Grid, or Flexbox layout
- **Responsiveness:** Fluid/hybrid inline-block columns for mobile stacking without media-query dependence
- **Outlook support:** MSO conditionals for width lock and VML bulletproof CTA button
- **Accessibility/content:** Semantic content where supported, descriptive image alt text, hidden preheader text

## Local Preview

Open the final email directly in a browser:

```powershell
Start-Process .\deliverables\newsletter.html
```

The HTML currently references local `images/...` paths for offline review.

## Pre-flight / Deployment

Before sending through an ESP or production email workflow:

1. Upload files from `deliverables/images/` to an HTTPS CDN or ESP asset host.
2. Replace `images/` paths in `deliverables/newsletter.html` with the hosted absolute URLs.
3. Replace `{{unsubscribe_url}}` and `{{preferences_url}}` with your ESP merge tags.
4. Re-test in target email clients (Gmail, Outlook, Apple Mail) before sending.

## Verification

Recorded checks are documented in:

- `deliverables/CLIENT_TEST_MATRIX.csv`
- `deliverables/technical_compatibility_report.md`
- `deliverables/evidence/static_checks.txt`
- `deliverables/evidence/viewport_*.png`

Automated/local checks reported in the deliverables include viewport renders at 320/375/768/1200, images-blocked rendering, static HTML checks, and live CTA URL checks. Email clients not directly tested are marked `NOT_TESTED` in the matrix.
