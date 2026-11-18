#!/bin/bash
# Использование: tools/math-gen/ship.sh "Блок II ... (главы 09–14)"
set -e
cd "$(dirname "$0")/../.."
for c in .github/scripts/check-local-links.mjs .github/scripts/check-inline-js.mjs chemistry/checks.mjs biology/checks.mjs; do node $c > /tmp/chk.txt 2>&1 || { echo "CHECK FAILED: $c"; cat /tmp/chk.txt | tail -5; exit 1; }; done
git add -A
git commit -q -F - <<MSG
Математика: $1

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01G7qTt2A4gPUhp7Xha7StDJ
MSG
git -c push.negotiate=true push origin HEAD:main 2>&1 | tail -2
