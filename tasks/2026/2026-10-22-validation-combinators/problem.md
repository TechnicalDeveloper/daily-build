# Validation Combinators

Build a set of validation combinators. A validator is a function that takes a value and returns a tuple `(bool, str)`, where `bool` indicates success (`True` for valid) and `str` is `None` on success or an error message on failure.

Implement the following functions:

- `predicate(check, error_msg)` – returns a validator that calls `check(value)` and returns `(True, None)` if true, else `(False, error_msg)`.
- `all_of(*validators)` – returns a validator that runs each validator in sequence and succeeds only if all succeed; returns the first failure.
- `any_of(*validators)` – returns a validator that succeeds if any validator succeeds; if all fail, returns `(False, concatenated error messages with '; ')`.
- `optional(validator)` – returns a validator that passes `None` without error, otherwise runs the given validator.
- `not_validator(validator)` – returns a validator that negates the given validator; if the original succeeds, it fails with `'Value not expected'` and vice versa (success with `None`).

Edge cases to respect:
- `all_of()` with no arguments must always succeed.
- `any_of()` with no arguments must always fail with `'No validators provided'`.
- Nested combinators (e.g., `all_of(any_of(...), optional(...))`) must work correctly.
- Validators must handle `None` values when used with `optional`.
