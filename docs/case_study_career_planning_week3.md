# Designing a local-first human-in-the-loop career decision agent

## Executive Summary

Career Planning Agent is a local-first decision-support workflow for career planning. It helps a human reviewer structure profile context, draft strategy, intake opportunities, evaluate fit, and run a review session without turning AI into a job-application actor.

The design lesson is that more capable agents need clearer commitment boundaries. The agent can make the work legible; the human owns career decisions.

## Problem

Career opportunity review is noisy. Inputs are incomplete, job descriptions vary in quality, and personal context matters. A useful agent must preserve nuance without creating unreviewed external actions.

## Why Full Autonomy Is Wrong

Applying to jobs, sending messages, rejecting opportunities, or changing career strategy affects real-world commitments. Those actions require human ownership. The agent's job is to prepare evidence, questions, and drafts.

## Workflow

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

## Autonomy Matrix

Low-risk structure work can be automated: parsing, summarizing, draft verdicts, and data health reports. Commitment actions cannot be automated: applying strategy, advancing opportunities, sending messages, creating approved opportunities, and using external channels.

## Data Model

The model separates drafts, active state, advisory artifacts, human decisions, and public demo artifacts. Privacy class and public eligibility are documented for every entity.

## Review Session

The Review Session converts an Opportunity Verdict into a human decision agenda. It lists evidence, risks, missing information, and next-step options. It does not send messages, apply to jobs, or update committed opportunity state.

## Privacy Boundary

Real profile data, context, resumes, JDs, exported JSON, localStorage, private notes, and tracker details remain private. Public artifacts use fictional examples only.

## Eval

The eval suite contains 10 simulated cases for insufficient JDs, avoid-signal conflicts, missing context, status safety, strategy overwrite prevention, salary ambiguity, snippet-only inputs, and public-demo privacy.

## Demo

The sanitized demo uses Fictional Candidate A and ExampleCo Labs. It shows draft profile, draft strategy, candidate intake, data health, opportunity verdict, review session, and human-confirmed review decision with no external side effects.

## What I Learned

- Reliable agents need explicit workflow boundaries.
- Schema contracts make draft and commitment states reviewable.
- Public mirrors need their own privacy gate.
- Human-in-the-loop is a product architecture, not a disclaimer.

## What Remains Planned

- Expand browser-level review-session tests.
- Add more nuanced stale-context and compensation ambiguity evals.
- Keep public portfolio artifacts synchronized with sanitized schemas and demos.
