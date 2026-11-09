# Tiny Expression Evaluator

Implement a function `evaluate(expression: string): number` that evaluates a simple arithmetic expression and returns the numeric result.

**Signature**
```typescript
evaluate(expression: string): number
```

**Requirements**
- The expression consists of integers (non-negative), the operators `+`, `-`, `*`, `/`, and parentheses `(` and `)`. Spaces may appear anywhere.
- Operator precedence: `*` and `/` have higher precedence than `+` and `-`; all operators are left-associative.
- Unary minus is **not** required – assume no leading `-` or `(-5)` patterns (but subtraction like `0-5` works).
- Division must perform integer division truncating toward zero (like most languages when both operands are integers).
- Throw an `Error` with a descriptive message if:
  - Division by zero is attempted.
  - The expression is malformed (e.g., mismatched parentheses, multiple operators in a row, trailing operator).

**Edge cases to respect**
- Empty string or whitespace-only input → throw `Error`.
- Expression like `"1+2*3"` → should return `7`, not `9` (precedence).
- Expression like `"(1+2)*3"` → should return `9`.
- Expression like `"10/0"` → throws `Error`.
