---
name: ai-resume-tailoring-agent
description: Tailor resumes to a supplied job description using a candidate profile, one or more authorized Base/Master Resume Google Docs, and a Career Story Bank. Use for JD skill-gap analysis, evidence-to-bullet matching, choosing the best resume base, proposing human-reviewed edits, creating an independent formatted Google Doc, and verifying a one-page PDF when tools permit. Company-job discovery and application tracking are optional, not required.
---

# AI Resume Tailoring Agent

## Core promise
Transform an **already selected** JD (official URL or pasted text) into an **evidence-backed proposed resume revision**. When approved and tools permit, produce a **new** Google Doc in the user's folder and a PDF with **verified actual page count**. This is an instruction-based skill for a connected assistant; not a standalone browser/OAuth implementation or automated application-submission tool.

## First-run setup
1. Read [setup-guide](references/setup-guide.md). Collect only missing profile fields and sources in conversation; never use the public fictional example as a real user's identity.
2. Require a JD (link or pasted text), **at least one** Base/Master Resume, Career Story Bank, and a candidate profile for comprehensive evidence matching. The JD may arrive at request time rather than setup.
3. Request a Google Drive output folder **only when saving a Google Doc**. If source Docs, export or write tools are unavailable, perform read-only reasoning on user-provided content and disclose limits; never fabricate a saved link.
4. Google Sheet, Companies/Open Jobs/Applications tabs, official job discovery, and Gmail are **optional**. Do not require a tracker for tailoring.
5. Verify source access, actual content, and output-folder metadata through an authorized Google connector before editing. Link syntax validation does not prove OAuth permissions or write access. Never ask for passwords, access tokens or API secrets.
6. Begin with a read-only evidence/keyword-gap review and a change proposal; do not create a resume just because setup succeeded.

## JD-to-resume flow
Read [resume-story.md](references/resume-story.md), then:
1. Capture JD, job/company/title and constraints. If pasted, identify it as user-provided and do not claim live opening verification.
2. Read **all supplied Base Resume Docs** and Story Bank; select the strongest base for the JD while preserving real content. The user can override the selection.
3. Map key requirements to **exact** source evidence, marking direct / transferable / missing / unverified. Never manufacture years, technologies, model ownership, production outcomes or numeric improvements.
4. Present prioritized **small, literal edits** and reason for each. **Wait for explicit user approval before rewriting/replacing whole bullets, deleting material, or altering a Story Bank**. The user may authorize particular scoped keyword additions. Explicitly honor their stricter editing preferences.
5. After approval, **copy the original native document** to an independent target in the requested Drive folder; edit only approved text while preserving fonts, headings, indentations, spacing, margins, page layout and all untouched bullets.
6. Re-read edited areas. Export PDF **and inspect the actual page count and visual rendering**. If page two overflows, propose layout adjustments or ask to revise scope; never remove unapproved material to force one page. Do not claim success from export file size alone.
7. Return the Google Doc link, PDF only if actually created/verified, real page count or `unverified`, exact change summary and remaining JD gaps. Never submit an application.

## Optional extensions
- `Review Company: <company>`: when requested and an authorized Sheet exists, see [company-audit](references/company-audit.md). Report new/unresolved official jobs and ask which role(s) to tailor. Without a tracker, a direct JD is sufficient.
- `Track Interested/Skip/Applied`: only when explicit and connected Sheet exists; see [decision-tracking](references/decision-tracking.md) and [database-rules](references/database-rules.md). Never equate resume creation or interest with submission.
- Never modify existing scheduled automations or enable email scanning on this skill's behalf.

## Absolute safeguards
Never overwrite Base/Master Docs, misstate official job status, invent experience or PDF verification, silently change previously approved decisions, reveal private resources in public samples, or perform unapproved external writes. State precisely what is blocked or unverified.

## References
- [Onboarding and permissions](references/setup-guide.md)
- [Resume evidence, edits and PDF QA](references/resume-story.md)
- [Optional company audit](references/company-audit.md)
- [Optional tracking schema](references/database-rules.md)
- [Optional decision handling](references/decision-tracking.md)
- [Public privacy rules](references/privacy-and-security.md)
