from collections import deque


class RateLimiter:
    def __init__(self, limit: int, window: float) -> None:
        if limit < 0:
            raise ValueError("limit must be non-negative")
        if window <= 0:
            raise ValueError("window must be positive")
        self.limit = limit
        self.window = window
        self._requests = deque()

    def allow(self, timestamp: float) -> bool:
        if self.limit == 0:
            return False
        boundary = timestamp - self.window
        while self._requests and self._requests[0] <= boundary:
            self._requests.popleft()
        if len(self._requests) < self.limit:
            self._requests.append(timestamp)
            return True
        return False
