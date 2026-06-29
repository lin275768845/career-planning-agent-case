from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SchemaContractsTest(unittest.TestCase):
    def test_schema_json_files_parse(self) -> None:
        for path in sorted((ROOT / "schemas").glob("*.json")):
            with self.subTest(path=path.name):
                data = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(data.get("type"), "object")
                self.assertIn("required", data)
                self.assertIn("properties", data)

    def test_demo_json_files_parse(self) -> None:
        for path in sorted((ROOT / "demo_run").glob("*.json")):
            with self.subTest(path=path.name):
                data = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(data.get("schema_version"), "2026-06-week3")

    def test_key_schema_contracts_stay_public_safe(self) -> None:
        verdict = json.loads((ROOT / "schemas/opportunity_verdict.schema.json").read_text())
        review = json.loads((ROOT / "schemas/review_decision.schema.json").read_text())

        verdict_required = set(verdict["required"])
        self.assertIn("human_review_required", verdict_required)
        self.assertIn("external_side_effects", verdict_required)
        self.assertIn("approved_opportunity_created", verdict_required)

        review_required = set(review["required"])
        self.assertIn("human_confirmed", review_required)
        self.assertIn("external_action", review_required)
        self.assertIn("message_send", review_required)


if __name__ == "__main__":
    unittest.main()
