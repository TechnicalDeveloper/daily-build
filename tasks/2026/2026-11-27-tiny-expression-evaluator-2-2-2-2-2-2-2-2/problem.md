# Tiny Expression Evaluator

Implement a function `evaluate(expression: str) -> float` that evaluates a basic arithmetic expression. The expression can contain non-negative integers, decimal numbers, operators `+`, `-`, `*`, `/`, parentheses `( )`, and unary minus. Whitespace should be ignored. The function must respect standard operator precedence (`*` and `/` before `+` and `-`) and left associativity. Use float division.

Edge cases to handle:
- Division by zero must raise `ZeroDivisionError`.
- Invalid tokens or syntax (e.g., `1+`, `(1+2`, `1/0`) must raise appropriate errors (`SyntaxError` or `ValueError`).
- Empty expressions should raise `ValueError`.
- Unary minus must work, e.g., `-5` gives `-5.0`, `-(-5)` gives `5.0`.
- Decimal numbers and mixed operations must work correctly.
