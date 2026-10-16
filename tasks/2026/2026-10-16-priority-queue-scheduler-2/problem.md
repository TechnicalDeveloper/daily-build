# Priority Queue Scheduler

# Priority Queue Scheduler

Implement a priority queue scheduler that manages tasks with associated priorities. The scheduler should return tasks in order of their priority (higher priority first) and maintain FIFO order for tasks with equal priority.

## Function Signature

Your implementation should define a class `PriorityScheduler` with the following methods:

- `__init__(self)`
- `add_task(self, task, priority=0)` – adds a task with given priority (higher number means higher priority).
- `get_next_task(self)` – removes and returns the highest priority task (if multiple, the one added first). Raises `IndexError` if no tasks.
- `peek(self)` – returns the highest priority task without removing it. Raises `IndexError` if empty.
- `is_empty(self) -> bool`
- `size(self) -> int`

## Edge Cases

- Ensure that tasks with equal priority are returned in FIFO order.
- Handle negative and zero priorities correctly.
- Attempting to get a task from an empty scheduler should raise `IndexError`.
- Tasks can be any hashable object (e.g., strings, integers).
