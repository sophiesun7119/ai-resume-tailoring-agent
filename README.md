# AI Resume Tailoring Agent

**Turn a job description into an evidence-backed, role-specific resume—without inventing qualifications or overwriting the original.**

An open, reusable **human-approved AI skill** that compares a real job description (JD) with a candidate's Base/Master Resume and Career Story Bank, selects relevant experience, and helps create a formatted copy of the resume in Google Docs. Optional job discovery and Google Sheets tracking are supported, **not required**.

> This is an instruction-driven skill for a compatible AI assistant with authorized Google Docs/Drive and web/PDF tools. It is **not** an autonomous application bot, hosted OAuth service, or standalone resume generator.

## Primary workflow

```text
JD (official link or pasted text)
          +
Candidate Profile + Base/Master Resume(s) + Career Story Bank
          |
   JD requirements & evidence matching
          |
Select best resume base + propose scoped edits
          |
     Human reviews material rewrites
          |
Copy original Google Doc → tailored Google Doc in output folder
          |
Export / render PDF → verify page count & visual layout
          |
Share Google Doc, verified PDF (if supported) & change log
```

**Never** invent skills, remove accomplishments silently, change a master/base resume, or claim that a PDF is one page without checking its rendered pages. Applications are **never** submitted automatically.

## Quick start: JD + your own resume

1. Clone or download this repository, or install its skill bundle in a compatible skill-capable assistant. Copying files alone does not connect Google or create a running agent.
2. Tell your assistant: **"Read SKILL.md. Help me configure AI Resume Tailoring Agent. Do not edit any documents yet."**
3. Provide:
   - **Candidate Profile:** target roles, experience level, technologies, location/preferences and editing restrictions (or answer a few onboarding questions).
   - **Job Description:** official job link **or** pasted JD text. You can supply this later on each tailoring request.
   - **Google Docs:** **at least one** Base/Master Resume link, a Career Story Bank Doc link, and a Drive output-folder link. You may provide several Base resumes (e.g., backend/cloud/AI); the assistant should recommend the most relevant original before copying it.
4. Connect Google Docs/Drive through the assistant's official connector/OAuth settings. The assistant checks read access to each source Doc and folder metadata before any edit. For a first document copy, confirm actual write permission with an authorized operation; metadata alone does not prove it.
5. Start with a **read-only JD/evidence analysis**, review the proposed targeted changes, then explicitly approve document creation. **Substantial bullet rewrites or deletions require line-by-line approval.**

Optional: connect a tracker Google Sheet to discover company jobs, preserve decisions and record applications **after actual submission**. The basic JD → Resume workflow **does not need a Sheet**.

### Private configuration (optional)

Copy `config/profile.example.json` → `config/profile.local.json` and `config/resources.example.json` → `config/resources.local.json`. These `*.local.json` files are Git-ignored. Do not upload personal resumes, real Google IDs, or access tokens to this public repository.

Syntax-only preflight (Python standard library, no network/OAuth):

```bash
python3 scripts/preflight.py --profile config/profile.local.json --resources config/resources.local.json
python3 -m unittest discover -s tests -v
```

The preflight checks the resume paths and config shape; actual Google authorization, PDF rendering and JD verification happen **in the connected assistant**, not in this script. See [onboarding and permission gates](references/setup-guide.md).

## A realistic example

Try a fictional role described in [sample-jd.md](examples/sample-jd.md), view the [JD-to-evidence comparison](examples/requirement-evidence-matrix.md), and inspect the [proposed edit and approval example](examples/sample-review.md). The examples are **mock data**, not claims of a live job or a completed PDF.

## What is optional vs. essential?

| Capability | Needed for |
| --- | --- |
| Candidate Profile + one Resume Doc + Story Bank Doc | Source-backed personalization and story selection |
| JD link **or** pasted JD | Requirement analysis |
| Connected Google Docs/Drive + output folder | Create a native Google Doc copy |
| Working PDF export **and** PDF viewer | Verify an actual one-page PDF |
| Google Sheet + Sheets permission | **Optional** tracking and company/job audit |
| Official careers browsing | **Optional** official posting verification and discovery |
| Gmail + scheduling | **Out of scope**; separate setup, never installed automatically |

If a source is missing, report the limitation and request it before making unsupported claims. When export/viewer is unavailable, deliver the Doc and label PDF verification **not performed**.

## Engineering safeguards

- **Evidence first:** classify JD requirements as demonstrated, transferable, gap or unknown; quote source-backed achievements rather than generating plausible-sounding bullets.
- **Human-in-the-loop:** show material before/after text for approval; preserve dense technical bullets and one-page layout unless the user authorizes changes.
- **Non-destructive:** copy the most suitable Base Resume; never overwrite an original.
- **Truthful verification:** Google export success is not PDF page-count proof.
- **Small, inspectable actions:** track what changed and surface unsupported keywords or required permissions.

## Connected projects

- [ATS collector — search-job](https://github.com/sophiesun7119/search-job): separate Python/SQLite job ingestion implementation.
- [Scheduler prompt generator](https://github.com/sophiesun7119/search-job-scheduler-prompt-tool): separate company/job discovery scheduler templates.
- This repo: **JD matching + evidence-backed resume tailoring**. The wider lifecycle can be showcased in a separate portfolio/case-study repo.

## Boundaries & privacy

This Skill cannot grant OAuth permissions, browse private Docs without a connector, guarantee Google Docs layout, or submit job applications. Only fictional examples/configs are public. See [privacy checklist](references/privacy-and-security.md).

License: [MIT](LICENSE).
