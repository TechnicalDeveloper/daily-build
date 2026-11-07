# Backpressure-Aware Queue

Implement a bounded queue with backpressure notification. When the queue reaches its maximum capacity, callers attempting to push an item should be notified (via return value or exception) so they can slow down or drop items.

## Signature

```python
class BackpressureQueue:
    def __init__(self, maxsize: int):
        """Initialize queue with maxsize capacity."""

    def push(self, item: Any) -> bool:
        """
        Add item to queue. Return True if successfully added.
        Return False if queue is full (backpressure signal).
        """

    def pop(self) -> Any:
        """Remove and return the oldest item. Raise IndexError if empty."""

    def size(self) -> int:
        """Return current number of items."""

    def empty(self) -> bool:
        """Return True if queue is empty."""

    def full(self) -> bool:
        """Return True if queue is full."""
```

## Edge Cases
- Push to a full queue returns False, does not overwrite or drop items.
- Pop from an empty queue raises IndexError.
- Queue with maxsize=0 should behave as if always full (no capacity).
- Queue with maxsize negative or None should be treated as unlimited (never full).
