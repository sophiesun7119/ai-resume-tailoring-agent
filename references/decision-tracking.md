# Optional human decisions and application tracking

For **JD-to-resume tailoring without a tracker**, decisions are simply approval to edit/copy the resume; do **not** require or create application records.

When the user **opted into** a connected Google Sheet tracker:

- `Interested` / `Apply later` means prospective intent only. If the specific role is identified and the user requests it, preserve existing row notes and set Interested where the schema supports it.
- `Skip` records an explicit opt-out; never infer Skip from silence.
- `Closed` requires official evidence where possible; temporary ATS errors do not establish closed.
- `Applied` requires an explicit actual submission confirmation or reliable evidence the user asks you to record. A tailored Doc or resume download is never proof of submission.

Upon confirmed submission: read current Open Jobs and Applications, identify the exact job by ATS ID/URL and attempt, deduplicate, preserve status history, write only after authorization, and re-read both tables to confirm outcome. Retain manual fields.

Gmail classification and periodic monitoring are separate workflows requiring their own user request, access permissions and status-precedence policy. Do not configure either by default. No automatic job submission.
