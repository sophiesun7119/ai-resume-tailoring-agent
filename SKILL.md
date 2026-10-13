---
name: job-application-manager
description: Configure and operate an evidence-based, human-approved job application review workflow using a candidate profile and user-authorized Google Sheets, Google Docs, and Google Drive folder. Use when someone wants to set up their job tracker, review a company and official ATS jobs, rank fits, mark interests/skips, tailor a resume after selection, or record a confirmed application. Require first-run onboarding and connector checks before live writes.
---

# Job Application Manager

## Purpose
Run the user-controlled, on-demand lifecycle from company review to confirmed application tracking. This skill is an instruction-driven integration, NOT a self-running daemon, scheduler, applicant-bot, or OAuth implementation. The assistant's actual connector permissions determine which stages are possible.

## First run: mandatory onboarding
1. Read [setup-guide.md](references/setup-guide.md). Never use creator-specific defaults or hardcoded IDs. If no user profile and resource bindings are provided, ask for the missing inputs in small conversational groups, starting with the profile and the Google Sheet/Docs/folder links.
2. Read `config/profile.local.json` and `config/resources.local.json` if present and user-authorized, or collect equivalent values in chat. `config/*.example.json` are fictional templates, not connected accounts. Do not publish local config.
3. Verify live Google connector identity and authorization using read-only metadata, current Sheets tabs/headers, source Google Docs and target Drive folder. A CLI preflight only checks input syntax; it does NOT verify access. On a missing permission, report the required access and stop before dependent operations.
4. Establish required application tables and status semantics based on [database-rules.md](references/database-rules.md). **Never rewrite a populated schema automatically.** New empty tables/headers require explicit authorization and confirmation.
5. Perform a no-write, one-company dry run with official careers evidence. Summarize what was read, what was blocked, and what user action remains. Switch to controlled writes only with appropriate consent.
6. Do not install or modify any scheduled task or run an hourly Gmail listener without a separate explicit request.

## Commands / intent routing
- `Review Company: <company>` -> [company-audit.md](references/company-audit.md): existing tracker audit, official jobs, incremental review, dedup, fit ranking, official links. No resume creation until the user selects positions.
- `Interested`, `Skip`, `Apply later` -> [decision-tracking.md](references/decision-tracking.md): track explicit decision only; intention is never actual submission.
- `Tailor resume for <selected role>` -> [resume-story.md](references/resume-story.md): read live official JD, master resume, story bank, and preserve formatting in an independent document, with PDF visual/page-count validation if supported.
- `I submitted my application` -> [decision-tracking.md](references/decision-tracking.md): confirm job identity, update both Open Jobs and Applications without duplicates.
- `Status / Continue review` -> read the current workbook and prior decisions; avoid reprocessing historical Applied/Skip/Closed entries.

## Always enforce
- Do not auto-submit job applications or autonomously change user decisions.
- Protect manual statuses, notes, first-seen dates, formulas, and original resume/story documents.
- Use official careers/ATS IDs and normalized URLs; report uncertainty and partial scan coverage.
- Separate prospective openings from actually submitted applications.
- Never fabricate skills, numbers, production claims, job availability, PDF fit, or action success.
- Do not expose real profiles, private Google links, emails, secrets, or resumes in output samples or public repositories.
- Only call actions actually available in the hosting environment. If unsupported, deliver a review and precise setup instructions, not a pretend completion.

## References
- [Setup and permissions](references/setup-guide.md)
- [Company audit](references/company-audit.md)
- [Database and fields](references/database-rules.md)
- [User decisions and applications](references/decision-tracking.md)
- [Resume and evidence](references/resume-story.md)
- [Security and publishing](references/privacy-and-security.md)
