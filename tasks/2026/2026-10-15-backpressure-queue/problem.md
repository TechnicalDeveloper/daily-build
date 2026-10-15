# Backpressure Queue

## Backpressure Queue

Implement a bounded blocking queue that applies backpressure: producers block when the queue is full, and consumers block when the queue is empty. The queue must support timeouts and raise custom exceptions.

### Signature

```python
class BackpressureQueue:
    def __init__(self, maxsize: int)
    def put(self, item, timeout: Optional[float] = None) -> None
    def get(self, timeout: Optional[float] = None) -> Any
```

### Exceptions
- `Full` – raised by `put()` on timeout when queue is full.
- `Empty` – raised by `get()` on timeout when queue is empty.

### Edge Cases
- `put()` blocks until space becomes available (or timeout).
- `get()` blocks until an item becomes available (or timeout).
- Multiple producers/consumers must work correctly (thread-safety).
- `maxsize` must be a positive integer (> 0).
