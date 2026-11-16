import test from "node:test";
import assert from "node:assert";
import { parseDuration, formatDuration, addDuration } from "./solution";

test("parseDuration handles mixed units", () => {
  assert.strictEqual(parseDuration("1d2h3m4s"), 86400000 + 7200000 + 180000 + 4000);
  assert.strictEqual(parseDuration("2h30m"), 9000000);
});

test("parseDuration throws on invalid input", () => {
  assert.throws(() => parseDuration(""));
  assert.throws(() => parseDuration("2h3x"));
  assert.throws(() => parseDuration("abc"));
});

test("formatDuration formats correctly", () => {
  assert.strictEqual(formatDuration(0), "0ms");
  assert.strictEqual(formatDuration(86400000 + 7200000 + 180000 + 4000), "1d 2h 3m 4s");
  assert.strictEqual(formatDuration(1500), "1s 500ms");
});

test("addDuration returns new Date with added time", () => {
  const start = new Date("2023-01-01T00:00:00Z");
  const end = addDuration(start, "1d");
  assert.strictEqual(end.toISOString(), "2023-01-02T00:00:00.000Z");
  assert.notStrictEqual(start, end);
});
