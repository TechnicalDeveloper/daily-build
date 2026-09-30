# Circular Buffer

Implement a circular buffer with a fixed capacity.

**Signature:**
```python
class CircularBuffer:
    def __init__(self, capacity: int):
        ...
    def enqueue(self, item: Any) -> None:
        ...
    def dequeue(self) -> Any:
        ...
    def peek(self) -> Any:
        ...
    def is_empty(self) -> bool:
        ...
    def is_full(self) -> bool:
        ...
    def size(self) -> int:
        ...
```

**Edge cases to respect:**
- Dequeue from an empty buffer should raise an `IndexError`.
- Peek on an empty buffer should raise an `IndexError`.
- Enqueue to a full buffer should overwrite the oldest item (drop behavior).
