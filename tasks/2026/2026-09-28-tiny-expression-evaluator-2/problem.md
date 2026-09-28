# Tiny Expression Evaluator

Implement a function `evaluate(expr: str) -> int` that evaluates a simple arithmetic expression and returns the integer result.

The expression supports:
- Integers (non-negative, but can be negative via unary minus)
- Binary operators `+`, `-`, `*`, `/` (integer division, truncating toward negative infinity as in Python floor division)
- Parentheses `(` and `)` for grouping
- Whitespace is ignored

**Signature:**
```python
def evaluate(expr: str) -> int:
```

**Edge cases to respect:**
1. Division by zero must raise `ZeroDivisionError`.
2. An empty string must raise `ValueError`.
3. Invalid characters (anything other than digits, `+`, `-`, `*`, `/`, `(`, `)`, and whitespace) must raise `ValueError`.
