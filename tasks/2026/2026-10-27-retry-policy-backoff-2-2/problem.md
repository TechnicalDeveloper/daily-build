# Retry Policy with Exponential Backoff

Implement a decorator `retry` that wraps a function with an exponential backoff retry policy. The decorator accepts the following optional keyword arguments:
- `max_retries`: maximum number of retries (default 3)
- `base_delay`: initial delay in seconds (default 1)
- `max_delay`: maximum delay in seconds (default 60)
- `backoff_factor`: multiplier for delay after each retry (default 2)
- `exceptions`: tuple of exception types to catch and retry (default (Exception,))

**Signature**:
```python
def retry(max_retries=3, base_delay=1, max_delay=60, backoff_factor=2, exceptions=(Exception,)):
    # returns a decorator
```
The wrapped function must raise the last caught exception if all retries are exhausted. Non-retryable exceptions (not in `exceptions`) must propagate immediately.

**Edge cases to handle**:
- `max_retries=0`: the function is called exactly once and any exception (if in `exceptions`) is raised without retry.
- `exceptions` is a custom tuple; exceptions not in this tuple should not be caught and must propagate.
- The backoff delay should never exceed `max_delay`.
