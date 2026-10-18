import test from 'node:test';
import assert from 'node:assert';
import { evaluate } from './solution';

test('basic arithmetic', () => {
  assert.strictEqual(evaluate('1+2'), 3);
  assert.strictEqual(evaluate('2*3'), 6);
  assert.strictEqual(evaluate('10/2'), 5);
  assert.strictEqual(evaluate('7-3'), 4);
});

test('operator precedence', () => {
  assert.strictEqual(evaluate('1+2*3'), 7);
  assert.strictEqual(evaluate('2*3+4'), 10);
  assert.strictEqual(evaluate('5-3*2'), -1);
  assert.strictEqual(evaluate('10/2+3'), 8);
});

test('parentheses', () => {
  assert.strictEqual(evaluate('(1+2)*3'), 9);
  assert.strictEqual(evaluate('((2+3)*4)-5'), 15);
  assert.strictEqual(evaluate('2*(3+4)'), 14);
});

test('edge cases', () => {
  assert.throws(() => evaluate('1/0'), RangeError);
  assert.throws(() => evaluate('(1+2'), SyntaxError);
  assert.throws(() => evaluate('1+2)'), SyntaxError);
  assert.throws(() => evaluate('1+a'), SyntaxError);
  assert.strictEqual(evaluate('  2 + 3 '), 5);
  assert.strictEqual(evaluate('(-5)'), -5);
});
