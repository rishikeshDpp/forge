# 00 Intake

Input: ClickUp ticket URL, doc path/URL, or pasted text.

1. **CP 00.1** Subagent fetches the input (ClickUp via the configured skill/tools; docs read in full). Pasted text is used as-is.
2. **CP 00.2** Pick a short kebab-case `feature` slug; confirm it with the user in one line. Ticket input: record its id as `clickup.story` (01 then reuses it).
3. **CP 00.3** Create `<docs_root>/<feature>/`, copy `templates/state.json`, fill `feature`, `title`, `source`. Save the raw input verbatim as `prd-source.md` (the PRD; never edited later). Write the active pointer.
