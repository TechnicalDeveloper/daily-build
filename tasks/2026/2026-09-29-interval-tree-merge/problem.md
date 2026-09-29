# Interval Tree / Range Merge

Implement an `IntervalTree` class that stores closed intervals `[start, end]` (inclusive) and supports merging overlapping or adjacent intervals.

**Signature:**
- `__init__(self)` – create an empty tree.
- `add(self, start: int, end: int) -> None` – insert the interval `[start, end]`. Automatically merge any overlapping or adjacent intervals.
- `get_intervals(self) -> list[tuple[int, int]]` – return a sorted list of all disjoint merged intervals.
- `remove(self, start: int, end: int) -> None` – remove the range `[start, end]` from the stored intervals, splitting intervals if necessary.

**Edge cases to respect:**
1. Overlapping and adjacent intervals (e.g., `[1,3]` and `[3,5]` → `[1,5]`).
2. Removing a range that covers multiple intervals, partially trimming them.
3. Removing a range that is completely outside all stored intervals (should be a no-op).
