# Demo Walkthrough

The demo run is fictional, simulated, and sanitized. It exists to show artifact
shape and safety posture, not to represent a real person, real job, or real
application.

## Demo Cast

- Candidate: `Fictional Candidate A`
- Company: `ExampleCo Labs`
- Opportunity: `DEMO-OPP-001`
- Role: `Product Operations AI Analyst`

## Demo Flow

1. `demo_profile_summary.json` shows a draft profile summary with no real
   resume content.
2. `demo_career_strategy.json` shows a draft strategy path. It is not applied
   to active strategy.
3. `demo_candidate_intake_item.json` shows a simulated opportunity snippet.
   It is not a real JD and not an application.
4. `demo_data_health_report.json` marks missing compensation, reporting line,
   team scope, and full JD.
5. `demo_opportunity_verdict.json` returns a cautious advisory verdict and
   requires human review.
6. `demo_review_session.md` turns the verdict into questions and decision
   options for the human reviewer.
7. `demo_review_decision.json` records a simulated human decision to request
   more information, with no external action and no message sent.
8. `demo_output_summary.md` summarizes the boundary demonstrated by the run.

## Safety Markers

Every demo JSON artifact must include `artifact_safety` with:

- `simulated: true`
- `sanitized: true`
- `contains_real_personal_data: false`
- `contains_real_resume: false`
- `contains_real_jd_export: false`
- `external_application_submitted: false`
- `external_message_sent: false`

The validation harness and tests enforce these markers.

## What The Demo Proves

- Sparse or partial inputs lower confidence.
- Missing salary and full JD lead to questions, not automatic rejection.
- A verdict is advisory and requires human review.
- A review decision can be recorded without creating an Approved Opportunity.
- No application is submitted.
- No message is sent.
- No external channel is used.

## Run The Demo Checks

```bash
python3 scripts/validate_public_mirror.py
python3 -m unittest discover -s tests
```
