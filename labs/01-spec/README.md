# Lab 01 — Plan Station with Spec Kit

**Timebox: ~20 minutes.**

## Goal

Have an implementation-ready spec for **Escape the Labyrinth** to hand to the
Squad in Lab 02.

> **`specs/speckit/` holds reference solutions — an answer key.** Don't edit
> them. Choose a path below.

## Fast path — adopt the reference (recommended for a 1-hour run)

Read [`specs/speckit/spec.md`](../../specs/speckit/spec.md) (5 min). Confirm you
can explain its scope, edge cases, and 8 acceptance scenarios, then **designate
it as the source of truth** for Lab 02. Then skip to the handoff.

Use this path if you're short on time or just want to reach the Squad station.
New to Spec Kit? Even on this path you adopt a completed Spec Kit artifact chain,
so skim [what Spec Kit is](../../README.md#2-spec-kit-the-tool-you-plan-with)
first (2 min) so the four files in `specs/speckit/` make sense.

## Full path — author it yourself with Spec Kit (~15 min)

Spec Kit is GitHub's phase-gated spec workflow: `constitution` (guardrails) →
`spec` (what & why) → `plan` (how) → `tasks` (checklist). Initialize it in a
**scratch folder** so it doesn't collide with the reference:

```bash
mkdir -p specs/mine && cd specs/mine
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
