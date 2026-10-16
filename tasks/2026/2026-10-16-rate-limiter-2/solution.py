import time
from collections import deque


class RateLimiter:
    def __init__(self, max_calls: int, period: float):
        if max_calls <= 0:
            raise ValueError("max_calls must be positive")
        if period <= 0:
            raise ValueError("period must be positive")
        self.max_calls = max_calls
        self.period = period
        self._calls = deque()

    def allow(self) -> bool:
        now = time.monotonic()
        while self._calls and now - self._calls[0] >= self.period:
            self._calls.popleft()
        if len(self._calls) < self.max_calls:
            self._calls.append(now)
            return True
        return False
