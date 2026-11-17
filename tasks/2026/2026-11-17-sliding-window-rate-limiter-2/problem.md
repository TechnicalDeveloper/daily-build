# Sliding Window Rate Limiter

Implement a `RateLimiter` class that restricts the number of allowed events within a sliding time window.

## Signature

```python
class RateLimiter:
    def __init__(self, max_events: int, window_seconds: float, clock=time.time) -> None
    def allow(self) -> bool
```

- `max_events`: maximum number of events allowed within any `window_seconds` period.
- `window_seconds`: length of the time window.
- `clock`: a callable returning the current time (in seconds). Defaults to `time.time`. Useful for testing.

The `allow()` method should return `True` if an event can be accepted at the current time, and record the event. Otherwise return `False`. Events are considered valid for exactly `window_seconds` seconds; an event whose timestamp is exactly at the boundary (now - window_seconds) is considered expired.

## Edge Cases

1. If `max_events` is `0`, no event is ever allowed.
2. If `max_events` is negative or `window_seconds` is non-positive, raise `ValueError`.
3. The limiter must work correctly with fractional window sizes and event counts (e.g., `max_events=2`, `window_seconds=0.5`).
