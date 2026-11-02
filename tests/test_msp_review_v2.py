"""Review-revision 2 synthetic examples, compatibility and evidence integrity checks."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / 'examples/msp'
SCRIPT = ROOT / 'tools/validate_msp.py'
spec = importlib.util.spec_from_file_location('msp_review2_checks', SCRIPT)
msp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(msp)


class Review2Checks(unittest.TestCase):
    def test_review2_expected_outcomes_and_cli(self):
        for case in json.loads((EXAMPLES / 'expected_outcomes_v2.json').read_text())['cases']:
            with self.subTest(fixture=case['file']):
                result = subprocess.run([sys.executable, '-B', str(SCRIPT), str(EXAMPLES / case['file'])],
                                        text=True, capture_output=True)
                self.assertEqual(result.returncode, case['expected_exit'], result.stdout + result.stderr)
                output = json.loads(result.stdout)
                self.assertEqual(sorted({e['code'] for e in output['errors']}), case['expected_error_codes'])
                self.assertEqual(sorted({e['code'] for e in output['limitations']}), case['expected_limitation_codes'])

    def test_legacy_fixture_bytes_and_outcomes_match_public_golden_pins(self):
        # Public synthetic pins replace private snapshot access. This checks bytes
        # and outcomes, not custody or completeness of the development archive.
        oracle = json.loads((EXAMPLES / 'expected_outcomes.json').read_text())
        for case in oracle['cases']:
            with self.subTest(fixture=case['file']):
                fixture = EXAMPLES / case['file']
                self.assertEqual(hashlib.sha256(fixture.read_bytes()).hexdigest(),
                                 case['synthetic_fixture_sha256'])
                current = msp.load_document(fixture)
                output = msp.validate(current)
                self.assertEqual(sorted({e['code'] for e in output['errors']}), case['expected_error_codes'])
                self.assertEqual(sorted({e['code'] for e in output['limitations']}), case['expected_limitation_codes'])
                self.assertIn('Legacy', output['check_scope'])

    def test_status_dimensions_do_not_follow_acceptance(self):
        data = msp.load_document(EXAMPLES / 'v2_valid_accepted_unverified.json')
        self.assertTrue(msp.validate(data)['valid_structure'])
        self.assertEqual(data['proposals'][0]['canonical_record']['lifecycle'], 'source-candidate')
        self.assertEqual(data['proposals'][0]['scientific_evidence']['status'], 'not_independently_verified')
        # A source's own state labels are not a prescribed DRM canonical state machine.
        data['proposals'][0]['canonical_record']['lifecycle'] = 'source-owned-review-label'
        self.assertTrue(msp.validate(data)['valid_structure'])
        # Rejection for inadequate scientific evidence must remain expressible.
        data = msp.load_document(EXAMPLES / 'v2_valid_accepted_unverified.json')
        proposal = data['proposals'][0]
        proposal['state'] = 'rejected'
        proposal['change_history'][-1]['state'] = 'rejected'
        proposal['change_history'][-1]['decision']['purpose'] = 'scientific_acceptance'
        self.assertTrue(msp.validate(data)['valid_structure'])

    def test_file_bytes_and_pins_are_checked_without_cwd_assumptions(self):
        data = msp.load_document(EXAMPLES / 'v2_valid_file_edition.json')
        self.assertFalse(msp.validate(data)['valid_structure'])  # explicit base needed
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            (base / 'evidence').mkdir()
            file = base / 'evidence/synthetic_source.txt'
            file.write_bytes((EXAMPLES / 'evidence/synthetic_source.txt').read_bytes())
            self.assertTrue(msp.validate(data, base_dir=base)['valid_structure'])
            file.write_text('An edited edition must not replace the old citation.')
            self.assertIn('EDITION_HASH_MISMATCH', {e['code'] for e in msp.validate(data, base_dir=base)['errors']})

    def test_bad_review2_containers_fail_without_crashing(self):
        original = msp.load_document(EXAMPLES / 'v2_valid_accepted_unverified.json')
        for field in ['evidence_editions', 'format_version']:
            for value in [None, {}, [], True]:
                data = copy.deepcopy(original)
                data[field] = value
                with self.subTest(root_field=field, value=value):
                    self.assertFalse(msp.validate(data)['valid_structure'])
        for field in ['canonical_record', 'scientific_evidence', 'rights', 'asserting_authority']:
            for value in [None, [], 'bad', True]:
                data = copy.deepcopy(original)
                data['proposals'][0][field] = value
                with self.subTest(proposal_field=field, value=value):
                    self.assertFalse(msp.validate(data)['valid_structure'])
        data = copy.deepcopy(original)
        data['proposals'][0]['change_history'][-1]['decision']['reviews'] = []
        self.assertIn('REQUIRED_SCOPED_REVIEW_MISSING', {e['code'] for e in msp.validate(data)['errors']})

    def test_template_stays_unpopulated_and_declares_limits(self):
        data = msp.load_document(ROOT / 'templates/development_register.template.json')
        self.assertEqual(data['proposals'], [])
        output = msp.validate(data)
        self.assertTrue(output['valid_structure'])
        self.assertEqual({e['code'] for e in output['limitations']}, {'RIGHTS_UNKNOWN', 'SENSITIVITY_UNKNOWN'})
        self.assertIn('actual reviewer authority are not verified', output['assurance'])


if __name__ == '__main__':
    unittest.main()
