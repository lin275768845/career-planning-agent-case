# Runtime Object Map

| Runtime object | File/object | Producer | Consumer | Allowed transitions | Approval gate | Public eligibility |
| --- | --- | --- | --- | --- | --- | --- |
| User Model | local app state / `src/types/career.ts` | user edits, profile/context draft application | strategy, verdict, review session | draft -> active by human apply | Approval Gate | no real data |
| Career Strategy | local app state / strategy types | AI draft generator, user edits | discovery, candidate fit, verdict | draft -> active by human apply | Strategy Ownership Gate | sanitized example only |
| Candidate Intake Inbox | candidate intake state | user paste/import, manual discovery lead | parser, candidate pool | draft -> candidate by human action | Data Sufficiency Gate | sanitized example only |
| Candidate Pool | candidate state | confirmed intake item | verdict, review session | candidate -> review states by human action | Decision Ownership Gate | sanitized example only |
| Opportunity Verdict | generated verdict artifact | rules and AI synthesis | review session | draft -> reviewed by human | Decision Ownership Gate | yes if simulated |
| Review Session | generated review artifact | verdict and evidence summary | human reviewer | draft -> decision record | Approval Gate | yes if simulated |
| Review Decision | decision record | human reviewer | tracker, audit trail | hold/reject/archive/advance by human | Decision Ownership Gate | yes if simulated |
| Approved Opportunity | tracker state | human-approved decision | progress tracker | saved/to-apply/applied/interviewing/offer/closed by human | Approval Gate | no real data |
| Data Health Report | validation artifact | local checker | user, review session | regenerated as inputs change | Privacy Gate | yes if simulated |
| Public Mirror Artifact | sanitized files | Week 3 export process | portfolio reviewer | local commit only unless separately approved | Public Mirror Gate | yes |

## Transition Rules

- Draft objects can be regenerated.
- Active objects require human confirmation.
- External actions require explicit approval and separate execution.
- Public artifacts must be sanitized and simulated.
- Private runtime state must not be mirrored.
