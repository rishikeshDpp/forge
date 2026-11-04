---
credit: Adapted from the "grilling" skill in mattpocock/skills (MIT), https://github.com/mattpocock/skills
---

# 04 Grilling

Interview the user until shared understanding. Map a design tree: each decision branches into the decisions that hang off it.

## Rounds
- The frontier is every question whose prerequisites are settled. Ask the whole frontier each round; one round = one checkpoint (**CP 04.<pass><n>**).
- A question that depends on another open question waits for a later round.
- Format:

```
❓ **Q<n> – <title>**: <body, options if any>

➡️ <recommendation>
```

- Word each question so "yes" accepts the recommendation.
- Follow-ups are `Q<n>.<m>`. Numbers are never reused.
- After each answer, immediately write the question, answer and decision to `questions.md`, `decisions.md` (`D<n> — <decision> (Q<n>)`) and state.json, then re-render the tracker.

## Facts
- Facts are your job, never the user's. Send a subagent; ask the rest of the frontier meanwhile.
- A subagent result arriving mid-round is queued and shown at the start of the next round, never mid-question.

## Passes
- **Pass A, product:** requirements, users, flows, edge cases.
- **Pass B, implementation:** table/model changes first; then base architecture against existing repo patterns and best practice; then a short list of changes grouped by product flow. Backend answers must satisfy `review_checklists.backend` and the `skills.backend_conventions` skill.
- Start Pass B early only when a Pass A requirement depends on it.

## End
Only when the frontier is empty and the user confirms shared understanding. Then mark the stage done; from here run without pausing.
