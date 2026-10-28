# Backpressure-Aware Queue

Build a bounded, thread-safe queue that applies backpressure to its producer. Implement the `BackpressureQueue` class in `solution.py` using `collections.deque` and `threading.Lock`.

The class must provide:
- `__init__(self, maxsize: int)`
- `put(self, item)` — append to the tail; raise `QueueFull` if the queue is full
- `get(self)` — remove and return from the head; raise `QueueEmpty` if the queue is empty
- `qsize(self) -> int`
- `full(self) -> bool`
- `empty(self) -> bool`

The module must also define exception classes `QueueFull` and `QueueEmpty`.

Behavior:
- `put` raises `QueueFull` when the queue already holds `maxsize` items.
- `get` raises `QueueEmpty` when no items are available.
- The queue must preserve FIFO order and be safe for concurrent use by multiple threads.

Edge cases to respect:
- `maxsize` must be a positive integer; anything else should raise `ValueError`.
- A full queue must reject new items without changing its size.
- After an item is removed from a full queue, `put` must be accepted again.
