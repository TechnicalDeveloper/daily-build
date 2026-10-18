# Tiny Expression Evaluator

Write a function `evaluate(expression: string): number` that evaluates a simple arithmetic expression and returns the numeric result. The expression may contain:
- Non-negative integers (no decimal points)
- Operators `+`, `-`, `*`, `/`
- Parentheses `(` and `)`
- Whitespace (ignored)

Operator precedence: `*` and `/` have higher precedence than `+` and `-`. Evaluation is left-to-right for same precedence.

Edge cases to handle:
1. Division by zero: throw a `RangeError`.
2. Mismatched parentheses: throw a `SyntaxError`.
3. Invalid characters (anything other than digits, operators, parentheses, or whitespace): throw a `SyntaxError`.
