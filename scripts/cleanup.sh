#!/usr/bin/env bash
# cleanup.sh — remove generated artifacts from the playground

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

log() { echo "[cleanup] $*"; }

remove_if_exists() {
  if [[ -e "$1" ]]; then
    rm -rf "$1"
    log "Removed: $1"
  fi
}

log "Cleaning up playground artifacts …"

# Python caches
find "$REPO_ROOT" -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find "$REPO_ROOT" -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
find "$REPO_ROOT" -name "*.pyc" -delete 2>/dev/null || true
log "Python caches cleared ✓"

# Virtual environment (optional — pass --venv to also remove it)
if [[ "${1:-}" == "--venv" ]]; then
  remove_if_exists "$REPO_ROOT/.venv"
fi

# Node.js artifacts
remove_if_exists "$REPO_ROOT/javascript/node_modules"
log "Node modules cleared ✓"

log "Cleanup complete."
