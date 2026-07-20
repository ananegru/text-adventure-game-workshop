"""Baseline smoke tests — these pass before Lab 02 begins.

They prove the project is wired correctly (packages import, the engine
instantiates, the implementation seam exists) without asserting any game
behavior. Keep these green; add real behavior tests in ``test_acceptance.py``.
"""

from game.engine import GameEngine


def test_engine_instantiates():
    engine = GameEngine()
    assert engine.won is False


def test_execute_returns_text_response():
    # After Lab 02 the seam is implemented: execute returns a text response.
    out = GameEngine().execute("look")
    assert isinstance(out, str) and out.strip()
