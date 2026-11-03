# Tiny Expression Evaluator

Implement a function `evaluate(expr: string): number` that parses and evaluates a simple arithmetic expression. The expression may contain:
- Numbers (integers and decimals, e.g., `42`, `3.14`)
- Operators `+`, `-`, `*`, `/`
- Parentheses `(` and `)`
- Whitespace (ignored)

The function should respect standard operator precedence (`*` and `/` before `+` and `-`) and left-associativity.

**Edge cases to handle:**
1. Division by zero -- throw an `Error`.
2. Unary minus (e.g., `-3+2` or `5*-2`).
3. Invalid input (unexpected characters, mismatched parentheses) -- throw an `Error`.
