from heapq import heappush, heappop
import itertools

class PriorityQueue:
    def __init__(self):
        self._pq = []
        self._counter = itertools.count()

    def add_task(self, task, priority):
        count = next(self._counter)
        entry = [priority, count, task]
        heappush(self._pq, entry)

    def get_next_task(self):
        if not self._pq:
            raise IndexError("get_next_task from empty priority queue")
        priority, count, task = heappop(self._pq)
        return task
