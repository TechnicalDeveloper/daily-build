import test from 'node:test';
import assert from 'node:assert';
import { chunk } from './solution';

test('chunks array into equal parts', () => {
  const result = chunk([1, 2, 3, 4, 5, 6], 2);
  assert.deepStrictEqual(result, [[1, 2], [3, 4], [5, 6]]);
});

test('handles array with odd number of elements', () => {
  const result = chunk([1, 2, 3, 4, 5], 2);
  assert.deepStrictEqual(result, [[1, 2], [3, 4], [5]]);
});

test('returns empty array for empty input', () => {
  const result = chunk([], 3);
  assert.deepStrictEqual(result, []);
});

test('returns single chunk when size >= length', () => {
  const result = chunk([1, 2, 3], 5);
  assert.deepStrictEqual(result, [[1, 2, 3]]);
});

test('chunks each element individually when size is 1', () => {
  const result = chunk(['a', 'b', 'c'], 1);
  assert.deepStrictEqual(result, [['a'], ['b'], ['c']]);
});

test('throws on non-positive size', () => {
  assert.throws(() => chunk([1], 0), /positive/);
  assert.throws(() => chunk([1], -1), /positive/);
});
