---
name: "spec-to-tasks"
description: "Turn the Escape the Labyrinth spec in specs/speckit/ into a concrete implementation task checklist under docs/tasks/."
domain: "planning"
confidence: "high"
source: "manual"
---

## Context

Apply this skill when the user wants to convert the spec into an executable
checklist — it connects the Plan station (Lab 01) to the Implement station
(Lab 02). Trigger it conversationally, e.g.:

> Use the spec-to-tasks skill to turn `specs/speckit/spec.md` into an
> implementation checklist.

Default to `specs/speckit/spec.md` when no path is given. This is a knowledge
pattern, not a CLI command — there is no `squad skill run`.

## Patterns

- Stay self-contained — use only repository files. Do not implement the game or
  contact external systems.
- Reject spec paths outside `specs/`; the workshop keeps planning artifacts
  under `specs/speckit/`.
- Keep tasks small enough that one owner can complete each. Owners are
  **workstreams** (backend, frontend, docs, tests), so the checklist works
  whether one Copilot agent or the multi-agent Squad executes it.
- Include validation commands, expected results, and a commit message for every
  task.

Concrete steps:

1. Read the selected spec from `specs/speckit/`.
2. Extract the feature goal, supported commands, edge-case behavior, the eight
   Given/When/Then acceptance scenarios, and the non-goals.
3. Identify affected areas: backend `app/src/game/` (world graph, items, parser,
   win logic); frontend `app/src/ui/` (prompt, rendering, messages); tests
   `app/tests/`; docs and labs.
4. Write the checklist to `docs/tasks/`. For `specs/speckit/spec.md` use
   `docs/tasks/spec-checklist.md`; for another spec use the same base name with
   the `-checklist.md` suffix.
5. Order tasks tests-first: failing acceptance tests → backend world/engine →
   frontend loop/rendering → docs → final review.
6. Assign one primary workstream and one reviewer workstream per task.
7. Use the real stack command: `cd app && uv run pytest`.
8. End with a `Definition of done` section.

## Examples

```markdown
# Implementation checklist: Escape the Labyrinth

Source spec: specs/speckit/spec.md

## Task 1: Acceptance tests (failing-first)
- Primary workstream: tests
- Reviewer workstream: backend
- Files:
  - app/tests/test_acceptance.py
- Steps:
  - [ ] Turn each skipped scenario into a real failing test.
  - [ ] Run `cd app && uv run pytest` and confirm the expected failures.
  - [ ] Commit with a conventional-commit message after implementation passes.
- Validation:
  - Command: cd app && uv run pytest
  - Expected: acceptance tests fail for the right reason before implementation.

## Definition of done
- Every acceptance scenario maps to at least one task.
- `cd app && uv run pytest` is green with no remaining skips.
```

## Anti-Patterns

- Implementing the game instead of planning it.
- Writing the checklist outside `docs/tasks/`, or pointing it at a spec outside
  `specs/`.
- Tasks too big for one owner, or missing validation commands.

## Done criteria

- The checklist file exists under `docs/tasks/` and references the source spec
  path.
- Every acceptance scenario maps to at least one task.
- Every task has a primary workstream, reviewer workstream, files, steps,
  validation command, expected result, and commit message.
