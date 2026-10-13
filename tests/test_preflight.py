import importlib.util
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('preflight',ROOT/'scripts'/'preflight.py')
preflight=importlib.util.module_from_spec(spec)
spec.loader.exec_module(preflight)


class PreflightTests(unittest.TestCase):
    def setUp(self):
        self.profile=json.loads((ROOT/'config'/'profile.example.json').read_text())
        self.resources=json.loads((ROOT/'config'/'resources.example.json').read_text())

    def test_empty_real_links_fail_closed(self):
        errors=preflight.check(self.profile,self.resources)
        self.assertEqual(4,len([e for e in errors if 'url' in e.lower()]))

    def test_valid_syntactic_links(self):
        self.resources.update(tracker_spreadsheet_url='https://docs.google.com/spreadsheets/d/demo_sheet_123/edit',master_resume_doc_url='https://docs.google.com/document/d/demo_doc_123/edit',career_story_bank_doc_url='https://docs.google.com/document/d/demo_story_123/edit',resume_output_folder_url='https://drive.google.com/drive/folders/demo_folder_123')
        self.assertEqual([],preflight.check(self.profile,self.resources))

    def test_block_non_google_links(self):
        self.resources['tracker_spreadsheet_url']='https://evil.example.com/spreadsheets/d/abc/edit'
        self.assertFalse(preflight.valid_resource(self.resources['tracker_spreadsheet_url'],'docs.google.com',preflight.SHEET))

    def test_bad_weights(self):
        self.profile['scoring']['location']=25
        self.assertTrue(any('100' in x for x in preflight.check(self.profile,self.resources)))


if __name__=='__main__':
    unittest.main()
