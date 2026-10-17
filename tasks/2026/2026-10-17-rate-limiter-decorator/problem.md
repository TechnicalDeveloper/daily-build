# Rate Limiter Decorator

## Problem

Build a decorator `rate_limiter` that limits the number of calls to a function within a sliding time window.

### Signature

```python
def rate_limiter(max_calls: int, time_window: float):
    ...
```

It should return a decorator that wraps a function. The wrapped function raises `RuntimeError` if the number of calls within the last `time_window` seconds (measured by `time.monotonic`) equals or exceeds `max_calls`.

### Edge Cases to Respect

1. **Zero max_calls**: A `max_calls` of 0 should immediately deny any call (always raise).
2. **Zero time_window**: With `time_window=0`, the window never expires, so calls are limited to exactly `max_calls` for the entire program lifetime.
3. **Boundary behavior**: A call that occurs exactly `time_window` seconds after the first call should be allowed (the window is inclusive of the start, exclusive of the end).
