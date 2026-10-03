import heapq

class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._counter = 0

    def insert(self, item, priority):
        self._counter += 1
        heapq.heappush(self._heap, (priority, self._counter, item))

    def extract_min(self):
        if not self._heap:
            raise IndexError("extract from empty queue")
        priority, counter, item = heapq.heappop(self._heap)
        return item

    def is_empty(self):
        return len(self._heap) == 0

    def size(self):
        return len(self._heap)
