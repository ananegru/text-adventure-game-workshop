# Facilitator Run of Show

## Session Objective

Teach spec-driven development through a game scenario where teams write a durable spec first,
then implement with a multi-agent Squad team against explicit acceptance criteria.

## Preflight

- Have each participant run `./scripts/preflight.sh` from the workshop root — it
  checks tools, GitHub auth, the `app/` tests, and `squad doctor` in one pass.
- Confirm each participant can run Spec Kit (`uvx ... specify`) and Squad commands in this repository.
- Confirm teams can open `specs/speckit/` and `.squad/` locally.
- Remind teams that `specs/speckit/` holds reference solutions — they author their own in Lab 01.
- Share these resources before starting:
  - `prerequisites.md`
  - `materials/spec-template.md`
  - `materials/scoring-rubric.md`
  - `labs/01-spec/README.md`
  - `labs/02-squad/README.md`

## Delivery Flow (~60 min with setup pre-done)

1. Framing (~5 min)
- Explain the core rule: no implementation before a stable spec.
- Set success criteria: acceptance fidelity over feature quantity; a vertical slice beats a broken whole.

2. Plan station (~20 min)
- Teams adopt the reference spec or author their own with Spec Kit (see `labs/01-spec/README.md`).
- Facilitator checks scope, edge cases, and Given/When/Then criteria, then teams designate a source of truth.

3. Implement station (~25 min)
- Teams build the **movement slice** (scenarios 1, 2, 7, 8) from `labs/02-squad/README.md`.
- Encourage role-specific and parallel prompts; the full game is stretch.
- Require explicit tracking of assumptions and unresolved behavior.

4. Playtest and scoring (~10 min)
- Cross-team (or solo) validation against the spec; score with `materials/scoring-rubric.md`.

5. Debrief
- Identify where ambiguous specs caused extra implementation work.
- Identify which Squad capabilities increased throughput or clarity.
- Capture one process change each team will adopt after the workshop.

## Suggested Debrief Questions

- Which acceptance criterion was most ambiguous and how was it resolved?
- Which implementation assumption should have been explicit in the spec?
- How did routing and parallel execution affect your delivery flow?
- What spec or review habit will you carry into production work?

## Facilitator Tips

- Keep teams inside MVP scope to protect completion.
- Redirect design debates back to the written spec.
- Reward explicit assumptions and clear acceptance mapping.
- Prioritize working behavior that matches criteria over extra features.
