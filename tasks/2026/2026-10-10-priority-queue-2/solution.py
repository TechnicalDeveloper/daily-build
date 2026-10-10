import heapq
import itertools

class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._counter = itertools.count()

    def push(self, priority, item):
        count = next(self._counter)
        heapq.heappush(self._heap, (priority, count, item))

    def pop(self):
        if not self._heap:
            raise IndexError('pop from empty priority queue')
        priority, count, item = heapq.heappop(self._heap)
        return item

    def __len__(self):
        return len(self._heap)
