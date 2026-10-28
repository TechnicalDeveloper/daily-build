import threading
from collections import deque


class QueueFull(Exception):
    pass


class QueueEmpty(Exception):
    pass


class BackpressureQueue:
    def __init__(self, maxsize: int):
        if type(maxsize) is not int or maxsize <= 0:
            raise ValueError('maxsize must be a positive integer')
        self._maxsize = maxsize
        self._queue = deque()
        self._lock = threading.Lock()

    def put(self, item):
        with self._lock:
            if len(self._queue) >= self._maxsize:
                raise QueueFull('queue is full')
            self._queue.append(item)

    def get(self):
        with self._lock:
            if not self._queue:
                raise QueueEmpty('queue is empty')
            return self._queue.popleft()

    def qsize(self):
        with self._lock:
            return len(self._queue)

    def full(self):
        with self._lock:
            return len(self._queue) >= self._maxsize

    def empty(self):
        with self._lock:
            return len(self._queue) == 0
