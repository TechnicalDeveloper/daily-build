import test from 'node:test';
import assert from 'node:assert';
import { chunk } from './solution';

test('chunk with empty array returns []', () => {
  assert.deepStrictEqual(chunk([], 3), []);
});

test('chunk with size 1 returns array of singletons', () => {
  assert.deepStrictEqual(chunk([1, 2, 3], 1), [[1], [2], [3]]);
});

test('chunk with size 2 on odd-length array', () => {
  assert.deepStrictEqual(chunk(['a', 'b', 'c', 'd', 'e'], 2), [['a', 'b'], ['c', 'd'], ['e']]);
});

test('chunk with size larger than array returns single chunk', () => {
  assert.deepStrictEqual(chunk([10, 20, 30], 10), [[10, 20, 30]]);
});

test('chunk throws RangeError for size less than 1', () => {
  assert.throws(() => chunk([1, 2], 0), RangeError);
  assert.throws(() => chunk([1, 2], -1), RangeError);
});
