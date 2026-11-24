# Circular Buffer with Overwrite

Implement a fixed-capacity `CircularBuffer` class. It behaves as a FIFO queue: `append` adds an item at the back and `pop` removes the item at the front. When the buffer is full, `append` overwrites the oldest item.

**Signature**

- `CircularBuffer(capacity: int)`
- `append(item: Any) -> None`
- `pop() -> Any`
- `peek() -> Any`
- `__len__() -> int`
- `is_empty() -> bool`
- `is_full() -> bool`

**Edge cases**

- `capacity` must be a positive integer; raise `ValueError` otherwise.
- Popping or peeking an empty buffer must raise `IndexError`.
- Once full, the next append should overwrite the oldest element, preserving FIFO order.
