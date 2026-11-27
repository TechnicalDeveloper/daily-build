import test from "node:test";
import assert from "node:assert";
import { paginate } from "./solution";

test("returns correct pagination for a middle page", () => {
  const result = paginate({ page: 2, pageSize: 10, totalItems: 25 });
  assert.deepStrictEqual(result, {
    page: 2,
    pageSize: 10,
    totalItems: 25,
    totalPages: 3,
    hasNextPage: true,
    hasPreviousPage: true,
    startIndex: 10,
    endIndex: 20,
  });
});

test("clamps page number to at least 1", () => {
  const result = paginate({ page: 0, pageSize: 5, totalItems: 10 });
  assert.strictEqual(result.page, 1);
  assert.strictEqual(result.hasPreviousPage, false);
  assert.strictEqual(result.startIndex, 0);
});

test("clamps page size to at least 1", () => {
  const result = paginate({ page: 1, pageSize: 0, totalItems: 10 });
  assert.strictEqual(result.pageSize, 1);
  assert.strictEqual(result.totalPages, 10);
  assert.strictEqual(result.endIndex, 1);
});

test("handles empty data set", () => {
  const result = paginate({ page: 3, pageSize: 10, totalItems: 0 });
  assert.strictEqual(result.page, 1);
  assert.strictEqual(result.totalPages, 0);
  assert.strictEqual(result.startIndex, 0);
  assert.strictEqual(result.endIndex, 0);
  assert.strictEqual(result.hasNextPage, false);
  assert.strictEqual(result.hasPreviousPage, false);
});

test("clamps page to last page when page exceeds totalPages", () => {
  const result = paginate({ page: 10, pageSize: 10, totalItems: 25 });
  assert.strictEqual(result.page, 3);
  assert.strictEqual(result.endIndex, 25);
  assert.strictEqual(result.hasNextPage, false);
  assert.strictEqual(result.hasPreviousPage, true);
});
