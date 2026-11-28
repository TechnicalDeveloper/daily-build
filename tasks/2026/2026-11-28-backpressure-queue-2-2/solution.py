import threading
import queue
import time
from collections import deque

class BackpressureQueue:
    def __init__(self, maxsize):
        if maxsize <= 0:
            raise ValueError("maxsize must be positive")
        self.maxsize = maxsize
        self._queue = deque()
        self._cond = threading.Condition()

    def put(self, item, block=True, timeout=None):
        with self._cond:
            if not block:
                if len(self._queue) >= self.maxsize:
                    raise queue.Full
                self._queue.append(item)
                self._cond.notify()
                return
            if timeout is not None and timeout < 0:
                raise ValueError("timeout must be non-negative")
            end_time = None if timeout is None else time.time() + timeout
            while len(self._queue) >= self.maxsize:
                if timeout is None:
                    self._cond.wait()
                else:
                    remaining = end_time - time.time()
                    if remaining <= 0:
                        raise queue.Full
                    self._cond.wait(remaining)
            self._queue.append(item)
            self._cond.notify()

    def get(self, block=True, timeout=None):
        with self._cond:
            if not block:
                if not self._queue:
                    raise queue.Empty
                item = self._queue.popleft()
                self._cond.notify()
                return item
            if timeout is not None and timeout < 0:
                raise ValueError("timeout must be non-negative")
            end_time = None if timeout is None else time.time() + timeout
            while not self._queue:
                if timeout is None:
                    self._cond.wait()
                else:
                    remaining = end_time - time.time()
                    if remaining <= 0:
                        raise queue.Empty
                    self._cond.wait(remaining)
            item = self._queue.popleft()
            self._cond.notify()
            return item

    def put_nowait(self, item):
        self.put(item, block=False)

    def get_nowait(self):
        return self.get(block=False)

    def qsize(self):
        with self._cond:
            return len(self._queue)

    def empty(self):
        with self._cond:
            return not self._queue

    def full(self):
        with self._cond:
            return len(self._queue) >= self.maxsize
