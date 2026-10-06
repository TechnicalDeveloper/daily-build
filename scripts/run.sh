#!/usr/bin/env bash
# Build the day's exercises and push them. Cron runs it at 20:00, 22:10 and 23:50;
# each run only fills what is still missing today, so the later runs are retries.
# Only the last chance of the day (from 23:30) raises a loud alert.
# Exit 0 = full day, 2 = partial (some committed), 1 = nothing built today or push failed.
set -uo pipefail

cd /opt/projects/daily-build
export GIT_SSH_COMMAND='ssh -i /root/.ssh/dailybuild_deploy -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new'
day=$(date +%F)
echo "=== $day $(date +%T) start"

exec 9>/run/daily-build.lock
if ! flock -n 9; then
  echo "=== $(date +%T) previous run still in progress - skipped"
  exit 0
fi

last_chance() { [ "$(date +%F)" != "$day" ] || [ "$(date +%H%M)" -ge 2330 ]; }
retry_note() { last_chance || echo ", the next run retries"; }

notify() { # <title> <message> <priority>
  [ -x /usr/local/bin/pushover-notify ] || return 0
  /usr/local/bin/pushover-notify monitoring "$1" "$2" "$3" >/dev/null 2>&1 || true
}

out="$(python3 scripts/build.py 2>&1)"; rc=$?
echo "$out"

if ! err=$(git push -q origin main 2>&1); then
  echo "push: $err"
  if ! err=$( { git pull --rebase -q origin main && git push -q origin main; } 2>&1 ); then
    echo "push retry: $err"
    last_chance && notify "daily-build: push failed" "Commits are local on $(hostname) but did not reach GitHub.
$err" 1
    echo "=== $(date +%T) push failed$(retry_note)"
    exit 1
  fi
fi

case "$rc" in
  0)
    echo "=== $(date +%T) pushed - day complete"
    exit 0 ;;
  2)
    last_chance && notify "daily-build: partial day" "$(echo "$out" | tail -3)" -1
    echo "=== $(date +%T) pushed - day incomplete$(retry_note)"
    exit 2 ;;
  *)
    last_chance && notify "daily-build failed" "No exercise built for $day. The streak is at risk.
$(echo "$out" | tail -4)" 1
    echo "=== $(date +%T) nothing built today$(retry_note)"
    exit 1 ;;
esac
