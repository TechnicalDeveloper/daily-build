import time

class RateLimiter:
    """A sliding window rate limiter."""
    def __init__(self, max_events: int, window_seconds: float, clock=time.time):
        if max_events < 0:
            raise ValueError("max_events must be non-negative")
        if window_seconds <= 0:
            raise ValueError("window_seconds must be positive")
        self.max_events = max_events
        self.window_seconds = window_seconds
        self.clock = clock
        self.events = []

    def allow(self) -> bool:
        now = self.clock()
        # Remove expired events
        cutoff = now - self.window_seconds
        while self.events and self.events[0] <= cutoff:
            self.events.pop(0)
        if len(self.events) < self.max_events:
            self.events.append(now)
            return True
        return False
