// solution.ts
export function evaluate(expression: string): number {
  const tokens = tokenize(expression);
  if (tokens.length === 0) throw new Error('Empty expression');
  let pos = 0;
  const result = parseExpression(tokens);
  if (pos !== tokens.length) throw new Error('Unexpected token after expression');
  return result;

  function tokenize(input: string): Token[] {
    const tokens: Token[] = [];
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
        tokens.push({ type: 'number' as const, value: parseInt(num, 10) });
        continue;
      }
      if ('+-*/()'.includes(ch)) {
        tokens.push({ type: ch as TokenType });
        i++;
        continue;
      }
      throw new Error(`Unexpected character: ${ch}`);
    }
    return tokens;
  }

  function parseExpression(tokens: Token[]): number {
    let left = parseTerm(tokens);
    while (pos < tokens.length && (tokens[pos].type === '+' || tokens[pos].type === '-')) {
      const op = tokens[pos].type;
      pos++;
      const right = parseTerm(tokens);
      if (op === '+') left += right;
      else left -= right;
    }
    return left;
  }

  function parseTerm(tokens: Token[]): number {
    let left = parseFactor(tokens);
    while (pos < tokens.length && (tokens[pos].type === '*' || tokens[pos].type === '/')) {
      const op = tokens[pos].type;
      pos++;
      const right = parseFactor(tokens);
      if (op === '*') {
        left *= right;
      } else {
        if (right === 0) throw new Error('Division by zero');
        left = Math.trunc(left / right);
      }
    }
    return left;
  }

  function parseFactor(tokens: Token[]): number {
    if (pos >= tokens.length) throw new Error('Unexpected end of expression');
    const token = tokens[pos];
    if (token.type === 'number') {
      pos++;
      return token.value as number;
    }
    if (token.type === '(') {
      pos++;
      const value = parseExpression(tokens);
      if (pos >= tokens.length || tokens[pos].type !== ')') {
        throw new Error('Missing closing parenthesis');
      }
      pos++;
      return value;
    }
    throw new Error(`Unexpected token: ${token.type}`);
  }
}

type TokenType = '+' | '-' | '*' | '/' | '(' | ')';

interface Token {
  type: TokenType | 'number';
  value?: number;
}
