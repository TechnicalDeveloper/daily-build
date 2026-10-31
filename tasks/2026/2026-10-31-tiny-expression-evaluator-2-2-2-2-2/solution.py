def evaluate(expr: str) -> int:
    """Evaluate a simple arithmetic expression (+, -, *) with integer non-negative operands."""
    # Remove all whitespace
    expr = ''.join(expr.split())
    if not expr:
        return 0

    # First pass: handle * (higher precedence)
    # We'll process tokens: numbers and operators
    tokens = []
    i = 0
    while i < len(expr):
        ch = expr[i]
        if ch.isdigit():
            num = 0
            while i < len(expr) and expr[i].isdigit():
                num = num * 10 + (ord(expr[i]) - 48)
                i += 1
            tokens.append(num)
        else:
            tokens.append(ch)
            i += 1

    # Now scan for * and / perform multiplication
    new_tokens = []
    i = 0
    while i < len(tokens):
        if i < len(tokens) - 1 and tokens[i+1] == '*':
            left = tokens[i]
            right = tokens[i+2]
            product = left * right
            new_tokens.append(product)
            i += 3
        else:
            new_tokens.append(tokens[i])
            i += 1

    # Now scan for + and - (left to right)
    result = new_tokens[0]
    i = 1
    while i < len(new_tokens):
        op = new_tokens[i]
        num = new_tokens[i+1]
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        i += 2

    return result
