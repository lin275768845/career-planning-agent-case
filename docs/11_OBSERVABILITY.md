# Observability

Career Planning Agent uses local-first observability. It should make decisions auditable without creating telemetry or external logging by default.

## Local Artifacts

- decision records for human approvals
- review session logs
- data health reports
- validation reports
- privacy scan summaries
- eval checker output
- public mirror validation summaries

## No Telemetry By Default

- no cloud telemetry
- no external logging
- no hidden analytics
- no automatic external sync
- no scraping logs from external sites

## Redaction Policy

Reports may include:

- file paths for public-facing artifacts
- pattern category
- severity
- redacted explanation

Reports must not include:

- secret values
- token values
- webhook values
- full private career notes
- real resume raw text
- real JD exports
- localStorage dumps

## Human Approval Audit Trail

For every committed career action, record:

- actor
- timestamp
- action
- related opportunity or strategy ID
- gate result
- rationale or audit note
- whether any external action was performed

If an action is only drafted, the audit trail should say it was draft-only.
