# Escape the Labyrinth Constitution

> **Reference solution.** A completed example artifact for comparison. Author
> your own in Lab 01 with Spec Kit; treat this as the answer key.


## Principle 1: Spec before implementation
Implementation work must follow accepted specification artifacts.
No coding starts before `spec.md` and `tasks.md` are clear.

## Principle 2: Scope discipline
The MVP is a text adventure with room traversal, inventory, item use,
and one explicit win condition. Non-goals must stay out.

## Principle 3: Acceptance criteria are the contract
Given/When/Then criteria in `spec.md` define done.
Implementation quality is measured against these criteria.

## Principle 4: Edge-case behavior is explicit
Unknown commands, invalid movement, missing items, and unmet prerequisites
must have deterministic responses documented in the spec.

## Principle 5: Multi-agent ownership
Work is routed by domain across backend, frontend, docs, tests, devops,
reviewer, architect, and security.
