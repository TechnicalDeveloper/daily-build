type Op = '+' | '-' | '*' | '/' | '(' | ')';
type Token =
  | { type: 'number'; value: number }
  | { type: 'op'; value: Op }
  | { type: 'eof' };

function tokenize(input: string): Token[] {
  const tokens: Token[] = [];
  let i = 0;
  while (i < input.length) {
    const ch = input[i];
    if (ch === ' ' || ch === '\t' || ch === '\n' || ch === '\r') {
      i++;
      continue;
    }
    if ((ch >= '0' && ch <= '9') || ch === '.') {
      const start = i;
      let seenDot = false;
      while (i < input.length) {
        const c = input[i];
        if (c >= '0' && c <= '9') {
          i++;
        } else if (c === '.') {
          if (seenDot) throw new Error('Unexpected token: .');
          seenDot = true;
          i++;
        } else {
          break;
        }
      }
      const text = input.slice(start, i);
      const num = Number(text);
      if (Number.isNaN(num)) throw new Error('Unexpected token: ' + text);
      tokens.push({ type: 'number', value: num });
      continue;
    }
    if (ch === '+' || ch === '-' || ch === '*' || ch === '/' || ch === '(' || ch === ')') {
      tokens.push({ type: 'op', value: ch as Op });
      i++;
      continue;
    }
    throw new Error('Unexpected token: ' + ch);
  }
  tokens.push({ type: 'eof' });
  return tokens;
}

class Parser {
  private pos = 0;

  constructor(private tokens: Token[]) {}

  parse(): number {
    const value = this.parseAddSub();
    if (this.peek().type !== 'eof') throw new Error('Unexpected token');
    return value;
  }

  private peek(): Token {
    return this.tokens[this.pos];
  }

  private consume(): Token {
    return this.tokens[this.pos++];
  }

  private matchOp(op: Op): boolean {
    const t = this.peek();
    if (t.type === 'op' && t.value === op) {
      this.pos++;
      return true;
    }
    return false;
  }

  private expectOp(op: Op): void {
    const t = this.peek();
    if (t.type !== 'op' || t.value !== op) {
      throw new Error('Expected ' + op);
    }
    this.consume();
  }

  private parseAddSub(): number {
    let left = this.parseMulDiv();
    while (true) {
      const t = this.peek();
      if (t.type === 'op' && (t.value === '+' || t.value === '-')) {
        this.consume();
        const right = this.parseMulDiv();
        left = t.value === '+' ? left + right : left - right;
      } else {
        break;
      }
    }
    return left;
  }

  private parseMulDiv(): number {
    let left = this.parseUnary();
    while (true) {
      const t = this.peek();
      if (t.type === 'op' && (t.value === '*' || t.value === '/')) {
        this.consume();
        const right = this.parseUnary();
        if (t.value === '*') {
          left *= right;
        } else {
          if (right === 0) throw new Error('Division by zero');
          left /= right;
        }
      } else {
        break;
      }
    }
    return left;
  }

  private parseUnary(): number {
    if (this.matchOp('-')) return -this.parseUnary();
    if (this.matchOp('+')) return this.parseUnary();
    return this.parsePrimary();
  }

  private parsePrimary(): number {
    const t = this.peek();
    if (t.type === 'number') {
      this.consume();
      return t.value;
    }
    if (t.type === 'op' && t.value === '(') {
      this.consume();
      const value = this.parseAddSub();
      this.expectOp(')');
      return value;
    }
    if (t.type === 'eof') throw new Error('Unexpected end of expression');
    throw new Error('Unexpected token: ' + (t.type === 'op' ? t.value : '?'));
  }
}

export function evaluate(expr: string): number {
  const tokens = tokenize(expr);
  return new Parser(tokens).parse();
}
