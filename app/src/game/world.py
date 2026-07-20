"""World data — backend-owned starter seam (``src/game/world.py``).

The Squad's `backend` role fills this in from ``specs/speckit/spec.md``:
4–6 connected rooms with directional exits, 2–3 collectible items, and at
least one lock-and-key dependency (tasks.md T001–T003).

The placeholders below are intentionally minimal. Replace them with the real
room graph and item table during Lab 02 — do not treat them as the answer.
"""

# TODO(backend, T001): define 4–6 rooms and their directional exits.
# Example shape only — expand to match the accepted spec:
START_ROOM = "cell"
WIN = "__win__"

ROOMS: dict = {
    "cell": {
        "name": "Cell",
        "description": "A damp stone cell with a cold iron door to the east.",
        "exits": {"east": "armory"},
    },
    "armory": {
        "name": "Armory",
        "description": "A ransacked armory. Bare weapon racks line the walls.",
        "exits": {"west": "cell", "east": "hall"},
    },
    "hall": {
        "name": "Hall",
        "description": "A vaulted hall. A heavy gate seals the passage east.",
        "exits": {"west": "armory", "east": "exit tunnel"},
    },
    "exit tunnel": {
        "name": "Exit Tunnel",
        "description": "A low tunnel. Daylight spills in from the east.",
        "exits": {"west": "hall", "east": WIN},
    },
}

# TODO(backend, T002): define 2–3 collectible items and their locations.
ITEMS: dict = {
    "rusty key": {"name": "Rusty Key", "location": "armory"},
    "torch": {"name": "Torch", "location": "cell"},
}

# TODO(backend, T003): define at least one lock-and-key dependency and the
# single explicit win condition.
LOCKS: dict = {
    "gate": {"room": "hall", "direction": "east", "needs": "rusty key", "locked": True},
}
