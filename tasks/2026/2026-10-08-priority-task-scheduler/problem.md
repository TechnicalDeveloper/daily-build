# Priority Task Scheduler

Implement a task scheduler that returns the highest-priority task whose due time has passed.

**Class:** `TaskScheduler`
- `add_task(name: str, priority: int, due_time: int) -> None`
  - Adds a task with a given name, priority (lower value = higher priority), and absolute due_time (integer timestamp).
- `get_next_task(current_time: int) -> str | None`
  - Returns the name of the highest-priority task among all tasks with `due_time <= current_time`. If multiple tasks have the same priority, the one with the smallest due_time is returned; if both are equal, the one added first is returned. The returned task is removed from the scheduler. If no task is ready, returns `None`.

**Edge cases to respect:**
1. Tasks with a due_time in the past (`due_time <= current_time`) must be immediately available.
2. Multiple tasks with the same priority and same due_time – return them in the order they were added (FIFO).
3. Calling `get_next_task` when no tasks are ready returns `None` without error.
