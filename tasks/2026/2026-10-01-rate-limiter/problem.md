# Rate Limiter with Sliding Window

Implement a rate limiter that limits the number of allowed requests within a sliding time window.

**Signature:**

```python
class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: float):
        ...

    def allow_request(self) -> bool:
        ...
```

**Edge cases to respect:**

1. If `max_requests` is zero or negative, `allow_request()` should always return `False`.
2. If `window_seconds` is zero or negative, `allow_request()` should always return `False`.
3. Requests that fall exactly on the window boundary (i.e., the oldest timestamp is exactly equal to `current_time - window_seconds`) should be considered expired and removed from the window.
