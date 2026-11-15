import test from "node:test";
import assert from "node:assert";
import { rollingHash } from "./solution";

test("returns empty array when windowSize > string length", () => {
  assert.deepStrictEqual(rollingHash("abc", 4), []);
});

test("throws for windowSize <= 0", () => {
  assert.throws(() => rollingHash("abc", 0), /positive/);
  assert.throws(() => rollingHash("abc", -1), /positive/);
});

test("returns one hash for windowSize equal to string length", () => {
  const result = rollingHash("hello", 5);
  assert.strictEqual(result.length, 1);
  const expected = "hello"
    .split("")
    .reduce((acc, ch) => (acc * 31 + ch.charCodeAt(0)) % 1000000007, 0);
  assert.strictEqual(result[0], expected);
});

test("rolling hash matches naive hash for each window", () => {
  const s = "abcdefg";
  const w = 3;
  const naive: number[] = [];
  for (let i = 0; i + w <= s.length; i++) {
    let h = 0;
    for (let j = i; j < i + w; j++) {
      h = (h * 31 + s.charCodeAt(j)) % 1000000007;
    }
    naive.push(h);
  }
  assert.deepStrictEqual(rollingHash(s, w), naive);
});

test("works with single character windows", () => {
  assert.deepStrictEqual(rollingHash("abc", 1), [97, 98, 99]);
});
