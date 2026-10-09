import test from "node:test";
import assert from "node:assert";
import { chunk } from "./solution";

test("chunk splits array into chunks of specified size", () => {
  assert.deepStrictEqual(chunk([1,2,3,4,5], 2), [[1,2],[3,4],[5]]);
  assert.deepStrictEqual(chunk([1,2,3,4], 2), [[1,2],[3,4]]);
  assert.deepStrictEqual(chunk([1,2,3], 1), [[1],[2],[3]]);
});

test("chunk handles empty array", () => {
  assert.deepStrictEqual(chunk([], 3), []);
});

test("chunk handles size larger than array length", () => {
  assert.deepStrictEqual(chunk([1,2,3], 10), [[1,2,3]]);
});

test("chunk throws error for non-positive size", () => {
  assert.throws(() => chunk([1,2], 0), { message: "Size must be a positive integer" });
  assert.throws(() => chunk([1,2], -1), { message: "Size must be a positive integer" });
});
