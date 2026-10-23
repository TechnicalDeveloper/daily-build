# Validation Combinators Library

## Validation Combinators

Build a set of validation combinators. A **validator** is a callable that takes a value and returns `None` if the value is valid, or an error message string if invalid.

Implement the following factory and combinator functions:

- `is_integer() -> Validator`: passes if value is an `int`.
- `is_positive() -> Validator`: passes if value is an `int` and > 0.
- `is_non_empty_string() -> Validator`: passes if value is a non-empty `str`.
- `is_email() -> Validator`: passes if value is a `str` matching a simple email pattern (contains `@` and a domain).
- `and_(v1, v2) -> Validator`: passes if both `v1` and `v2` pass. Returns the first error.
- `or_(v1, v2) -> Validator`: passes if at least one of `v1` or `v2` passes. Returns error from the second if both fail.
- `not_(v) -> Validator`: passes if `v` fails. Returns a default error message when `v` passes.
- `all_(*validators) -> Validator`: passes if all validators pass. Returns first error.
- `any_(*validators) -> Validator`: passes if at least one validator passes. Returns error from the last if all fail. If no validators given, always fails.
- `maybe(v) -> Validator`: passes if value is `None`; otherwise runs `v`.

### Edge Cases
1. `not_` on a passing validator: should return an error string, not `None`.
2. `all_()` with no arguments: should always pass (return `None`).
3. `maybe` with `None`: should pass regardless of the inner validator.
