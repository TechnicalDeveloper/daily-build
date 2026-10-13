# Priority Queue

Build a `PriorityQueue` class that stores items with associated priorities. Lower numeric priority indicates higher urgency and items are dequeued first. If two items have the same priority, the order in which they are dequeued is not guaranteed.

## Signature
```
class PriorityQueue:
    def push(self, priority: int, item: Any) -> None
    def pop(self) -> Any
    def peek(self) -> Any
    def is_empty(self) -> bool
```

## Edge Cases
- Popping from an empty queue must raise `IndexError`.
- Peeking from an empty queue must raise `IndexError`.
- Items with equal priority may be returned in any order.
