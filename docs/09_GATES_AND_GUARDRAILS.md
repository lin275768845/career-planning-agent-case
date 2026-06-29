# Gates And Guardrails

| Gate | Trigger | Required check | Pass condition | Fail action | Human escalation | Logged artifact |
| --- | --- | --- | --- | --- | --- | --- |
| Privacy Gate | input or output may include personal career data | identify private fields and permitted scope | private data stays local or redacted | stop processing public artifact | ask user for scope | privacy scan summary |
| Secret Gate | file path or content may include credentials | scan for `.env`, tokens, keys, webhooks | no secret values are read or copied | stop and report redacted path/category | ask user to remove/rotate if needed | secret scan summary |
| Source Provenance Gate | opportunity source enters workflow | check source type and whether full JD or snippet | source provenance is explicit | mark needs_more_info | ask user for source/context | intake record |
| Data Sufficiency Gate | verdict or review is generated | check required fields and ambiguity | confidence reflects evidence quality | lower confidence or block full verdict | request missing info | data health report |
| Strategy Ownership Gate | active strategy may change | verify action is draft or human-confirmed | strategy change is explicitly confirmed | keep as draft | ask user to apply/edit | decision record |
| Decision Ownership Gate | opportunity may advance/reject/archive | verify human decision | actor is human or reviewer | block transition | ask user to decide | review decision |
| Approval Gate | committed state may be updated | verify explicit approval | approval is present and scoped | block update | ask for confirmation | approval record |
| External Side Effect Gate | message, application, scraping, or external channel use | check explicit approval and allowed tool | no hidden external side effect | stop | ask user for direct approval | external action log |
| Public Mirror Gate | content may enter public mirror | scan for private data, paths, secrets, real examples | only sanitized content included | block mirror commit | ask user to sanitize | mirror validation report |
| Demo Sanitation Gate | demo artifact is generated | verify fictional names and simulated IDs | no real personal or employer data | block demo | regenerate with placeholders | demo validation report |
| Retention / Deletion Gate | user data may be deleted or reset | verify backup and explicit intent | deletion is user-confirmed and reversible when possible | block deletion | ask user to confirm | retention decision |
| Conflict Gate | instructions or evidence conflict | identify stricter rule and source of truth | stricter privacy/safety rule wins | stop if unclear | ask human | conflict note |

## Guardrail Principles

- Evidence before narrative.
- Draft before commit.
- Gate before publish.
- Human approval before career commitment.
- Public artifacts must be sanitized by construction.
