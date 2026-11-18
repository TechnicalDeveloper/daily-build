import test from "node:test";
import assert from "node:assert";
import { diff } from "./solution";

test("identical arrays yield all keeps", () => {
  const a = ["a", "b", "c"];
  const result = diff(a, [...a]);
  assert.deepStrictEqual(result, [
    { type: "keep", line: "a" },
    { type: "keep", line: "b" },
    { type: "keep", line: "c" },
  ]);
});

test("empty target produces all deletes", () => {
  const a = ["x", "y"];
  const b: string[] = [];
  const result = diff(a, b);
  assert.deepStrictEqual(result, [
    { type: "delete", line: "x" },
    { type: "delete", line: "y" },
  ]);
});

test("empty source produces all inserts", () => {
  const a: string[] = [];
  const b = ["p", "q"];
  const result = diff(a, b);
  assert.deepStrictEqual(result, [
    { type: "insert", line: "p" },
    { type: "insert", line: "q" },
  ]);
});

test("mixed changes produce correct operation sequence", () => {
  const a = ["a", "b", "c", "d"];
  const b = ["a", "x", "c", "e", "d"];
  const result = diff(a, b);
  assert.deepStrictEqual(result, [
    { type: "keep", line: "a" },
    { type: "delete", line: "b" },
    { type: "insert", line: "x" },
    { type: "keep", line: "c" },
    { type: "insert", line: "e" },
    { type: "keep", line: "d" },
  ]);
});

test("both empty arrays yield empty diff", () => {
  const result = diff([], []);
  assert.deepStrictEqual(result, []);
});
