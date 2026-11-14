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
            elif timeout is not None and timeout < 0:
                raise ValueError("timeout must be non-negative")
            else:
                end_time = None if timeout is None else time.monotonic() + timeout
                while len(self._queue) >= self.maxsize:
                    if end_time is None:
                        self._cond.wait()
                    else:
                        remaining = end_time - time.monotonic()
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
            elif timeout is not None and timeout < 0:
                raise ValueError("timeout must be non-negative")
            else:
                end_time = None if timeout is None else time.monotonic() + timeout
                while not self._queue:
                    if end_time is None:
                        self._cond.wait()
                    else:
                        remaining = end_time - time.monotonic()
                        if remaining <= 0:
                            raise queue.Empty
                        self._cond.wait(remaining)
            item = self._queue.popleft()
            self._cond.notify()
            return item

    def qsize(self):
        with self._cond:
            return len(self._queue)
