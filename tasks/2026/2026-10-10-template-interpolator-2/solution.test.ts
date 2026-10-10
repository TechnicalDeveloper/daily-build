import test from "node:test";
import assert from "node:assert";
import { interpolate } from "./solution";

test("replaces a single placeholder", () => {
  const result = interpolate("Hello, {{name}}!", { name: "Alice" });
  assert.strictEqual(result, "Hello, Alice!");
});

test("replaces multiple placeholders", () => {
  const result = interpolate("{{greeting}}, {{name}}!", {
    greeting: "Hi",
    name: "Bob",
  });
  assert.strictEqual(result, "Hi, Bob!");
});

test("throws when a key is missing", () => {
  assert.throws(
    () => interpolate("{{a}} {{b}}", { a: "x" }),
    /Missing key: b/
  );
});

test("converts non-string values to string", () => {
  const result = interpolate("Age: {{age}}, Active: {{active}}", {
    age: 30,
    active: true,
  });
  assert.strictEqual(result, "Age: 30, Active: true");
});

test("handles placeholders with digits and underscores in keys", () => {
  const result = interpolate("Value: {{my_key_1}}", { my_key_1: 42 });
  assert.strictEqual(result, "Value: 42");
});

test("throws on missing key even if other keys exist", () => {
  assert.throws(
    () => interpolate("{{a}} {{b}} {{c}}", { a: 1, c: 2 }),
    /Missing key: b/
  );
});
