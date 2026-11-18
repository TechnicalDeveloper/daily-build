# Merge Overlapping Intervals

Write a function `merge_intervals(intervals)` that takes a list of intervals, where each interval is a pair `(start, end)` with `start <= end`. The function should return a list of merged intervals sorted by start. Two intervals overlap if `start <= current_end` (including touching). Handle these edge cases:
- Empty input returns an empty list.
- Input may be unsorted.
- Intervals may be nested inside another.
- Adjacent intervals like `[1,2]` and `[2,3]` should be merged because they touch.
