# Validation Combinators

## Problem

Implement a set of validation combinators. A validator is a function that takes a value and returns a tuple `(bool, result)`. If the bool is `True`, the validation succeeded and the result is the validated value (possibly transformed). If the bool is `False`, the validation failed and the result is an error message (string) or a list of error messages.

### Functions to implement:

- `ok()` - returns a validator that always succeeds, returning the value unchanged.
- `fail(error_message)` - returns a validator that always fails with the given error message.
- `all_of(*validators)` - returns a validator that applies each validator in order. Returns the first failure if any, otherwise succeeds with the original value.
- `one_of(*validators)` - returns a validator that tries each validator in order. Returns the first success if any; if all fail, returns failure with a list of all error messages.
- `transform(validator, func)` - returns a validator that, if the inner validator succeeds, applies `func` to the value and returns the transformed value; if it fails, returns the error. If `func` raises an exception, return failure with the exception string.
- `satisfies(predicate, error_message)` - returns a validator that succeeds if the predicate returns `True` for the value, otherwise fails with the given error message.

### Edge cases to respect:

- `all_of()` (no arguments) should always succeed.
- `one_of()` (no arguments) should always fail with an empty list of errors.
- `one_of` should collect all error messages when all validators fail.
- `transform` should catch exceptions during transformation and return them as error messages.
