"""Command-line UI — frontend-owned starter seam (``src/ui/cli.py``).

Reads player input, hands each command to the game engine, and prints the
response. STARTER STUB — the Squad's `frontend` role implements the real play
loop, room/inventory rendering, and edge-case messaging in Lab 02
(tasks.md T006–T008).
"""

from __future__ import annotations

from game.engine import GameEngine

BANNER = "Escape the Labyrinth — type 'look' to begin, 'quit' to exit."


def main() -> None:
    engine = GameEngine()
    print(BANNER)
    while True:
        try:
            raw = input("> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if raw.strip().lower() in {"quit", "exit"}:
            break
        try:
            print(engine.execute(raw))
        except NotImplementedError as exc:
            # Starter behavior: the engine is a stub until Lab 02.
            print(exc)


if __name__ == "__main__":
    main()
