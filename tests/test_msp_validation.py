"""Synthetic Phase 3 structural checks, not historical/Phase 7 conformance tests."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools/validate_msp.py"
spec = importlib.util.spec_from_file_location("msp_candidate_checks", SCRIPT)
msp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(msp)
EXAMPLES = ROOT / "examples/msp"


class MSPExampleChecks(unittest.TestCase):
    def test_fixture_expectations_and_cli(self):
        manifest = json.loads((EXAMPLES / "expected_outcomes.json").read_text())
        for case in manifest["cases"]:
            with self.subTest(fixture=case["file"]):
                result = subprocess.run([sys.executable, "-B", str(SCRIPT),
                                         str(EXAMPLES / case["file"])],
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, case["expected_exit"], result.stdout + result.stderr)
                data = json.loads(result.stdout)
                self.assertEqual(sorted({e["code"] for e in data["errors"]}), case["expected_error_codes"])
                self.assertEqual(sorted({e["code"] for e in data["limitations"]}), case["expected_limitation_codes"])
                self.assertEqual(data["valid_structure"], case["expected_exit"] == 0)

    def test_template_is_not_operational(self):
        data = msp.load_document(ROOT / "templates/development_register.template.json")
        self.assertEqual(data["proposals"], [])
        self.assertTrue(msp.validate(data)["valid_structure"])
        data["proposals"] = [data["proposal_template"]]
        self.assertFalse(msp.validate(data)["valid_structure"])

    def test_bad_container_types_do_not_crash_or_pass(self):
        valid = msp.load_document(EXAMPLES / "valid_register.json")
        for value in [None, [], "text", 1, True]:
            with self.subTest(root=value):
                self.assertFalse(msp.validate(value)["valid_structure"])
        for key in ["proposals", "known_material", "classification_schemes", "relationship_types"]:
            for value in [None, {}, "text", True]:
                data = copy.deepcopy(valid)
                data[key] = value
                with self.subTest(key=key, value=value):
                    self.assertFalse(msp.validate(data)["valid_structure"])
        for key in ["versions", "change_history", "provenance", "affected_material"]:
            data = copy.deepcopy(valid)
            data["proposals"][0][key] = None
            with self.subTest(proposal_field=key):
                self.assertFalse(msp.validate(data)["valid_structure"])

    def test_same_identifier_allowed_in_different_material_scope(self):
        data = msp.load_document(EXAMPLES / "valid_register.json")
        self.assertTrue(msp.validate(data)["valid_structure"])
        data["known_material"].append(copy.deepcopy(data["known_material"][0]))
        self.assertIn("DUPLICATE_ID", {e["code"] for e in msp.validate(data)["errors"]})

    def test_declared_authority_and_verification_are_not_authenticated(self):
        data = msp.load_document(EXAMPLES / "valid_register.json")
        data["proposals"][0]["provenance"][0]["evidence_status"] = "independently_verified"
        result = msp.validate(data)
        self.assertTrue(result["valid_structure"])
        self.assertIn("actual reviewer authority are not verified", result["assurance"])

    def test_input_errors_and_duplicate_keys_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            for text in ["{", '{"a":1,"a":2}', '{"a":NaN}', '{"a":Infinity}']:
                path.write_text(text)
                with self.subTest(text=text):
                    result = subprocess.run([sys.executable, "-B", str(SCRIPT), str(path)],
                                            capture_output=True, text=True)
                    self.assertEqual(result.returncode, 2)
                    self.assertEqual(json.loads(result.stdout)["outcome"], "input_error")


if __name__ == "__main__":
    unittest.main()
