import re

def tokenize(expr: str):
    i = 0
    n = len(expr)
    while i < n:
        ch = expr[i]
        if ch.isspace():
            i += 1
            continue
        if ch.isdigit() or ch == '.':
            start = i
            while i < n and (expr[i].isdigit() or expr[i] == '.'):
                i += 1
            num_str = expr[start:i]
            if num_str.count('.') > 1:
                raise ValueError("Invalid number literal")
            yield ('NUMBER', float(num_str))
            continue
        if ch in '+-*/':
            yield ('OP', ch)
            i += 1
            continue
        if ch == '(':
            yield ('LPAREN', ch)
            i += 1
            continue
        if ch == ')':
            yield ('RPAREN', ch)
            i += 1
            continue
        raise ValueError(f"Unexpected character: {ch}")


def evaluate(expression: str) -> float:
    tokens = list(tokenize(expression))
    pos = 0

    def peek():
        return tokens[pos] if pos < len(tokens) else None

    def consume(expected=None):
        nonlocal pos
        token = tokens[pos]
        if expected is not None:
            if token[0] != expected and token[1] != expected:
                raise ValueError(f"Expected {expected}, got {token[1]}")
        pos += 1
        return token

    def parse_expression() -> float:
        result = parse_term()
        while peek() and peek()[0] == 'OP' and peek()[1] in ('+', '-'):
            op = consume()[1]
            right = parse_term()
            if op == '+':
                result += right
            else:
                result -= right
        return result

    def parse_term() -> float:
        result = parse_factor()
        while peek() and peek()[0] == 'OP' and peek()[1] in ('*', '/'):
            op = consume()[1]
            right = parse_factor()
            if op == '*':
                result *= right
            else:
                if right == 0:
                    raise ZeroDivisionError("division by zero")
                result /= right
        return result

    def parse_factor() -> float:
        token = peek()
        if token is None:
            raise ValueError("Unexpected end of expression")
        if token[0] == 'NUMBER':
            return consume()[1]
        if token[0] == 'LPAREN':
            consume()
            val = parse_expression()
            if not peek() or peek()[0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            consume()
            return val
        if token[0] == 'OP' and token[1] == '-':
            consume()
            return -parse_factor()
        raise ValueError(f"Unexpected token: {token[1]}")

    result = parse_expression()
    if pos != len(tokens):
        raise ValueError("Extra tokens after expression")
    return result
