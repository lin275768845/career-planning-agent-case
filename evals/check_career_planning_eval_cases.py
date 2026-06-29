#!/usr/bin/env python3
"""Validate Week 3 Career Planning Agent eval cases.

Standard library only. The checker validates structure and safety invariants; it
does not call external services.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_TAGS = {
    "jd_insufficient_needs_more_info",
    "avoid_signal_conflict_high_risk",
    "user_background_missing_request_profile",
    "context_missing_lower_confidence",
    "no_auto_advance_opportunity",
    "no_auto_create_approved_opportunity",
    "no_auto_overwrite_active_strategy",
    "salary_missing_role_clear_caution",
    "snippet_only_no_full_verdict",
    "exported_json_not_public_demo",
}

FORBIDDEN_POSITIVE_CLAIMS = (
    "should automatically apply",
    "may automatically apply",
    "should send a message",
    "may send a message",
    "should create approved opportunity",
    "may create approved opportunity",
    "auto-create approved opportunity",
)


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def main() -> int:
    path = Path(__file__).with_name("career_planning_eval_cases.jsonl")
    cases = []
    seen_ids = set()
    tags = set()

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return fail(f"could not read {path}: {exc}")

    for line_no, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            case = json.loads(line)
        except json.JSONDecodeError as exc:
            return fail(f"line {line_no} is not valid JSON: {exc}")

        case_id = case.get("id")
        if not case_id:
            return fail(f"line {line_no} is missing id")
        if case_id in seen_ids:
            return fail(f"duplicate id: {case_id}")
        seen_ids.add(case_id)

        if case.get("must_require_human_review") is not True:
            return fail(f"{case_id} must require human review")
        if not case.get("must_not_actions"):
            return fail(f"{case_id} must define must_not_actions")
        if case.get("simulated") is not True or case.get("sanitized") is not True:
            return fail(f"{case_id} must be simulated and sanitized")
        if case.get("privacy_expectation") != "simulated_sanitized_only":
            return fail(f"{case_id} has invalid privacy_expectation")

        joined_positive_text = " ".join(
            str(case.get(key, ""))
            for key in ("scenario", "input_summary", "expected_behavior", "expected_verdict_or_gate")
        ).lower()
        for claim in FORBIDDEN_POSITIVE_CLAIMS:
            if claim in joined_positive_text:
                return fail(f"{case_id} contains forbidden positive automation claim: {claim}")

        case_tags = case.get("coverage_tags")
        if not isinstance(case_tags, list) or not case_tags:
            return fail(f"{case_id} must include coverage_tags")
        tags.update(case_tags)
        cases.append(case)

    if len(cases) < 10:
        return fail(f"expected at least 10 cases, found {len(cases)}")
    if len(cases) != 10:
        return fail(f"expected exactly 10 Week 3 cases, found {len(cases)}")

    missing = sorted(REQUIRED_TAGS - tags)
    if missing:
        return fail("missing coverage tags: " + ", ".join(missing))

    print(f"PASS: {len(cases)} simulated sanitized eval cases validated.")
    print("PASS: required coverage tags present.")
    print("PASS: all cases require human review and define must-not actions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
