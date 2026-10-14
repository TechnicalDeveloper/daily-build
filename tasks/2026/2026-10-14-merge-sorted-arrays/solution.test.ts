import test from "node:test";
import assert from "node:assert";
import { mergeSorted } from "./solution";

test("both arrays empty", () => {
  assert.deepStrictEqual(mergeSorted([], []), []);
});

test("one array empty", () => {
  assert.deepStrictEqual(mergeSorted([1, 3, 5], []), [1, 3, 5]);
  assert.deepStrictEqual(mergeSorted([], [2, 4, 6]), [2, 4, 6]);
});

test("duplicate values preserved", () => {
  assert.deepStrictEqual(mergeSorted([1, 2, 2], [2, 3]), [1, 2, 2, 2, 3]);
});

test("mixed lengths and typical case", () => {
  assert.deepStrictEqual(mergeSorted([1, 3, 5, 7], [2, 4, 6]), [1, 2, 3, 4, 5, 6, 7]);
  assert.deepStrictEqual(mergeSorted([0, 10, 20], [5, 15, 25, 30]), [0, 5, 10, 15, 20, 25, 30]);
});
