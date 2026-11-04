#!/usr/bin/env python3
"""Render <feature-dir>/state.json into a self-contained, auto-refreshing tracker.html."""
import html
import json
import sys
from pathlib import Path

CSS = """
body{font:14px/1.5 -apple-system,system-ui,sans-serif;margin:0;background:#0f1115;color:#e6e6e6}
main{max-width:1100px;margin:auto;padding:24px}
h1{margin:0 0 4px}h2{margin:28px 0 8px;font-size:16px;color:#9fb3c8}
.muted{color:#8a8f98}.pill{display:inline-block;padding:1px 8px;border-radius:10px;font-size:12px}
.done{background:#1f4d2e}.running{background:#5a4a12}.pending{background:#2a2e36}.skipped{background:#4a2a2a}
.pass{background:#1f4d2e}.fail{background:#6b1f1f}.open{background:#5a4a12}.answered{background:#1f4d2e}
ol.tl{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:6px}
ol.tl li{padding:6px 10px;border-radius:6px;min-width:120px}
table{border-collapse:collapse;width:100%}td,th{border-bottom:1px solid #2a2e36;padding:6px;text-align:left;vertical-align:top}
.q1{padding-left:24px}.q2{padding-left:48px}.paused{background:#6b1f1f;padding:8px;border-radius:6px}
"""


def e(v):
    return html.escape(str(v if v is not None else ""))


def table(head, rows):
    if not rows:
        return '<p class="muted">None yet.</p>'
    h = "".join(f"<th>{e(c)}</th>" for c in head)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"<table><tr>{h}</tr>{body}</table>"


def pill(status):
    return f'<span class="pill {e(status)}">{e(status)}</span>'


def render(s):
    cur = s.get("current", {})
    out = [f"<h1>{e(s.get('title') or s.get('feature'))}</h1>",
           f"<p class='muted'>Stage {e(cur.get('stage'))} · checkpoint {e(cur.get('checkpoint') or '-')}"
           f"{' · ClickUp ' + e(s['clickup'].get('story')) if s.get('clickup', {}).get('story') else ''}</p>"]
    if s.get("pause"):
        out.append("<p class='paused'>Paused. Run /forge resume to continue.</p>")

    out.append("<h2>Stages</h2><ol class='tl'>")
    for st in s.get("stages", []):
        cps = st.get("checkpoints", [])
        done = sum(1 for c in cps if c.get("done"))
        extra = f"<br><span class='muted'>{done}/{len(cps)} CPs</span>" if cps else ""
        reason = f"<br><span class='muted'>{e(st.get('reason'))}</span>" if st.get("reason") else ""
        out.append(f"<li class='{e(st.get('status'))}'>{e(st['id'])}{extra}{reason}</li>")
    out.append("</ol>")

    qs = s.get("questions", [])
    rows = []
    for q in qs:
        depth = str(q.get("id", "")).count(".")
        rows.append([f"<span class='q{min(depth, 2)}'>{e(q.get('id'))}</span>", e(q.get("text")),
                     e(q.get("recommendation")), e(q.get("answer")), pill(q.get("status", "open"))])
    n_open = sum(1 for q in qs if q.get("status") != "answered")
    out.append(f"<h2>Questions ({n_open} open / {len(qs)})</h2>")
    out.append(table(["Id", "Question", "Recommendation", "Answer", "Status"], rows))

    out.append("<h2>Decisions</h2>")
    out.append(table(["Id", "Decision", "From"],
                     [[e(d.get("id")), e(d.get("text")), e(d.get("from"))] for d in s.get("decisions", [])]))

    out.append("<h2>PRs</h2>")
    out.append(table(["Repo", "Branch", "PR", "Subtask", "Files", "Status"],
                     [[e(p.get("repo")), e(p.get("branch")), e(p.get("number")), e(p.get("subtask")),
                       e(p.get("files")), e(p.get("status"))] for p in s.get("prs", [])]))

    approved = "approved" if s.get("test_flows_approved") else "not approved"
    out.append(f"<h2>Test flows ({approved})</h2>")
    out.append(table(["TF", "Result", "Note"],
                     [[e(k), pill(v.get("status", "pending")), e(v.get("note"))]
                      for k, v in sorted(s.get("tests", {}).items())]))

    out.append("<h2>Audits</h2>")
    for a in s.get("audits", []):
        out.append(f"<h3>{e(a.get('point'))} <span class='muted'>{e(a.get('at'))}</span></h3>")
        for key, label in (("prd_not_built", "PRD says, not built"), ("built_not_prd", "Built, PRD doesn't mention")):
            items = "".join(f"<li>{e(i)}</li>" for i in a.get(key, [])) or "<li class='muted'>none</li>"
            out.append(f"<p>{label}</p><ul>{items}</ul>")
    if not s.get("audits"):
        out.append('<p class="muted">None yet.</p>')

    title = e(s.get("feature", "feature"))
    return (f"<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
            f"<meta http-equiv='refresh' content='5'><title>{title} · tracker</title>"
            f"<style>{CSS}</style></head><body><main>{''.join(out)}</main></body></html>\n")


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: render-tracker.py <feature-dir>")
    d = Path(sys.argv[1])
    state = json.loads((d / "state.json").read_text())
    (d / "tracker.html").write_text(render(state))
    print(d / "tracker.html")


if __name__ == "__main__":
    main()
