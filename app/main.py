"""Entry point for Escape the Labyrinth.

Run the game from the `app/` directory:

    uv run python main.py       # (or: python main.py)

This wires the player-facing UI loop (``src/ui``, frontend-owned) to the
game engine (``src/game``, backend-owned). The behavior itself is defined in
``specs/speckit/spec.md`` and implemented by the Squad in Lab 02 — this file
only connects the two seams.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from ui.cli import main  # noqa: E402  (path set above before import)

if __name__ == "__main__":
    main()
