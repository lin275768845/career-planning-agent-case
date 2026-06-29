# Career Planning Agent

Chinese mirror: [README.zh-CN.md](README.zh-CN.md).

## Executive Summary: More Than an Auto-Apply Assistant

Career Planning Agent is not an auto-apply bot. Its purpose is to turn
fragmented personal context, incomplete job descriptions, role snippets, and
career preferences into structured review artifacts that help a human make
better career decisions.

The hard product problem is commitment control. Career decisions affect
reputation, compensation, time, relationships, and long-term direction. An AI
agent can parse, summarize, compare, question, draft, and organize evidence,
but it must not silently apply to jobs, send messages, overwrite strategy,
advance opportunities, reject opportunities, or create committed tracker
state. The useful agent is the one that makes the decision surface clearer
while preserving human ownership.

This sanitized public mirror demonstrates the reusable methods extracted from
the private Career Planning Agent: local-first personal-data boundaries,
draft-versus-committed state design, opportunity intake and review workflow,
data sufficiency gates, decision ownership gates, external side-effect gates,
schema contracts for advisory artifacts, no-side-effect eval cases, and
simulated demo outputs that are safe to review publicly.

## Public Case-Study Mirror

This repository is a sanitized public portfolio mirror for architecture review,
workflow review, privacy-boundary review, human-in-the-loop product review,
schema/eval review, and case-study review.

It is validation-runnable, not production-runnable. It is not a full production
clone and it is not connected to real career data. The private local project
remains separate.

Production source code, private app state, real profile/context material, real
resume content, real job descriptions, exported app JSON, localStorage dumps,
private opportunity trackers, external account data, and secrets are
intentionally excluded.

For the concise scope statement, see
[docs/PUBLIC_MIRROR_SCOPE.md](docs/PUBLIC_MIRROR_SCOPE.md).

Visual architecture guide:
[docs/ARCHITECTURE_OVERVIEW.md](docs/ARCHITECTURE_OVERVIEW.md).

Agent strategy panel:
[docs/STRATEGY_PANEL.md](docs/STRATEGY_PANEL.md).

## What This Mirror Is

- A sanitized portfolio mirror based on a private local career-planning agent.
- A case-study repository for human-owned career decision workflows.
- A review target for privacy boundaries, workflow gates, schemas, eval cases,
  and simulated demo artifacts.
- A compact evidence bundle that shows the shape of the product without
  exposing personal career data or production source code.

## What This Mirror Is Not

- Not a turnkey app repository.
- Not a full clone of the private project.
- Not connected to real LinkedIn, Boss, BOSS career platform, Liepin, email,
  messaging, provider, scraper, or application channels.
- Not intended to reproduce the private local app after clone.
- Not a place for real resumes, real salary information, real offers, real job
  descriptions, private notes, localStorage dumps, or exported app state.
- Not capable of applying to jobs, sending messages, scraping platforms, or
  updating committed career state.

## What You Can Review

- Workflow design from profile/context modeling to strategy, intake, verdict,
  review session, and human-confirmed decision.
- Autonomy boundaries that separate draft generation from committed career
  actions.
- Privacy and public-mirror gates for personal-data workflows.
- Data sufficiency gates that prevent snippet-only inputs from becoming
  confident verdicts.
- JSON schema contracts for opportunity verdicts, review decisions, and data
  health reports.
- No-side-effect eval cases and the local static checker under `evals/`.
- Sanitized simulated demo artifacts under `demo_run/`.

## What You Can Run Locally

These checks are local. They require no secrets, no provider keys, no browser
session, no platform login, and no external side effects:

```bash
python3 -m json.tool schemas/opportunity_verdict.schema.json >/dev/null
python3 -m json.tool schemas/review_decision.schema.json >/dev/null
python3 -m json.tool schemas/data_health_report.schema.json >/dev/null
for f in demo_run/*.json; do python3 -m json.tool "$f" >/dev/null; done
python3 evals/check_career_planning_eval_cases.py
```

The full private local app is intentionally out of scope for this mirror.

## What Is Intentionally Excluded

- Production source code.
- `.env`, `.env.*`, token files, webhook configs, cookies, keys, and secrets.
- Real profile text, career context, resumes, job descriptions, compensation
  data, offers, employer notes, and opportunity trackers.
- Real LinkedIn exports, Boss career platform exports, Liepin exports, or other
  external platform data.
- Exported JSON from private app state.
- localStorage dumps, browser session data, private logs, and private runtime
  outputs.
- Production prompts, provider integrations, scraper code, message-send logic,
  auto-apply logic, and private runbooks.
- Local private paths and machine-specific configuration.

## Runability Boundary

This mirror is optimized for reviewable architecture, safety posture, schemas,
eval definitions, and sanitized demos. It is validation-runnable, not
production-runnable.

End-to-end production execution would require private app source code, local
state, user-owned career data, credentials, browser sessions, provider
configuration, external channel permissions, and explicit human approvals that
are not included here.

## Project Overview

Career Planning Agent is a local-first, human-in-the-loop decision-support
agent. It helps a human reviewer organize private career context, draft a
strategy, intake opportunities, evaluate fit, surface risks and missing
information, and prepare a review session.

The public mirror focuses on the agent design:

- Draft before commit.
- Context before verdict.
- Data sufficiency before confidence.
- Human ownership before career action.
- Privacy gates before public artifacts.
- Local evals before broader automation.
- Simulated demos before public storytelling.

## Current Status

| Area | Public mirror status | Notes |
| --- | --- | --- |
| Core workflow docs | Implemented | Workflow, autonomy, tools, gates, eval plan, observability, and runbook are documented. |
| Advisory artifact schemas | Implemented | Opportunity Verdict, Review Decision, and Data Health Report schemas exist in `schemas/`. |
| Static eval definitions | Implemented | 10 no-side-effect eval cases are defined in JSONL. |
| Static eval checker | Implemented | Local checker validates eval definitions and safety invariants. |
| Runtime eval integration | Out of scope | This public mirror validates definitions and demo artifacts, not private runtime behavior. |
| Sanitized demo run | Implemented | Demo artifacts are deterministic, fictional, and explicitly simulated. |
| Chinese README and selected docs | Implemented | Chinese mirror docs live in `README.zh-CN.md` and `docs/zh-CN/`. |
| Production source code | Omitted | The public mirror intentionally excludes the private app implementation. |
| External career actions | Prohibited | Applications, messages, scraping, and platform actions are not part of this mirror. |

## Workflow Sketch

```text
User Model
  -> Career Strategy
  -> Opportunity Discovery
  -> Candidate Intake Inbox
  -> Candidate Pool
  -> Opportunity Verdict
  -> Review Session
  -> Human Review Decision
  -> Optional Private Approved Opportunity
```

The public mirror includes docs, schemas, evals, and sanitized demo artifacts
that make this workflow reviewable. It does not include the private source code
or personal data required to run the private app end to end.

## Review Map

| Artifact | Purpose |
| --- | --- |
| [docs/PUBLIC_MIRROR_SCOPE.md](docs/PUBLIC_MIRROR_SCOPE.md) | Scope and runability boundary for this public mirror. |
| [docs/STRATEGY_PANEL.md](docs/STRATEGY_PANEL.md) | High-level product doctrine for human-owned career decisions. |
| [docs/ARCHITECTURE_OVERVIEW.md](docs/ARCHITECTURE_OVERVIEW.md) | Visual workflow, gates, observability, and public/private boundary guide. |
| [docs/03_WORKFLOW.md](docs/03_WORKFLOW.md) | Workflow stages from user model to review decision. |
| [docs/04_AUTONOMY_MATRIX.md](docs/04_AUTONOMY_MATRIX.md) | Autonomy boundaries and human-approval points. |
| [docs/05_DATA_MODEL.md](docs/05_DATA_MODEL.md) | Draft, active, advisory, committed, and demo data classes. |
| [docs/06_TOOLS_AND_PERMISSIONS.md](docs/06_TOOLS_AND_PERMISSIONS.md) | Tool permission matrix and side-effect classes. |
| [docs/09_GATES_AND_GUARDRAILS.md](docs/09_GATES_AND_GUARDRAILS.md) | Privacy, data sufficiency, decision ownership, and public mirror gates. |
| [docs/10_EVAL_PLAN.md](docs/10_EVAL_PLAN.md) | Eval strategy and static checker status. |
| [docs/11_OBSERVABILITY.md](docs/11_OBSERVABILITY.md) | Local artifacts, redaction policy, and human approval audit trail. |
| [docs/12_RUNBOOK.md](docs/12_RUNBOOK.md) | Safe local modes, common failures, and emergency stop guidance. |
| [docs/13_RUNTIME_OBJECT_MAP.md](docs/13_RUNTIME_OBJECT_MAP.md) | Relationship between workflow objects, gates, schemas, evals, and demos. |
| [schemas/opportunity_verdict.schema.json](schemas/opportunity_verdict.schema.json) | Advisory verdict schema contract. |
| [schemas/review_decision.schema.json](schemas/review_decision.schema.json) | Human-confirmed review decision schema contract. |
| [schemas/data_health_report.schema.json](schemas/data_health_report.schema.json) | Data completeness and blocked-action schema contract. |
| [evals/career_planning_eval_cases.jsonl](evals/career_planning_eval_cases.jsonl) | No-side-effect eval case definitions. |
| [evals/check_career_planning_eval_cases.py](evals/check_career_planning_eval_cases.py) | Local static checker. |
| [demo_run/demo_output_summary.md](demo_run/demo_output_summary.md) | Sanitized simulated demo summary. |
| [docs/case_study_career_planning_week3.md](docs/case_study_career_planning_week3.md) | Public case-study draft. |

## Public Repository Structure

```text
.
├── demo_run/                # Sanitized simulated demo artifacts
├── docs/                    # Curated architecture, workflow, and safety docs
│   └── zh-CN/               # Chinese mirror docs for portfolio review
├── evals/                   # Static no-side-effect eval cases and checker
├── schemas/                 # Advisory artifact schema contracts
├── README.md
└── README.zh-CN.md
```

## Demo Artifacts

The `demo_run/` directory contains deterministic, sanitized, simulated
artifacts. They are designed to show artifact shape and safety posture without
using real personal data.

Included demo artifacts:

- `demo_profile_summary.json`
- `demo_career_strategy.json`
- `demo_candidate_intake_item.json`
- `demo_data_health_report.json`
- `demo_opportunity_verdict.json`
- `demo_review_session.md`
- `demo_review_decision.json`
- `demo_output_summary.md`

They are not real career advice, not real opportunity records, not real
application history, and not production outputs.

## Safety And Privacy Notes

- Do not commit `.env`, secrets, tokens, cookies, webhooks, private logs, or
  real credentials.
- Do not put real resumes, job descriptions, salary information, offers,
  employer notes, contact details, exported app state, localStorage dumps, or
  private career notes into this mirror.
- Treat private app state, private outputs, and private opportunity trackers as
  personal operational artifacts.
- Logs and summaries should stay redacted. They should not emit full prompts,
  full private profile text, real JD payloads, browser session data, HTTP
  headers, secrets, or webhook URLs.
- External applications, message sending, platform scraping, workflow dispatch,
  and committed opportunity state changes remain human-owned actions outside
  this public mirror.

## Maintenance Notes

- Keep this public README focused on architecture, workflow, safety, evals,
  schemas, and sanitized demos.
- Keep private source code, private runbooks, prompts, app state, exports, and
  personal career data outside the public mirror.
- When updating docs, preserve the distinction between implemented, omitted,
  simulated, out-of-scope, and private-only behavior.
- When updating demos, use fictional entities and simulated IDs only.
- When updating evals, keep external side effects forbidden by construction.

## License

License not yet specified. This repository is published for portfolio review;
reuse rights are not granted unless a license is later added.
