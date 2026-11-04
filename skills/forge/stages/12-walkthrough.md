# 12 Walkthrough

Only when every TF passes. Output: `<folder>/walkthrough/walkthrough.html`, a copy of `templates/walkthrough.html` filled in.

- **Screenshots:** only from local drisp/Playwright runs (stage 10). Embed as base64 data URIs; no external links.
- **Routes:** one route divider per TF group; one step slide per arrow in its flows.
- **Step slides:** `.say` = one or two plain product sentences; `.show` = the screenshot; actor chips say who acts. Use `.show.api` only where a request/response explains the step.
- **Coverage:** main use cases first, then edge cases.
- **Text:** minimal product language; no code, no internal ids, no credentials.
- **Observations:** last slide. One `.find` per issue seen during testing, with a `.sev` level.

Checkpoints: **CP 12.<group>** per route, then **CP 12.obs**. Fill the `{{…}}` slots; delete unused example slides.
