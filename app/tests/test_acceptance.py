"""Acceptance scenarios from specs/speckit/spec.md.

Implemented for a full playthrough: each test maps to one Given/When/Then
scenario so coverage stays traceable to the spec.
"""

from game.engine import GameEngine


def _at_armory() -> GameEngine:
    engine = GameEngine()
    engine.execute("go east")  # Cell -> Armory
    return engine


def _in_hall_with_key() -> GameEngine:
    engine = GameEngine()
    engine.execute("go east")        # Cell -> Armory
    engine.execute("take rusty key")
    engine.execute("go east")        # Armory -> Hall
    return engine


def test_look_returns_room_description_and_exits():
    out = GameEngine().execute("look")
    assert "Cell" in out
    assert "east" in out.lower()


def test_go_blocked_direction_preserves_room():
    engine = GameEngine()
    out = engine.execute("go north")
    assert "can't" in out.lower()
    assert "Cell" in engine.execute("look")


def test_take_item_adds_to_inventory():
    engine = _at_armory()
    engine.execute("take rusty key")
    assert "rusty key" in engine.execute("inventory").lower()


def test_use_key_unlocks_gate():
    engine = _in_hall_with_key()
    out = engine.execute("use rusty key gate")
    assert "unlock" in out.lower()


def test_move_through_unlocked_gate():
    engine = _in_hall_with_key()
    engine.execute("use rusty key gate")
    out = engine.execute("go east")
    assert "Exit Tunnel" in out


def test_reaching_exit_tunnel_wins():
    engine = _in_hall_with_key()
    engine.execute("use rusty key gate")
    engine.execute("go east")        # Hall -> Exit Tunnel
    out = engine.execute("go east")  # Exit Tunnel -> win
    assert engine.won is True
    assert "win" in out.lower()


def test_unknown_command_returns_guidance():
    engine = GameEngine()
    out = engine.execute("dance")
    assert "unknown" in out.lower()
    assert "Cell" in engine.execute("look")


def test_mixed_case_input_is_processed():
    engine = GameEngine()
    out = engine.execute("GO EAST")
    assert "Armory" in out
