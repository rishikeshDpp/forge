# 00 Intake

Input: ClickUp ticket URL, doc path/URL, or pasted text. Or a preset folder name only: first ask the user for the requirement (ticket link, doc or text).

1. **CP 00.1** Subagent fetches the input (ClickUp via the configured skill/tools; docs read in full). Pasted text is used as-is.
2. **CP 00.2** Use the preset folder name as the `feature` slug if given; otherwise pick a short kebab-case slug and confirm it with the user in one line. Ticket input: record its id as `clickup.story` (01 then reuses it).
3. **CP 00.3** A subagent creates `<docs_root>/<feature>/`, copies `templates/state.json`, fills `feature`, `title`, `source`, saves the raw input verbatim as `prd-source.md` (the PRD; never edited later) and writes the active pointer.
