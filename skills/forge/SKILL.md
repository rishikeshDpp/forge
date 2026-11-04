---
name: forge
description: Staged, pausable feature pipeline from ticket to tested PRs. Use for "/forge <ticket|doc|text>", "/forge resume|status|pause|skip <stage> [reason]", or when the user starts a feature end to end.
argument-hint: "<ticket url|doc|text> | resume [feature] | status | pause | skip <stage> [reason]"
---

# /forge

Runs the stages in `<skill>/stages/` in order. One file per stage; read a stage file only when entering it.

## Setup
- Paths: `<skill>` is this skill's base directory. Repo root: `<root>` = `$(realpath <skill>)/../..`.
- Config: `~/.config/forge/config.json` (shape: `<root>/config.example.json`). Missing: ask the user to copy and fill it; stop.
- Feature folder: `<docs_root>/<feature>/`. Active pointer: `~/.config/forge/active` holds the folder's absolute path.
- Source of truth: `<folder>/state.json` (shape: `templates/state.json`). Re-render after every write: `python3 "<root>/scripts/render-tracker.py" <folder>`.
- Starting or resuming `/forge` is the user's approval to write that feature's folder for the run.

## Subcommands
- `<input>`: start at `00-intake`.
- `resume [feature]`: set active pointer, clear `pause`, read only the folder files, continue at `current.stage`/`current.checkpoint`.
- `status`: summarise state.json in 5 lines; give the tracker path.
- `pause`: set `pause: true`; stop at the next checkpoint.
- `skip <stage> [reason]`: set status `skipped` + reason. A hook also flags "skip <stage>" in any prompt.

## Main thread rules
- Main thread does product Q&A only. Every lookup, edit, build, test, PR or ClickUp action runs in a subagent with a full brief (goal, paths, config values, what is ruled out, output wanted). Run independent subagents in parallel, always.
- Relay results short, organised, in product language. State a subagent claim as fact only if it says it read or ran it; otherwise label it unverified.
- Never ask the user a fact a subagent can look up.

## Checkpoints and pause
- Each stage lists small checkpoints. After each: update state.json (`current`, stage `checkpoints[]`, results) and the folder files, then re-render. A cleared context loses nothing.
- Before each step, read `pause`. If true: write state, report where it stopped, end the turn.
- After grilling (stage 04) ends, run every later stage without stopping for the user, except the test-flow approval gate (06) and pauses.

## Git and safety
- Branches: `<type>/CU-<id>-<slug>`; with ClickUp off: `<type>/<slug>`. Worktrees off latest `origin/<default_branch>`.
- Before test-flow approval: no commit, push or PR without the user's explicit yes.
- After approval: commit, plain push and PR creation on this feature's own branches proceed only if the user's own instructions pre-approve them; otherwise ask.
- Never merge, label, close, force-push, rebase or bypass hooks. Never touch shared or production environments; tests run locally only.
- No `Co-Authored-By` lines.

## Stages
`00-intake` → `01-clickup-story` → `02-scaffold` → `03-research` → `04-grilling` → `05-rewrite-folder` → `06-test-flows` → `07-build` → `08-review` → `09-prs` → `10-test` → `12-walkthrough`. `11-audit` runs after 05, 07 and 10.

Templates (under `<skill>`): `templates/folder/` (folder files incl. test-flow and audit formats), `templates/state.json`, `templates/walkthrough.html`.
