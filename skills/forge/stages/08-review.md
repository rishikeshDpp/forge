# 08 Review

Per planned PR, a fresh subagent with no build context reviews the diff before push (**CP 08.<pr>**):
- Backend: `review_checklists.backend` + `skills.backend_conventions`.
- Frontend: `review_checklists.frontend` + `repo_rules`.
- Output: findings tagged blocking / non-blocking, each with `path:line`.

Fix every blocking finding in a subagent, then re-review that PR. Record non-blocking ones in `plan.md` under "Follow-ups".
