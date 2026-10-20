# Circular Buffer

Implement a circular buffer (ring buffer) with a fixed capacity.

## Signature
```python
class CircularBuffer:
    def __init__(self, capacity: int):
        """Initialize buffer with given capacity (>=1)."""
    def enqueue(self, item: object) -> None:
        """Add an item, overwriting the oldest if full."""
    def dequeue(self) -> object:
        """Remove and return the oldest item. Raises IndexError if empty."""
    def peek(self) -> object:
        """Return the oldest item without removing. Raises IndexError if empty."""
    def is_empty(self) -> bool:
        """Return True if buffer is empty."""
    def is_full(self) -> bool:
        """Return True if buffer is full."""
    def __len__(self) -> int:
        """Return current number of items."""
```

## Edge cases to respect
1. Enqueuing when full overwrites the oldest item (the buffer never rejects an item).
2. Dequeue or peek on empty buffer must raise IndexError.
3. Capacity must be >= 1; if capacity < 1, raise ValueError.
