# Retry Policy with Exponential Backoff

Implement a decorator `retry` that retries a function with exponential backoff. The decorator should be defined as:

```python
def retry(max_retries=3, base_delay=1, backoff_factor=2, exceptions=(Exception,)):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # ...
        return wrapper
    return decorator
```

- The wrapped function is called. If it raises an exception that is a subclass of any exception in `exceptions`, the function is retried up to `max_retries` times. The delay between retries is `base_delay * (backoff_factor ** attempt)` seconds (attempt starts at 0).
- If the function raises an exception not in `exceptions`, it should propagate immediately without retrying.
- If all retries fail, the last exception is raised.

**Edge cases to respect:**
1. Function succeeds on the first call – should return immediately.
2. Function fails multiple times then succeeds – should retry until success.
3. Function always fails – should raise the last exception after exhausting all retries.
4. Function raises an exception not in the retryable set – should not be retried, raise immediately.
