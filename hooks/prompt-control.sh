#!/bin/sh
# UserPromptSubmit: inject forge context; set pause flag / flag skip requests for the active forge run.
HOME_DIR="${FORGE_HOME:-$HOME/.config/forge}"
exec python3 -I -c '
import json, os, re, sys
home = sys.argv[1]
def out(lines):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": "\n".join(lines)}}))
    sys.exit(0)
try:
    cfg = json.load(open(home + "/config.json"))
except Exception:
    out(["forge: no config"])
ctx = ["forge: docs_root=%s" % cfg.get("docs_root", "")]
a = (cfg.get("clickup") or {}).get("default_assignee") or {}
if a.get("name"):
    ctx.append("forge: clickup default_assignee=%s (id %s)" % (a.get("name"), a.get("id")))
d = ""
if os.path.isfile(home + "/active"):
    d = open(home + "/active").readline().strip()
if not d or not os.path.isfile(d + "/state.json"):
    out(["forge: no active feature"] + ctx)
try:
    prompt = json.load(sys.stdin).get("prompt", "")
except Exception:
    prompt = ""
path = d + "/state.json"
s = json.load(open(path))
notes = []
if re.search(r"\bpause\b", prompt, re.I):
    s["pause"] = True
    json.dump(s, open(path, "w"), indent=2)
    notes.append("forge: pause flag set in %s. Finish the current step, write state and folder files, then stop at the next checkpoint. Do not start new steps." % path)
tokens = {}
for st in s.get("stages", []):
    sid = st["id"]
    num, _, name = sid.partition("-")
    for t in (sid, num, name, name.split("-")[0]):
        tokens[t.lower()] = sid
for m in re.finditer(r"\bskip\s+([\w-]+)", prompt, re.I):
    sid = tokens.get(m.group(1).lower())
    if sid:
        notes.append("forge: user asked to skip stage %s. Set its status to skipped with the reason from the prompt in state.json, re-render the tracker, and move on." % sid)
cur = s.get("current") or {}
ctx.insert(1, "forge: active=%s" % d)
ctx.insert(2, "forge: stage=%s checkpoint=%s pause=%s" % (cur.get("stage", ""), cur.get("checkpoint", "") or "-", str(bool(s.get("pause"))).lower()))
out(ctx + notes)
' "$HOME_DIR"
