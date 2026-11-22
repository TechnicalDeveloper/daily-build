# Set of Validation Combinators

# Validation Combinators

Build a small library of higher-order functions that combine validation functions (validators). A validator is any callable that takes a single value and returns `True` if the value is considered valid, `False` otherwise.

Your task is to implement four combinators:

- `all_of(*validators)`: returns a validator that returns `True` only if all given validators return `True` for the value.
- `any_of(*validators)`: returns a validator that returns `True` if at least one given validator returns `True`.
- `none_of(*validators)`: returns a validator that returns `True` if none of the given validators return `True`.
- `not_validator(validator)`: returns a validator that negates the result of the given validator.

All functions should be defined in `solution.py` and should be importable by `from solution import all_of, any_of, none_of, not_validator`.

## Edge Cases to Respect

- An empty argument list to `all_of` should return `True` (vacuous truth).
- An empty argument list to `any_of` should return `False`.
- An empty argument list to `none_of` should return `True` (no validator passes).
- The combinators must work with any callable, including lambdas, built-in functions, or user-defined functions.

## Example (Not Part of Output)

```python
def is_even(x): return x % 2 == 0
def is_positive(x): return x > 0

validator = all_of(is_even, is_positive)
print(validator(4))   # True
print(validator(-2))  # False
```
