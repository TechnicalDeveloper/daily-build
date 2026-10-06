#!/usr/bin/env bash
# Build the day's exercises and push them. Invoked by cron.
# Exit 0 = full day, 2 = partial (some committed), 1 = nothing built.
set -uo pipefail

cd /opt/projects/daily-build
export GIT_SSH_COMMAND='ssh -i /root/.ssh/dailybuild_deploy -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new'

notify() { # <title> <message> <priority>
  [ -x /usr/local/bin/pushover-notify ] || return 0
  /usr/local/bin/pushover-notify monitoring "$1" "$2" "$3" >/dev/null 2>&1 || true
}

out="$(python3 scripts/build.py 2>&1)"; rc=$?
echo "$out"

if [ "$rc" -eq 1 ]; then
  notify "daily-build failed" "No exercise built for $(date +%F). The streak is at risk.
$(echo "$out" | tail -4)" 1
  exit 1
fi

if ! git push -q origin main 2>/dev/null; then
  if ! (git pull --rebase -q origin main && git push -q origin main); then
    notify "daily-build: push failed" "Commits are local on $(hostname) but did not reach GitHub." 1
    exit 1
  fi
fi

[ "$rc" -eq 2 ] && notify "daily-build: partial day" "$(echo "$out" | tail -3)" -1
echo "pushed"
exit 0
