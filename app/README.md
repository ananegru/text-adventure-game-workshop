# Implementation Workspace — Escape the Labyrinth

This is where the **Squad** builds the game during
[Lab 02](../labs/02-squad/README.md). It is a **starter skeleton**, not a
finished game: the structure, toolchain, and tests are wired up so you can run
and verify from the first minute, but the game behavior is intentionally
unimplemented. The Squad implements it from
[`specs/speckit/spec.md`](../specs/speckit/spec.md).

## Toolchain

Python + [uv](https://docs.astral.sh/uv/) + pytest. No web build step — the
game is a terminal text adventure.

## Run the game

```bash
cd app
uv run python main.py      # (or: python main.py, if you manage your own venv)
```

Before Lab 02 the engine is a stub: it prints a "not implemented yet" message
and `quit` exits. After the Lab 02 slice, the movement commands work; the full
adventure is stretch.

## Run the tests

```bash
cd app
uv run pytest              # (or: python -m pytest)
```

Baseline state: **2 passed, 8 skipped**. The 8 skipped tests in
`tests/test_acceptance.py` are the acceptance scenarios from the spec. The Lab
02 slice turns **4 of them** green (look, blocked move, unknown command, mixed
case); the remaining scenarios (items, locks, win) are stretch.

## Layout (maps to Squad roles via `.squad/routing.md`)

```text
app/
├── pyproject.toml            # uv project + pytest config
├── main.py                   # entry point: wires UI → engine
├── src/
│   ├── game/                 # backend-owned (rooms, items, parser, win logic)
│   │   ├── world.py          #   room graph + item/lock data  (T001–T003)
│   │   └── engine.py         #   command execution + state     (T004–T005)
│   └── ui/                   # frontend-owned (prompt, rendering, messages)
│       └── cli.py            #   play loop + display           (T006–T008)
└── tests/                    # tests-owned
    ├── test_smoke.py         #   green baseline (keep passing)
    └── test_acceptance.py    #   one skipped test per spec scenario (T009–T011)
```

> The stubs are **starting seams**, not reference answers. Implement the real
> behavior from the spec during Lab 02 — do not treat the placeholders as the
> intended design.
