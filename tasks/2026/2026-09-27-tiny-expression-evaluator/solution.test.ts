import test from "node:test";
import assert from "node:assert";
import { evaluate } from "./solution";

test("basic arithmetic", () => {
  assert.strictEqual(evaluate("1+2"), 3);
  assert.strictEqual(evaluate("3*4"), 12);
  assert.strictEqual(evaluate("10-5"), 5);
  assert.strictEqual(evaluate("20/4"), 5);
});

test("operator precedence", () => {
  assert.strictEqual(evaluate("1+2*3"), 7);
  assert.strictEqual(evaluate("2*3+4"), 10);
  assert.strictEqual(evaluate("10-2*3"), 4);
});

test("parentheses", () => {
  assert.strictEqual(evaluate("(1+2)*3"), 9);
  assert.strictEqual(evaluate("10/(2+3)"), 2);
  assert.strictEqual(evaluate("((1+2)*3)"), 9);
});

test("division by zero", () => {
  assert.throws(() => evaluate("5/0"), /Division by zero/);
});

test("invalid expressions", () => {
  assert.throws(() => evaluate(""), /Empty expression/);
  assert.throws(() => evaluate("(1+2"), /Missing closing parenthesis/);
  assert.throws(() => evaluate("1+2a"), /Expected number/);
});
