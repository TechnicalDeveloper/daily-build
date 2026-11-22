import test from "node:test";
import assert from "node:assert";
import { formatDuration, parseDuration } from "./solution";

test("formatDuration zero", () => {
  assert.strictEqual(formatDuration(0), "0s");
});

test("formatDuration rollover at 60", () => {
  assert.strictEqual(formatDuration(60), "1m");
  assert.strictEqual(formatDuration(59), "59s");
});

test("formatDuration multiple units", () => {
  assert.strictEqual(formatDuration(3661), "1h 1m 1s");
  assert.strictEqual(formatDuration(90061), "1d 1h 1m 1s");
});

test("parseDuration handles negative by throwing", () => {
  assert.throws(() => parseDuration(-1), /negative/);
});
