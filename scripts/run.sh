#!/usr/bin/env bash
# Build the day's exercise and push it. Invoked by cron.
set -euo pipefail

cd /opt/projects/daily-build
export GIT_SSH_COMMAND='ssh -i /root/.ssh/dailybuild_deploy -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new'

if ! python3 scripts/build.py; then
  echo "build failed; nothing committed"
  exit 1
fi

git push -q origin main || { git pull --rebase -q origin main && git push -q origin main; }
echo "pushed"
