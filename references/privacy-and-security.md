# Public repository privacy checklist

- Never publish private candidate profiles, actual Google Sheet/Doc/Drive IDs, resumes, Story Bank, recruiters' names or emails, internal company datasets, real application history, OAuth tokens, passwords, API keys or unredacted screen captures.
- Public artifacts are **fictional** profiles, dummy resource binding keys with empty strings, generic Markdown workflow references, and mock jobs using `example.com` domains.
- Add `.gitignore` before creating local config; ignore `config/*.local.json`, `.env`, private source documents, output, credentials and spreadsheets. Inspect `git status` and `git diff --cached` before committing.
- For screenshots, remove personally identifying details, employer-only details, Google account identity, record-specific IDs, private scores, and any exposed token or query parameters. Prefer generated mock visuals.
- If creating a demo from real application data, generate synthetic records instead of merely changing names; dates, combinations and employer notes may still identify the user.
- Configure authorization only in the host's official connector/OAuth flow. Public repo can't grant Google file access. Ask only for minimum permissions and avoid writes during permission preflight.
- Do not claim zero risk of accidental disclosure. Do not publish until a human reviews every new file and Git diff. Do not auto-enable jobs/Gmail schedules.
