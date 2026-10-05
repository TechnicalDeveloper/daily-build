# Circular Buffer Implementation

Implement a fixed-size circular buffer (ring buffer) that overwrites the oldest element when full.

Define a class `CircularBuffer` with the following methods:

- `__init__(self, capacity: int)`: initializes buffer with given capacity (capacity > 0). Raises `ValueError` if capacity <= 0.
- `append(self, item)`: adds item to the buffer. If the buffer is full, the oldest item is overwritten.
- `get(self)`: removes and returns the oldest item. Raises `IndexError` if the buffer is empty.
- `peek(self)`: returns the oldest item without removing it. Raises `IndexError` if the buffer is empty.
- `is_empty(self) -> bool`: returns `True` if the buffer has no elements.
- `is_full(self) -> bool`: returns `True` if the buffer is at capacity.

Edge cases to respect:
- Appending to a full buffer must overwrite the oldest element (the buffer always holds the most recent `capacity` items).
- `get`/`peek` on an empty buffer must raise `IndexError`.
- The order of elements returned by `get` must be FIFO (first in, first out).

Signature:
```python
class CircularBuffer:
    def __init__(self, capacity: int): ...
    def append(self, item): ...
    def get(self): ...
    def peek(self): ...
    def is_empty(self): ...
    def is_full(self): ...
```
