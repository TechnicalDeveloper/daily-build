# Tiny Expression Evaluator

Implement a tiny arithmetic expression evaluator.

Write a function `evaluate(expression: str) -> float` that parses and evaluates arithmetic expressions containing non-negative integer literals, the operators `+`, `-`, `*`, `/`, parentheses, and unary `+`/`-`. Whitespace is ignored.

The evaluation should follow normal operator precedence: `*` and `/` bind tighter than `+` and `-`, and parentheses group sub-expressions.

Edge cases to respect:

- Division by zero must raise `ZeroDivisionError`.
- Invalid characters, empty expressions, unbalanced parentheses, and trailing tokens must raise `ValueError`.
- Unary minus works on numbers and parenthesized expressions.
