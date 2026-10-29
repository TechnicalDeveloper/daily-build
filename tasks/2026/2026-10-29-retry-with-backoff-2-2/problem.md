# Retry with Exponential Backoff

Implement a decorator `retry` that retries a function when it raises an exception, using exponential backoff.

**Signature:**
```python
def retry(max_attempts: int = 3, base_delay: float = 1.0, exceptions: tuple = (Exception,)):
    ...
```

The decorator should:
- Retry the function up to `max_attempts` times if it raises an exception matching `exceptions`.
- After each failed attempt (except the last), wait `base_delay * (2 ** attempt)` seconds before the next attempt.
- If `max_attempts` is not positive, raise `ValueError`.
- If the function raises an exception not in `exceptions`, it should **not** be retried – the exception should propagate immediately.
- On the last attempt, if it fails, the last exception is raised.

**Edge cases to respect:**
1. Function that succeeds on the first attempt – no retry, no delay.
2. Function that always fails – after `max_attempts` attempts, the final exception is raised.
3. Function that succeeds on the third attempt – should sleep twice (with delays `base_delay` and `base_delay * 2`).
4. Function raises an exception not in `exceptions` – should raise immediately without any retry.
