# Feature Specification: Escape the Labyrinth

> **Reference solution.** This file is a completed example spec you can compare
> your own work against. In Lab 01 you author your own version with Spec Kit;
> use `materials/spec-template.md` as your blank starting point and treat this
> as the answer key, not the place to write. In Lab 02 the Squad implements
> against whichever spec your facilitator designates as the source of truth.


## User story
As a player, I want to navigate a dungeon, collect key items, and unlock an exit,
so I can complete a short text adventure through clear commands.

## Functional requirements
- The game MUST include 4-6 connected rooms with defined directional exits.
- The game MUST include 2-3 collectible items.
- The game MUST include at least one lock-and-key dependency.
- The game MUST support commands: `look`, `go <direction>`, `take <item>`, `use <item> <target>`, `inventory`.
- The game MUST have one explicit win condition.
- Command parsing MUST be case-insensitive.

## Edge-case requirements
- Unknown command returns an explanatory error and preserves state.
- Movement to a blocked direction returns a blocked message and preserves room.
- Taking a missing item returns a not-found message.
- Using an item before prerequisites are met returns a failure reason.

## Acceptance scenarios
1. Given the player starts in Cell, when the player runs `look`, then room description and visible exits are returned.
2. Given there is no north exit from Cell, when the player runs `go north`, then movement is denied and player remains in Cell.
3. Given Rusty Key is in Armory, when the player runs `take rusty key` in Armory, then inventory includes Rusty Key.
4. Given Gate is locked, when player runs `use rusty key gate`, then Gate unlocks.
5. Given Gate is unlocked and player is in Hall, when player runs `go east`, then player moves to Exit Tunnel.
6. Given player is in Exit Tunnel, when player runs `go east`, then game reports win condition reached.
7. Given invalid command text, when player runs `dance`, then game returns unknown command guidance.
8. Given mixed-case input, when player runs `GO EAST`, then command is processed as valid.

## Non-goals
- Combat mechanics
- NPC dialogue trees
- Procedural map generation
- Save/load system
