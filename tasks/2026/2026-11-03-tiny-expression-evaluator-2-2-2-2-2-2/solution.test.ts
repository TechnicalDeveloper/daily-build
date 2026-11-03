import test from "node:test";
import assert from "node:assert";
import { evaluate } from "./solution";

test('basic addition', () => {
  assert.strictEqual(evaluate('1+2'), 3);
});

test('operator precedence', () => {
  assert.strictEqual(evaluate('2+3*4'), 14);
  assert.strictEqual(evaluate('10-2*3'), 4);
});

test('parentheses', () => {
  assert.strictEqual(evaluate('(1+2)*3'), 9);
  assert.strictEqual(evaluate('(2+3)*(4-1)'), 15);
});

test('unary minus', () => {
  assert.strictEqual(evaluate('-5+3'), -2);
  assert.strictEqual(evaluate('3+-2'), 1);
  assert.strictEqual(evaluate('5*-2'), -10);
});

test('division by zero throws', () => {
  assert.throws(() => evaluate('1/0'), /Division by zero/);
});

test('invalid expression throws', () => {
  assert.throws(() => evaluate('1+'), /Unexpected end/);
  assert.throws(() => evaluate('(1+2'), /Expected \)/);
  assert.throws(() => evaluate('abc'), /Unexpected token/);
});
