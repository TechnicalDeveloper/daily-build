def _tokenize(expression: str):
    tokens = []
    i = 0
    while i < len(expression):
        c = expression[i]
        if c.isspace():
            i += 1
            continue
        if c.isdigit():
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            tokens.append(int(expression[i:j]))
            i = j
            continue
        if c in "+-*/()":
            tokens.append(c)
            i += 1
            continue
        raise ValueError(f"Unknown character {c!r}")
    return tokens


class _Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0

    def peek(self):
        if self.idx < len(self.tokens):
            return self.tokens[self.idx]
        return None

    def consume(self):
        token = self.peek()
        if token is None:
            raise ValueError("Unexpected end of input")
        self.idx += 1
        return token

    def match(self, value):
        if self.peek() == value:
            return self.consume()
        return None

    def expect(self, value):
        if self.peek() == value:
            return self.consume()
        raise ValueError(f"Expected {value!r}")

    def parse_expression(self):
        value = self.parse_term()
        while self.peek() in ("+", "-"):
            op = self.consume()
            right = self.parse_term()
            if op == "+":
                value += right
            else:
                value -= right
        return value

    def parse_term(self):
        value = self.parse_factor()
        while self.peek() in ("*", "/"):
            op = self.consume()
            right = self.parse_factor()
            if op == "*":
                value *= right
            else:
                if right == 0:
                    raise ZeroDivisionError("division by zero")
                value /= right
        return value

    def parse_factor(self):
        token = self.peek()
        if token == "-":
            self.consume()
            return -self.parse_factor()
        if token == "+":
            self.consume()
            return self.parse_factor()
        if isinstance(token, int):
            self.consume()
            return float(token)
        if token == "(":
            self.consume()
            value = self.parse_expression()
            self.expect(")")
            return value
        raise ValueError(f"Unexpected token {token!r}")


def evaluate(expression: str) -> float:
    tokens = _tokenize(expression)
    if not tokens:
        raise ValueError("Empty expression")
    parser = _Parser(tokens)
    result = parser.parse_expression()
    if parser.peek() is not None:
        raise ValueError(f"Unexpected token {parser.peek()!r}")
    return result
