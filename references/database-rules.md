# Google Sheet contract (generic, never hardcode a user's column positions)

## Separate tables and identities

- `Companies`: company name, Tier/priority, company official careers URL, eligibility status, eligibility date, user notes. Example statuses: `Active`, `Inactive`, `Cooldown`. Resolve the LIVE header names and allowed dropdown values rather than assuming this example matches an existing workbook.
- `Open Jobs`: First Seen, Company, Title, Location/Work Mode, Level, Match, Job Link, Status, Notes. Allowed review states where configured: `New`, `Interested`, `Applied`, `Skip`, `Closed`. Status is USER REVIEW, not definitive job availability.
- `Applications` (an existing user's different tab name is supported): Date Applied, Company, Title, Official Job URL/ATS ID, Application Stage, Last Updated, Notes. Contains ACTUALLY submitted applications only.
- Scan Status/Scan Runs and Gmail-derived columns are optional runtime-specific extensions. This on-demand skill does NOT own or modify external scheduler bookkeeping.

## Safe reads/writes

1. Read metadata, exact tab names, headers, validation, formulas and matching rows before any proposed change; reconcile user-specific schema, don't silently migrate.
2. Honor company eligibility gates and next eligible dates. No automatic reactivation of Inactive/Cooldown.
3. Compare stable identity: `(company, provider/ATS namespace, requisition ID)` first, normalized official URL next. Strip tracking query parameters and harmless trailing slashes. On inconclusive identity, STOP and request review, don't blindly append.
4. Preserve First Seen, past human notes, manual decision and Applied/Skip/Closed status; notes are append-only when updating. Do not rewrite a whole row and erase other fields.
5. New relevant verified opening can be appended as `New` with official link. Treat accessibility failure or a 404 as **unknown**, not proof of closure.
6. Any external write must be authorized, targeted, deduplicated, batched where connector supports it, and verified by a fresh read. If blocked, report failure instead of claiming update.
7. Do not change scheduled automations, task prompts, Scan Runs, or unrelated tabs during an on-demand company review.

## Scoring
Use profile weights and user's hard requirements; if a hard requirement is unknown, describe uncertainty. Evidence labels: direct, transferable, missing, unknown. Keep tracker score separate from recommendation priority. Never manufacture dates or compensation.
