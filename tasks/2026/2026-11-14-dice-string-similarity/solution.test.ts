import test from "node:test";
import assert from "node:assert";
import { diceCoefficient } from "./solution";

test("identical non-empty strings have similarity 1", () => {
  assert.strictEqual(diceCoefficient("abc", "abc"), 1);
});

test("completely different strings have similarity 0", () => {
  assert.strictEqual(diceCoefficient("abc", "xyz"), 0);
});

test("empty strings both return 1", () => {
  assert.strictEqual(diceCoefficient("", ""), 1);
});

test("one empty string returns 0", () => {
  assert.strictEqual(diceCoefficient("abc", ""), 0);
  assert.strictEqual(diceCoefficient("", "abc"), 0);
});

test("handles single-character strings", () => {
  assert.strictEqual(diceCoefficient("a", "a"), 1);
  assert.strictEqual(diceCoefficient("a", "b"), 0);
});

test("case sensitivity matters", () => {
  assert.ok(diceCoefficient("Hello", "hello") < 1);
  assert.ok(diceCoefficient("Hello", "hello") > 0);
});

test("similar strings have higher similarity than dissimilar ones", () => {
  assert.ok(diceCoefficient("kitten", "sitting") > diceCoefficient("kitten", "school"));
});
