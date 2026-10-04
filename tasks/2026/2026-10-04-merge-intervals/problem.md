# Merge Intervals

## Problem
Implement a function to merge overlapping intervals. The function should take an array of intervals (each interval is a tuple [start, end]) and return a new array of intervals with all overlapping intervals merged.

### Signature
`export function mergeIntervals(intervals: [number, number][]): [number, number][]`

### Edge Cases
- Empty input array should return an empty array.
- Intervals that are adjacent (e.g., [1,4] and [4,5]) should be merged because they touch.
- Input may be unsorted; the function should handle that.
