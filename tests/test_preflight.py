import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("preflight", ROOT / "scripts" / "preflight.py")
preflight = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preflight)


class PreflightTests(unittest.TestCase):
    def setUp(self):
        self.profile = json.loads((ROOT / "config" / "profile.example.json").read_text())
        self.resources = json.loads((ROOT / "config" / "resources.example.json").read_text())

    def bind_sources(self):
        self.resources.update(
            master_resume_doc_url="https://docs.google.com/document/d/demo_base_123/edit",
            career_story_bank_doc_url="https://docs.google.com/document/d/demo_story_123/edit",
            resume_output_folder_url="https://drive.google.com/drive/folders/demo_folder_123",
        )

    def test_no_sources_fail_analysis(self):
        self.assertTrue(preflight.check(self.profile, self.resources, "analysis"))

    def test_jd_analysis_does_not_require_sheet_or_folder(self):
        self.bind_sources()
        self.resources["resume_output_folder_url"] = ""
        self.assertEqual([], preflight.check(self.profile, self.resources, "analysis"))

    def test_doc_creation_requires_folder(self):
        self.bind_sources()
        self.assertEqual([], preflight.check(self.profile, self.resources, "tailor"))
        self.resources["resume_output_folder_url"] = ""
        self.assertTrue(any("folder" in x for x in preflight.check(self.profile, self.resources, "tailor")))

    def test_multiple_base_resumes_optional_master(self):
        self.bind_sources()
        self.resources["master_resume_doc_url"] = ""
        self.resources["base_resume_doc_urls"] = ["https://docs.google.com/document/d/demo_cloud_456/edit"]
        self.assertEqual([], preflight.check(self.profile, self.resources, "tailor"))

    def test_reject_fake_docs_host(self):
        self.bind_sources()
        self.resources["master_resume_doc_url"] = "https://evil.example.com/document/d/base/edit"
        self.assertTrue(any("Resume" in x for x in preflight.check(self.profile, self.resources, "tailor")))

    def test_tracking_only_requires_sheet_in_tracking_mode(self):
        self.bind_sources()
        self.assertEqual([], preflight.check(self.profile, self.resources, "tailor"))
        self.assertTrue(preflight.check(self.profile, self.resources, "tracking"))
        self.resources["tracker_spreadsheet_url"] = "https://docs.google.com/spreadsheets/d/demo_sheet_123/edit"
        self.assertEqual([], preflight.check(self.profile, self.resources, "tracking"))

    def test_optional_scoring_must_sum_to_100(self):
        self.resources["tracker_spreadsheet_url"] = "https://docs.google.com/spreadsheets/d/demo_sheet_123/edit"
        self.profile["optional_job_tracking"]["scoring"]["location"] = 25
        self.assertTrue(any("100" in x for x in preflight.check(self.profile, self.resources, "tracking")))


if __name__ == "__main__":
    unittest.main()
