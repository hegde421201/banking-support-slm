import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from src.schema import ValidationError, load_jsonl, proposal_hash, validate_records

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "examples/starter_cases.jsonl"


class SchemaTests(unittest.TestCase):
    def setUp(self):
        self.cases = load_jsonl(SOURCE)
        self.case = copy.deepcopy(self.cases[0])

    def event(self, decision="accept", second=0):
        return {"id": f"test-event-{second}", "case_id": self.case["id"],
                "proposal_sha256": proposal_hash(self.case), "decision": decision,
                "reviewer_id": "fictional-test-reviewer",
                "reviewed_at": f"2026-10-11T10:00:{second:02d}+00:00",
                "correction": copy.deepcopy(self.case["proposal"]) if decision == "edit" else None}

    def test_original_twenty_records_are_unchanged_and_ineligible(self):
        before = copy.deepcopy(self.cases)
        result = validate_records(self.cases)
        self.assertEqual(len(result), 20)
        self.assertTrue(all(r["training_eligible"] is False for r in result))
        self.assertEqual(self.cases, before)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                         "6f39e4b4fa64f580d5c1b54ffd143d171fcf3454ee4d325c8b1570b178145a20")

    def test_missing_and_extra_fields(self):
        for name in self.case:
            with self.subTest(name=name):
                bad = copy.deepcopy(self.case)
                del bad[name]
                with self.assertRaises(ValidationError): validate_records([bad])
        self.case["extra"] = True
        with self.assertRaises(ValidationError): validate_records([self.case])

    def test_bad_types_provenance_and_embedded_approval(self):
        for field, value in [("id", []), ("context", []), ("context", {"x": float("nan")}),
                             ("source_type", "public"), ("author_method", " "),
                             ("policy_version", "v9"), ("split", "test"),
                             ("training_eligible", True), ("training_eligible", 0),
                             ("review_status", "accepted"), ("reviewer_id", "fake"),
                             ("reviewed_at", "2026-10-11")]:
            with self.subTest(field=field, value=value):
                bad = copy.deepcopy(self.case)
                bad[field] = value
                with self.assertRaises(ValidationError): validate_records([bad])

    def test_unknown_and_malformed_decisions(self):
        for field, value in [("intent", "made_up"), ("action", "refund_money"),
                             ("action", []), ("policy_ids", ["P-99"]),
                             ("policy_ids", []), ("policy_ids", [["P-10"]]),
                             ("policy_ids", ["P-10", "P-10"]), ("response", " ")]:
            with self.subTest(field=field):
                bad = copy.deepcopy(self.case)
                bad["proposal"][field] = value
                with self.assertRaises(ValidationError): validate_records([bad])

    def test_duplicate_cases_and_reviews(self):
        with self.assertRaises(ValidationError): validate_records([self.case, self.case])
        event = self.event()
        with self.assertRaises(ValidationError): validate_records([self.case], [event, event])

    def test_broken_and_stale_review_links(self):
        event = self.event()
        event["case_id"] = "absent"
        with self.assertRaises(ValidationError): validate_records([self.case], [event])
        event = self.event()
        self.case["customer_message"] = "Changed source message"
        with self.assertRaises(ValidationError): validate_records([self.case], [event])

    def test_review_fields_identity_time_and_decision(self):
        for field, value in [("reviewer_id", " "), ("reviewed_at", "2026-10-11"),
                             ("reviewed_at", "invalid"), ("decision", "auto_approve"),
                             ("correction", {})]:
            with self.subTest(field=field):
                event = self.event()
                event[field] = value
                with self.assertRaises(ValidationError): validate_records([self.case], [event])
        for field in self.event():
            event = self.event()
            del event[field]
            with self.assertRaises(ValidationError): validate_records([self.case], [event])

    def test_accept_edit_reject_defer_and_reaccept(self):
        events = []
        for second, decision in enumerate(["accept", "edit", "reject", "defer", "accept"]):
            event = self.event(decision, second)
            if decision == "edit": event["correction"]["response"] = "Corrected test response"
            events.append(event)
            result = validate_records([self.case], events)[0]
            self.assertEqual(result["training_eligible"], decision in {"accept", "edit"})
            expected = event["correction"] if decision == "edit" else self.case["proposal"]
            self.assertEqual(result["effective_proposal"], expected)

    def test_edit_validation_and_input_immutability(self):
        event = self.event("edit")
        before = copy.deepcopy((self.case, event))
        result = validate_records([self.case], [event])[0]
        result["effective_proposal"]["response"] = "Changed derived output"
        result["review"]["reviewer_id"] = "Changed derived reviewer"
        self.assertEqual((self.case, event), before)
        event["correction"]["action"] = "transfer_funds"
        with self.assertRaises(ValidationError): validate_records([self.case], [event])

    def test_review_order_and_timezone_equivalence(self):
        first, second = self.event(second=1), self.event(second=2)
        second["reviewed_at"] = "2026-10-11T15:30:01+05:30"
        with self.assertRaises(ValidationError): validate_records([self.case], [first, second])
        with self.assertRaises(ValidationError):
            validate_records([self.case], [self.event(second=2), self.event(second=1)])

    def test_strict_json_and_cli_failure(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.jsonl"
            for value in ['{"id":1,"id":2}', '{"x":NaN}', '{bad}', '', '\n']:
                path.write_text(value, encoding="utf-8")
                with self.assertRaises(ValidationError): load_jsonl(path)
            path.write_text(json.dumps({"training_eligible": True}), encoding="utf-8")
            run = subprocess.run([sys.executable, str(ROOT / "src/schema.py"), str(path)],
                                 capture_output=True, text=True)
            self.assertEqual(run.returncode, 1)
            self.assertIn("Validation failed", run.stderr)

    def test_cli_success(self):
        run = subprocess.run([sys.executable, str(ROOT / "src/schema.py"), str(SOURCE)],
                             capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(run.stdout), {"valid_records": 20, "training_eligible": 0})


if __name__ == "__main__":
    unittest.main()
