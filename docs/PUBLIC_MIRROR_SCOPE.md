# Public Mirror Scope

## Why This Mirror Exists

This mirror lets a reviewer inspect the product architecture, human-review
workflow, privacy boundary, eval suite, schema contracts, and sanitized demo
without accessing private local data or production runtime state.

It is intentionally validation-runnable and not production-runnable. The goal
is to show the shape, gates, and review evidence of the agent-product design,
not to publish a deployable copy of the private app.

## Included

- `README.md`
- `README.zh-CN.md`
- selected workflow and architecture docs
- `docs/PUBLIC_MIRROR_SCOPE.md`
- `docs/ARCHITECTURE_OVERVIEW.md`
- `docs/STRATEGY_PANEL.md`
- selected Chinese mirror docs under `docs/zh-CN/`
- JSON schemas
- simulated eval suite
- sanitized demo run

## Excluded

- production source code
- production prompts and provider integrations
- real app state
- real personal career data
- real resumes
- real JD exports
- real salary, offer, employer, contact, or application data
- private notes
- exported JSON from the local app
- `.env*`, tokens, secrets, keys, webhooks, cookies
- external account data
- private runtime outputs
- local private paths
- browser sessions and localStorage dumps
- scraping, auto-apply, and message-send implementation

## Privacy Boundary

All examples are fictional. The mirror uses Fictional Candidate A, ExampleCo Labs, and simulated IDs such as `DEMO-OPP-001`. No real person, employer, opportunity, salary, offer, message, or application is represented.

## Not A Production Clone

This repository is not a deployable copy of the private app. It is a
portfolio-facing evidence bundle. It is not connected to real career platforms,
email, messaging tools, provider accounts, browser sessions, or private local
state.

## No External Side Effect

The mirror does not apply to jobs, send messages, scrape sites, access external
channels, update committed opportunity state, or publish private career data.

## Public Eligibility Rule

A file is eligible for this public mirror only when it is:

- fictional or fully sanitized
- free of secrets and local private paths
- free of real personal career data
- explicitly marked as simulated when it looks like a runtime output
- useful for architecture, workflow, gate, schema, eval, or portfolio review

Anything derived from real profile, context, resume, JD, salary, offer,
employer, opportunity, browser session, localStorage, private note, or exported
app state is private by default.
