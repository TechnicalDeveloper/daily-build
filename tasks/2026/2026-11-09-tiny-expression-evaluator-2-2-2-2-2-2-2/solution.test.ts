// tests.ts
import test from "node:test";
import assert from "node:assert";
import { evaluate } from "./solution";

test("basic arithmetic", () => {
  assert.strictEqual(evaluate("3+5"), 8);
  assert.strictEqual(evaluate("10-4"), 6);
  assert.strictEqual(evaluate("2*3"), 6);
  assert.strictEqual(evaluate("8/2"), 4);
});

test("operator precedence and parentheses", () => {
  assert.strictEqual(evaluate("1+2*3"), 7);
  assert.strictEqual(evaluate("(1+2)*3"), 9);
  assert.strictEqual(evaluate("2*3+4"), 10);
  assert.strictEqual(evaluate("10-2*3"), 4);
});

test("multiple operators and whitespace", () => {
  assert.strictEqual(evaluate(" 1 + 2 "), 3);
  assert.strictEqual(evaluate("2*3+4/2"), 8);
  assert.strictEqual(evaluate("((1+2)*(3+4))"), 21);
  assert.strictEqual(evaluate("100/3/2"), 16);
});

test("throws on division by zero or malformed input", () => {
  assert.throws(() => evaluate("10/0"), /Division by zero/);
  assert.throws(() => evaluate(""), /Empty expression/);
  assert.throws(() => evaluate("   "), /Empty expression/);
  assert.throws(() => evaluate("1+"), /Unexpected end/);
  assert.throws(() => evaluate("(1+2"), /Missing closing parenthesis/);
});
