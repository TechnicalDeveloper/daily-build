import test from "node:test";
import assert from "node:assert";
import { evaluate } from "./solution";

test("simple addition", () => {
  assert.strictEqual(evaluate("1+2"), 3);
});

test("operator precedence", () => {
  assert.strictEqual(evaluate("2+3*4"), 14);
});

test("parentheses", () => {
  assert.strictEqual(evaluate("(2+3)*4"), 20);
});

test("division by zero throws", () => {
  assert.throws(() => evaluate("1/0"), /Division by zero/);
});

test("unary minus", () => {
  assert.strictEqual(evaluate("-5+2"), -3);
  assert.strictEqual(evaluate("1+(-2)"), -1);
});

test("complex expression", () => {
  assert.strictEqual(evaluate("((1+2)*3-4)/2"), 2.5);
});

test("malformed expression throws", () => {
  assert.throws(() => evaluate("1++2"), /Unexpected token/);
  assert.throws(() => evaluate("(1+2"), /Missing closing parenthesis/);
});
