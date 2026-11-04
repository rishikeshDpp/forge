# forge

A Claude Code plugin that runs a feature from ticket to tested PRs as a staged, pausable pipeline. State lives in one `state.json` per feature, so any stage can resume after a crash or context clear.

## Install

```sh
claude plugin marketplace add rishikeshDpp/forge   # or a local clone path
claude plugin install forge@forge
cp config.example.json ~/.config/forge/config.json  # then edit
```

## Commands

| Command | Does |
|---|---|
| `/forge <ticket url\|doc\|text>` | Start a run |
| `/forge resume [feature]` | Continue from the last checkpoint |
| `/forge status` | Short summary + tracker path |
| `/forge pause` | Stop at the next checkpoint (or type "pause" in any prompt) |
| `/forge skip <stage> [reason]` | Skip a stage (or type "skip <stage>") |

Bare `/forge` resolves to the plugin skill; if it is ambiguous, use `/forge:forge`.

## Stages

00 intake · 01 ClickUp story · 02 scaffold (folder + worktrees) · 03 research (no round cap) · 04 grilling · 05 rewrite folder · 06 test flows (approval gate) · 07 build · 08 review · 09 PRs (chained, ≤10 non-test files) · 10 local e2e test via drisp · 11 audit (after 05, 07, 10) · 12 walkthrough.

Each stage is one file in `skills/forge/stages/`; swap or edit them freely.

## Feature folder

`README.md`, `prd-source.md`, `context.md`, `questions.md`, `decisions.md`, `plan.md`, `test-flows.md`, `audit.md`, `walkthrough/`, `state.json`, `tracker.html` (auto-refreshing view of `state.json`).

## Config

`~/.config/forge/config.json` (never committed). See `config.example.json`: docs root, GitHub owner, repos (path, type, local URL), review checklists, repo rules, skill names, drisp flags, PR size cap.

## Status line

`scripts/statusline.sh` prints `feature · stage · CP · open Qs`. Add it to your `statusLine` command, or chain it after an existing one.

## Credits

Stage 04 adapts the `grilling` skill from [mattpocock/skills](https://github.com/mattpocock/skills) (MIT).

## License

MIT
