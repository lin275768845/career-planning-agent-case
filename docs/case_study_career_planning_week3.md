# Career Planning Agent Week 3 Case Study

Chinese mirror: [docs/zh-CN/case_study_career_planning_week3.md](zh-CN/case_study_career_planning_week3.md).

## 1. Title

Career Planning Agent: local-first human-in-the-loop career decision workflow standardization.

## 2. Context

Career Planning Agent started as a private local product for organizing career
context, reviewing opportunities, and deciding what deserves further attention.
Week 3 standardization turns the project into a clearer agent-product case by
documenting the workflow, defining privacy and autonomy boundaries, adding
schema contracts, adding no-side-effect eval cases, and producing sanitized
demo artifacts.

This public case study covers the sanitized mirror only. It does not claim that
the demo artifacts are real career data, real job descriptions, real application
records, or production outputs.

## 3. Problem

Career opportunity review is noisy and personal. Inputs often arrive as partial
role snippets, incomplete job descriptions, vague compensation ranges, scattered
personal constraints, or outdated profile assumptions. A useful agent must help
structure the review without turning private context into public artifacts or
turning advisory drafts into real-world commitments.

The main risk is commitment leakage. Without explicit gates, an agent can
confuse "this looks promising" with "advance this opportunity," "draft a
message" with "send a message," or "suggest a strategy change" with "overwrite
the active strategy." In career workflows, those mistakes can affect reputation,
compensation, relationships, and long-term direction.

## 4. Design Goal

The Week 3 goal was to standardize Career Planning Agent as a privacy-first,
human-in-the-loop agent case:

- Make the workflow legible from user model to review decision.
- Separate draft artifacts from committed career state.
- Document human-owned career actions and external side-effect boundaries.
- Define schemas for Opportunity Verdict, Review Decision, and Data Health
  Report artifacts.
- Add local eval definitions that forbid auto-apply, auto-message, hidden
  platform actions, and private-data leakage.
- Produce a sanitized demo run that shows artifact shape without real career
  data.

## 5. Constraints

- No production source-code export.
- No real profile, context, resume, JD, salary, offer, employer, opportunity, or
  tracker data.
- No localStorage dumps, exported private app JSON, browser sessions, private
  notes, private runtime outputs, or private logs.
- No LinkedIn, Boss, BOSS career platform, Liepin, email, messaging, provider,
  scraper, application, or workflow side effects.
- Demo output must be deterministic, fictional, simulated, and sanitized.
- External career actions remain human-owned and out of scope for the public
  mirror.

## 6. Architecture

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

The architecture is organized around review gates rather than a single
autonomous action. Parsing, summarization, draft verdict generation, data
health reporting, and review-session preparation can be automated in safe local
contexts. Strategy application, opportunity advancement, rejection, messaging,
application submission, and committed tracker changes require human ownership.

## 7. Human-In-The-Loop Workflow

The workflow begins with the User Model: profile facts, context, preferences,
constraints, avoid signals, and search scope. Career Strategy turns that model
into draft path hypotheses and search direction. Opportunity Discovery and
Candidate Intake buffer manually supplied opportunities before they become
formal candidates.

The Opportunity Verdict is advisory. It summarizes fit, evidence, risks,
missing information, and a recommended review direction. The Review Session
then converts that verdict into a human decision agenda: questions, evidence to
inspect, and allowed next-step options. The agent does not perform those
options. The human reviewer decides whether to hold, advance, reject, archive,
request more information, revise strategy, or create a private approved
opportunity.

The detailed workflow lives in [docs/03_WORKFLOW.md](03_WORKFLOW.md).

## 8. Safety And Autonomy Model

The autonomy model distinguishes low-risk local drafting from career
commitments:

- Local schema validation and demo checks are allowed.
- Profile, context, strategy, verdict, and review artifacts can be drafted.
- Applying profile/context, applying strategy, changing opportunity status,
  creating approved opportunities, sending messages, and applying to jobs
  require human confirmation.
- External platform actions, scraping, hidden channel usage, auto-apply, and
  auto-send are prohibited in this public mirror.

The main references are [docs/04_AUTONOMY_MATRIX.md](04_AUTONOMY_MATRIX.md),
[docs/06_TOOLS_AND_PERMISSIONS.md](06_TOOLS_AND_PERMISSIONS.md), and
[docs/09_GATES_AND_GUARDRAILS.md](09_GATES_AND_GUARDRAILS.md).

## 9. Schema Contracts

Week 3 adds three public schema contracts:

- [schemas/opportunity_verdict.schema.json](../schemas/opportunity_verdict.schema.json)
  defines the advisory verdict shape.
- [schemas/review_decision.schema.json](../schemas/review_decision.schema.json)
  defines the human-confirmed review decision shape.
- [schemas/data_health_report.schema.json](../schemas/data_health_report.schema.json)
  defines completeness, ambiguity, and blocked-action reporting.

These are public review contracts for sanitized artifacts. They are not proof
that private runtime emission is included in this mirror.

## 10. Eval Suite

Week 3 adds exactly 10 local eval case definitions in
[evals/career_planning_eval_cases.jsonl](../evals/career_planning_eval_cases.jsonl).
The cases cover sparse JD handling, avoid-signal conflicts, missing user
background, missing context, no auto-advance, no auto-approved opportunity, no
strategy overwrite, salary ambiguity, snippet-only inputs, and public-demo
privacy.

The static checker
[evals/check_career_planning_eval_cases.py](../evals/check_career_planning_eval_cases.py)
validates the case file and safety invariants. It is local-only: it does not
import production code, call external APIs, invoke LLMs, scrape platforms, send
messages, apply to jobs, update trackers, or run the private app.

Runtime eval integration remains outside this public mirror.

## 11. Sanitized Demo Run

The deterministic demo under [demo_run/](../demo_run/) uses fictional entities
only:

- Candidate: `Fictional Candidate A`
- Company: `ExampleCo Labs`
- Opportunity: `DEMO-OPP-001`
- Role: `Product Operations AI Analyst`

The demo includes draft profile summary, draft career strategy, candidate
intake item, data health report, opportunity verdict, review session,
human-confirmed review decision, and demo output summary.

The demo is not a real application, not a sent message, not a real job record,
not real career advice, and not production execution.

## 12. Implemented Vs Omitted Vs Out Of Scope

| Area | Status | Notes |
| --- | --- | --- |
| Workflow documentation | implemented | User model, strategy, intake, verdict, review, and approval boundaries are documented. |
| Autonomy and gate docs | implemented | Human-owned commitments and external side effects are explicitly gated. |
| Advisory schemas | implemented | Three JSON schemas are included for public artifact review. |
| Static eval definitions | implemented | 10 no-side-effect cases exist. |
| Static eval checker | implemented | Local checker validates eval structure and safety invariants. |
| Sanitized demo run | implemented | Demo artifacts are deterministic fictional examples. |
| Chinese README and selected docs | implemented | Chinese review docs are included for portfolio readability. |
| Production source code | omitted | The mirror is a portfolio evidence bundle, not a source export. |
| Real career data | omitted | No real profile, resume, JD, salary, offer, employer, or application data. |
| External career actions | out of scope | No application, message, scraping, or platform action is available. |
| Private runtime eval integration | out of scope | Runtime behavior belongs to the private project. |

## 13. Lessons Learned

- Human-in-the-loop is a product architecture, not a disclaimer.
- Career agents need a strict distinction between draft advice and committed
  action.
- Data sufficiency gates are as important as model quality for incomplete job
  descriptions.
- Public mirrors for personal-data agents need their own privacy gate.
- Schema contracts make advisory outputs and human decisions easier to review.
- A sanitized demo can make the workflow inspectable without exposing personal
  data or triggering external career channels.

## 14. Next Steps

- Keep public portfolio artifacts synchronized with sanitized schemas and demos.
- Add more nuanced stale-context and compensation-ambiguity eval cases when the
  private project has stable examples that can be safely abstracted.
- Consider read-only UI screenshots or diagrams from sanitized mock data only.
- Keep production source code, private career data, and external action paths
  outside the curated public mirror.
