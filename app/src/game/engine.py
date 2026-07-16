"""Game engine — backend-owned starter seam (``src/game/engine.py``).

Implements the room graph traversal, inventory, item dependencies,
case-insensitive command parsing, deterministic edge-case messages, and the
win condition described in ``specs/speckit/spec.md`` (tasks.md T001–T005).

This is a STARTER STUB. ``execute`` deliberately raises ``NotImplementedError``
so the implementation seam is obvious and the baseline tests stay honest. The
Squad replaces this with real behavior in Lab 02 — map each branch back to an
acceptance scenario in the spec.
"""

from __future__ import annotations


class GameEngine:
    """Holds world state and executes one player command at a time."""

    def __init__(self) -> None:
        # TODO(backend, T001–T003): load rooms/items/locks from world.py,
        # set the starting room, and initialize inventory + lock state.
        self.won: bool = False

    def execute(self, command: str) -> str:
        """Parse and run a single command, returning the text response.

        Replace this stub with real behavior. Every supported command
        (`look`, `go <direction>`, `take <item>`, `use <item> <target>`,
        `inventory`) and every edge case (unknown command, blocked movement,
        missing item, unmet prerequisite, mixed-case input) must map to an
        acceptance scenario in ``specs/speckit/spec.md``.
        """
        raise NotImplementedError(
            "Command handling is not implemented yet. Implement it in Lab 02 "
            "(see specs/speckit/tasks.md T004 and the acceptance scenarios in "
            "specs/speckit/spec.md)."
        )
