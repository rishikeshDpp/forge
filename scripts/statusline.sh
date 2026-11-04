#!/bin/sh
# Prints "feature · stage · CP · open Qs" for the active forge run.
ACTIVE="${FORGE_HOME:-$HOME/.config/forge}/active"
cat >/dev/null 2>&1
[ -f "$ACTIVE" ] || exit 0
DIR=$(head -n 1 "$ACTIVE")
[ -f "$DIR/state.json" ] || exit 0
python3 -I -c '
import json, sys
s = json.load(open(sys.argv[1] + "/state.json"))
cur = s.get("current", {})
openq = sum(1 for q in s.get("questions", []) if q.get("status") != "answered")
p = " · PAUSED" if s.get("pause") else ""
print("%s · %s · CP %s · %d open Qs%s" % (s.get("feature", "?"), cur.get("stage") or "-", cur.get("checkpoint") or "-", openq, p))
' "$DIR"
