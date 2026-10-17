# Mini Expression Evaluator

Build a tiny expression evaluator that parses and evaluates arithmetic expressions consisting of numbers (integers or floats), the operators +, -, *, /, parentheses, and unary minus. The function must respect standard operator precedence (* and / before + and -) and left associativity. Spaces are ignored.

**Signature:**
```python
def evaluate(expression: str) -> float:
```

**Edge cases to handle:**
- Division by zero must raise `ZeroDivisionError`.
- Invalid syntax (e.g., missing operand, extra operator, mismatched parentheses, empty expression) must raise `ValueError` with a descriptive message.
- Unary minus (e.g., `-3`, `-(5+2)`) must be supported.
