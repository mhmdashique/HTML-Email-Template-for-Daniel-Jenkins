# Email Compatibility and Implementation Summary

**Campaign:** Better Web Digest — The Accessibility Issue, November 2026  
**Implementation File:** `newsletter.html`  
**Date:** 23 November 2026  

---

## 1. Implementation approach

### Table Layout & Structural Hierarchy
The email is constructed using a robust single-column nested table structure designed for universal compatibility across desktop, web, and mobile email clients:
1. **Outer Viewport Wrapper Table:** A $100\%$ width outer presentation table with background color `#E9F0EF`, providing consistent outer gutters and centering.
2. **Centered 600px Main Card Container:** A `<table role="presentation">` bounded by `max-width: 600px; width: 100%;` with background `#FFFFFF`, rounded bottom corners (`16px border-radius`), and subtle box shadow.
3. **Ghost Tables for MSO / Outlook:** Outlook Windows classic does not support CSS `max-width`. The layout wraps the container in conditional MSO comments (`<!--[if (gte mso 9)|(IE)]><table align="center" width="600" ...>`) ensuring Outlook enforces a strict 600px container width without stretching to 100% of the reading pane.
4. **Pure Inline CSS (No `<style>` Tags):** In accordance with the project specification and acceptance criteria, zero internal `<style>` blocks, external stylesheets, JavaScript, CSS Grid, or Flexbox are used. All presentation properties are applied inline on elements.

### Fluid / Hybrid Responsive Multi-Column Approach
To achieve responsiveness without relying on `<style>` media queries (which are stripped or ignored by certain webmail clients and older Android/Gmail apps):
- Each feature card uses a container cell with `font-size: 0; text-align: left;`.
- The image column is an `inline-block` `<div>` with `max-width: 220px; width: 100%; vertical-align: top;`.
- The text content column is an `inline-block` `<div>` with `max-width: 270px; width: 100%; vertical-align: middle;` and reset `font-size: 14px;`.
- **Behavior:**
  - On viewports $\ge 530\text{ px}$ (desktop), the two blocks sum to $\le 506\text{ px}$ and sit side-by-side horizontally.
  - On viewports $< 530\text{ px}$ (mobile/small tablets), the text block automatically wraps below the image block, expanding to $100\%$ container width.
  - For Outlook desktop, MSO conditional two-column table cells (`<td width="220">` and `<td width="270">`) guarantee side-by-side column positioning.

### Bulletproof CTA Button
The primary CTA ("EXPLORE THE GUIDE") employs a bulletproof hybrid architecture:
- For standards-based email clients: A styled table cell with `bgcolor="#177E80"`, rounded corners (`10px border-radius`), and an inline-styled `<a>` tag with generous padding.
- For Outlook Windows: An embedded VML `<v:roundrect>` element with explicit width ($210\text{ px}$), height ($48\text{ px}$), fillcolor `#177E80`, and `arcsize="20%"`.

### Asset Hosting & Reading Order
- **Asset Paths:** In the local delivery package, all five images reference local paths under `images/`. For live email broadcast, these paths must be replaced with authorized HTTPS CDN/ESP URLs as documented in the Delivery Notes.
- **Reading Order:** Logical DOM hierarchy is maintained from Header $\rightarrow$ Eyebrow $\rightarrow$ Headline $\rightarrow$ Intro $\rightarrow$ Hero $\rightarrow$ CTA $\rightarrow$ Section Label $\rightarrow$ Cards 1 to 3 $\rightarrow$ Footer. Screen readers encounter content in exact semantic sequence.

---

## 2. Verification matrix

Real tests were executed on 23 November 2026 using Playwright Chromium (version 1.58.0) and automated Python static inspection scripts. In strict adherence to testing standards, external email clients that were not physically accessible or tested via an active Litmus/Email on Acid service are recorded honestly as `NOT_TESTED`.

| Test ID | Environment | Viewport / Scope | Check | Result | Actual Observation & Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T01** | Chromium Browser | 320px | No horizontal scroll | **PASS** | `scrollWidth` = 320px, `clientWidth` = 320px; zero horizontal scroll. Evidence: `viewport_320.png` |
| **T02** | Chromium Browser | 375px | Text & image wrap | **PASS** | `scrollWidth` = 375px; cards stack vertically; "Navigation without guesswork" wraps cleanly at 249px width. Evidence: `viewport_375.png` |
| **T03** | Chromium Browser | 768px | Centered 600px container | **PASS** | Centered 600px main card on `#E9F0EF` background; 2-column card layout active. Evidence: `viewport_768.png` |
| **T04** | Chromium Browser | 1200px | Centered container | **PASS** | Container remains bounded at max-width 600px. Evidence: `viewport_1200.png` |
| **T05** | Gmail Web | Desktop | Links, images, spacing | **NOT_TESTED** | No live client or rendering service confirmed during run |
| **T06** | Gmail Mobile | 375px | Single-column readability | **NOT_TESTED** | No live client or rendering service confirmed during run |
| **T07** | Outlook Windows Classic | Desktop | Tables, fonts, VML button | **NOT_TESTED** | No live client or rendering service confirmed during run |
| **T08** | Outlook Web | Desktop | Buttons, layout, links | **NOT_TESTED** | No live client or rendering service confirmed during run |
| **T09** | Apple Mail macOS | Desktop | Image scaling, alt text | **NOT_TESTED** | No live client or rendering service confirmed during run |
| **T10** | Apple Mail iOS | 375px | Single column scaling | **NOT_TESTED** | No live client or rendering service confirmed during run |
| **T11** | Static Inspection | N/A | Inline CSS, no `<style>` | **PASS** | Size 15.61 KB; 0 `<style>`, 0 `<script>`, 0 Grid/Flex, 23/23 tables presentation. Evidence: `static_checks.txt` |
| **T12** | Static Inspection | N/A | Full copy, alt text, CTAs | **PASS** | 100% copy match; all 5 alt texts verified; all 4 CTA URLs HTTP 200. Evidence: `static_checks.txt` |

---

## 3. Deviations and remaining issues

1. **Outlook Windows Desktop Rounded Corners (`border-radius`):**
   - Microsoft Outlook 2016/2019/365 (Windows desktop using Word rendering engine) does not support CSS `border-radius` on HTML `<table>` or `<div>` elements.
   - *Graceful Degradation:* The primary CTA gracefully retains rounded corners via VML `<v:roundrect>`. The cards and outer container will render with clean, crisp square corners in Outlook Windows classic, which is standard email behavior.
2. **Display Differences vs. Visual References:**
   - In `desktop_1440.png`, the canvas is 1440px wide; in email implementation, standard 600px max-width container is used per email development best practices.
   - The headline is formatted with a line break (`Make the web<br>work for everyone.`) matching the two-line presentation in desktop references.
   - On mobile (375px), feature cards fluidly stack with images above copy, matching `mobile_375.png`.

---

## 4. Delivery notes

### File Size & Asset Inventory
* **Final HTML Size:** **15,988 bytes (15.61 KB)** — well below the 100 KB threshold preventing Gmail clipping.
* **Optimized PNG Assets:**
  - `brand_mark.png`: $420 \times 110\text{ px}$ (7.42 KB)
  - `hero_accessible.png`: $1100 \times 560\text{ px}$ (20.65 KB)
  - `feature_images.png`: $600 \times 380\text{ px}$ (7.34 KB)
  - `feature_menus.png`: $600 \times 380\text{ px}$ (6.86 KB)
  - `feature_writing.png`: $600 \times 380\text{ px}$ (5.81 KB)
  - **Total Images Weight:** 48.08 KB

### CTA Link Destinations
All four approved CTA links verified live with HTTP 200 responses:
* **L01 (Hero):** `https://www.w3.org/WAI/tips/writing/`
* **L02 (Section 1):** `https://www.w3.org/WAI/tutorials/images/`
* **L03 (Section 2):** `https://www.w3.org/WAI/tutorials/menus/`
* **L04 (Section 3):** `https://www.w3.org/WAI/tips/writing/`

### Asset Hosting & Unsubscribe Configuration for Deployment
1. **Asset Hosting Replacement:**  
   Before final distribution via an ESP (e.g., Mailchimp, Iterable, Sendgrid, Salesforce Marketing Cloud):
   - Upload the 5 optimized files in `images/` to your authorized CDN or ESP media library.
   - Perform a global search-and-replace in `newsletter.html`: replace `images/` with your HTTPS base path (e.g., `https://cdn.yourdomain.example/emails/2026-11/`).
2. **Recipient-Specific Unsubscribe & Preferences URLs:**  
   In `newsletter.html`, the footer contains merge placeholders:
   - `href="{{unsubscribe_url}}"`
   - `href="{{preferences_url}}"`  
   When connecting to your email sending platform, replace these placeholders with the platform’s native merge tags (e.g., `*|UNSUB|*` for Mailchimp, `%mailing_unsubscribe_link%`, or your configured preference center URL). Do not hardcode fictitious links.
