# 05 Rewrite folder

1. **CP 05.1** Subagent rewrites `README.md`, `context.md` and `plan.md` from scratch using only settled facts and decisions. Minimum words, nothing lost, no history or dead options. `prd-source.md`, `questions.md` and `decisions.md` stay as they are.
2. **CP 05.2** `plan.md`: model changes, then per product flow the files to change per repo, then the PR split (≤ `max_non_test_files_per_pr` non-test files each, unless the user said "one PR").
3. **CP 05.3** Run audit #1 (`11-audit.md`).
