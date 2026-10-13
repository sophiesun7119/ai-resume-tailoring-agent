# Job Application Manager

An open, reusable **human-in-the-loop job application workflow** that connects official ATS job research, a Google Sheets tracker, a master resume, a career story bank, and a Google Drive output folder.

This is the reusable **Job Application Manager** component. It is separate from the [ATS collector](https://github.com/sophiesun7119/search-job) and [scheduler-prompt generator](https://github.com/sophiesun7119/search-job-scheduler-prompt-tool). An optional fourth portfolio repository can explain the full lifecycle and link to all three.

## What you can do

- Audit a company's official career page; discover only **new or unresolved** jobs and deduplicate by requisition ID/normalized URL.
- Rank jobs by **your** technologies, experience, geography and career preferences, with direct official links and explicit hard-requirement gaps.
- Record Interested/Skip decisions without mistaking them for an actual submission.
- Once **you choose a role**, tailor an independent Google Doc from your real resume and story bank; verify a one-page PDF when PDF export/rendering tools are available.
- Only when **you confirm submitting**, update both prospective-job and actual-application records.

## Quick start: bring your own profile and Google links

**You provide:** (1) a candidate profile, (2) a Google Sheet tracker link, (3) a master-resume Google Doc link, (4) a career-story Google Doc link, and (5) a Drive folder link for tailored resumes.

**Your assistant needs:** connected Google Sheets, Google Docs and Drive permissions for these exact files, and a way to inspect official careers/ATS pages. A browser/web capability is required for job verification. PDF rendering/export is required to claim a one-page validation.

1. Download/clone this repository or install the packaged `skill.zip` in a compatible skill-capable assistant. **Cloning alone does not create an agent or grant any app access.**
2. Ask: `Read SKILL.md and help me set up Job Application Manager. Ask for my profile and Google resource links; do not write anything yet.`
3. Optionally copy `config/profile.example.json` to `config/profile.local.json` and `config/resources.example.json` to `config/resources.local.json`. Your AI can help fill them by asking questions. Local files are ignored by Git.
4. Connect your Google account through your assistant's official connector/OAuth flow and grant access to the referenced Sheet, Docs and folder. **Never paste passwords, API keys or OAuth tokens into chat, YAML, JSON or GitHub.**
5. Validate the config structure locally (Python standard library only):

   ```bash
   python3 scripts/preflight.py --profile config/profile.local.json --resources config/resources.local.json
   ```

6. Ask the assistant to run the **read-only connector access check** and a **one-company dry run**. Once the report looks correct, explicitly authorize permitted changes.

### First-run question flow

Your assistant will ask, in ordinary language:

**Profile:** What roles, experience level, primary technologies, work locations/remote policy and career priorities should the matching reflect? What requirements are hard filters versus preferences?

**Resources:** Paste your tracker Google Sheet, master-resume Google Doc, career-story Google Doc, and destination Drive folder links. Confirm which workbook tabs store Companies, Open Jobs, and submitted Applications.

**Authorization:** Connect Google through your assistant's account settings. The assistant verifies metadata and readable content; for writes, confirm compatible sheet headers and write scope. Nothing is shared publicly or submitted on your behalf.

**Dry run:** Name one company to review without changes. Check discovered jobs, eligibility, status preservation and evidence gaps. Then select a job before any resume is made.

## Example configuration

- [Fictional candidate profile](config/profile.example.json)
- [Blank user resource bindings](config/resources.example.json)
- [Mock job records](examples/mock-jobs.json)
- [Illustrative company review](examples/sample-review.md)
- [Setup and permission guide](references/setup-guide.md)

## System boundaries

| Operation | What executes it | Does this repo execute it automatically? |
| --- | --- | --- |
| Validate local configuration syntax | `scripts/preflight.py` | Yes, when you run it |
| Review official careers/ATS pages | Your assistant's web/browser tools | No |
| Read/write Google Sheets/Docs | Your assistant's authorized Google connectors | No |
| Create a formatted tailored resume | Your assistant's Docs/PDF tools after approval | No |
| Submit a job application | The user | **Never** |
| Hourly company/job or Gmail schedules | Separately configured, authorized runtime tasks | **Not included** |

The Python preflight does not contact Google, store credentials or grant permissions. Repo instructions do not guarantee an assistant has connected apps, working web access, local filesystem access or task-scheduling capabilities.

## Engineering safeguards

Official-source provenance; stable ATS identities and normalized URLs; incremental re-review; guarded statuses; preserved manual notes; stage-by-stage approval; resume evidence checks; no invented results; permission gate; explicit report of blocked/partial work.

## Privacy

Only fictional configs and mock examples belong in Git. Actual links, Sheets, resumes, Story Bank, recruiting emails, personal profile, local output, and credentials stay private. Inspect changes with `git diff --cached` before committing. See [publishing checklist](references/privacy-and-security.md).

## Limitations and contributions

This is an **agent instruction/skill package**, not a hosted service, desktop application, independent CLI application bot, or a fully wired OAuth client. It supports a guided connected-assistant workflow; a standalone local runtime would require separately implemented Google OAuth, ATS clients, document rendering and scheduling.

Check `python3 -m unittest discover -s tests -v` for configuration/identity guard tests. Use your own credentials and sources only in an authorized environment. No scheduled automations or existing repositories are changed by installing this package.
