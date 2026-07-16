# Work Routing

## Routing table

| Work type | Paths | Route to |
|-----------|-------|----------|
| Backend game logic | `app/src/game/**` | backend |
| Frontend/player interaction | `app/src/ui/**` | frontend |
| Tests | `app/tests/**` | tests |
| Docs and materials | `README.md`, `docs/**`, `labs/**`, `materials/**` | docs |
| CI and automation | `.github/**`, `scripts/**` | devops |
| Cross-cutting design | `specs/**`, architecture changes | architect |
| Security checks | auth/input validation/risk review | security |
| Final quality gate | any merged implementation change | reviewer |

## Rules

1. Prompts starting with `Team,` should fan out in parallel where possible.
2. All implementation changes require reviewer validation.
3. Unclear requirements must be logged as assumptions.
4. Acceptance criteria drive completion decisions.
