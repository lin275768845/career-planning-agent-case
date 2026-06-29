# Strategy Panel

## Product Positioning

Career Planning Agent is a local-first decision-support system for reviewing
career opportunities. It structures personal context, strategy, opportunity
evidence, verdicts, and review decisions while keeping career commitments
human-owned.

The product is not an auto-apply workflow. More agentic behavior should mean
better context handling, better evidence organization, better uncertainty
surfacing, and better review sessions, not silent external action.

## Stakeholder View

- User: wants clearer career decisions without losing control.
- Reviewer: wants evidence, gates, and evals that prove the agent is safe.
- Builder: wants a reusable pattern for personal-data agent workflows.
- Future maintainer: wants public artifacts that can be reviewed without
  exposing private source code or private career data.

## Why Human-In-The-Loop Matters

Career actions can affect reputation, compensation, relationships, and long-term path. The product therefore separates draft intelligence from committed action.

## Why More Agent Does Not Mean Auto Apply

More agentic behavior should mean better context handling, cleaner evidence, stronger gate checks, and more useful review sessions. It should not mean silent applications, messages, strategy overwrites, or status changes.

## Operating Doctrine

- Draft before commit.
- Context before verdict.
- Missing information before confidence.
- Human ownership before career action.
- Privacy gate before public artifact.
- Validation before portfolio publication.

## Core Product Bets

| Bet | Product implication |
| --- | --- |
| Career data is personal operational data | Keep real profile, context, resume, JD, and tracker state private by default. |
| Opportunity inputs are often incomplete | Add Data Sufficiency Gate before full verdicts. |
| A verdict is advice, not action | Require human review before advance, reject, archive, apply, or message. |
| Strategy changes are commitments | Treat strategy application as human-owned state transition. |
| Public mirrors need independent safety gates | Only fictional, simulated, sanitized artifacts can enter this repo. |

## Portfolio Talking Points

- workflow-first agent design
- schema-first contracts for verdict and review decisions
- privacy-first public mirror design
- simulated eval cases for human-review boundaries
- clear external side-effect gate
- local-first pattern for personal-data agents
- decision traceability without telemetry by default

## Risks And Mitigations

| Risk | Mitigation |
| --- | --- |
| AI overstates fit | Data Sufficiency Gate and human review |
| Private data enters public artifact | Public Mirror Gate and demo sanitation |
| Agent commits career action | Decision Ownership Gate and Approval Gate |
| External side effect happens silently | External Side Effect Gate |
| Strategy is overwritten | Strategy Ownership Gate |
| Sparse role snippet becomes overconfident verdict | Data Sufficiency Gate |
| Public demo is mistaken for production output | Explicit simulated/sanitized markers |

## Roadmap

- broaden eval cases for ambiguous roles
- add browser-level review-session QA
- strengthen stale context detection
- keep public mirror generated from sanitized artifacts only
- consider read-only mock screenshots from simulated data only
