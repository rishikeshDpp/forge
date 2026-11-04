# 09 PRs

1. **CP 09.1** Split per `plan.md`: ≤ `max_non_test_files_per_pr` non-test files per PR, unless the user said "one PR".
2. **CP 09.2** Per PR: create a ClickUp subtask under the story (`skills.clickup`); branch `<type>/CU-<subtaskId>-<slug>` (ClickUp off: `<type>/<slug>`).
3. **CP 09.3** Chain within a repo: `main ← PR1 ← PR2 …`; each PR's base is the previous branch.
4. **CP 09.4** Per PR: commit, plain push, raise via `skills.raising_pr`. Set its subtask to "in review". No `Co-Authored-By`. Record `prs[]`: repo, branch, base, number, subtask, files, status.

Never merge, label, close, force-push or rebase.
