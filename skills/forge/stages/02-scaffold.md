# 02 Scaffold

1. **CP 02.1** Create the folder from `templates/folder/`:
   - `README.md`: status + next step. The only index.
   - `context.md`: requirements + verified code facts (`path:line`, no pasted code).
   - `questions.md`: live numbered question tree.
   - `decisions.md`: append-only, one line each, linked to its Q id.
   - `plan.md`, `test-flows.md`, `audit.md`, `walkthrough/`, `state.json`, `prd-source.md`.
   One fact lives in one file; link, don't copy.
2. **CP 02.2** Subagent picks the repos touched (from `config.repos` + the PRD). Per repo: `git fetch origin`, then `git worktree add <repo>-<feature> -b <branch> origin/<default_branch>`, next to the repo. Record `repos[]`: name, worktree, branch.
