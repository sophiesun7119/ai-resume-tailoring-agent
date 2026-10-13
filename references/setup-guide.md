# First-run setup, user consent, and connector gates

## Intake: request only missing details

**Step 1 — Candidate profile**: Request target engineering roles, desired seniority/years, confirmed strengths, location/work authorization constraints (do not infer personal legal status), remote preferences, priorities, optional avoid list and contact language. Treat personal information as private; public example JSON is fictional. Accept natural-language replies and generate private configuration with user consent.

**Step 2 — Google resources**: Request these exact user-owned or shared links individually: Google Sheet tracking workbook, Master Resume Google Doc, Career Story Bank Google Doc, and Drive folder for generated resumes. If no workbook exists, ask whether the user wants an empty template. Never assume a particular person's IDs or tab names. Default tab names are Companies / Open Jobs / Applications only for a NEW workbook; existing workbook headers are authoritative.

**Step 3 — Official permission flow**: Instruct the user to connect/authorize Google Drive, Docs, Sheets in the host assistant (or the corresponding client application). Check that the connected identity can read metadata, target Sheets tabs and the two Docs, and list/write the destination folder (only when an authorized tool supports it). Do not request passwords, OAuth tokens or direct credentials. This skill cannot grant privileges.

**Step 4 — Permission-safe verification**: Preflight CLI validates syntax/required input but NOT OAuth scopes. Live tool probes must read metadata and headers first, without edits. Do not perform a write probe to a live user workbook without specific approval; a dedicated throwaway test spreadsheet is preferable. If a particular read or write is forbidden, mark it blocked and request a targeted grant. Verify connector access separately from mere possession of a URL.

**Step 5 — Dry run**: Review one company using read-only existing rows and official ATS sources. Report new/unresolved vs historical records, duplicate identities, eligibility and Match reasoning, no changes. If live data unavailable, use fictional mock example, label it clearly, and do not present it as actual verification.

**Step 6 — Enable controlled actions**: Ask for explicit approval before initializing an empty sheet, appending verified new roles, recording a decision or generating a resume. A future application row requires user-confirmed submission. Never automatically create a schedule or send an application.

## Setup readiness matrix

| Resource | Required for | Missing => |
| --- | --- | --- |
| Candidate profile | Personalized matching | Ask; example only with disclosure |
| Sheet link + readable tabs | Tracking, dedup, decisions | No tracking actions |
| Master Resume Doc | Evidence-backed tailoring | No tailored resume |
| Career Story Bank Doc | Evidence-backed stories | Flag missing evidence; ask |
| Output folder + write permission | Saving tailored Doc | No save claim |
| Official careers web access | Confirming active jobs | Preliminary review only |
| Docs export + PDF viewer | Verified one-page resume | Don't claim verified |

## Example user conversation

Assistant: "Let's set up your personal Job Application Manager. What engineering roles are you targeting, which tools have you used professionally, and where do you want to work?"

User: "Backend and platform roles; Python, AWS, SQL; US remote preferred."

Assistant: "Please share your tracker Sheet link, master-resume Doc, story-bank Doc, and Drive output-folder link. I'll read them only after you authorize the Google connection."

Assistant (after connected reads): "I can read 3 required tabs and both Docs. Folder access is confirmed. I have not changed anything. Which company should I audit in dry-run mode?"
