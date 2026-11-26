import test from "node:test";
import assert from "node:assert";
import { memoize } from "./solution";

test('memoize caches results for primitive arguments', () => {
  let calls = 0;
  const add = (a: number, b: number) => {
    calls++;
    return a + b;
  };
  const memoizedAdd = memoize(add);
  assert.equal(memoizedAdd(1, 2), 3);
  assert.equal(memoizedAdd(1, 2), 3);
  assert.equal(calls, 1);
});

test('memoize uses a resolver for object arguments', () => {
  let calls = 0;
  const fn = (obj: { id: number }) => {
    calls++;
    return obj.id * 2;
  };
  const memoized = memoize(fn, { resolver: (o: { id: number }) => String(o.id) });
  assert.equal(memoized({ id: 1 }), 2);
  assert.equal(memoized({ id: 1 }), 2);
  assert.equal(calls, 1);
});

test('memoize respects ttlMs expiration', async () => {
  let calls = 0;
  const fn = (x: number) => {
    calls++;
    return x + 1;
  };
  const memoized = memoize(fn, { ttlMs: 50 });
  assert.equal(memoized(1), 2);
  assert.equal(memoized(1), 2);
  assert.equal(calls, 1);
  await new Promise((resolve) => setTimeout(resolve, 60));
  assert.equal(memoized(1), 2);
  assert.equal(calls, 2);
});

test('memoize evicts least recently used when maxSize is exceeded', () => {
  let calls = 0;
  const fn = (x: number) => {
    calls++;
    return x * 2;
  };
  const memoized = memoize(fn, { maxSize: 2 });
  memoized(1);
  memoized(2);
  memoized(1); // make 2 the least recently used
  memoized(3); // evict 2
  assert.equal(memoized(2), 4);
  assert.equal(calls, 4);
});

test('memoize does not cache errors', () => {
  let calls = 0;
  const fn = (x: number) => {
    calls++;
    if (calls < 2) throw new Error('boom');
    return x;
  };
  const memoized = memoize(fn);
  assert.throws(() => memoized(7), /boom/);
  assert.doesNotThrow(() => memoized(7));
  assert.equal(calls, 2);
});
