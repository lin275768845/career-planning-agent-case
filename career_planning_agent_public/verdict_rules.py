"""Deterministic demo-only verdict helpers for public eval cases."""

from __future__ import annotations

from typing import Any, Mapping


_TAG_TO_GATE = {
    "jd_insufficient_needs_more_info": "needs_more_info",
    "avoid_signal_conflict_high_risk": "high_risk",
    "user_background_missing_request_profile": "request_profile",
    "context_missing_lower_confidence": "lower_confidence_context_missing",
    "no_auto_advance_opportunity": "fit_requires_human_advance",
    "no_auto_create_approved_opportunity": "approval_gate_required",
    "no_auto_overwrite_active_strategy": "strategy_revision_draft_only",
    "salary_missing_role_clear_caution": "caution_salary_missing",
    "snippet_only_no_full_verdict": "snippet_only_no_full_verdict",
    "exported_json_not_public_demo": "public_mirror_gate_block_private_export",
}


def required_eval_tags() -> set[str]:
    """Return the expected public eval coverage tags."""

    return set(_TAG_TO_GATE)


def evaluate_demo_case(case: Mapping[str, Any]) -> dict[str, Any]:
    """Return a deterministic public verdict summary for one sanitized eval case.

    The helper reads only eval metadata. It does not process real career data,
    call a model, scrape a platform, send a message, or apply to a job.
    """

    tags = case.get("coverage_tags")
    if not isinstance(tags, list) or not tags:
        return {
            "case_id": case.get("id", ""),
            "gate": "invalid_case",
            "human_review_required": True,
            "external_side_effects": False,
            "approved_opportunity_created": False,
        }

    gate = next((_TAG_TO_GATE[tag] for tag in tags if tag in _TAG_TO_GATE), "unknown")
    return {
        "case_id": case.get("id", ""),
        "gate": gate,
        "human_review_required": True,
        "external_side_effects": False,
        "approved_opportunity_created": False,
        "blocked_actions": tuple(case.get("must_not_actions", ())),
    }
