import test from 'node:test';
import assert from 'node:assert';
import { stableSortByKeys } from './solution';
import type { SortKey } from './solution';

test('sorts by a single key ascending', () => {
  const items = [
    { name: 'z', age: 10 },
    { name: 'a', age: 20 },
    { name: 'm', age: 15 },
  ];
  const keys: SortKey<typeof items[0]>[] = [{ key: 'name' }];
  const sorted = stableSortByKeys(items, keys);
  assert.deepStrictEqual(sorted, [
    { name: 'a', age: 20 },
    { name: 'm', age: 15 },
    { name: 'z', age: 10 },
  ]);
});

test('sorts by multiple keys with descending direction', () => {
  const items = [
    { name: 'b', age: 30 },
    { name: 'a', age: 30 },
    { name: 'a', age: 10 },
  ];
  const keys: SortKey<typeof items[0]>[] = [
    { key: 'age', direction: 'desc' },
    { key: 'name' },
  ];
  const sorted = stableSortByKeys(items, keys);
  assert.deepStrictEqual(sorted, [
    { name: 'a', age: 30 }, // age 30, name 'a' < 'b'
    { name: 'b', age: 30 },
    { name: 'a', age: 10 },
  ]);
});

test('is stable (preserves original order for equal keys)', () => {
  const items = [
    { id: 1, value: 10 },
    { id: 2, value: 10 },
    { id: 3, value: 5 },
  ];
  const keys: SortKey<typeof items[0]>[] = [{ key: 'value' }];
  const sorted = stableSortByKeys(items, keys);
  // items with value 10 should keep original order: id 1 before id 2
  assert.deepStrictEqual(sorted, [
    { id: 3, value: 5 },
    { id: 1, value: 10 },
    { id: 2, value: 10 },
  ]);
});

test('handles empty array and empty sort keys', () => {
  assert.deepStrictEqual(stableSortByKeys([], [{ key: 'x' as never }]), []);
  const input = [{ x: 1 }, { x: 2 }];
  const result = stableSortByKeys(input, []);
  assert.deepStrictEqual(result, input);
  assert.notStrictEqual(result, input); // should be a copy
});

test('handles null and undefined values correctly', () => {
  const items = [
    { name: 'a', age: undefined as number | undefined | null },
    { name: 'b', age: 10 },
    { name: 'c', age: null },
    { name: 'd', age: 5 },
  ];
  const keys: SortKey<typeof items[0]>[] = [{ key: 'age' }];
  const sorted = stableSortByKeys(items, keys);
  assert.deepStrictEqual(sorted, [
    { name: 'a', age: undefined },
    { name: 'c', age: null },
    { name: 'd', age: 5 },
    { name: 'b', age: 10 },
  ]);
});
