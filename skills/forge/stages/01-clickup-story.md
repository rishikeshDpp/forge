# 01 ClickUp story

If the user says "no clickup" at any point: set `clickup.enabled: false`, skip this stage and all later ClickUp work, use branches `<type>/<slug>` (CI may flag the missing id; accepted).

1. **CP 01.1** Story already given at intake: reuse it. Otherwise a subagent creates a user story via the `skills.clickup` skill from `prd-source.md`.
2. **CP 01.2** Subagent assigns `clickup.default_assignee` from config (or whoever the user names this run); sets status "in progress". Record `clickup.story` and `clickup.story_url`.
