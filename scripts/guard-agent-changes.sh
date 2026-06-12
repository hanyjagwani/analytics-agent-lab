#!/usr/bin/env bash
set -euo pipefail

mapfile -t changed_files < <(
  git diff --cached --name-only --diff-filter=ACDMR
)

if (( ${#changed_files[@]} == 0 )); then
  echo "No staged files were found."
  exit 1
fi

if (( ${#changed_files[@]} > 20 )); then
  echo "Blocked: the agent modified more than 20 files."
  exit 1
fi

meaningful_file_count=0

for file in "${changed_files[@]}"; do
  case "$file" in
    .agent/backlog.yaml|.agent/latest-report.md)
      ;;
    .github/*)
      echo "Blocked: the agent attempted to modify a GitHub workflow: $file"
      exit 1
      ;;
    scripts/guard-agent-changes.sh|scripts/verify.sh)
      echo "Blocked: the agent attempted to modify a trusted script: $file"
      exit 1
      ;;
    .agent/*)
      echo "Blocked: the agent attempted to modify a protected agent file: $file"
      exit 1
      ;;
    .env|.env.*|*/.env|*/.env.*|*.pem|*.key|*.p12|*.pfx)
      echo "Blocked: the agent attempted to modify a secret-like file: $file"
      exit 1
      ;;
    *)
      meaningful_file_count=$((meaningful_file_count + 1))
      ;;
  esac
done

if (( meaningful_file_count == 0 )); then
  echo "Blocked: the proposed commit contains only agent metadata."
  exit 1
fi

changed_line_count="$(
  git diff --cached --numstat |
    awk '
      {
        if ($1 ~ /^[0-9]+$/) additions += $1
        if ($2 ~ /^[0-9]+$/) deletions += $2
      }
      END { print additions + deletions + 0 }
    '
)"

if (( changed_line_count > 1500 )); then
  echo "Blocked: the agent modified more than 1500 lines."
  exit 1
fi

git diff --cached --check

echo "Guard checks passed."
