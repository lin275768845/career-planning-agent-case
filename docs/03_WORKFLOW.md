# Workflow

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

## 1. User Model

- Purpose: maintain the user's active profile, context, preferences, constraints, avoid signals, and search scope.
- Input: profile text, context text, preferences, avoid signals, manually edited facts.
- Output: Active Profile, Active Context, draft parse artifacts, decision preferences.
- AI role: parse profile and context into drafts; identify missing or conflicting information.
- Human role: review, edit, and apply drafts.
- Gate: Privacy Gate and Approval Gate.
- Forbidden shortcut: AI must not apply Profile or Context automatically.

## 2. Career Strategy

- Purpose: translate user model into strategic career paths and search direction.
- Input: Active Profile, Active Context, preferences, avoid signals, current goals.
- Output: Career Strategy draft or active strategy, path hypotheses, discovery keywords.
- AI role: draft strategic options and explain tradeoffs.
- Human role: apply, edit, pause, archive, or reject strategy drafts.
- Gate: Strategy Ownership Gate.
- Forbidden shortcut: AI must not overwrite active strategy.

## 3. Opportunity Discovery

- Purpose: keep manual opportunity discovery organized without turning the product into a crawler.
- Input: strategy paths, manual source notes, simulated or user-entered snippets.
- Output: discovery leads and candidate intake drafts.
- AI role: suggest keywords or classify snippets when explicitly requested.
- Human role: choose sources, paste inputs, and decide what enters intake.
- Gate: Source Provenance Gate and External Side Effect Gate.
- Forbidden shortcut: no LinkedIn, Boss, BOSS直聘, Liepin, 猎聘, or external site scraping.

## 4. Candidate Intake Inbox

- Purpose: buffer opportunities before they become formal candidates.
- Input: pasted JD, role snippet, manual opportunity note, simulated demo snippet.
- Output: Candidate Intake Item.
- AI role: parse fields, identify insufficiency, and mark whether a full verdict is possible.
- Human role: confirm whether an intake item should become a candidate.
- Gate: Data Sufficiency Gate.
- Forbidden shortcut: snippets must not become confident verdicts.

## 5. Candidate Pool

- Purpose: hold confirmed candidate records that can be reviewed.
- Input: human-confirmed Candidate Intake Item.
- Output: Candidate Pool Item with parsed role information and evidence.
- AI role: enrich advisory evidence and missing-information questions.
- Human role: maintain candidate status and notes.
- Gate: Approval Gate.
- Forbidden shortcut: AI must not move candidates between committed statuses.

## 6. Opportunity Verdict

- Purpose: produce a decision-support verdict for an opportunity.
- Input: candidate details, user model, strategy, context, evidence sufficiency.
- Output: Opportunity Verdict draft with fit summary, risks, missing information, and next-step suggestion.
- AI role: synthesize evidence and recommend review direction.
- Human role: interpret verdict and decide action.
- Gate: Decision Ownership Gate.
- Forbidden shortcut: AI must not approve, reject, archive, apply, or send messages.

## 7. Review Session

- Purpose: help the human make a review decision with structured evidence.
- Input: Opportunity Verdict, candidate evidence, missing information, strategy relation.
- Output: Review Session draft and optional Review Decision record.
- AI role: prepare agenda, questions, and draft next steps.
- Human role: make and record the decision.
- Gate: Approval Gate and External Side Effect Gate.
- Forbidden shortcut: review session must not perform external actions.

## 8. Approved Opportunity

- Purpose: track only opportunities the human has explicitly approved.
- Input: human-confirmed Review Decision.
- Output: Approved Opportunity record and progress notes.
- AI role: summarize status or draft follow-up suggestions.
- Human role: create, update, progress, archive, or close the record.
- Gate: Decision Ownership Gate and Retention / Deletion Gate.
- Forbidden shortcut: AI must not create approved opportunities automatically.
