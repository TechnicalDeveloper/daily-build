import test from 'node:test';
import assert from 'node:assert';
import { memoize } from './solution';

test('should cache result of a function with no arguments', () => {
  let callCount = 0;
  const fn = () => {
    callCount++;
    return 42;
  };
  const memoizedFn = memoize(fn);

  assert.strictEqual(memoizedFn(), 42);
  assert.strictEqual(memoizedFn(), 42);
  assert.strictEqual(memoizedFn(), 42);
  assert.strictEqual(callCount, 1); // Should only call once
});

test('should cache based on multiple arguments', () => {
  let callCount = 0;
  const sum = (a: number, b: number) => {
    callCount++;
    return a + b;
  };
  const memoizedSum = memoize(sum);

  assert.strictEqual(memoizedSum(1, 2), 3);
  assert.strictEqual(memoizedSum(2, 1), 3); // Different order: should not reuse cache
  assert.strictEqual(memoizedSum(1, 2), 3); // Same order: should use cache
  assert.strictEqual(callCount, 2); // Only first two calls are unique
});

test('should treat objects with same properties as equal keys', () => {
  let callCount = 0;
  const fn = (obj: { x: number; y?: number }) => {
    callCount++;
    return obj.x + (obj.y ?? 0);
  };
  const memoizedFn = memoize(fn);

  const obj1 = { x: 5, y: 10 };
  const obj2 = { x: 5, y: 10 }; // Different reference, same value

  assert.strictEqual(memoizedFn(obj1), 15);
  assert.strictEqual(memoizedFn(obj2), 15); // Should use cache
  assert.strictEqual(callCount, 1);

  const obj3 = { x: 5 }; // Missing y
  assert.strictEqual(memoizedFn(obj3), 5); // Different key, should call again
  assert.strictEqual(callCount, 2);
});

test('should differentiate between undefined and null arguments', () => {
  let callCount = 0;
  const fn = (a: unknown, b: unknown) => {
    callCount++;
    return `${a}::${b}`;
  };
  const memoizedFn = memoize(fn);

  // undefined and null should produce different cache keys
  const result1 = memoizedFn(undefined, null);
  const result2 = memoizedFn(undefined, null); // same as before
  const result3 = memoizedFn(null, undefined); // different order
  const result4 = memoizedFn(null, undefined);

  assert.strictEqual(result1, 'undefined::null');
  assert.strictEqual(result2, 'undefined::null');
  assert.strictEqual(result3, 'null::undefined');
  assert.strictEqual(callCount, 2); // Two unique key combinations
});

test('should work with mixed primitive and object arguments', () => {
  let callCount = 0;
  const fn = (prefix: string, num: number, cfg: { flag: boolean }) => {
    callCount++;
    return `${prefix}:${num}:${cfg.flag}`;
  };
  const memoizedFn = memoize(fn);

  const cfg1 = { flag: true };
  const cfg2 = { flag: true }; // same value
  const cfg3 = { flag: false };

  assert.strictEqual(memoizedFn('A', 1, cfg1), 'A:1:true');
  assert.strictEqual(memoizedFn('A', 1, cfg2), 'A:1:true'); // cache hit
  assert.strictEqual(memoizedFn('B', 2, cfg3), 'B:2:false');
  assert.strictEqual(callCount, 2);
})
