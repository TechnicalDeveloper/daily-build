import re

def tokenize(expr):
    expr = expr.replace(' ', '').replace('\t', '').replace('\n', '')
    if not expr:
        raise ValueError("empty expression")
    if not re.match(r'^[\d+\-*/()]+$', expr):
        raise ValueError("invalid characters")
    pattern = r'\d+|[+\-*/()]'
    tokens = re.findall(pattern, expr)
    return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, expected=None):
        tok = self.peek()
        if expected is not None and tok != expected:
            raise ValueError(f"expected '{expected}', got '{tok}'")
        self.pos += 1
        return tok

    def parse_expr(self):
        left = self.parse_term()
        while self.peek() in ('+', '-'):
            op = self.consume()
            right = self.parse_term()
            if op == '+':
                left += right
            else:
                left -= right
        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.peek() in ('*', '/'):
            op = self.consume()
            right = self.parse_factor()
            if op == '*':
                left *= right
            else:
                if right == 0:
                    raise ZeroDivisionError("division by zero")
                left //= right
        return left

    def parse_factor(self):
        tok = self.peek()
        if tok is None:
            raise ValueError("unexpected end of expression")
        if tok == '(':
            self.consume('(')
            val = self.parse_expr()
            self.consume(')')
            return val
        elif tok == '-':
            self.consume('-')
            val = self.parse_factor()
            return -val
        else:
            try:
                val = int(self.consume())
            except ValueError:
                raise ValueError(f"invalid number '{tok}'")
            return val

def evaluate(expr: str) -> int:
    tokens = tokenize(expr)
    parser = Parser(tokens)
    result = parser.parse_expr()
    if parser.peek() is not None:
        raise ValueError("unexpected tokens after expression")
    return result
