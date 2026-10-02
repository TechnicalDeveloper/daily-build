# Tiny Expression Evaluator

Build a function `evaluate(expr: str) -> int` that evaluates a simple arithmetic expression. The expression contains non-negative integers and the operators `+`, `-`, `*`, `/`. No parentheses. Operators follow standard precedence: `*` and `/` bind tighter than `+` and `-`. The expression may contain spaces. Division is integer division (floor division). If division by zero occurs, raise `ValueError`.

Signature: `def evaluate(expr: str) -> int:`

Edge cases to respect:
- Single number returns that number.
- Division by zero raises `ValueError`.
- Expressions with multiple operators and precedence.
