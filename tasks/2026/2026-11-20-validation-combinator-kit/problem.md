# Validation Combinator Kit

Build a small validation combinator library. A validator is a callable that takes a value and returns it unchanged if valid, or raises ValueError with a clear message. Implement the following functions:

- `is_string(value)`
- `is_integer(value)`
- `min_length(n)` returns a validator requiring `len(value) >= n`
- `regex(pattern)` returns a validator requiring the value to be a string and fully match `pattern`
- `all_of(*validators)` returns a validator applying each validator in order
- `any_of(*validators)` returns a validator succeeding if at least one validator succeeds
- `optional(validator)` returns a validator that only validates non-None values

Edge cases to respect:
- Booleans are not accepted as integers.
- `regex` uses fullmatch, so partial matches fail.
- `all_of` short-circuits on the first failing validator.
- `any_of` raises a combined error message when none succeed.
