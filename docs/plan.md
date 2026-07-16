# SquadSDD Workshop Plan

## Problem Statement

Teams that skip formal specifications move quickly at first, then pay with drift and rework.
With AI agent teams this gets worse: humans and agents fill ambiguity differently.

This workshop enforces a simple rule: write and align on the spec first, then implement.

## Goal

Teach participants to treat the specification as a durable, version-controlled artifact,
then use a pre-built Squad team to implement directly against that artifact.

## Learning Objectives

By the end, participants can:

- Produce a usable Spec Kit artifact chain (`constitution`, `spec`, `plan`, `tasks`)
- Translate acceptance criteria into implementation and tests
- Route work across a specialized Squad instead of one general agent
- Score implementation fidelity against the original specification

## Workshop Stations

1. Plan station
- Create the feature specification for "Escape the Labyrinth"
- Capture scope, behavior, edge cases, non-goals, and acceptance criteria
- Finalize Spec Kit artifacts under `specs/speckit/`

2. Implement station
- Hand the spec to the Squad team in `.squad/`
- Execute with role routing, model selection, and parallel work
- Track assumptions and unresolved criteria explicitly

3. Validate and debrief
- Cross-check implementation versus acceptance criteria
- Score clarity, fidelity, robustness, and team flow
- Capture improvements for the next iteration

## Running Example

"Escape the Labyrinth" text adventure with:

- Room navigation
- Item collection and use
- Lock-and-key dependency
- Explicit win condition
- Defined command and edge-case behavior

## Deliverables

- Spec files in `specs/speckit/`
- A working vertical slice in `app/` (full game is stretch)
- Implementation summary from the Squad run
- Acceptance pass/fail map
- Scoring rubric from playtest

## Risks and Mitigations

1. Risk: teams overbuild and miss core acceptance criteria
Mitigation: enforce MVP scope and non-goals from the spec.

2. Risk: implementation starts before specification is stable
Mitigation: require spec sign-off before squad implementation prompts.

3. Risk: unclear ownership during multi-agent execution
Mitigation: use `.squad/routing.md` and explicit role prompts.

4. Risk: subjective evaluation during playtest
Mitigation: score only against written acceptance criteria.
