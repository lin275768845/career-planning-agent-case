# Strategy Panel

## Product Positioning

Career Planning Agent is a decision-support system for reviewing career opportunities. It structures personal context, strategy, opportunity evidence, verdicts, and review decisions while keeping career commitments human-owned.

## Stakeholder View

- User: wants clearer career decisions without losing control.
- Reviewer: wants evidence, gates, and evals that prove the agent is safe.
- Builder: wants a reusable pattern for personal-data agent workflows.

## Why Human-In-The-Loop Matters

Career actions can affect reputation, compensation, relationships, and long-term path. The product therefore separates draft intelligence from committed action.

## Why More Agent Does Not Mean Auto Apply

More agentic behavior should mean better context handling, cleaner evidence, stronger gate checks, and more useful review sessions. It should not mean silent applications, messages, strategy overwrites, or status changes.

## Portfolio Talking Points

- workflow-first agent design
- schema-first contracts for verdict and review decisions
- privacy-first public mirror design
- simulated eval cases for human-review boundaries
- clear external side-effect gate

## Risks And Mitigations

| Risk | Mitigation |
| --- | --- |
| AI overstates fit | Data Sufficiency Gate and human review |
| Private data enters public artifact | Public Mirror Gate and demo sanitation |
| Agent commits career action | Decision Ownership Gate and Approval Gate |
| External side effect happens silently | External Side Effect Gate |
| Strategy is overwritten | Strategy Ownership Gate |

## Roadmap

- broaden eval cases for ambiguous roles
- add browser-level review-session QA
- strengthen stale context detection
- keep public mirror generated from sanitized artifacts only
