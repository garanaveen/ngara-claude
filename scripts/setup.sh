#!/usr/bin/env bash
# setup.sh — bootstrap the playground environment

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_MIN="3.10"

log() { echo "[setup] $*"; }
die() { echo "[setup] ERROR: $*" >&2; exit 1; }

# Check Python version
check_python() {
  if ! command -v python3 &>/dev/null; then
    die "python3 not found. Install Python $PYTHON_MIN or newer."
  fi
  local version
  version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
  python3 -c "
import sys
major, minor = $version.split('.')
if (int(major), int(minor)) < (3, 10):
    sys.exit(1)
" 2>/dev/null || die "Python $PYTHON_MIN+ required, found $version"
  log "Python $version ✓"
}

# Create and activate a virtual environment
setup_venv() {
  local venv_dir="$REPO_ROOT/.venv"
  if [[ ! -d "$venv_dir" ]]; then
    log "Creating virtual environment at .venv …"
    python3 -m venv "$venv_dir"
  else
    log "Virtual environment already exists, skipping creation."
  fi
  # shellcheck source=/dev/null
  source "$venv_dir/bin/activate"
  log "Virtual environment activated ✓"
}

# Install Python deps
install_python_deps() {
  local req="$REPO_ROOT/python/requirements.txt"
  if [[ -f "$req" ]]; then
    log "Installing Python dependencies …"
    pip install --quiet --upgrade pip
    pip install --quiet -r "$req"
    log "Python dependencies installed ✓"
  fi
}

main() {
  log "Starting setup for ngara-claude playground …"
  check_python
  setup_venv
  install_python_deps
  log "Setup complete. Run 'source .venv/bin/activate' to activate the venv."
}

main "$@"
