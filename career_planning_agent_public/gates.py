"""Safe gate helpers for the public Career Planning Agent case mirror.

These helpers are deterministic and demo-only. They intentionally do not touch
network, browser, platform, messaging, application, provider, or private app
state.
"""

from __future__ import annotations

from typing import Any, Mapping

from .models import ArtifactSafety, GateResult


COMMITMENT_ACTIONS = {
    "advance_opportunity",
    "reject_opportunity",
    "archive_opportunity",
    "create_approved_opportunity",
    "apply_strategy",
    "overwrite_strategy",
    "apply_to_job",
    "send_message",
}

FORBIDDEN_PUBLIC_ACTIONS = {
    "auto_apply",
    "auto_send",
    "auto_message",
    "auto_approve",
    "auto_reject",
    "auto_archive",
    "auto_advance",
    "auto_approved_opportunity",
    "apply_to_job",
    "send_message",
    "scrape_platform",
    "create_approved_opportunity",
}


def _artifact_safety(artifact: Mapping[str, Any]) -> ArtifactSafety | None:
    safety = artifact.get("artifact_safety")
    if isinstance(safety, Mapping):
        return ArtifactSafety.from_mapping(safety)
    if "simulated" in artifact or "sanitized" in artifact:
        return ArtifactSafety(
            simulated=artifact.get("simulated") is True,
            sanitized=artifact.get("sanitized") is True,
        )
    return None


def privacy_gate(artifact: Mapping[str, Any]) -> GateResult:
    """Pass only simulated, sanitized public artifacts with no real-data flags."""

    safety = _artifact_safety(artifact)
    if safety is None:
        return GateResult(False, "privacy_gate", "missing artifact_safety markers")
    if not safety.is_public_safe():
        return GateResult(False, "privacy_gate", "artifact is not public safe")
    return GateResult(True, "privacy_gate", "simulated sanitized artifact")


def approval_gate(action: str, *, human_confirmed: bool) -> GateResult:
    """Require explicit human confirmation for commitment actions."""

    if action in FORBIDDEN_PUBLIC_ACTIONS:
        return GateResult(False, "approval_gate", "forbidden in public mirror")
    if action in COMMITMENT_ACTIONS and not human_confirmed:
        return GateResult(False, "approval_gate", "human approval required")
    return GateResult(True, "approval_gate", "no approval blocker")


def decision_ownership_gate(action: str, *, actor: str, human_confirmed: bool) -> GateResult:
    """Block AI-owned or unconfirmed career commitment actions."""

    if action in FORBIDDEN_PUBLIC_ACTIONS:
        return GateResult(False, "decision_ownership_gate", "public mirror cannot perform this action")
    if action in COMMITMENT_ACTIONS and (actor != "human" or not human_confirmed):
        return GateResult(False, "decision_ownership_gate", "career commitments are human-owned")
    return GateResult(True, "decision_ownership_gate", "decision ownership preserved")


def public_mirror_gate(artifact: Mapping[str, Any], *, requested_action: str = "review") -> GateResult:
    """Gate for public portfolio artifacts and reviewer-only actions."""

    if requested_action in FORBIDDEN_PUBLIC_ACTIONS:
        return GateResult(False, "public_mirror_gate", "external or committed action is forbidden")
    privacy = privacy_gate(artifact)
    if not privacy.passed:
        return GateResult(False, "public_mirror_gate", privacy.reason)
    return GateResult(True, "public_mirror_gate", "artifact is eligible for public review")
