# Optional Google Sheet tracking contract

The **default JD-to-resume tailoring flow does not require any Google Sheet**. Load this reference only if the user opts into company/job discovery, job decisions or submission tracking.

## Separate tables, never hardcode column indices
- `Companies`: company, Tier, official careers site, eligibility status/date, user notes (optional example statuses Active / Inactive / Cooldown).
- `Open Jobs`: First Seen, company, job title, location, official link, ATS job ID, review status and notes (example statuses New / Interested / Applied / Skip / Closed). Review status is NOT proof of current job availability.
- `Applications`: date applied, job ID/URL, application stage, notes, last updated; contains confirmed submission events only.
- The user's existing tab names, headers, dropdowns, formulas and records take priority. Never auto-migrate or create populated tabs.

## Tracking rules
1. Require authorized Sheet URL and verified read access to headers, validation and matching rows before writing. Ask to resolve incompatible schema; no silent migration.
2. Use stable job identity `(company, provider/ATS namespace, requisition ID)` first; normalized official URL second. Remove tracking parameters; ambiguous identifiers require review.
3. Preserve First Seen, Applied/Skip/Closed, manual Notes, formulas and status precedence. New rows may be appended only after explicit permission and verified official source.
4. Interested and resume creation do not mean Applied. No Applications entry without confirmed user submission.
5. Batch connector writes where supported, and re-read to verify. Report unavailable permissions rather than claiming success.
6. Do not create/update schedules, Scan Runs, mail labels or external automations as a side effect of tailoring.

## Ranking
Use optional profile scoring weights to rank roles, considering actual fit, career direction and hard eligibility. A score is not an excuse to invent unsupported expertise, locations or compensation.
