# User decisions vs. submitted applications

## Explicit choices
- `Interested`, `plan to apply`, `Apply job #1 later`: after resolving a stable job ID/URL, set review state Interested where permitted, preserving old notes. Do NOT create a submitted application row.
- `Skip`: preserve stated reason verbatim or summarized faithfully in appended notes; never create Applications row.
- `Closed`: only when official evidence supports closure and handling respects old Applied/Skip decisions. Preserve the historical decision if re-reviewing availability.
- No response to a recommendation means `New`, not Skip.

## Confirmed submission
Only after an unambiguous explicit submission confirmation or a trustworthy confirmation the user asks to record:
1. Verify the company/title/ATS ID against current Open Jobs and Applications.
2. Mark matching prospective role Applied, preserving notes/history.
3. Insert or update Applications for the actual attempt; preserve dates, old emails, previous stages and manually authored fields. Deduplicate by stable role and attempt when repeat applications are possible.
4. Re-read both places and report actual updates; do not invent a confirmation from a generated resume.

## Gmail (optional, separate connector)
With explicit user authorization and a separately defined Gmail reconciliation workflow, track stage transitions and actionable replies. Match unambiguously; avoid status regression; retain processed/reviewable mail and append history. Never create a submitted application from an email alone without corroboration. Gmail is NOT required for base manager setup.
