#!/bin/bash
# Check external links in _posts/*.md files and output broken links as markdown table

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
POSTS_DIR="${SCRIPT_DIR}/_posts"

echo "| Filename | Link | Response Code |"
echo "|----------|------|---------------|"

grep -HriE 'external_link:' "${POSTS_DIR}"/*.md 2>/dev/null | while IFS= read -r line; do
  file=$(basename "$(echo "$line" | cut -d: -f1)")
  url=$(echo "$line" | sed "s/.*external_link:[[:space:]]*//" | tr -d "'" | xargs)

  # Skip empty URLs
  [ -z "$url" ] && continue

  code=$(curl --insecure -L -o /dev/null --silent --head --write-out '%{http_code}' --max-time 10 "$url" 2>/dev/null)

  # Only output non-200 responses
  [ "$code" = "200" ] && continue

  echo "| $file | $url | $code |"
done
