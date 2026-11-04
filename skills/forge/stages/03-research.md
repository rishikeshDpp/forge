# 03 Research

Goal: answer every question the code can answer before asking the user anything.

Each round is one checkpoint (**CP 03.R<n>**):
1. List open unknowns from the PRD and prior rounds.
2. Fan out parallel subagents, one per repo or topic, read-only. Each returns facts with `path:line` and says what it read.
3. Write verified facts to `context.md`; new unknowns go back on the list.

Repeat with no round cap until no remaining unknown can be answered from code. What remains needs a human decision: write each as an open question (Pass A or B) in `questions.md` and state.json. These seed grilling.
