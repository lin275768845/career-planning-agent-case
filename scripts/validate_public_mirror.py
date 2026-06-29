#!/usr/bin/env python3
"""Validate the sanitized Career Planning Agent public mirror.

Standard library only. This script performs static checks on public artifacts.
It does not call networks, providers, browsers, career platforms, message
channels, or the private app.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from career_planning_agent_public.gates import public_mirror_gate
from career_planning_agent_public.models import DemoReviewDecision, DemoVerdict
from career_planning_agent_public.verdict_rules import evaluate_demo_case, required_eval_tags


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def pass_check(message: str) -> None:
    print(f"PASS: {message}")


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def check_json_files() -> int:
    for path in sorted((ROOT / "schemas").glob("*.json")):
        data = load_json(path)
        if not isinstance(data, dict) or data.get("type") != "object":
            return fail(f"invalid schema contract: {path.relative_to(ROOT)}")
    pass_check("schema JSON files parse")

    for path in sorted((ROOT / "demo_run").glob("*.json")):
        data = load_json(path)
        if not isinstance(data, dict) or data.get("schema_version") != "2026-06-week3":
            return fail(f"invalid demo JSON: {path.relative_to(ROOT)}")
    pass_check("demo JSON files parse")
    return 0


def load_eval_cases() -> list[dict[str, object]]:
    path = ROOT / "evals/career_planning_eval_cases.jsonl"
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def check_eval_cases() -> int:
    cases = load_eval_cases()
    if len(cases) != 10:
        return fail(f"expected 10 eval cases, found {len(cases)}")
    ids = [str(case.get("id", "")) for case in cases]
    if len(set(ids)) != len(ids):
        return fail("duplicate eval case ids")
    tags = {tag for case in cases for tag in case.get("coverage_tags", [])}
    missing = required_eval_tags() - tags
    if missing:
        return fail("missing eval tags: " + ", ".join(sorted(missing)))
    for case in cases:
        if case.get("simulated") is not True or case.get("sanitized") is not True:
            return fail(f"{case.get('id')} is not simulated and sanitized")
        if case.get("must_require_human_review") is not True:
            return fail(f"{case.get('id')} does not require human review")
        if not case.get("must_not_actions"):
            return fail(f"{case.get('id')} has no must_not_actions")
        result = evaluate_demo_case(case)
        if result["gate"] != case.get("expected_verdict_or_gate"):
            return fail(f"{case.get('id')} rule helper mismatch")
    pass_check("eval JSONL has 10 cases and required safety tags")
    return 0


def check_demo_safety() -> int:
    for path in sorted((ROOT / "demo_run").glob("*.json")):
        data = load_json(path)
        if not isinstance(data, dict):
            return fail(f"demo artifact is not an object: {path.relative_to(ROOT)}")
        result = public_mirror_gate(data)
        if not result.passed:
            return fail(f"{path.relative_to(ROOT)} failed public mirror gate: {result.reason}")

    verdict_data = load_json(ROOT / "demo_run/demo_opportunity_verdict.json")
    if not isinstance(verdict_data, dict):
        return fail("demo verdict is not an object")
    verdict = DemoVerdict.from_mapping(verdict_data)
    if (
        not verdict.human_review_required
        or verdict.approved_opportunity_created
        or verdict.message_sent
        or verdict.application_submitted
        or verdict.external_channel_used
    ):
        return fail("demo verdict violates human-review or no-side-effect contract")

    review_data = load_json(ROOT / "demo_run/demo_review_decision.json")
    if not isinstance(review_data, dict):
        return fail("demo review decision is not an object")
    review = DemoReviewDecision.from_mapping(review_data)
    if review.approved_opportunity_created or review.external_action_performed or review.message_sent:
        return fail("demo review decision performs a forbidden action")

    pass_check("demo safety markers and no-side-effect contracts hold")
    return 0


def check_privacy_scan() -> int:
    user_path_pattern = "/" + "Users" + "/|" + "Desktop" + "/AI"
    token_pattern = "|".join(
        [
            "gho" + "_",
            "github" + "_pat" + "_",
            "sk" + r"-[A-Za-z0-9_-]{20,}",
            "xox" + r"[baprs]-",
        ]
    )
    automation_pattern = "|".join(
        [
            "actual " + "auto-apply",
            "actual " + "auto-send",
            "submitted " + "real application",
            "sent " + "real message",
        ]
    )
    high_confidence_patterns = {
        "local absolute path": re.compile(user_path_pattern),
        "token value": re.compile(f"({token_pattern})"),
        "webhook url": re.compile(r"https://[^\\s)]+webhook[^\\s)]*", re.IGNORECASE),
        "actual automation claim": re.compile(automation_pattern, re.IGNORECASE),
    }
    paths = [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and path.suffix in {".md", ".py", ".json", ".jsonl", ".yml", ".yaml"}
    ]
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for label, pattern in high_confidence_patterns.items():
            if pattern.search(text):
                return fail(f"privacy scan found {label}: {path.relative_to(ROOT)}")
    pass_check("privacy scan found no high-confidence leaks")
    return 0


def main() -> int:
    for check in (check_json_files, check_eval_cases, check_demo_safety, check_privacy_scan):
        status = check()
        if status != 0:
            return status
    print("PASS: public mirror validation complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
