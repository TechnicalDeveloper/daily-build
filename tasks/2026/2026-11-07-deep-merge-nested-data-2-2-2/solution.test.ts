import test from 'node:test';
import assert from 'node:assert';
import { deepMerge } from './solution';

test('merges flat objects', () => {
  const target = { a: 1, b: 2 };
  const source = { b: 3, c: 4 };
  const result = deepMerge(target, source);
  assert.deepStrictEqual(result, { a: 1, b: 3, c: 4 });
});

test('deeply merges nested objects', () => {
  const target = { a: { x: 1, y: 2 }, b: 3 };
  const source = { a: { y: 99, z: 100 }, c: 4 };
  const result = deepMerge(target, source);
  assert.deepStrictEqual(result, { a: { x: 1, y: 99, z: 100 }, b: 3, c: 4 });
});

test('replaces arrays instead of merging', () => {
  const target = { arr: [1, 2], obj: { a: 1 } };
  const source = { arr: [3, 4], obj: { b: 2 } };
  const result = deepMerge(target, source);
  assert.deepStrictEqual(result, { arr: [3, 4], obj: { a: 1, b: 2 } });
});

test('ignores undefined properties in source', () => {
  const target = { a: 1, b: 2 };
  const source = { a: undefined, b: 3 };
  const result = deepMerge(target, source);
  assert.deepStrictEqual(result, { a: 1, b: 3 });
});

test('overwrites with null and keeps primitives', () => {
  const target = { a: 1, b: { c: 2 }, d: 'hello' };
  const source = { a: null, b: null, d: 'world' };
  const result = deepMerge(target, source);
  assert.deepStrictEqual(result, { a: null, b: null, d: 'world' });
});
