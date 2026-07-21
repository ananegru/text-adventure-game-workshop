#!/usr/bin/env pwsh
#
# SquadSDD Workshop — pre-flight readiness check (Windows / PowerShell edition).
# This is the Windows counterpart of scripts/preflight.sh and runs the identical
# checks. Run this the day before (or at the start of) the workshop so tool
# installs, GitHub auth, and Squad setup are ready before you need them.
#
# Usage:  ./scripts/preflight.ps1   (from the workshop root, in PowerShell 7+)
#
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
# Handle native-command exit codes ourselves (mirrors bash `set -e`).
$PSNativeCommandUseErrorActionPreference = $false

function Write-Section {
    param([string]$Title)
    Write-Host ''
    Write-Host "==> $Title"
}

function Require-Command {
    param([string]$Name)
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        [Console]::Error.WriteLine("Missing required command: $Name")
        [Console]::Error.WriteLine('See prerequisites.md for install instructions.')
        exit 1
    }
}

Write-Section 'Checking local developer tools'

# Python is 'python' on most Windows installs and 'python3' elsewhere — accept either.
$pythonCmd = $null
foreach ($candidate in @('python', 'python3')) {
    if (Get-Command $candidate -ErrorAction SilentlyContinue) {
        & $candidate --version *> $null
        if ($LASTEXITCODE -eq 0) { $pythonCmd = $candidate; break }
    }
}
if (-not $pythonCmd) {
    [Console]::Error.WriteLine('Missing required command: python (or python3)')
    [Console]::Error.WriteLine('See prerequisites.md for install instructions.')
    exit 1
}

$requiredTools = @('node', 'npm', $pythonCmd, 'uv', 'squad', 'copilot', 'gh')
foreach ($tool in $requiredTools) {
    Require-Command $tool
    $versionOutput = (& $tool --version 2>$null | Select-Object -First 1)
    if (-not $versionOutput) { $versionOutput = 'version unavailable' }
    Write-Host "$tool found: $versionOutput"
}

Write-Section 'Checking GitHub CLI authentication'
gh auth status *> $null
if ($LASTEXITCODE -ne 0) {
    [Console]::Error.WriteLine('GitHub CLI is not authenticated. Run: gh auth login')
    exit 1
}
Write-Host 'GitHub CLI authentication OK.'

Write-Section 'Checking the game workspace (app/)'
if (Test-Path 'app/pyproject.toml') {
    Push-Location app
    uv run pytest -q
    $testExit = $LASTEXITCODE
    Pop-Location
    if ($testExit -ne 0) {
        [Console]::Error.WriteLine('app/ tests failed.')
        exit $testExit
    }
    Write-Host 'app/ tests ran (baseline: 2 passed, 8 skipped before Lab 02).'
} else {
    [Console]::Error.WriteLine('app/pyproject.toml not found — run this from the workshop root.')
    exit 1
}

Write-Section 'Running Squad health check'
squad doctor
if ($LASTEXITCODE -ne 0) {
    [Console]::Error.WriteLine('squad doctor reported problems.')
    exit $LASTEXITCODE
}

Write-Section 'Preflight complete'
Write-Host 'Environment ready. Two Squad info lines about vscode-jsonrpc and'
Write-Host '@github/copilot-sdk are normal and harmless for global installs.'
