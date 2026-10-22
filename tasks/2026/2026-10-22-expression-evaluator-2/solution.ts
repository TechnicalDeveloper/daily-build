enum TokenType { Number, Plus, Minus, Star, Slash, LParen, RParen, End }

interface Token {
  type: TokenType;
  value: number;
}

class Lexer {
  private pos = 0;
  private tokens: Token[] = [];

  constructor(private text: string) {}

  tokenize(): Token[] {
    while (this.pos < this.text.length) {
      const ch = this.text[this.pos];
      if (ch === ' ' || ch === '\t') {
        this.pos++;
        continue;
      }
      if (ch >= '0' && ch <= '9') {
        let num = '';
        while (this.pos < this.text.length && ((this.text[this.pos] >= '0' && this.text[this.pos] <= '9') || this.text[this.pos] === '.')) {
          num += this.text[this.pos];
          this.pos++;
        }
        this.tokens.push({ type: TokenType.Number, value: parseFloat(num) });
      } else if (ch === '+') {
        this.tokens.push({ type: TokenType.Plus, value: 0 });
        this.pos++;
      } else if (ch === '-') {
        this.tokens.push({ type: TokenType.Minus, value: 0 });
        this.pos++;
      } else if (ch === '*') {
        this.tokens.push({ type: TokenType.Star, value: 0 });
        this.pos++;
      } else if (ch === '/') {
        this.tokens.push({ type: TokenType.Slash, value: 0 });
        this.pos++;
      } else if (ch === '(') {
        this.tokens.push({ type: TokenType.LParen, value: 0 });
        this.pos++;
      } else if (ch === ')') {
        this.tokens.push({ type: TokenType.RParen, value: 0 });
        this.pos++;
      } else {
        throw new Error(`Unexpected character '${ch}'`);
      }
    }
    this.tokens.push({ type: TokenType.End, value: 0 });
    return this.tokens;
  }
}

export class Parser {
  private pos = 0;
  private tokens: Token[];

  constructor(tokens: Token[]) {
    this.tokens = tokens;
  }

  parse(): number {
    const result = this.parseExpression();
    if (this.current().type !== TokenType.End) {
      throw new Error('Unexpected token after expression');
    }
    return result;
  }

  private current(): Token {
    return this.tokens[this.pos];
  }

  private advance(): Token {
    const token = this.tokens[this.pos];
    this.pos++;
    return token;
  }

  private parseExpression(): number {
    let left = this.parseTerm();
    while (this.current().type === TokenType.Plus || this.current().type === TokenType.Minus) {
      const op = this.advance();
      const right = this.parseTerm();
      if (op.type === TokenType.Plus) {
        left += right;
      } else {
        left -= right;
      }
    }
    return left;
  }

  private parseTerm(): number {
    let left = this.parseFactor();
    while (this.current().type === TokenType.Star || this.current().type === TokenType.Slash) {
      const op = this.advance();
      const right = this.parseFactor();
      if (op.type === TokenType.Star) {
        left *= right;
      } else {
        if (right === 0) {
          throw new Error('Division by zero');
        }
        left /= right;
      }
    }
    return left;
  }

  private parseFactor(): number {
    const token = this.current();
    if (token.type === TokenType.Number) {
      this.advance();
      return token.value;
    } else if (token.type === TokenType.LParen) {
      this.advance(); // consume '('
      const expr = this.parseExpression();
      if (this.current().type !== TokenType.RParen) {
        throw new Error('Missing closing parenthesis');
      }
      this.advance(); // consume ')'
      return expr;
    } else if (token.type === TokenType.Minus) {
      // unary minus
      this.advance();
      return -this.parseFactor();
    } else {
      throw new Error('Unexpected token in factor position');
    }
  }
}

export function evaluate(expression: string): number {
  const lexer = new Lexer(expression);
  const tokens = lexer.tokenize();
  const parser = new Parser(tokens);
  return parser.parse();
}
