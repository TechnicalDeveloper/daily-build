# Interval Tree and Range Merge

## Build
Implement a class `IntervalTree` that stores intervals (inclusive start, exclusive end) and supports:
- `add(interval)`: add a single interval (tuple (start, end))
- `remove(interval)`: remove all points covered by the given interval
- `query(point)`: return the number of intervals that cover the given point
- `merge()`: return a sorted list of disjoint merged intervals covering the current union of all stored intervals. Each interval should be `[start, end)`.

## Signature
```python
class IntervalTree:
    def __init__(self): ...
    def add(self, interval: tuple) -> None: ...
    def remove(self, interval: tuple) -> None: ...
    def query(self, point: int) -> int: ...
    def merge(self) -> list: ...
```

## Edge cases to handle
- Intervals can be added in any order (overlapping / non-overlapping).
- Removing a part of an interval should split the interval.
- Querying a point that is not covered by any interval returns 0.
- Merge should return an empty list if no intervals remain.
