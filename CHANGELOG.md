# Changelog

## v1.2.0

- Orchestrator calls only Skill and Agent; all reads and writes go to subagents. Non-subcommand args route to intake.
- Hook injects a compact `forge:` context block (docs root, active feature, stage, pause, assignee) on every prompt.
- New config `clickup.default_assignee`, used for the story and PR subtasks.

## v1.1.0 — renamed to forge

- Plugin, marketplace, skill and config dir (`~/.config/forge`) renamed to forge.
- Invoke as `/forge`.
- Env override `FEATURE_FLOW_HOME` is now `FORGE_HOME`; skill paths resolve from the skill dir, not `${CLAUDE_PLUGIN_ROOT}`.

## v1.0.0

- Orchestrator skill with start, resume, status, pause, skip.
- 13 stage files, intake to walkthrough.
- `state.json` source of truth, auto-refreshing `tracker.html`, status line.
- UserPromptSubmit hook for "pause" and "skip <stage>".
- Lean folder templates and a content-free walkthrough deck template.
