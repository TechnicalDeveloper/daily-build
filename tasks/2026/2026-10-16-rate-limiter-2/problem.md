# Sliding Window Rate Limiter

Build a sliding-window rate limiter. Implement a `RateLimiter` class with constructor `RateLimiter(max_calls: int, period: float)` and method `allow()` -> bool. The limiter allows at most `max_calls` calls in any rolling `period` seconds. Calls outside the window are discarded. Use `time.monotonic` for timing.

Edge cases:
- The first `max_calls` calls must be allowed; immediately repeated calls after that must be denied.
- A call that arrives exactly `period` seconds after the oldest recorded call should be allowed.
- Invalid `max_calls` (<= 0) or `period` (<= 0) must raise `ValueError`.
