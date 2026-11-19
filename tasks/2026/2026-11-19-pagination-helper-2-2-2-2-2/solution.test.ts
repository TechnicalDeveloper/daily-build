import test from "node:test";
import assert from "node:assert";
import { paginate } from "./solution";

test("paginates a simple list", () => {
  const items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
  const result = paginate(items, { page: 2, pageSize: 5 });
  assert.deepEqual(result.items, [6, 7, 8, 9, 10]);
  assert.strictEqual(result.totalItems, 12);
  assert.strictEqual(result.totalPages, 3);
  assert.strictEqual(result.currentPage, 2);
  assert.strictEqual(result.hasNext, true);
  assert.strictEqual(result.hasPrev, true);
});

test("handles out-of-range page by clamping to last page", () => {
  const items = [1, 2, 3, 4, 5];
  const result = paginate(items, { page: 99, pageSize: 2 });
  assert.deepEqual(result.items, [5]);
  assert.strictEqual(result.currentPage, 3);
  assert.strictEqual(result.totalPages, 3);
  assert.strictEqual(result.hasNext, false);
  assert.strictEqual(result.hasPrev, true);
});

test("returns empty items and currentPage=1 for empty array", () => {
  const result = paginate([], { page: 2, pageSize: 10 });
  assert.deepEqual(result.items, []);
  assert.strictEqual(result.totalItems, 0);
  assert.strictEqual(result.totalPages, 0);
  assert.strictEqual(result.currentPage, 1);
  assert.strictEqual(result.hasNext, false);
  assert.strictEqual(result.hasPrev, false);
});

test("ignores invalid pageSize and negative page", () => {
  const items = [1, 2, 3, 4, 5];
  const result = paginate(items, { page: -5, pageSize: 0 });
  assert.deepEqual(result.items, [1, 2, 3, 4, 5]);
  assert.strictEqual(result.currentPage, 1);
  assert.strictEqual(result.pageSize, 10);
  const result2 = paginate(items, { page: -1, pageSize: -5 });
  assert.deepEqual(result2.items, [1, 2, 3, 4, 5]);
  assert.strictEqual(result2.pageSize, 10);
});
