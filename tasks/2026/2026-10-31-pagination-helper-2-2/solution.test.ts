import test from "node:test";
import assert from "node:assert";
import { paginate } from "./solution";

test("paginate returns correct slice and metadata for first page", () => {
  const items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const result = paginate(items, 1, 3);
  assert.deepStrictEqual(result.items, [1, 2, 3]);
  assert.strictEqual(result.totalItems, 10);
  assert.strictEqual(result.totalPages, 4);
  assert.strictEqual(result.currentPage, 1);
  assert.strictEqual(result.hasPrev, false);
  assert.strictEqual(result.hasNext, true);
});

test("paginate handles empty items", () => {
  const result = paginate([], 1, 5);
  assert.deepStrictEqual(result.items, []);
  assert.strictEqual(result.totalItems, 0);
  assert.strictEqual(result.totalPages, 1);
  assert.strictEqual(result.currentPage, 1);
  assert.strictEqual(result.hasPrev, false);
  assert.strictEqual(result.hasNext, false);
});

test("paginate clamps negative page to first page", () => {
  const items = [1, 2, 3];
  const result = paginate(items, -5, 2);
  assert.deepStrictEqual(result.items, [1, 2]);
  assert.strictEqual(result.currentPage, 1);
  assert.strictEqual(result.hasPrev, false);
});

test("paginate clamps page beyond total pages to last page", () => {
  const items = [1, 2, 3];
  const result = paginate(items, 10, 2);
  assert.deepStrictEqual(result.items, [3]);
  assert.strictEqual(result.currentPage, 2);
  assert.strictEqual(result.hasPrev, true);
  assert.strictEqual(result.hasNext, false);
});

test("paginate throws error for zero or negative pageSize", () => {
  assert.throws(() => paginate([1, 2, 3], 1, 0), /pageSize must be greater than zero/);
  assert.throws(() => paginate([1, 2, 3], 1, -1), /pageSize must be greater than zero/);
});
