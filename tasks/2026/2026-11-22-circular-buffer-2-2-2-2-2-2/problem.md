# Circular Buffer

Implement a circular buffer (ring buffer) in Python.

Create a class `CircularBuffer` with the following methods:

- `__init__(self, capacity: int)` - initializes the buffer with the given capacity (must be >= 1, otherwise raise `ValueError`).
- `append(self, item)` - adds an item to the buffer. If the buffer is full, the oldest item is overwritten.
- `pop(self)` - removes and returns the oldest item. Raise `IndexError` if the buffer is empty.
- `peek(self)` - returns the oldest item without removing it. Raise `IndexError` if the buffer is empty.
- `is_empty(self) -> bool` - returns `True` if the buffer contains no items.
- `is_full(self) -> bool` - returns `True` if the buffer is at capacity.
- `__len__(self) -> int` - returns the current number of items in the buffer.

Edge cases to handle:
1. Appending to a full buffer overwrites the oldest element.
2. `pop` or `peek` on an empty buffer should raise `IndexError`.
3. Capacity of 0 or negative should raise `ValueError`.
