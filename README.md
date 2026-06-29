# Career Planning Agent - Sanitized Public Mirror

This is a sanitized public mirror. It is for architecture, privacy, human-review workflow, eval, and demo review. It is not a production clone. It does not contain real personal career data. It does not apply to jobs or send messages. It only contains simulated demo artifacts.

## Executive Summary

Career Planning Agent helps evaluate career opportunities, not apply automatically. The key design challenge is human ownership of career commitments: AI can parse, summarize, evaluate, and draft, but the human decides whether to advance, reject, archive, approve, message, or apply.

The agent turns noisy opportunities into structured verdicts and review sessions. It protects privacy by keeping real profile, context, JD, localStorage, exported JSON, and tracker data out of this mirror, and it avoids external side effects by design.

## Included

- sanitized architecture and workflow docs
- human-in-the-loop autonomy matrix
- privacy and approval gate docs
- JSON schemas for verdict, review decision, and data health
- exactly 10 simulated eval cases
- Python standard-library eval checker
- fictional demo run using Fictional Candidate A and ExampleCo Labs

## Excluded

- production source code
- `.env*` files
- tokens, secrets, webhooks, cookies, private keys
- localStorage dumps
- private runtime outputs
- real resume content
- real JD exports
- real LinkedIn, Boss, BOSS直聘, Liepin, or 猎聘 data
- real salary, offer, employer, or private opportunity data
- local private paths

## How To Review

```bash
python3 -m json.tool schemas/opportunity_verdict.schema.json >/dev/null
python3 -m json.tool schemas/review_decision.schema.json >/dev/null
python3 -m json.tool schemas/data_health_report.schema.json >/dev/null
for f in demo_run/*.json; do python3 -m json.tool "$f" >/dev/null; done
python3 evals/check_career_planning_eval_cases.py
```

## Core Workflow

```text
User Model
-> Career Strategy
-> Opportunity Discovery
-> Candidate Intake Inbox
-> Candidate Pool
-> Opportunity Verdict
-> Review Session
-> Approved Opportunity
```

## Portfolio Point

The project demonstrates that "more Agent" does not mean "automatic applications." A stronger career agent should improve evidence quality, review structure, and decision traceability while keeping commitment, privacy, and external action under human control.
