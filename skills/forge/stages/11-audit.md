# 11 Audit (reusable)

Runs at #1 after 05, #2 after 07, #3 after 10. One checkpoint each (**CP 11.<n>**).

A fresh subagent compares `prd-source.md` against the current state (folder after #1; code diffs after #2 and #3). Output exactly two lists, one line per point:
- **PRD says, not built**
- **Built, PRD doesn't mention**

Append a snapshot to `audit.md` (format: `templates/folder/audit.md`) and to state `audits[]` (`point`, `at`, `prd_not_built`, `built_not_prd`). Show the user both lists. Gaps that need a decision become new questions; others get fixed before moving on.
