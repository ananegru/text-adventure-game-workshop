# SquadSDD Scoring Rubric

Use this sheet to score an implementation against the spec — in a cross-team
playtest **or** solo.

> **Solo?** Score your own slice against the reference `specs/speckit/spec.md`.
> Only the scenarios you implemented count toward Fidelity and Robustness; mark
> the rest as "not attempted (stretch)".

Team/participant being scored: ____________________
Spec used (source of truth): ______________________
Implemented by: ___________________________________

## Scoring Categories (100 points)

1. Clarity (30)
- 30: Spec is fully implementable with 0-1 clarifications
- 20: Minor ambiguity, 2-3 clarifications needed
- 10: Significant ambiguity, behavior guessed
- 0: Spec not implementable without major rewrite

2. Fidelity to Spec (35)
- 35: All acceptance criteria pass
- 25: Most criteria pass, minor misses
- 15: Several major misses
- 0: Core game behavior diverges from spec

3. Robustness (20)
- 20: Handles all required edge cases
- 12: Handles most edge cases
- 6: Only happy path works
- 0: Frequent invalid-state failures

4. Team Flow with Squad (15)
- 15: Clear use of routing, parallelization, and memory
- 10: Partial use of Squad capabilities
- 5: Mostly single-agent style usage
- 0: No visible Squad workflow

## Bonuses

- +5 Zero-Question Build: implemented with 0 clarifying questions
- +5 Spec Coverage: every acceptance criterion traced to a test/check

## Penalties

- -5 Hidden Assumption: undocumented behavior added silently
- -5 Scope Creep: non-requested features caused missed required behavior

## Final Score

Subtotal: ______ / 100
Bonuses: ______
Penalties: ______
Final: ______

## Notes

What worked well:

- 
- 

Where spec could improve:

- 
- 

Where implementation could improve:

- 
- 
