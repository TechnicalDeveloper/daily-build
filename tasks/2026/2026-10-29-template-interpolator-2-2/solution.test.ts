import test from "node:test";
import assert from "node:assert";
import { interpolate } from "./solution";

test("replaces a single placeholder", () => {
  const result = interpolate("Hello, {{name}}!", { name: "Alice" });
  assert.strictEqual(result, "Hello, Alice!");
});

test("throws when placeholder key is missing", () => {
  assert.throws(
    () => interpolate("{{missing}}", {}),
    /Missing value for placeholder "missing"/
  );
});

test("converts non-string values to strings", () => {
  const result = interpolate("Count: {{value}}", { value: 42 });
  assert.strictEqual(result, "Count: 42");
});

test("handles multiple occurrences of the same key", () => {
  const result = interpolate("{{a}} and {{a}}", { a: "same" });
  assert.strictEqual(result, "same and same");
});

test("returns unchanged template when no placeholders", () => {
  const result = interpolate("just text", {});
  assert.strictEqual(result, "just text");
});
