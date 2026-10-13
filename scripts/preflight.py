#!/usr/bin/env python3
"""Validate *local syntax* for resume tailoring setup; never uses network/OAuth."""
import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

SHEET = re.compile(r"^/spreadsheets/d/([A-Za-z0-9_-]+)(?:/|$)")
DOC = re.compile(r"^/document/d/([A-Za-z0-9_-]+)(?:/|$)")
FOLDER = re.compile(r"^/drive/folders/([A-Za-z0-9_-]+)(?:/|$)")


def valid_resource(url, host, path_re):
    if not isinstance(url, str) or not url:
        return False
    p = urlparse(url)
    return p.scheme == "https" and p.hostname == host and bool(path_re.match(p.path))


def check(profile, resources, mode="tailor"):
    """Return problems. Modes: analysis (sources only), tailor (save), tracking (sheet)."""
    if mode not in ("analysis", "tailor", "tracking"):
        return ["Unknown preflight mode."]
    errors = []
    career = profile.get("career", {})
    if not career.get("target_roles") or not isinstance(career["target_roles"], list):
        errors.append("Candidate profile needs at least one target role.")
    if not career.get("primary_technologies") or not isinstance(career["primary_technologies"], list):
        errors.append("Candidate profile needs a list of actual primary technologies.")
    if mode in ("analysis", "tailor"):
        links = [resources.get("master_resume_doc_url")] + resources.get("base_resume_doc_urls", [])
        if not any(valid_resource(link, "docs.google.com", DOC) for link in links):
            errors.append("At least one valid Google Docs Base/Master Resume URL is needed for Doc-based tailoring.")
        for link in links:
            if link and not valid_resource(link, "docs.google.com", DOC):
                errors.append("Invalid Base/Master Resume Google Docs URL.")
        if not valid_resource(resources.get("career_story_bank_doc_url"), "docs.google.com", DOC):
            errors.append("Missing/invalid Career Story Bank Google Doc URL.")
        if mode == "tailor" and not valid_resource(resources.get("resume_output_folder_url"), "drive.google.com", FOLDER):
            errors.append("Missing/invalid output Google Drive folder URL.")
    if mode == "tracking":
        if not valid_resource(resources.get("tracker_spreadsheet_url"), "docs.google.com", SHEET):
            errors.append("Missing/invalid optional tracking Google Sheet URL.")
        tabs = resources.get("sheet_tabs", {})
        for key in ("companies", "open_jobs", "applications"):
            if not isinstance(tabs.get(key), str) or not tabs.get(key).strip():
                errors.append("Missing Sheet tab mapping: " + key)
        scoring = profile.get("optional_job_tracking", {}).get("scoring", {})
        if scoring and (
            not all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in scoring.values())
            or sum(scoring.values()) != 100
        ):
            errors.append("Optional job scoring weights must be numbers totaling 100.")
    return errors


def main():
    parser = argparse.ArgumentParser(description="Local URL/profile checks only; no Google authorization")
    parser.add_argument("--profile", required=True, type=Path)
    parser.add_argument("--resources", required=True, type=Path)
    parser.add_argument("--mode", choices=["analysis", "tailor", "tracking"], default="tailor")
    args = parser.parse_args()
    try:
        profile = json.loads(args.profile.read_text(encoding="utf-8"))
        resources = json.loads(args.resources.read_text(encoding="utf-8"))
    except (OSError, ValueError) as err:
        print("CONFIG ERROR:", err, file=sys.stderr)
        return 2
    errors = check(profile, resources, args.mode)
    if errors:
        for err in errors:
            print("BLOCKED:", err)
        print("Live Google permissions and PDF page verification: NOT TESTED")
        return 1
    print("PASS: Required profile fields and link syntax for", args.mode, "mode.")
    print("NOT VERIFIED: Google OAuth, Docs content, folder writes, live JD or PDF pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
