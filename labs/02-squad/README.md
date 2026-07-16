# Lab 02 — Implement Station with Squad

**Timebox: ~30 minutes.** The goal is to feel a *team* of agents build from a
spec — not to finish the whole game. You'll implement one **vertical slice** and
leave the rest as stretch.

## Inputs

- Your source of truth from Lab 01 (default: `specs/speckit/spec.md`)
- `app/` — the runnable starter skeleton the Squad fills in
- `.squad/` (team, routing, config) and `.copilot/skills/`

## How Squad works (30-second version)

Squad is **conversational**. You launch an interactive session and talk to a
**coordinator** that reads `.squad/` + `.copilot/skills/` and routes work to the
right role. Shell blocks (`$`/`cd`) are typed in your terminal; chat blocks
(`> ...`) are typed **inside the `squad` session**.

```bash
squad          # interactive shell; 'quit' to exit  (or pick the Squad agent in VS Code Copilot Chat)
```

> **Cost:** a full `Team, ...` fan-out spawns several agents and consumes
> Copilot premium requests. The scoped slice below keeps that small.

## Setup (~3 min)

```bash
squad doctor   # expect: Summary: 9 passed, 0 failed  (2 info lines are harmless)
```

Launch `squad` and smoke-test the coordinator:

```text
> Who is on the team, and who owns app/src/game vs app/tests?
> List the available skills.
```

You should see the eight roles and the `spec-to-tasks` skill. Leave it open.

## Core: build one vertical slice (~20 min)

Implement just the **movement slice** — acceptance scenarios 1, 2, 7, 8 from the
spec (`look`, blocked `go`, unknown command, case-insensitive parsing). This
touches backend + frontend + tests without needing items, locks, or the win
condition. Drive it conversationally:

```text
> tests, in app/tests/test_acceptance.py un-skip and implement scenarios 1, 2, 7, and 8 as failing tests first.
> Team, make those tests pass: backend adds a small room graph + parser in app/src/game; frontend wires the play loop in app/src/ui. Keep scope to those four scenarios.
> reviewer, confirm each of the four scenarios passes with evidence.
```

Validate in your terminal:

```bash
cd app && uv run pytest -k "look or blocked or unknown or mixed_case"
```

Along the way you've exercised the core Squad capabilities:

| Capability | Where you saw it |
|---|---|
| Routing | game→backend, UI→frontend, tests→tests (`.squad/routing.md`) |
| Parallel execution | the `Team, ...` fan-out |
| Model tiers | `.squad/config.json` (cheap: docs/tests · high: backend) |
| Review gate | `reviewer` validating against acceptance criteria |

> **Model access:** `MAI-Code-1-Flash` isn't on every Copilot plan. If it's
> unavailable, Squad falls back to a fast model and the slice still works.

> **If the Squad stalls or drifts:** the spec's acceptance scenarios are the
> contract, not the agent output. Narrow the prompt to one scenario, or fix the
> failing test target yourself — then re-run `uv run pytest`.

## Required output

- A short implementation summary
- A pass/fail line for scenarios 1, 2, 7, 8
- Any assumptions you logged

## Score it (~5 min)

Use [`materials/scoring-rubric.md`](../../materials/scoring-rubric.md). **Solo?**
Score your own slice against the reference `specs/speckit/spec.md` (see the Solo
note in the rubric).

## Stretch (optional, beyond the hour)

Implement the rest of the game — items, the lock-and-key dependency, and the win
condition (scenarios 3–6) — then get `cd app && uv run pytest` fully green.
Try one memory demo: `> Always treat commands as case-insensitive; record it as
a team decision.` then `cat .squad/decisions.md`.
