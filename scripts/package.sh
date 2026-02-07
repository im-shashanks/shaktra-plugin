#!/usr/bin/env bash
# Package Shaktra plugin into dist/ for distribution.
# Only plugin-deliverable files are included — no dev artifacts.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIST="$REPO_ROOT/dist"

# Clean previous build
rm -rf "$DIST"
mkdir -p "$DIST"

# Plugin directories to include
PLUGIN_DIRS=(".claude-plugin" "skills" "agents" "hooks" "scripts" "templates")

for dir in "${PLUGIN_DIRS[@]}"; do
  if [ -d "$REPO_ROOT/$dir" ]; then
    cp -r "$REPO_ROOT/$dir" "$DIST/$dir"
  else
    mkdir -p "$DIST/$dir"
  fi
done

# Remove dev-only files from dist
rm -f "$DIST/scripts/package.sh"
rm -f "$DIST/.claude-plugin/marketplace.json"

# Copy LICENSE if it exists
if [ -f "$REPO_ROOT/LICENSE" ]; then
  cp "$REPO_ROOT/LICENSE" "$DIST/LICENSE"
fi

# Report
echo "Packaged to $DIST"
echo ""
find "$DIST" -type f | sort | while read -r f; do
  echo "  ${f#$DIST/}"
done
echo ""
echo "Test with: claude --plugin-dir $DIST"
