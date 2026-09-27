# Tiny Expression Evaluator

# Tiny Expression Evaluator

Implement a function `evaluate(expression: string): number` that evaluates arithmetic expressions.

**Supported features:**
- Integers (may have a leading minus sign only at the start of a number)
- Binary operators `+`, `-`, `*`, `/`
- Parentheses for grouping
- Spaces are ignored

**Operator precedence:** Multiplication and division have higher precedence than addition and subtraction.

**Edge cases to handle:**
1. Empty string should throw an Error.
2. Division by zero should throw an Error.
3. Mismatched parentheses should throw an Error.
4. Invalid characters (e.g., letters) should throw an Error.
