#!/usr/bin/env python3
"""Local *syntax* preflight only. Never accesses or validates Google OAuth."""
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
    return p.scheme == 'https' and p.hostname == host and bool(path_re.match(p.path))


def check(profile, resources):
    errors = []
    career = profile.get('career', {})
    prefs = profile.get('preferences', {})
    if not isinstance(career.get('target_roles'), list) or not career['target_roles']:
        errors.append('Candidate profile requires at least one target role.')
    if not isinstance(career.get('primary_technologies'), list) or not career['primary_technologies']:
        errors.append('Candidate profile requires primary technologies (or a truthful unknown list).')
    if not prefs.get('country'):
        errors.append('Candidate profile requires a preferred work country.')
    scoring = profile.get('scoring', {})
    if scoring and (not all(isinstance(v, (int, float)) for v in scoring.values()) or sum(scoring.values()) != 100):
        errors.append('Profile scoring weights must be numeric and total 100.')
    requirements = (
        ('tracker_spreadsheet_url', 'docs.google.com', SHEET),
        ('master_resume_doc_url', 'docs.google.com', DOC),
        ('career_story_bank_doc_url', 'docs.google.com', DOC),
        ('resume_output_folder_url', 'drive.google.com', FOLDER),
    )
    for key, host, pattern in requirements:
        if not valid_resource(resources.get(key), host, pattern):
            errors.append(f'Missing or invalid {key}. Supply a full https://{host}/... link.')
    tabs = resources.get('sheet_tabs', {})
    for key in ('companies', 'open_jobs', 'applications'):
        if not isinstance(tabs.get(key), str) or not tabs.get(key).strip():
            errors.append(f'Missing sheet tab mapping: {key}')
    return errors


def main():
    p = argparse.ArgumentParser(description='Check local profile and Google link syntax; NO network/OAuth tests')
    p.add_argument('--profile', type=Path, required=True)
    p.add_argument('--resources', type=Path, required=True)
    args = p.parse_args()
    try:
        profile = json.loads(args.profile.read_text(encoding='utf-8'))
        resources = json.loads(args.resources.read_text(encoding='utf-8'))
    except (OSError, ValueError) as e:
        print(f'CONFIG ERROR: {e}', file=sys.stderr)
        return 2
    errors = check(profile, resources)
    if errors:
        for e in errors:
            print('BLOCKED: ' + e)
        print('Live connector authorization: NOT TESTED')
        return 1
    print('PASS: Profile fields and Google link shapes look valid.')
    print('IMPORTANT: Google permissions, Sheet headers, Drive folder write and ATS reachability are NOT VERIFIED.')
    print('Next: connect Google via the host assistant, run live read-only checks, then one-company dry run.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
