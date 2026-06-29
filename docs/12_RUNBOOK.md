# Runbook

## Parse Schemas

```bash
python -m json.tool schemas/opportunity_verdict.schema.json >/dev/null
python -m json.tool schemas/review_decision.schema.json >/dev/null
python -m json.tool schemas/data_health_report.schema.json >/dev/null
```

## Parse Demo JSON

```bash
for f in demo_run/*.json; do python -m json.tool "$f" >/dev/null; done
```

## Run Eval Checker

```bash
python evals/check_career_planning_eval_cases.py
```

## Run Privacy Scan

Scan only safe public-facing files:

- `README.md`
- `AGENTS.md`
- `Decision-Log.md`
- `docs/`
- `schemas/`
- `evals/`
- `demo_run/`

Look for secret-like values, private paths, real emails, phone numbers, real resume markers, real JD export markers, private runtime state, and private opportunity data. Report only redacted categories.

## Run Boundary Scan

Verify public-facing docs and demo state:

- AI drafts only
- human confirms career decisions
- no auto apply
- no auto send
- no external side effect
- no automatic strategy overwrite
- no automatic approved opportunity creation

## Create Public Mirror Locally

1. Create an explicit local mirror directory.
2. Copy only sanitized docs, schemas, evals, and demo artifacts.
3. Exclude `.env*`, private data, localStorage, runtime outputs, real resumes, real JDs, and private opportunities.
4. Run mirror validation.
5. Initialize a local git repo and commit if safe.
6. Do not add a remote or push unless the human explicitly asks.

## When Validation Fails

- Stop the publish or mirror step.
- Keep private data out of reports.
- Fix generated artifacts if the failure is within scope.
- Ask the human when a source artifact may contain real private data.

## Requires Human Approval

- applying Profile, Context, or Career Strategy
- opportunity advance, reject, archive, or approval
- message sending
- external channel usage
- public mirror publication
- global/template rule changes
- destructive data operations
