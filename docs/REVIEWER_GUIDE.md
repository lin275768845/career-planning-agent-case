# Reviewer Guide

This repository is a sanitized public case mirror. It is designed for portfolio
and architecture review, not production execution.

## Fast Review Path

1. Read [README.md](../README.md) for positioning and runability boundaries.
2. Review [docs/ARCHITECTURE_OVERVIEW.md](ARCHITECTURE_OVERVIEW.md) for the
   workflow, gate placement, and public/private split.
3. Inspect [docs/STRATEGY_PANEL.md](STRATEGY_PANEL.md) for the product doctrine.
4. Open [docs/case_study_career_planning_week3.md](case_study_career_planning_week3.md)
   for the full case-study narrative.
5. Run the local validation harness:

```bash
python3 scripts/validate_public_mirror.py
python3 -m unittest discover -s tests
```

## What To Look For

- The mirror is validation-runnable, not production-runnable.
- Demo artifacts are fictional, simulated, and sanitized.
- Opportunity verdicts remain advisory and require human review.
- Review decisions do not send messages or perform external actions.
- Gate helpers block auto-apply, auto-send, and auto-approved-opportunity paths.
- Eval cases cover the main safety boundaries without calling external systems.

## What Not To Expect

- No production app source code.
- No real profile, resume, JD, salary, offer, employer, or opportunity data.
- No browser session, localStorage, exported app state, or platform account
  data.
- No provider integration, scraper, auto-apply path, or message-send path.
- No production runtime state or deployment workflow.

## Validation Artifacts

| Area | File |
| --- | --- |
| Public validator | [scripts/validate_public_mirror.py](../scripts/validate_public_mirror.py) |
| Schema tests | [tests/test_schema_contracts.py](../tests/test_schema_contracts.py) |
| Eval tests | [tests/test_eval_cases.py](../tests/test_eval_cases.py) |
| Demo safety tests | [tests/test_demo_safety_markers.py](../tests/test_demo_safety_markers.py) |
| Demo-only public helpers | [career_planning_agent_public/](../career_planning_agent_public/) |

## Review Verdict

This mirror is strongest when reviewed as an agent-product control system:
workflow first, gates before commitments, schemas before later runtime
integration, and human ownership before any career action.
