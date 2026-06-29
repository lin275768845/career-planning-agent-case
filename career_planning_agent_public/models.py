"""Demo-only public data models.

The models describe the sanitized artifact contracts used by this public
mirror. They are deliberately not app runtime models and should not be extended
to ingest real profile, resume, JD, platform, or opportunity data.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True)
class ArtifactSafety:
    """Safety markers required on public demo JSON artifacts."""

    simulated: bool
    sanitized: bool
    contains_real_personal_data: bool = False
    contains_real_resume: bool = False
    contains_real_jd_export: bool = False
    contains_real_employer_confidential_data: bool = False
    external_application_submitted: bool = False
    external_message_sent: bool = False

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any]) -> "ArtifactSafety":
        return cls(
            simulated=value.get("simulated") is True,
            sanitized=value.get("sanitized") is True,
            contains_real_personal_data=value.get("contains_real_personal_data") is True,
            contains_real_resume=value.get("contains_real_resume") is True,
            contains_real_jd_export=value.get("contains_real_jd_export") is True,
            contains_real_employer_confidential_data=(
                value.get("contains_real_employer_confidential_data") is True
            ),
            external_application_submitted=value.get("external_application_submitted") is True,
            external_message_sent=value.get("external_message_sent") is True,
        )

    def is_public_safe(self) -> bool:
        return (
            self.simulated
            and self.sanitized
            and not self.contains_real_personal_data
            and not self.contains_real_resume
            and not self.contains_real_jd_export
            and not self.contains_real_employer_confidential_data
            and not self.external_application_submitted
            and not self.external_message_sent
        )


@dataclass(frozen=True)
class GateResult:
    """Small gate result used by public tests and validation scripts."""

    passed: bool
    gate: str
    reason: str


@dataclass(frozen=True)
class DemoVerdict:
    """Minimal public verdict view used for demo safety checks."""

    verdict_id: str
    human_review_required: bool
    approved_opportunity_created: bool
    prohibited_actions: tuple[str, ...]
    message_sent: bool
    application_submitted: bool
    external_channel_used: bool

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any]) -> "DemoVerdict":
        effects = value.get("external_side_effects", {})
        return cls(
            verdict_id=str(value.get("verdict_id", "")),
            human_review_required=value.get("human_review_required") is True,
            approved_opportunity_created=value.get("approved_opportunity_created") is True,
            prohibited_actions=tuple(value.get("prohibited_actions", ())),
            message_sent=effects.get("message_sent") is True,
            application_submitted=effects.get("application_submitted") is True,
            external_channel_used=effects.get("external_channel_used") is True,
        )


@dataclass(frozen=True)
class DemoReviewDecision:
    """Minimal public review-decision view used for demo safety checks."""

    review_id: str
    human_confirmed: bool
    approved_opportunity_created: bool
    external_action_performed: bool
    message_sent: bool

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any]) -> "DemoReviewDecision":
        approved = value.get("approved_opportunity_creation", {})
        external_action = value.get("external_action", {})
        message_send = value.get("message_send", {})
        return cls(
            review_id=str(value.get("review_id", "")),
            human_confirmed=value.get("human_confirmed") is True,
            approved_opportunity_created=approved.get("created") is True,
            external_action_performed=external_action.get("performed") is True,
            message_sent=message_send.get("sent") is True,
        )
