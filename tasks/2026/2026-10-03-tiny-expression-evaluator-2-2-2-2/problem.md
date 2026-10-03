# Tiny Expression Evaluator

Build a function `evaluate(expression: str) -> int` that evaluates a simple arithmetic expression.

The expression may contain:
- Non-negative integers
- Parentheses `(` and `)`
- Operators `+`, `-`, `*`, `/` (integer division)

Return the integer result.

### Edge cases to respect
1. Division by zero -> raise `ValueError`
2. Mismatched parentheses -> raise `ValueError`
3. Invalid characters (any non-digit, non-whitespace, not `+-*/()`) -> raise `ValueError`
4. Empty expression -> raise `ValueError`
