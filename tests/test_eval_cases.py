from __future__ import annotations

import json
import unittest
from pathlib import Path

from career_planning_agent_public.verdict_rules import evaluate_demo_case, required_eval_tags


ROOT = Path(__file__).resolve().parents[1]


class EvalCasesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        path = ROOT / "evals/career_planning_eval_cases.jsonl"
        cls.cases = [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    def test_eval_jsonl_has_ten_cases(self) -> None:
        self.assertEqual(len(self.cases), 10)
        self.assertEqual(len({case["id"] for case in self.cases}), 10)

    def test_required_tags_are_present(self) -> None:
        tags = {tag for case in self.cases for tag in case.get("coverage_tags", [])}
        self.assertEqual(required_eval_tags() - tags, set())

    def test_all_cases_are_simulated_sanitized_and_human_reviewed(self) -> None:
        for case in self.cases:
            with self.subTest(case=case["id"]):
                self.assertIs(case.get("simulated"), True)
                self.assertIs(case.get("sanitized"), True)
                self.assertIs(case.get("must_require_human_review"), True)
                self.assertEqual(case.get("privacy_expectation"), "simulated_sanitized_only")
                self.assertTrue(case.get("must_not_actions"))

    def test_demo_rule_helper_matches_expected_gate(self) -> None:
        for case in self.cases:
            with self.subTest(case=case["id"]):
                result = evaluate_demo_case(case)
                self.assertEqual(result["gate"], case["expected_verdict_or_gate"])
                self.assertIs(result["human_review_required"], True)
                self.assertIs(result["external_side_effects"], False)
                self.assertIs(result["approved_opportunity_created"], False)


if __name__ == "__main__":
    unittest.main()
