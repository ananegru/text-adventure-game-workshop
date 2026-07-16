"""Baseline smoke tests — these pass before Lab 02 begins.

They prove the project is wired correctly (packages import, the engine
instantiates, the implementation seam exists) without asserting any game
behavior. Keep these green; add real behavior tests in ``test_acceptance.py``.
"""

import pytest

from game.engine import GameEngine


def test_engine_instantiates():
    engine = GameEngine()
    assert engine.won is False


def test_execute_is_the_implementation_seam():
    # Starting state: command handling is not implemented yet. The Squad
    # replaces this in Lab 02 (specs/speckit/tasks.md T004). Until then the
    # engine documents its own seam by raising NotImplementedError.
    with pytest.raises(NotImplementedError):
        GameEngine().execute("look")
