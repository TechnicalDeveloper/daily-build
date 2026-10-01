import time
from collections import deque

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: float):
        if max_requests <= 0 or window_seconds <= 0:
            self._disabled = True
        else:
            self._disabled = False
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.timestamps = deque()

    def allow_request(self) -> bool:
        if self._disabled:
            return False
        now = time.time()
        cutoff = now - self.window_seconds
        # Remove expired timestamps
        while self.timestamps and self.timestamps[0] <= cutoff:
            self.timestamps.popleft()
        if len(self.timestamps) < self.max_requests:
            self.timestamps.append(now)
            return True
        return False
