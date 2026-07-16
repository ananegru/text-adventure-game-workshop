#!/usr/bin/env bash
#
# SquadSDD Workshop — pre-flight readiness check.
# Run this the day before (or at the start of) the workshop so tool installs,
# GitHub auth, and Squad setup are ready before you need them.
#
# Usage:  ./scripts/preflight.sh   (from the workshop root)
#
set -euo pipefail

required_tools=(
  node
  npm
  python3
  uv
  squad
  copilot
  gh
)

print_section() {
  printf '\n==> %s\n' "$1"
}

require_command() {
  local command_name="$1"
  if ! command -v "$command_name" >/dev/null 2>&1; then
    printf 'Missing required command: %s\n' "$command_name" >&2
    printf 'See prerequisites.md for install instructions.\n' >&2
    exit 1
  fi
}

print_section "Checking local developer tools"
for tool in "${required_tools[@]}"; do
  require_command "$tool"
  version_output=$("$tool" --version 2>/dev/null | head -n 1 || true)
  printf '%s found: %s\n' "$tool" "${version_output:-version unavailable}"
done

print_section "Checking GitHub CLI authentication"
if ! gh auth status >/dev/null 2>&1; then
  printf 'GitHub CLI is not authenticated. Run: gh auth login\n' >&2
  exit 1
fi
printf 'GitHub CLI authentication OK.\n'

print_section "Checking the game workspace (app/)"
if [[ -f app/pyproject.toml ]]; then
  ( cd app && uv run pytest -q )
  printf 'app/ tests ran (baseline: 2 passed, 8 skipped before Lab 02).\n'
else
  printf 'app/pyproject.toml not found — run this from the workshop root.\n' >&2
  exit 1
fi

print_section "Running Squad health check"
squad doctor

print_section "Preflight complete"
printf 'Environment ready. Two Squad info lines about vscode-jsonrpc and\n'
printf '@github/copilot-sdk are normal and harmless for global installs.\n'
