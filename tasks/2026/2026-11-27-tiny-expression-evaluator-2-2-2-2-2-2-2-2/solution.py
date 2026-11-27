import re

def tokenize(expression: str):
    """Convert the expression into a list of tokens."""
    tokens = []
    i = 0
    while i < len(expression):
        c = expression[i]
        if c.isspace():
            i += 1
            continue
        if c.isdigit() or (c == '.' and i + 1 < len(expression) and expression[i + 1].isdigit()):
            j = i
            while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            tokens.append(expression[i:j])
            i = j
        elif c in '+-*/()':
            tokens.append(c)
            i += 1
        else:
            raise ValueError(f"Invalid character: {c}")
    return tokens

def evaluate(expression: str) -> float:
    """Evaluate a basic arithmetic expression."""
    tokens = tokenize(expression)
    if not tokens:
        raise ValueError("Empty expression")

    pos = 0

    def parse_expression():
        nonlocal pos
        left = parse_term()
        while pos < len(tokens) and tokens[pos] in ('+', '-'):
            op = tokens[pos]
            pos += 1
            right = parse_term()
            if op == '+':
                left += right
            else:
                left -= right
        return left

    def parse_term():
        nonlocal pos
        left = parse_factor()
        while pos < len(tokens) and tokens[pos] in ('*', '/'):
            op = tokens[pos]
            pos += 1
            right = parse_factor()
            if op == '*':
                left *= right
            else:
                if right == 0:
                    raise ZeroDivisionError("division by zero")
                left /= right
        return left

    def parse_factor():
        nonlocal pos
        if pos >= len(tokens):
            raise SyntaxError("Unexpected end of expression")
        token = tokens[pos]
        if token == '(':
            pos += 1
            val = parse_expression()
            if pos >= len(tokens) or tokens[pos] != ')':
                raise SyntaxError("Missing closing parenthesis")
            pos += 1
            return val
        elif token == '-':
            pos += 1
            return -parse_factor()
        else:
            try:
                val = float(token)
            except ValueError:
                raise SyntaxError(f"Unexpected token: {token}")
            pos += 1
            return val

    result = parse_expression()
    if pos != len(tokens):
        raise SyntaxError("Unexpected trailing characters")
    return result
