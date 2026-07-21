# Lab 02 — Implement Station with Squad

The goal is to feel a *team* of agents build from a spec, not to finish the whole game. You'll implement one **vertical slice** and leave the rest as stretch.

> **In a hurry?** The next three sections explain what Squad is and how you talk to it — skim them, or jump straight to [**Setup**](#setup) and start building.

## What is Squad?

Squad gives you a **human-directed AI development team**. Instead of one general
assistant juggling every concern, you get specialists — frontend, backend, tests,
reviewer, and more — that live in your repo as files under `.squad/`. They persist
across sessions, share decisions, and route work by role, so you move faster while
staying in control.

It's **not one chatbot wearing hats.** Each member runs in its own context, reads
only its own charter plus the shared team files, and writes durable decisions back
so the work stays inspectable. You stay accountable for priorities, approvals, and
final changes; Squad handles the coordination, repetition, and parallel execution.

> **Responsible AI stance.** Squad amplifies a human operator with GitHub Copilot —
> it is **not** a replacement for engineers, reviewers, or decision-makers, and not a
> way to take humans out of the loop. Use it to delegate faster, review better, and
> keep governance close to the code.

## How Squad works

Squad is **conversational**. You launch an interactive session and talk to a
**coordinator** that reads `.squad/` + `.copilot/skills/` and routes work to the
right role. Shell blocks (`$`/`cd`) are typed in your terminal; chat blocks
(`> ...`) are typed **inside the Squad session**.

```bash
copilot --agent squad   # launches the Squad coordinator; type 'quit' or /exit to leave
```

> **Which launch command?** `copilot --agent squad` is the current entry point and
> loads this repo's `.github/agents/squad.agent.md` coordinator. The bare `squad`
> interactive shell still works on v0.9.6 but is **deprecated upstream**; in VS Code
> you can instead pick the **Squad** agent in Copilot Chat.

**The team is just files you can read.** Nothing is hidden — open `.squad/` to see
exactly who does what:

| File | What it holds |
|---|---|
| `.squad/team.md` | Roster (eight roles + a coordinator) and per-role model tiers |
| `.squad/routing.md` | Which paths and work types map to which role |
| `.squad/agents/{role}/charter.md` | A member's identity, ownership, and boundaries |
| `.squad/decisions.md` | Durable team rules every agent must respect |

**Agents work in parallel — you stay in control.** A prompt that starts with
`Team, ...` fans out: the coordinator launches every role that can usefully start
at once, then routes the results through the `reviewer` gate before anything counts
as done.

```text
You: "Team, build the movement slice"

  🧭 Coordinator — reads routing.md, plans the fan-out...   ⎤
  🔧 backend    — adds room graph + parser in src/game...   ⎥ launched
  ⚛️ frontend   — wires the play loop in src/ui...          ⎥ in parallel
  🧪 tests      — writes the acceptance scenarios first...  ⎥
  ✅ reviewer   — validates each scenario against the spec  ⎦
```

**Knowledge persists in git.** Decisions land in `.squad/decisions.md`, and because
the whole `.squad/` folder is committed, anyone who clones the repo gets the same
team, the same routing rules, and the same accumulated decisions. (You'll see this
first-hand in the Stretch memory demo.)

> **Cost:** a full `Team, ...` fan-out spawns several agents and consumes
> Copilot premium requests. The scoped slice below keeps that small.

## Talking to the team

Inside the Squad session you drive everything in plain language. There are three
ways to direct work — this is why the prompts in this lab read the way they do:

- **Address one role** — start with its name: `backend, add the room graph` or
  `@tests, ...` (case-insensitive). The coordinator hands it straight to that role.
- **Fan out to the whole team** — start with `Team, ...` and the coordinator
  launches every role that can usefully start, in parallel.
- **Just describe the outcome** — plain natural language; the coordinator routes it
  for you using `.squad/routing.md`.

Slash commands help you stay oriented (type `/help` to see them all):

| Command | What it does |
|---------|-------------|
| `/status` | Show the active squad and what's happening |
| `/agents` | List all team members |
| `/history` | Show recent messages in this session |
| `/sessions`, `/resume <id>` | List saved sessions and restore one |
| `/nap` | Context hygiene — compress and prune the working context |
| `/help` | List every command |
| `/quit` (or `/exit`) | Leave the session |

## Inputs

- Your source of truth from Lab 01 (default: `specs/speckit/spec.md`)
- `app/` — the runnable starter skeleton the Squad fills in
- `.squad/` (team, routing, config) and `.copilot/skills/`

## Setup

```bash
squad doctor   # expect: Summary: 9 passed, 0 failed  (2 info lines are harmless)
```

Launch the Squad session (`copilot --agent squad`) and smoke-test the coordinator:

```text
> Who is on the team, and who owns app/src/game vs app/tests?
```

You should see the eight roles and the ownership split — `app/src/game` →
**backend**, `app/tests` → **tests**. (You'll use the `spec-to-tasks` skill in
`.copilot/skills/` during the build — see **Step 2** below.) Leave the session open.

## Core: build one vertical slice

Implement just the **movement slice** — acceptance scenarios 1, 2, 7, 8 from the
spec (`look`, blocked `go`, unknown command, case-insensitive parsing). This
touches backend + frontend + tests without needing items, locks, or the win
condition.

Work through the steps below **in order**. **Terminal** blocks (`$`, `cat`, `cd`)
are typed in your shell; **chat** blocks (`> ...`) are typed inside the Squad
session you left open from Setup.

### Step 1 — Read the spec (your contract)

The spec's eight numbered acceptance scenarios are the source of truth — the
movement slice is scenarios **1, 2, 7, 8**. Open it before you build so you know
exactly what each scenario requires:

```bash
cat specs/speckit/spec.md            # macOS / Linux
```

```powershell
Get-Content specs/speckit/spec.md    # Windows (PowerShell)
```

### Step 2 — Turn the spec into a task checklist (recommended)

Ask the coordinator to run the **`spec-to-tasks`** skill. It reads the spec and
writes an ordered, tests-first checklist to `docs/tasks/spec-checklist.md` — one
owner per task — which is the bridge from the Plan station (Lab 01) to here. In
the Squad session:

```text
> Use the spec-to-tasks skill to turn specs/speckit/spec.md into an implementation checklist.
```

Skim the generated checklist to see what to build and in what order. (You *can*
build straight from the spec without it — the acceptance scenarios are still the
contract — but the checklist makes the plan explicit.)

### Step 3 — Write the failing tests first

```text
> tests, in app/tests/test_acceptance.py un-skip and implement scenarios 1, 2, 7, and 8 as failing tests first.
```

### Step 4 — Make the tests pass (team fan-out)

```text
> Team, make those tests pass: backend adds a small room graph + parser in app/src/game; frontend wires the play loop in app/src/ui. Keep scope to those four scenarios.
```

### Step 5 — Run the review gate

```text
> reviewer, confirm each of the four scenarios passes with evidence.
```

### Step 6 — Validate in your terminal

```bash
cd app && uv run pytest -k "look or blocked or unknown or mixed_case"
```

Expect four passing tests. This runs from `app/`, so `cd ..` back to the repo
root before any `cat .squad/...` command later.

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

## Score it

Use [`materials/scoring-rubric.md`](../../materials/scoring-rubric.md). **Solo?**
Score your own slice against the reference `specs/speckit/spec.md` (see the Solo
note in the rubric).

## Stretch (optional)

Implement the rest of the game — items, the lock-and-key dependency, and the win
condition (scenarios 3–6) — then get `cd app && uv run pytest` fully green.
Try one memory demo: `> Always treat commands as case-insensitive; record it as
a team decision.` then `cat .squad/decisions.md`.

---

## Appendix — Squad in depth (reference)

Everything above is the hands-on lab. This appendix is **background reference** on
the Squad tool itself — skim it if you're curious, but you don't need it to finish
the slice.

> **Version drift (Squad is fast-moving).** Verified against `squad` **v0.9.6**
> (July 2026). Commands and flags change between releases — if something here differs
> from your machine, trust `squad --help` and `squad <command> --help` over this
> handout.

### Squad commands

Run `squad --help` for the full list (40+ subcommands in v0.9.6). The ones you're
most likely to use around this workshop:

| Command | What it does |
|---------|-------------|
| `copilot --agent squad` | Launch the Squad coordinator — the session you drive this lab from (current entry point) |
| `squad` (no args) | Legacy interactive shell — still works on v0.9.6, **deprecated upstream** in favor of `copilot --agent squad` |
| `squad init` | Scaffold `.squad/` in the current project (idempotent); `--preset <name>` applies a curated team, `--sdk` uses the TypeScript builder |
| `squad upgrade` | Update Squad-owned files to the latest version; never touches your `.squad/` team state |
| `squad status` | Show which squad is active and why |
| `squad doctor` | Validate setup — files, config, health (you run this in Setup) |
| `squad roles` | List the built-in roles; `--search <query>` to filter |
| `squad cost` | Report token usage from orchestration logs (`--all`, `--agent <name>`) |
| `squad nap` | Context hygiene — compress/prune/archive `.squad/` state (`--deep`, `--dry-run`) |
| `squad economy [on\|off]` | Toggle cost-conscious model selection |
| `squad triage` | **Watch mode** — scan for issues and optionally dispatch agents (below) |
| `squad loop` | Prompt-driven continuous work loop (reads `loop.md` each cycle) |
| `squad link <team-repo-path>` | Connect the project to a remote team root |
| `squad export` / `squad import <file>` | Snapshot a squad to a bundle / restore it |

### Legacy `squad` interactive shell — full reference

The bare `squad` interactive shell (still works on v0.9.6, **deprecated upstream** in
favor of `copilot --agent squad`) accepts `@AgentName` addressing (case-insensitive),
a leading `Name,`, a `Team,` fan-out, or plain natural language routed by the
coordinator — plus the slash
commands `/status`, `/agents`, `/history`, `/sessions`, `/resume <id>`, `/nap`,
`/help`, and `/quit` (or `/exit`). Beyond routing, the shell gives you real-time
visibility (agents working, decisions recorded, blockers surfacing), parallel
execution, and **session persistence** — an interrupted agent resumes from its last
checkpoint, so you don't lose context.

### Under the hood — parallelism & persistence

When you hand the team a task, the coordinator launches every role that can usefully
start at once while you keep priorities, review, and final decisions. As agents
finish they leave a breadcrumb trail so you can review with full context:

- **`.squad/decisions.md`** — every durable decision the team made (the one to watch
  in this workshop; try the Stretch memory demo)
- **orchestration / session logs** — what was spawned, why, and what happened
  (written under `.squad/` at runtime as the team works)

Knowledge compounds across sessions: as roles work they record learnings back into
`.squad/`, and because the whole folder is committed to git, anyone who clones the
repo inherits the same team and its accumulated decisions.

### Watch mode — Ralph's automated polling

Ralph is the memory-keeper role that can run a polling loop: it scans for work,
dispatches agents to handle actionable items, and escalates back to humans when
judgment or approval is needed — keeping a team responsive without a person
babysitting the queue.

```bash
# Triage only — scan and categorize, no execution (Ctrl+C to stop)
squad triage --interval 5

# Scan AND dispatch agents against actionable issues
squad triage --execute --max-concurrent 1 --timeout 30

# Mirror output to a log for later review
squad triage --execute --log-file ./watch.log
```

**Key flags (v0.9.6):**

| Flag | Description |
|------|-------------|
| `--interval <minutes>` | Poll frequency (default: 10) |
| `--execute` | Spawn agents to work on issues (otherwise triage-only) |
| `--copilot-flags "..."` | Extra flags passed to the Copilot CLI runner |
| `--max-concurrent N` | Parallel issue limit (default: 1) |
| `--timeout N` | Max minutes per issue (default: 30) |
| `--self-pull` | `git fetch`/`pull` at the start of each round |
| `--board` / `--board-project N` | Project-board lifecycle + reconciliation |
| `--monitor-teams` / `--monitor-email` | Scan Teams / email for actionable items |
| `--decision-hygiene` | Auto-merge the decision inbox |
| `--log-file <path>` | Tee timestamped output to a file |

Capabilities can also be set in `.squad/config.json`; `--no-<capability>` overrides
the config for a single run.

**How Ralph decides, and when it stops:**

- **Agent-delegated selection.** Ralph gathers a context snapshot (issue list, squad
  state, recent decisions), hands it to an agent, and lets the agent choose *which*
  item to work on and *how* — rather than blindly grabbing the top of the queue.
- **Escalation.** On a detected blocker it pauses, logs, and notifies humans instead
  of retrying forever.
- **Graceful shutdown.** Drop a sentinel file — `touch .squad/ralph-stop` — and the
  loop finishes its current round, logs final state, and exits cleanly.
- **Cleanup.** Stale scratch directories and old logs are pruned automatically
  between rounds.
- **Monitoring.** `--log-file` captures a timestamped record; `squad cost` reports
  token spend from the orchestration logs.

> Watch mode is **beyond this workshop** — it needs GitHub issues and auth and
> spends premium requests continuously. Don't start it during the workshop.

### Developing Squad itself (upstream project)

> These steps are for hacking on the **Squad tool's own source repo** —
> [`github.com/bradygaster/squad`](https://github.com/bradygaster/squad) — **not**
> this workshop. You don't run them to complete the lab.

Squad is a monorepo with two packages: `@bradygaster/squad-sdk` (core runtime for
programmable agent orchestration) and `@bradygaster/squad-cli` (the CLI, which
depends on the SDK).

```bash
git clone https://github.com/bradygaster/squad.git && cd squad
npm install          # npm workspaces
npm run build        # build the SDK, then the CLI
npm test             # run the test suite
npm run lint         # type-check (no emit)
```

Versioning uses [changesets](https://github.com/changesets/changesets)
(`npx changeset add`), resolved on `main` with independent per-package releases.

**SDK documentation.** The SDK offers programmatic control over orchestration —
custom tools, hook pipelines, file-write guards, PII scrubbing, reviewer lockout, and
event-driven monitoring. Install it with `npm install @bradygaster/squad-sdk`. Full
guides (API reference, tools & hooks, extensibility, samples) live in the Squad
project's [`docs/`](https://github.com/bradygaster/squad/tree/main/docs) directory.
