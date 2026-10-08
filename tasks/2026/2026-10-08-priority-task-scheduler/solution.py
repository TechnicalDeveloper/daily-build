from heapq import heappush, heappop

class TaskScheduler:
    def __init__(self):
        self._counter = 0
        self._pending = []          # min-heap of (due_time, priority, counter, name)
        self._ready = []            # min-heap of (priority, due_time, counter, name)

    def add_task(self, name: str, priority: int, due_time: int) -> None:
        heappush(self._pending, (due_time, priority, self._counter, name))
        self._counter += 1

    def get_next_task(self, current_time: int) -> str | None:
        # Move all tasks that are due from pending to ready
        while self._pending and self._pending[0][0] <= current_time:
            due_time, priority, counter, name = heappop(self._pending)
            heappush(self._ready, (priority, due_time, counter, name))

        if not self._ready:
            return None

        # Pop the highest-priority ready task
        _, _, _, name = heappop(self._ready)
        return name
