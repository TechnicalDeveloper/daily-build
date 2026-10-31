# Tiny Expression Evaluator

Implement a function `evaluate(expr: str) -> int` that evaluates a simple arithmetic expression consisting of non-negative integers, parentheses, and the operators `+`, `-`, `*`. The expression does not contain division. Input is guaranteed to be well-formed. Standard operator precedence applies: `*` binds tighter than `+` and `-`, and `+` and `-` have equal precedence (left-to-right). You must not use `eval()` or any similar dynamic execution.

Edge cases:
- Single number: `"42"` → 42
- Whitespace: `" 5 + 3 "` → 8 (ignore spaces)
- Unary minus is not allowed (no `-5` or `-(2+3)`).
