"""World data — backend-owned starter seam (``src/game/world.py``).

The Squad's `backend` role fills this in from ``specs/speckit/spec.md``:
4–6 connected rooms with directional exits, 2–3 collectible items, and at
least one lock-and-key dependency (tasks.md T001–T003).

The placeholders below are intentionally minimal. Replace them with the real
room graph and item table during Lab 02 — do not treat them as the answer.
"""

# TODO(backend, T001): define 4–6 rooms and their directional exits.
# Example shape only — expand to match the accepted spec:
ROOMS: dict = {
    # "cell": {"description": "...", "exits": {"east": "corridor"}},
}

# TODO(backend, T002): define 2–3 collectible items and their locations.
ITEMS: dict = {
    # "rusty key": {"location": "armory"},
}

# TODO(backend, T003): define at least one lock-and-key dependency and the
# single explicit win condition.
LOCKS: dict = {
    # "gate": {"needs": "rusty key", "unlocks": "exit tunnel"},
}
