# Optional: official company/job audit before resume tailoring

This extension runs **only when asked to review a company or select a job**. A Google Sheet is optional; a direct JD link/paste can skip this entire workflow.

1. If the user provided a tracker Sheet, read current company eligibility, open jobs, submitted applications, and manual decisions using [database-rules.md](database-rules.md). Preserve prior Applied, Skip and Closed decisions. If there is no tracker, research the official site without inventing history.
2. Check the company's official careers/ATS site for current openings; do not trust aggregator-only URLs. If browsing unavailable, label verification blocked and use any JD supplied by the user.
3. Identify new/unprocessed jobs with stable provider/ATS requisition ID and normalized official URL; reject duplicates, preserving First Seen, human notes and statuses.
4. Check role/level/location and hard requirements against the candidate profile. Rank strongly relevant roles using evidence from Base Resumes and Story Bank; include official job links and disclose uncertainties or incomplete scans.
5. If requested, write only authorized, verified new Sheet records with deduplication and readback. Never automatically mark closed after a temporary web failure or reactivate an Inactive/Cooldown company.
6. **Wait for user selection** before tailoring any resume. If the user already provided a specific JD for tailoring, that counts as selected and no company audit is required.
7. Report what was checked, what was new, what was uncertain, what changed in Sheets (if anything), and what needs approval.
