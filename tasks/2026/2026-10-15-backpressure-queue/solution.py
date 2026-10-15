from collections import deque
import threading
import time

class Full(Exception):
    pass

class Empty(Exception):
    pass

class BackpressureQueue:
    def __init__(self, maxsize=0):
        if maxsize <= 0:
            raise ValueError("maxsize must be positive")
        self.maxsize = maxsize
        self.queue = deque()
        self.mutex = threading.Lock()
        self.not_full = threading.Condition(self.mutex)
        self.not_empty = threading.Condition(self.mutex)

    def put(self, item, timeout=None):
        with self.mutex:
            if timeout is None:
                while len(self.queue) >= self.maxsize:
                    self.not_full.wait()
                self.queue.append(item)
                self.not_empty.notify()
            else:
                deadline = time.monotonic() + timeout
                while len(self.queue) >= self.maxsize:
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        raise Full
                    self.not_full.wait(timeout=remaining)
                self.queue.append(item)
                self.not_empty.notify()

    def get(self, timeout=None):
        with self.mutex:
            if timeout is None:
                while not self.queue:
                    self.not_empty.wait()
                item = self.queue.popleft()
                self.not_full.notify()
                return item
            else:
                deadline = time.monotonic() + timeout
                while not self.queue:
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        raise Empty
                    self.not_empty.wait(timeout=remaining)
                item = self.queue.popleft()
                self.not_full.notify()
                return item

    def qsize(self):
        with self.mutex:
            return len(self.queue)

    def empty(self):
        with self.mutex:
            return not self.queue

    def full(self):
        with self.mutex:
            return len(self.queue) >= self.maxsize
