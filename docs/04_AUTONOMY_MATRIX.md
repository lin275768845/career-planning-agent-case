# Autonomy Matrix

Career commitment actions are human-owned. AI can draft but cannot commit.

| Action | AI autonomy level | Allowed automatically? | Draft-only? | Human approval required? | External side effect? | Privacy risk | Gate | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Profile parsing | draft generation | yes | yes | before apply | no | high | Privacy Gate, Approval Gate | AI can parse, user applies |
| Context parsing | draft generation | yes | yes | before apply | no | high | Privacy Gate, Approval Gate | Context may include private life constraints |
| Career Strategy drafting | draft generation | yes | yes | before apply | no | medium | Strategy Ownership Gate | Strategy is advice until applied |
| Career Strategy application | no autonomous commit | no | no | yes | no | medium | Strategy Ownership Gate | Human owns active strategy |
| JD/snippet parsing | structured draft | yes | yes | before candidate commit | no | medium | Data Sufficiency Gate | Snippets cannot produce full verdicts |
| Opportunity Verdict generation | advisory synthesis | yes | yes | before decision | no | medium | Decision Ownership Gate | Verdict is not final action |
| Candidate Pool update | assisted draft | no | partial | yes | no | medium | Approval Gate | Formal candidate state is user-controlled |
| opportunity advance/reject/archive | no autonomous commit | no | no | yes | no | medium | Decision Ownership Gate | Status transition is a career commitment |
| Approved Opportunity creation | no autonomous commit | no | no | yes | no | high | Approval Gate | Only human-approved opportunities enter tracker |
| Review Session generation | draft generation | yes | yes | before decision | no | medium | Decision Ownership Gate | AI prepares agenda and questions |
| resume suggestion | draft generation | yes | yes | before use | no | high | Privacy Gate | Never publish or send automatically |
| outreach/message draft | draft generation | yes | yes | before send | possible | high | External Side Effect Gate | Draft only |
| real message sending | prohibited | no | no | yes | yes | high | External Side Effect Gate | Must remain human-owned |
| external channel usage | prohibited by default | no | no | yes | yes | high | External Side Effect Gate | No scraping or hidden channel use |
| public mirror export | sanitized artifact | no | no | yes | yes | high | Public Mirror Gate | Must exclude private data |
| private data deletion | prohibited by default | no | no | yes | no | high | Retention / Deletion Gate | Prefer backup and reversible flows |
| active strategy modification | no autonomous commit | no | no | yes | no | medium | Strategy Ownership Gate | User must confirm modifications |
