import test from "node:test";
import assert from "node:assert";
import { chunk } from "./solution";

test("chunks an array into equal-sized groups", () => {
  assert.deepEqual(chunk([1, 2, 3, 4, 5, 6], 2), [[1, 2], [3, 4], [5, 6]]);
});

test("leaves the final chunk short when array length is not divisible", () => {
  assert.deepEqual(chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]);
});

test("returns an empty array for an empty input", () => {
  assert.deepEqual(chunk([], 3), []);
});

test("throws for size less than 1", () => {
  assert.throws(() => chunk([1, 2, 3], 0), RangeError);
  assert.throws(() => chunk([1, 2, 3], -1), RangeError);
});

test("returns one chunk when size exceeds array length", () => {
  assert.deepEqual(chunk([1, 2, 3], 10), [[1, 2, 3]]);
});
