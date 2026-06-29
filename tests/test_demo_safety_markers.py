from __future__ import annotations

import json
import unittest
from pathlib import Path

from career_planning_agent_public.gates import (
    approval_gate,
    decision_ownership_gate,
    privacy_gate,
    public_mirror_gate,
)
from career_planning_agent_public.models import DemoReviewDecision, DemoVerdict


ROOT = Path(__file__).resolve().parents[1]


class DemoSafetyMarkersTest(unittest.TestCase):
    def test_all_demo_json_artifacts_have_safety_markers(self) -> None:
        for path in sorted((ROOT / "demo_run").glob("*.json")):
            with self.subTest(path=path.name):
                data = json.loads(path.read_text(encoding="utf-8"))
                safety = data.get("artifact_safety")
                self.assertIsInstance(safety, dict)
                self.assertIs(safety.get("simulated"), True)
                self.assertIs(safety.get("sanitized"), True)
                self.assertIs(safety.get("contains_real_personal_data"), False)
                self.assertIs(safety.get("contains_real_resume"), False)
                self.assertIs(safety.get("contains_real_jd_export"), False)
                self.assertIs(safety.get("external_application_submitted"), False)
                self.assertIs(safety.get("external_message_sent"), False)
                self.assertTrue(privacy_gate(data).passed)
                self.assertTrue(public_mirror_gate(data).passed)

    def test_verdict_demo_requires_human_review_and_no_approved_opportunity(self) -> None:
        data = json.loads((ROOT / "demo_run/demo_opportunity_verdict.json").read_text())
        verdict = DemoVerdict.from_mapping(data)
        self.assertTrue(verdict.human_review_required)
        self.assertFalse(verdict.approved_opportunity_created)
        self.assertFalse(verdict.message_sent)
        self.assertFalse(verdict.application_submitted)
        self.assertFalse(verdict.external_channel_used)
        self.assertIn("no_auto_apply", verdict.prohibited_actions)
        self.assertIn("no_auto_message", verdict.prohibited_actions)

    def test_review_decision_has_no_external_action_or_message(self) -> None:
        data = json.loads((ROOT / "demo_run/demo_review_decision.json").read_text())
        decision = DemoReviewDecision.from_mapping(data)
        self.assertTrue(decision.human_confirmed)
        self.assertFalse(decision.approved_opportunity_created)
        self.assertFalse(decision.external_action_performed)
        self.assertFalse(decision.message_sent)

    def test_gate_helpers_block_forbidden_public_actions(self) -> None:
        forbidden = (
            "auto_apply",
            "auto_send",
            "auto_approved_opportunity",
            "send_message",
            "apply_to_job",
            "scrape_platform",
        )
        for action in forbidden:
            with self.subTest(action=action):
                self.assertFalse(approval_gate(action, human_confirmed=True).passed)
                self.assertFalse(
                    decision_ownership_gate(action, actor="human", human_confirmed=True).passed
                )
                self.assertFalse(public_mirror_gate({}, requested_action=action).passed)

    def test_decision_ownership_blocks_ai_commitment(self) -> None:
        result = decision_ownership_gate(
            "create_approved_opportunity",
            actor="ai",
            human_confirmed=False,
        )
        self.assertFalse(result.passed)
        self.assertEqual(result.gate, "decision_ownership_gate")


if __name__ == "__main__":
    unittest.main()
