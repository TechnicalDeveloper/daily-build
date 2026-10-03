def tokenize(expr):
    tokens = []
    i = 0
    n = len(expr)
    while i < n:
        ch = expr[i]
        if ch.isspace():
            i += 1
            continue
        if ch.isdigit():
            start = i
            while i < n and expr[i].isdigit():
                i += 1
            tokens.append(int(expr[start:i]))
            continue
        if ch in '+-*/()':
            tokens.append(ch)
            i += 1
            continue
        raise ValueError(f"Invalid character: {ch}")
    return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self):
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def has_more(self):
        return self.pos < len(self.tokens)

    def parse_expression(self):
        result = self.parse_term()
        while self.peek() in ('+', '-'):
            op = self.consume()
            right = self.parse_term()
            if op == '+':
                result += right
            else:
                result -= right
        return result

    def parse_term(self):
        result = self.parse_factor()
        while self.peek() in ('*', '/'):
            op = self.consume()
            right = self.parse_factor()
            if op == '*':
                result *= right
            else:
                if right == 0:
                    raise ValueError("Division by zero")
                result //= right
        return result

    def parse_factor(self):
        token = self.peek()
        if token is None:
            raise ValueError("Unexpected end of expression")
        if isinstance(token, int):
            return self.consume()
        if token == '(':
            self.consume()
            result = self.parse_expression()
            if self.peek() != ')':
                raise ValueError("Mismatched parentheses")
            self.consume()
            return result
        raise ValueError(f"Unexpected token: {token}")

def evaluate(expression: str) -> int:
    tokens = tokenize(expression)
    if not tokens:
        raise ValueError("Empty expression")
    parser = Parser(tokens)
    result = parser.parse_expression()
    if parser.has_more():
        raise ValueError("Extra tokens after expression")
    return result
