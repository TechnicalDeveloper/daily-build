import heapq

class PriorityScheduler:
    def __init__(self):
        self._heap = []
        self._counter = 0

    def add_task(self, task, priority=0):
        # Use negative priority so larger priority is dequeued first
        heapq.heappush(self._heap, (-priority, self._counter, task))
        self._counter += 1

    def get_next_task(self):
        if not self._heap:
            raise IndexError("No tasks in scheduler")
        _, _, task = heapq.heappop(self._heap)
        return task

    def peek(self):
        if not self._heap:
            raise IndexError("No tasks in scheduler")
        return self._heap[0][2]

    def is_empty(self):
        return len(self._heap) == 0

    def size(self):
        return len(self._heap)
