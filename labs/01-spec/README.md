# Lab 01 — Plan Station with Spec Kit

**Timebox: ~20 minutes.**

## Goal

Have an implementation-ready spec for **Escape the Labyrinth** to hand to the
Squad in Lab 02.

## What is Spec Kit?

[Spec Kit](https://github.com/github/spec-kit) is GitHub's open-source tool for
**spec-driven development**: you define *what* to build and *why*, and how you'll
know it's done, **before** writing code. Instead of one freeform document, it walks
you through four ordered files, each answering a single question:

| Artifact | Question it answers | Plain meaning |
|---|---|---|
| `constitution` | What rules always hold? | Guardrails and principles the whole project must respect |
| `spec` | What and why? | The behavior you want and the reason for it |
| `plan` | How? | The technical approach and workstream breakdown |
| `tasks` | In what steps? | An ordered, checkable to-do list for implementation |

The workflow is **phase-gated** — you settle each phase before starting the next
(`constitution` → `spec` → `plan` → `tasks`). That ordering is the whole point: it
stops you coding before intent is clear, which is exactly the drift that spec-driven
development exists to prevent.

There's nothing to install: Spec Kit runs on demand via `uvx`, and you drive it with
slash commands inside Copilot — `/speckit.constitution`, `/speckit.specify`,
`/speckit.plan`, `/speckit.tasks`. This lab only needs the `spec.md` to hand to the
Squad, but authoring the full chain (the Full path below) shows how intent flows all
the way into an executable checklist.

## The game — Escape the Labyrinth

The spec you adopt or write describes a small **terminal text adventure**. The
player is trapped in a dungeon and escapes by exploring rooms, collecting items, and
using a key to open the way out.

**Objective:** start locked in the **Cell**, find the **Rusty Key** in the
**Armory**, `use` it to unlock the **Gate**, pass into the **Exit Tunnel**, and reach
the explicit **win condition** — escape the labyrinth.

The player does everything through five text commands:

| Command | What it does |
|---|---|
| `look` | Describe the current room and its visible exits |
| `go <direction>` | Move through an exit (e.g. `go east`) |
| `take <item>` | Pick an item up into your inventory |
| `use <item> <target>` | Apply an item to something (e.g. `use rusty key gate`) |
| `inventory` | List what you're carrying |

The scope is deliberately small and testable: **4–6 connected rooms**, **2–3
collectible items**, **at least one lock-and-key dependency**, one explicit **win
condition**, and **case-insensitive** parsing. It must also handle the obvious
mistakes gracefully — unknown commands, blocked movement, taking a missing item, and
using an item before its prerequisites are met — without crashing or losing state.

> **Why this game?** It's small enough to spec in minutes yet rich enough to force
> the decisions specs exist for: precise rooms and exits, item prerequisites, and a
> testable win condition. Those become the **8 acceptance scenarios** in
> [`specs/speckit/spec.md`](../../specs/speckit/spec.md) that the Squad implements
> against in Lab 02.

> **`specs/speckit/` holds reference solutions — an answer key.** Don't edit
> them. Choose a path below.

## Fast path — adopt the reference (recommended for a 1-hour run)

Read [`specs/speckit/spec.md`](../../specs/speckit/spec.md). Confirm you
can explain its scope, edge cases, and 8 acceptance scenarios, then **designate
it as the source of truth** for Lab 02. Then skip to the handoff.

Use this path if you're short on time or just want to reach the Squad station.
New to Spec Kit? Even on this path you adopt a completed Spec Kit artifact chain,
so read [What is Spec Kit?](#what-is-spec-kit) above first, so the four files in
`specs/speckit/` make sense.

## Full path — author it yourself with Spec Kit (~15 min)

Spec Kit workflow is as follows: `constitution` (guardrails) →
`spec` (what & why) → `plan` (how) → `tasks` (checklist). Initialize it in a
**scratch folder** so it doesn't collide with the reference:

**macOS / Linux (bash):**

```bash
mkdir -p specs/mine && cd specs/mine
uvx --from git+https://github.com/github/spec-kit.git specify init . --integration copilot
cd ../..
```

**Windows (PowerShell 7+):**

```powershell
mkdir specs/mine -Force | Out-Null
cd specs/mine
uvx --from git+https://github.com/github/spec-kit.git specify init . --integration copilot
cd ../..
```

Then run these slash commands **in Copilot** (CLI or VS Code Chat):

```text
/speckit.constitution
/speckit.specify Build "Escape the Labyrinth", a terminal text adventure: 4-6 connected rooms with directional exits, 2-3 collectible items, at least one lock-and-key dependency, and one explicit win condition. Commands: look, go <direction>, take <item>, use <item> <target>, inventory. Parsing is case-insensitive. Handle unknown command, blocked movement, taking a missing item, and using an item before prerequisites.
/speckit.plan
/speckit.tasks
```

> **Tool drift (Spec Kit is fast-moving).** Verified July 2026. If a flag or
> command name differs, run `specify init --help` and check the generated
> `.github/prompts/speckit.*.prompt.md` for the current slash-command names —
> trust the live tool over this handout.

## Handoff to Lab 02

Spec Kit writes to `specs/mine/specs/<NNN-feature>/spec.md` (and the
constitution to `.specify/memory/constitution.md`) — a different layout than the
flat reference. So pick **one** source of truth for Lab 02:

- **Reference (simplest):** use `specs/speckit/spec.md`.
- **Your own:** use your generated `specs/mine/specs/<NNN-feature>/spec.md` and
  point the Lab 02 prompts at that path instead.

That spec is the contract the Squad implements. Continue to
[`labs/02-squad/README.md`](../02-squad/README.md).
