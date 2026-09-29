import test from 'node:test';
import assert from 'node:assert';
import { chunk } from './solution';

test('chunk should throw for non-positive size', () => {
  assert.throws(() => chunk([1, 2, 3], 0), /positive/i);
  assert.throws(() => chunk([1, 2, 3], -1), /positive/i);
});

test('chunk should return empty array for empty input', () => {
  assert.deepStrictEqual(chunk([], 2), []);
});

test('chunk should return single chunk when size >= array length', () => {
  assert.deepStrictEqual(chunk([1, 2, 3], 5), [[1, 2, 3]]);
  assert.deepStrictEqual(chunk([1, 2, 3], 3), [[1, 2, 3]]);
});

test('chunk should split array into correct chunks', () => {
  assert.deepStrictEqual(chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]);
  assert.deepStrictEqual(chunk([1, 2, 3, 4], 2), [[1, 2], [3, 4]]);
  assert.deepStrictEqual(chunk([1, 2, 3, 4, 5, 6], 3), [[1, 2, 3], [4, 5, 6]]);
});

test('chunk should work with strings', () => {
  assert.deepStrictEqual(chunk(['a', 'b', 'c', 'd'], 3), [['a', 'b', 'c'], ['d']]);
});
