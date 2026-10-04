import test from 'node:test';
import assert from 'node:assert';
import { mergeIntervals } from './solution';

test('mergeIntervals: empty list returns empty list', () => {
    assert.deepStrictEqual(mergeIntervals([]), []);
});

test('mergeIntervals: single interval returns that interval', () => {
    assert.deepStrictEqual(mergeIntervals([[1, 5]]), [[1, 5]]);
});

test('mergeIntervals: merges overlapping intervals', () => {
    const input: [number, number][] = [[1, 3], [2, 6], [8, 10], [15, 18]];
    const expected: [number, number][] = [[1, 6], [8, 10], [15, 18]];
    assert.deepStrictEqual(mergeIntervals(input), expected);
});

test('mergeIntervals: merges all intervals into one', () => {
    const input: [number, number][] = [[1, 4], [4, 5]];
    const expected: [number, number][] = [[1, 5]];
    assert.deepStrictEqual(mergeIntervals(input), expected);
});

test('mergeIntervals: handles unsorted input', () => {
    const input: [number, number][] = [[2, 3], [1, 5]];
    const expected: [number, number][] = [[1, 5]];
    assert.deepStrictEqual(mergeIntervals(input), expected);
});
