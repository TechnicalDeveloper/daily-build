# Merge Overlapping Intervals

Implement a function `merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]` that merges all overlapping or adjacent intervals. Intervals are given as tuples `(start, end)` with `start <= end`. The input list may be unsorted. The output should be a list of merged intervals, sorted by start time.

Edge cases to consider:
- Empty input returns an empty list.
- Intervals that touch (e.g., `(1,2)` and `(2,3)`) should be merged into `(1,3)`.
- Intervals that are completely contained within another should be merged into the larger one.
