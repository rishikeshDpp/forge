# 10 Test

Local only. drisp cannot pass login/OTP screens headlessly, so the target env must be local with an OTP bypass. Never point it at a shared or production env.

1. **CP 10.1** Per repo, check out the LAST branch of its PR chain in its worktree (one branch per repo). Start the local stack; get the app URL from `repos.<name>.local_url`.
2. **CP 10.2** In a background subagent, per frontend:
   ```
   <drisp.bin> exec "<prompt>" --workflow=<drisp.workflow> <drisp.flags> \
     --timeout-ms=<drisp.timeout_ms> --output-last-message <folder>/walkthrough/drisp-<repo>.md \
     --project-dir <worktree>
   ```
   The prompt lists the URL and each TF id with its arrow chain, and asks for one pass/fail line per TF id plus a screenshot per step. Exit codes: 0 ok, 2 usage, 3 bootstrap, 4 runtime, 5 non-interactive policy, 6 timeout, 7 output write. Outputs: `e2e-plan/*`, `test-cases/*`, Playwright specs.
3. **CP 10.3** Record `tests[TF] = {status, note}`.
4. **CP 10.4** On a failure: fix in the PR branch that owns the file; carry it up the chain with plain merges (no rebase); push normally; retest. Loop until every TF passes.
5. **CP 10.5** Run audit #3 (`11-audit.md`).
