# Circular Buffer

## Circular Buffer

Implement a fixed-size circular buffer. The buffer has a maximum capacity and stores items in a FIFO order. When the buffer is full, adding a new item overwrites the oldest item.

### Class: `CircularBuffer`

Methods:
- `__init__(self, capacity: int)`: Initialize buffer with positive integer capacity.
- `put(self, item)`: Add item to the buffer. If full, overwrites oldest.
- `get(self)`: Remove and return the oldest item. Raise `IndexError` if empty.
- `is_empty(self) -> bool`: Returns `True` if empty.
- `is_full(self) -> bool`: Returns `True` if full.

### Edge Cases
1. Overwriting: When buffer is full and a new item is added, the oldest item is overwritten. Subsequent `get()` calls should return the next oldest.
2. Empty buffer: Calling `get()` on an empty buffer must raise `IndexError`.
3. Capacity of 1: Ensure correct behavior with minimal capacity.
