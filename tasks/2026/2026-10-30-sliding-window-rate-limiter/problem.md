# Sliding Window Rate Limiter

Implement a `RateLimiter` class that uses a sliding window to allow at most `limit` requests in any `window` seconds.

Signature:
```python
class RateLimiter:
    def __init__(self, limit: int, window: float) -> None: ...
    def allow(self, timestamp: float) -> bool: ...
```

- `__init__` sets the maximum number of allowed requests (`limit`) per sliding window of length `window` seconds.
- `allow(timestamp)` returns `True` if a request at `timestamp` is allowed, otherwise `False`. Timestamps are non-decreasing.

Edge cases to respect:
- Requests exactly `window` seconds apart should not be considered overlapping (the window is half-open: `(timestamp - window, timestamp]`).
- If `limit` is 0, no requests are allowed.
- A single timestamp may be passed multiple times; each call counts as a separate request.
