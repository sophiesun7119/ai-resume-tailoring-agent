# First-run setup: resume tailoring first

## What to ask (conversationally, only missing fields)

**1. Candidate Profile** — target roles/levels, years of experience, real technical strengths, location or work constraints if helpful, languages, preferred resume bases, and editing rules. Do not infer citizenship, clearance, degrees or proficiency. Profile can be answered in chat instead of filling a JSON file.

**2. Sources for tailored resumes** — ask for **one or more** Base/Master Resume Google Doc links and a Career Story Bank Google Doc link. A user may maintain separate Backend, Cloud, AI resumes. Ask for the destination Google Drive folder to save a new Doc. Never require a Google Sheet for the default JD-to-resume flow.

**3. JD** — accept an official job URL or pasted JD text. Job link can be sent per run. When no browsing is available, use only pasted JD and label it user-provided; don't claim opening is current or verified.

**4. Optional integrations** — ask **only if** user requests company discovery / application tracking for a Google Sheet URL and actual tab names. Do not automatically create sheets, schedules or inbox monitors.

**5. Authorization** — have the user connect Google Docs/Drive (and Google Sheets only for optional tracking) in the assistant/host app's **official OAuth/connector settings**. Never ask for credentials, cookies or tokens. Test read access to supplied source docs and inspect folder metadata. **Folder metadata access is not proof of write access**; only an authorized copy operation or confirmed permission verifies writes. Do not run a live write probe without approval.

**6. Read-only preview** — analyze the JD and all resume bases, compare requirements to Story Bank evidence, recommend a base and show exact proposed edits. Check which technical claims lack support. No creation or edits in preview.

**7. Approval** — obtain authorization to create the independent copy. If replacing/deleting whole bullets, show verbatim before-and-after text first and await explicit approval. Save only after consent; preserve originals and verify native Doc readback and visual PDF page count if the host supports it.

## Setup readiness

| Input/tool | JD analysis | Saved native Doc | Verified PDF | Optional tracking |
| --- | --- | --- | --- | --- |
| Candidate profile | Required | Required | Required | Recommended |
| JD link or text | Required per request | Required per request | Required | For review, can use company name instead |
| At least one Base Resume | Required for evidence-backed editing | Required | Required | Not required |
| Career Story Bank | Recommended; report missing evidence if unavailable | Required for full story-backed tailoring | Required for story-backed output | Not required |
| Output Drive folder | Not required | Required | Required for saved Doc | Not required |
| Google Docs/Drive permission | Not needed for pasted text analysis | Required | Required | Not required |
| PDF export AND page rendering | Not required | Not required | Required for page-count claim | Not required |
| Google Sheet + Sheets permission | Not required | Not required | Not required | Required |

## Two example interactions

**Basic (no tracker):**
- User: "Tailor my resume for this pasted backend JD."
- Assistant: "Please share your backend resume Doc, Career Story Bank Doc, and output folder, and authorize Google Docs/Drive. I'll first map JD requirements to real evidence and suggest edits. I won't overwrite your original."
- Assistant: "The backend base best matches this JD. These two changes are supported; one significant bullet rewrite needs your approval. No document has been modified yet."

**With tracker (optional):**
- User: "Review ExampleCloud's official careers and rank the new roles from my Sheet."
- Assistant: "Please connect your tracker Sheet and confirm tab names. I'll preserve Applied/Skip/Closed, review new/unprocessed roles, then wait for your selection before tailoring."

## Private config

`config/profile.local.json` and `config/resources.local.json` are private and Git-ignored. Source examples are **fictional only**. Run `python3 scripts/preflight.py --profile ... --resources ...` for resume-save configuration. It validates syntax, **not** actual Google access. Use `--mode analysis` for JD discussion without output folder, and `--mode tracking` only if tracker Sheets are configured.
