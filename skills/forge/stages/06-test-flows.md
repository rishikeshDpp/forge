# 06 Test flows

1. **CP 06.1** Write `test-flows.md` in the format of `templates/folder/test-flows.md`: product flows grouped by feature/user flow, ids `TF-<group>.<n>`, each one arrow chain (`A → B → C`). Cover main use cases and edge cases. Add each id to state `tests` as `pending`.
2. **CP 06.2** Show them to the user. Apply comments; repeat until the user approves.
3. **CP 06.3** On approval set `test_flows_approved: true`. This is the hard gate and the goal for build, and it activates the commit pre-approval (see SKILL.md, Git and safety).
