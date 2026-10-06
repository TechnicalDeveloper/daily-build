import test from "node:test";
import assert from "node:assert";
import { memoize } from "./solution";

test("memoize should cache results for primitive arguments", () => {
  let callCount = 0;
  const add = (a: number, b: number) => {
    callCount++;
    return a + b;
  };
  const memoizedAdd = memoize(add);
  assert.strictEqual(memoizedAdd(1, 2), 3);
  assert.strictEqual(memoizedAdd(1, 2), 3);
  assert.strictEqual(callCount, 1);
});

test("memoize should not cache errors", () => {
  let callCount = 0;
  const throwFn = (x: number) => {
    callCount++;
    throw new Error("error");
  };
  const memoizedThrow = memoize(throwFn);
  assert.throws(() => memoizedThrow(42), /error/);
  assert.strictEqual(callCount, 1);
  assert.throws(() => memoizedThrow(42), /error/);
  assert.strictEqual(callCount, 2, "should be called again because previous call threw");
});

test("memoize should handle object arguments with default key", () => {
  let callCount = 0;
  const processObj = (obj: { a: number }) => {
    callCount++;
    return obj.a * 2;
  };
  const memoizedProcess = memoize(processObj);
  assert.strictEqual(memoizedProcess({ a: 1 }), 2);
  assert.strictEqual(memoizedProcess({ a: 1 }), 2);
  assert.strictEqual(callCount, 1, "first and second calls with equal objects should be same key");
});

test("memoize should allow custom key function", () => {
  let callCount = 0;
  const fn = (x: number | undefined): string => {
    callCount++;
    return `value: ${x}`;
  };
  const memoizedFn = memoize(fn, (...args) => args.map(String).join(","));
  assert.strictEqual(memoizedFn(undefined), "value: undefined");
  assert.strictEqual(memoizedFn(undefined), "value: undefined");
  assert.strictEqual(callCount, 1);
});
