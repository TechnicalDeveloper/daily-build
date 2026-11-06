# Priority Queue Scheduler

Implement a `PriorityQueue` class that manages tasks with associated priorities.

## Signature

```python
class PriorityQueue:
    def add_task(self, task: str, priority: int) -> None:
        """Add a task with the given priority (smaller value = higher priority)."""

    def get_next_task(self) -> str:
        """Return the task with the highest priority (lowest numeric value).
        If two tasks have the same priority, return the one added first (FIFO).
        Raise IndexError if the queue is empty."""
```

## Edge Cases

- Calling `get_next_task()` on an empty queue must raise `IndexError`.
- When priorities are equal, tasks are retrieved in the order they were added.
- The queue may contain an arbitrary number of tasks; you may assume tasks are strings.
