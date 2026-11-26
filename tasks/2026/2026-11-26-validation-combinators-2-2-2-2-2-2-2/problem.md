# Validation Combinators

Build a small combinator library for validators. A validator is any callable that takes a single value and returns a boolean.

Implement four functions:

- `all_of(*validators)` – returns a validator that returns `True` only when all given validators return `True` for the value.
- `any_of(*validators)` – returns a validator that returns `True` when at least one given validator returns `True`.
- `none_of(*validators)` – returns a validator that returns `True` when none of the given validators return `True`.
- `not_validator(validator)` – returns a validator that returns the negation of the given validator.

**Edge cases**:
- When called with zero validators, `all_of()` should return a validator that always `True` (vacuous truth), `any_of()` always `False`, and `none_of()` always `True`.

Write your solution in `solution.py` and tests in `test_solution.py`.
