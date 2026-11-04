#!/bin/sh
# UserPromptSubmit: set pause flag / flag skip requests for the active forge run.
ACTIVE="${FORGE_HOME:-$HOME/.config/forge}/active"
[ -f "$ACTIVE" ] || exit 0
DIR=$(head -n 1 "$ACTIVE")
[ -f "$DIR/state.json" ] || exit 0
exec python3 -I -c '
import json, re, sys
d = sys.argv[1]
try:
    prompt = json.load(sys.stdin).get("prompt", "")
except Exception:
    sys.exit(0)
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
if notes:
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": "\n".join(notes)}}))
' "$DIR"
