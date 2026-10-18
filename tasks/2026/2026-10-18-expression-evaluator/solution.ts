export function evaluate(expression: string): number {
  const tokens = tokenize(expression);
  let pos = 0;

  function peek(): string | undefined {
    return tokens[pos];
  }

  function consume(): string {
    return tokens[pos++];
  }

  function parseExpression(): number {
    let left = parseTerm();
    while (peek() === '+' || peek() === '-') {
      const op = consume();
      const right = parseTerm();
      left = op === '+' ? left + right : left - right;
    }
    return left;
  }

  function parseTerm(): number {
    let left = parseFactor();
    while (peek() === '*' || peek() === '/') {
      const op = consume();
      const right = parseFactor();
      left = op === '*' ? left * right : divide(left, right);
    }
    return left;
  }

  function divide(a: number, b: number): number {
    if (b === 0) {
      throw new RangeError('Division by zero');
    }
    return a / b;
  }

  function parseFactor(): number {
    const token = peek();
    if (token === '(') {
      consume();
      const value = parseExpression();
      if (peek() !== ')') {
        throw new SyntaxError('Mismatched parentheses');
      }
      consume();
      return value;
    }
    if (token === '-' || token === '+') {
      const op = consume();
      const factor = parseFactor();
      return op === '-' ? -factor : factor;
    }
    if (token !== undefined && /^\d+$/.test(token)) {
      return parseInt(consume(), 10);
    }
    throw new SyntaxError(`Unexpected token: ${token}`);
  }

  const result = parseExpression();
  if (pos !== tokens.length) {
    throw new SyntaxError('Unexpected characters after expression');
  }
  return result;
}

function tokenize(input: string): string[] {
  const tokens: string[] = [];
  let i = 0;
  while (i < input.length) {
    const ch = input[i];
    if (/\s/.test(ch)) {
      i++;
      continue;
    }
    if (/[0-9]/.test(ch)) {
      let num = '';
      while (i < input.length && /[0-9]/.test(input[i])) {
        num += input[i];
        i++;
      }
      tokens.push(num);
      continue;
    }
    if ('+-*/()'.includes(ch)) {
      tokens.push(ch);
      i++;
      continue;
    }
    throw new SyntaxError(`Invalid character: '${ch}'`);
  }
  return tokens;
}
