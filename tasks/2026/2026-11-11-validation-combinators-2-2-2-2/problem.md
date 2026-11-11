# Validation Combinators

Build a small set of validation combinators. A validator is any callable that accepts a value and returns a bool. Implement functions that combine validators into new validators.

Signatures:

- `all_of(*validators)` -> callable
- `any_of(*validators)` -> callable
- `none_of(*validators)` -> callable
- `negate(validator)` -> callable

Behaviour:

- `all_of` returns True only when every validator returns True.
- `any_of` returns True when at least one validator returns True.
- `none_of` returns True when every validator returns False.
- `negate` returns True exactly when the wrapped validator returns False.

Edge cases:

- Empty combinators: `all_of()` accepts every value, `any_of()` rejects every value, `none_of()` accepts every value.
- Short-circuit: `all_of` may stop at the first False, `any_of` at the first True, and `none_of` at the first True.
- Validators are called with one positional argument; combine them without mutating global state.
