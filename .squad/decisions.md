# Squad Decisions

## Active decisions

| Decision | Owner | Rationale |
|----------|-------|-----------|
| Spec artifacts in `specs/speckit/` are the source of truth for implementation. | architect | Keep planning and implementation aligned. |
| Command parsing is case-insensitive. | backend | Required by spec acceptance criteria. |
| Completion is measured by acceptance pass/fail, not feature count. | reviewer | Enforce fidelity over scope creep. |

## Governance

- Record newly discovered assumptions in implementation output.
- Resolve unresolved criteria before final scoring when possible.
