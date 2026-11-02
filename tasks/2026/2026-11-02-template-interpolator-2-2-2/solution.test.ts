import test from "node:test";
import assert from "node:assert";
import { interpolate } from "./solution";

test('simple replacement', () => {
  assert.strictEqual(interpolate("Hello {{name}}!", { name: "World" }), "Hello World!");
});

test('multiple placeholders', () => {
  assert.strictEqual(interpolate("{{a}} and {{b}}", { a: "foo", b: "bar" }), "foo and bar");
});

test('missing key replaced with empty string', () => {
  assert.strictEqual(interpolate("{{x}}", { y: "z" }), "");
});

test('number converted to string', () => {
  assert.strictEqual(interpolate("Age: {{age}}", { age: 25 }), "Age: 25");
});

test('whitespace inside placeholders trimmed', () => {
  assert.strictEqual(interpolate("Hi {{ name }}!", { name: "Alice" }), "Hi Alice!");
});
