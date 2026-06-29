# Tools And Permissions

## Allowed Local Tools

- local file read/write inside this repo for docs, schemas, evals, and sanitized demo artifacts
- JSON parse checks with Python standard library
- eval checker with Python standard library
- static privacy scan over safe public-facing files
- local git status, diff, branch, log, and commit
- `npm run test:server`
- `npm run build`

## Draft-Only Tools

- verdict generator
- review session generator
- strategy draft generator
- profile draft parser
- context draft parser
- JD or snippet parser
- message draft generator

Draft-only tools can prepare evidence and suggestions. They must not apply drafts, change committed statuses, or create external side effects.

## Forbidden Tools And Actions

- LinkedIn scraping
- Boss or BOSS直聘 scraping
- Liepin or 猎聘 scraping
- automatic job applications
- automatic email or message sending
- direct external channel use
- public data export of `private_raw`
- deleting user data automatically
- overwriting active strategy automatically
- creating Approved Opportunity records without human approval
- pushing, publishing, creating PRs, or creating public repos unless explicitly requested

## Permission Rule

The agent may automate reversible local structure. The human owns irreversible, external, private, and commitment-bearing actions.
