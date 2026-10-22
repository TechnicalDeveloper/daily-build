# Tiny Expression Evaluator

Build a tiny expression evaluator that parses and evaluates arithmetic expressions consisting of numbers (integers or decimals), binary operators +, -, *, /, parentheses, and unary minus. The function must be named `evaluate` and have the signature `evaluate(expression: string): number`. If the expression is malformed (invalid characters, mismatched parentheses, double operators) or division by zero occurs, throw an `Error` with a descriptive message. Whitespace is allowed and should be ignored.

Edge cases to respect:
- Division by zero must throw an error.
- A leading minus (e.g., `-5+2`) or a minus after an opening parenthesis (e.g., `1+(-2)`) should be treated as unary negation.
- Expressions like `1+(2*3)` must respect operator precedence: `*` and `/` have higher precedence than `+` and `-`.
