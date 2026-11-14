# Backpressure-aware Queue

Implement a thread-safe bounded queue that applies backpressure: `put` blocks when the queue is full, and `get` blocks when the queue is empty, with optional timeouts. The class should be named `BackpressureQueue` and have the following signature:

```python
class BackpressureQueue:
    def __init__(self, maxsize): ...
    def put(self, item, block=True, timeout=None): ...
    def get(self, block=True, timeout=None): ...
    def qsize(self): ...
```

- `maxsize` must be a positive integer; raise `ValueError` otherwise.
- When `block=True` and the operation cannot complete immediately, wait until it can or until `timeout` seconds (if given) have elapsed. If the timeout expires, raise `queue.Full` from `put` or `queue.Empty` from `get`.
- When `block=False`, do not wait; raise `queue.Full` or `queue.Empty` immediately if the operation would block.
- `timeout` must be non‑negative if provided; raise `ValueError` for negative values.
- The queue must be safe for concurrent producers and consumers (use `threading.Condition`).

Edge cases to respect:
- `timeout=0` should behave exactly like `block=False` (immediate raise if the queue is full or empty).
- A call with `block=True` and `timeout=None` must block indefinitely until space or item is available.
- Multiple threads calling `put` and `get` concurrently must not deadlock or lose data.
