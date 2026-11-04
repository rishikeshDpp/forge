# 07 Build

Build `plan.md` in parallel subagents, one per repo/flow, each in its worktree. One checkpoint per product flow (**CP 07.<flow>**).

Each brief includes:
- the flow's decisions, files and TF ids;
- `repo_rules` for the repo type (e.g. one-line comments, constants only in constants files, yup on the frontend);
- backend: read `review_checklists.backend` and invoke `skills.backend_conventions` first;
- write unit tests, but do not run full local suites (GitHub CI is the test gate); a targeted test or type-check is fine;
- leave changes uncommitted in the worktree; 09 splits them into PR branches.

After all flows: run audit #2 (`11-audit.md`).
