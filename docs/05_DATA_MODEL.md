# Data Model

## Entity Summary

| Entity | Purpose | Key fields | Source of truth | Mutability | Privacy class | Human approval requirement | Public mirror eligibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| User Model | active career facts and preferences | profile, context, preferences, avoid signals | local app state | user-editable | private | required for apply | no |
| Profile Draft | parsed profile proposal | draft facts, confidence, missing info | AI draft artifact | replaceable | private | required before active profile | sanitized example only |
| Context Draft | parsed context proposal | constraints, goals, ambiguity flags | AI draft artifact | replaceable | private | required before active context | sanitized example only |
| Career Strategy | active or draft path strategy | paths, rationale, risks, keywords | local app state | user-controlled | private | required before apply | sanitized example only |
| Opportunity Discovery Source | manual lead or source note | source type, snippet, provenance | user-provided input | user-controlled | mixed | required before intake | sanitized example only |
| Candidate Intake Item | buffered opportunity input | intake id, role snippet, completeness | local app state | user-controlled | private | required before formal candidate | sanitized example only |
| Candidate Pool Item | confirmed candidate record | candidate id, role, company, status | local app state | user-controlled | private | status changes require human action | sanitized example only |
| Opportunity Verdict | advisory decision-support output | verdict, evidence, risks, missing info | generated artifact | regenerable | private / sanitized | required before decision | yes if simulated |
| Data Health Report | quality and completeness report | missing fields, stale fields, blocked actions | local validation | regenerable | private / sanitized | no commit action | yes if simulated |
| Review Session | structured review agenda | questions, options, evidence summary | generated artifact | regenerable | private / sanitized | decision remains human-owned | yes if simulated |
| Review Decision | human decision record | decision, human_confirmed, next steps | human-confirmed record | append/update by user | private / sanitized | yes | yes if simulated |
| Approved Opportunity | committed tracker item | opportunity id, status, progress | local app state | user-controlled | private | yes | no real data |
| Audit Log / Decision Record | trace of approvals and gates | gate, actor, result, notes | local artifact | append-only preferred | private / sanitized | yes for commitments | sanitized summary only |
| Public Demo Artifact | fictional demonstration | simulated ids, fake user, fake opportunity | repo demo files | versioned | public | not a real decision | yes |

## Design Notes

- Drafts are not active state.
- Active state and committed opportunity decisions require human approval.
- Exported JSON can contain private career data and must not be copied into public artifacts.
- Public demo artifacts use fictional entities and simulated IDs only.
