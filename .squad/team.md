# Squad Team

## Coordinator

| Name | Role | Notes |
|------|------|-------|
| Squad | Coordinator | Routes work, orchestrates handoffs, and enforces reviewer validation. |

## Members

| Name | Role | Charter | Status |
|------|------|---------|--------|
| frontend | Frontend Engineer | agents/frontend/charter.md | active |
| backend | Backend Engineer | agents/backend/charter.md | active |
| docs | Docs Writer | agents/docs/charter.md | active |
| tests | Test Engineer | agents/tests/charter.md | active |
| devops | DevOps Engineer | agents/devops/charter.md | active |
| reviewer | Reviewer | agents/reviewer/charter.md | active |
| architect | Architect | agents/architect/charter.md | active |
| security | Security Reviewer | agents/security/charter.md | active |

## System agents

| Name | Role | Notes |
|------|------|-------|
| scribe | Scribe | Merges durable decisions and history notes. |
| ralph | Memory keeper | Maintains continuity across sessions. |

## Model tiers

| Tier | Model | Roles |
|------|-------|-------|
| cheap | `MAI-Code-1-Flash` | docs, tests |
| medium | `gpt-5.3-codex` | frontend, devops, reviewer |
| high | `claude-opus-4.6` | backend, architect, security |

> Model availability varies by Copilot plan. `MAI-Code-1-Flash` is not on every
> plan; if a pinned model is unavailable, Squad falls back to a fast model (e.g.
> `claude-haiku-4.5`) and the workshop still works. Change assignments in
> `.squad/config.json`.
