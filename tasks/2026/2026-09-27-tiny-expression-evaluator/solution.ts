export function evaluate(expression: string): number {
  const s = expression.replace(/\s+/g, '');
  if (s.length === 0) throw new Error('Empty expression');
  let pos = 0;

  function parseExpression(): number {
    let left = parseTerm();
    while (pos < s.length && (s[pos] === '+' || s[pos] === '-')) {
      const op = s[pos++];
      const right = parseTerm();
      if (op === '+') left += right;
      else left -= right;
    }
    return left;
  }

  function parseTerm(): number {
    let left = parseFactor();
    while (pos < s.length && (s[pos] === '*' || s[pos] === '/')) {
      const op = s[pos++];
      const right = parseFactor();
      if (op === '*') left *= right;
      else {
        if (right === 0) throw new Error('Division by zero');
        left /= right;
      }
    }
    return left;
  }

  function parseFactor(): number {
    if (pos >= s.length) throw new Error('Unexpected end of expression');
    if (s[pos] === '(') {
      pos++;
      const val = parseExpression();
      if (pos >= s.length || s[pos] !== ')') throw new Error('Missing closing parenthesis');
      pos++;
      return val;
    }
    let sign = 1;
    if (s[pos] === '-') {
      sign = -1;
      pos++;
    }
    if (pos >= s.length || !isDigit(s[pos])) throw new Error('Expected number');
    let num = 0;
    while (pos < s.length && isDigit(s[pos])) {
      num = num * 10 + (s.charCodeAt(pos) - 48);
      pos++;
    }
    return sign * num;
  }

  function isDigit(ch: string): boolean {
    return ch >= '0' && ch <= '9';
  }

  const result = parseExpression();
  if (pos !== s.length) throw new Error('Expected number');
  return result;
}
