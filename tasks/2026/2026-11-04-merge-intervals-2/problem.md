# Merge Intervals

Implement a function to merge overlapping intervals.

**Signature:**
```python
def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
```

**Description:**
Take a list of intervals, where each interval is a tuple `(start, end)` with `start <= end`. Merge all overlapping intervals and return the resulting list sorted by start value.

**Edge Cases:**
- Empty list → returns empty list.
- Intervals that are already non-overlapping (e.g., `[(1,2), (3,4)]`) → returned as is.
- Intervals where one is completely contained within another (e.g., `[(1,5), (2,3)]`) → merged to `[(1,5)]`.
- Intervals that touch at boundaries (e.g., `[(1,2), (2,3)]`) → should be merged to `[(1,3)]` (since end of first equals start of second).
