import heapq

class PriorityQueue:
    def __init__(self):
        self._heap = []

    def push(self, priority, item):
        heapq.heappush(self._heap, (priority, item))

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        priority, item = heapq.heappop(self._heap)
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        return self._heap[0][1]

    def is_empty(self):
        return len(self._heap) == 0
