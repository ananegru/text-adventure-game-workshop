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

import copy

from . import world


class GameEngine:
    """Holds world state and executes one player command at a time."""

    def __init__(self) -> None:
        # TODO(backend, T001–T003): load rooms/items/locks from world.py,
        # set the starting room, and initialize inventory + lock state.
        self.rooms = copy.deepcopy(world.ROOMS)
        self.items = copy.deepcopy(world.ITEMS)
        self.locks = copy.deepcopy(world.LOCKS)
        self.location = world.START_ROOM
        self.inventory: list[str] = []
        self.won: bool = False

    def execute(self, command: str) -> str:
        """Parse and run a single command, returning the text response.

        Case-insensitive. Each command and edge case maps to an acceptance
        scenario in ``specs/speckit/spec.md``.
        """
        text = (command or "").strip()
        if not text:
            return self._unknown("")
        parts = text.lower().split()
        verb, args = parts[0], parts[1:]

        if verb == "look":
            return self._look()
        if verb == "inventory":
            return self._inventory()
        if verb == "go":
            if not args:
                return "Go where? Try: go <direction>."
            return self._go(args[0])
        if verb == "take":
            if not args:
                return "Take what? Try: take <item>."
            return self._take(" ".join(args))
        if verb == "use":
            if len(args) < 2:
                return "Use what on what? Try: use <item> <target>."
            return self._use(" ".join(args[:-1]), args[-1])
        return self._unknown(text)

    # --- helpers -------------------------------------------------------

    def _room(self) -> dict:
        return self.rooms[self.location]

    def _look(self) -> str:
        room = self._room()
        exits = ", ".join(sorted(room["exits"])) or "none"
        lines = [room["name"], room["description"], f"Exits: {exits}."]
        here = sorted(
            self.items[i]["name"]
            for i in self.items
            if self.items[i]["location"] == self.location
        )
        if here:
            lines.append("You see: " + ", ".join(here) + ".")
        return "\n".join(lines)

    def _go(self, direction: str) -> str:
        exits = self._room()["exits"]
        if direction not in exits:
            available = ", ".join(sorted(exits)) or "none"
            return f"You can't go {direction} from here. (Exits: {available}.)"
        lock_name = self._lock_for(self.location, direction)
        if lock_name and self.locks[lock_name]["locked"]:
            return f"The {lock_name} is locked. You need to unlock it first."
        dest = exits[direction]
        if dest == world.WIN:
            self.won = True
            return "You step through into the daylight beyond. You escaped the labyrinth. You win!"
        self.location = dest
        return self._look()

    def _take(self, item_name: str) -> str:
        item_id = self._resolve_item(item_name)
        if item_id is None or self.items[item_id]["location"] != self.location:
            return f"There is no {item_name} here to take."
        self.items[item_id]["location"] = "__inventory__"
        self.inventory.append(item_id)
        return f"You take the {self.items[item_id]['name']}."

    def _use(self, item_name: str, target: str) -> str:
        item_id = self._resolve_item(item_name)
        if item_id is None or item_id not in self.inventory:
            return f"You don't have a {item_name} to use."
        target = target.strip().lower()
        lock = self.locks.get(target)
        if lock is None:
            return f"You can't use the {self.items[item_id]['name']} on {target}."
        if lock["needs"] != item_id:
            return f"The {self.items[item_id]['name']} doesn't fit the {target}."
        if not lock["locked"]:
            return f"The {target} is already unlocked."
        lock["locked"] = False
        return f"You use the {self.items[item_id]['name']} on the {target}. The {target} unlocks."

    def _inventory(self) -> str:
        if not self.inventory:
            return "Your inventory is empty."
        names = ", ".join(self.items[i]["name"] for i in self.inventory)
        return f"Inventory: {names}."

    def _resolve_item(self, name: str) -> str | None:
        name = name.strip().lower()
        for item_id, data in self.items.items():
            if item_id == name or data["name"].lower() == name:
                return item_id
        return None

    def _lock_for(self, room: str, direction: str) -> str | None:
        for name, lock in self.locks.items():
            if lock["room"] == room and lock["direction"] == direction:
                return name
        return None

    def _unknown(self, text: str) -> str:
        return (
            f"Unknown command: '{text}'. "
            "Try: look, go <direction>, take <item>, use <item> <target>, inventory."
        )
