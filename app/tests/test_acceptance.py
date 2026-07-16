"""Acceptance scenarios from ``specs/speckit/spec.md``.

TEMPLATE — every test here is skipped until Lab 02. The Squad's `tests` role
turns each skip into a real *failing-first* test (tasks.md T009–T011), then
`backend` and `frontend` implement until they pass. One test maps to one
Given/When/Then scenario in the spec so coverage is traceable.

Remove the module-level skip (and each ``...`` body) as you implement.
"""

import pytest

from game.engine import GameEngine  # noqa: F401  (used once implemented)

pytestmark = pytest.mark.skip(
    reason="Implement in Lab 02 — see specs/speckit/spec.md acceptance scenarios"
)


def test_look_returns_room_description_and_exits():
    # Scenario 1: Given start in Cell, when `look`, then description + exits.
    ...


def test_go_blocked_direction_preserves_room():
    # Scenario 2: Given no north exit from Cell, when `go north`, then denied
    # and player remains in Cell.
    ...


def test_take_item_adds_to_inventory():
    # Scenario 3: Given Rusty Key in Armory, when `take rusty key` in Armory,
    # then inventory includes Rusty Key.
    ...


def test_use_key_unlocks_gate():
    # Scenario 4: Given Gate is locked, when `use rusty key gate`, then Gate
    # unlocks.
    ...


def test_move_through_unlocked_gate():
    # Scenario 5: Given Gate unlocked and player in Hall, when `go east`, then
    # player moves to Exit Tunnel.
    ...


def test_reaching_exit_tunnel_wins():
    # Scenario 6: Given player in Exit Tunnel, when `go east`, then win
    # condition reached.
    ...


def test_unknown_command_returns_guidance():
    # Scenario 7: Given invalid command text, when `dance`, then unknown
    # command guidance is returned and state is preserved.
    ...


def test_mixed_case_input_is_processed():
    # Scenario 8: Given mixed-case input, when `GO EAST`, then command is
    # processed as valid (parsing is case-insensitive).
    ...
