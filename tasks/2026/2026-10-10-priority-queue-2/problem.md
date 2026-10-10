# Priority Queue

## Priority Queue

Implement a `PriorityQueue` class that provides two methods: `push(priority, item)` and `pop()`.

- `push(priority, item)` adds an item with an integer priority.
- `pop()` removes and returns the item with the lowest priority value (highest priority). If multiple items have the same priority, they are returned in the order they were inserted (FIFO).

### Signature

```python
class PriorityQueue:
    def __init__(self): ...
    def push(self, priority: int, item: Any) -> None: ...
    def pop(self) -> Any: ...
    def __len__(self) -> int: ...
```

### Edge Cases

1. Popping from an empty queue must raise an `IndexError`.
2. Items with the same priority must be popped in insertion order.
3. Priorities are integers (you may assume valid input).
