# Retry Policy with Backoff

Implement a `retry` decorator that retries a function with exponential backoff.

Signature:

```python
def retry(max_attempts=3, base_delay=0.1, backoff_factor=2, exceptions=(Exception,)):
    ...
```

`retry` returns a decorator. It should call the wrapped function at most `max_attempts` times. Before each retry, sleep for `base_delay * backoff_factor ** (attempt - 1)`, where `attempt` is the failed attempt number. Only exceptions in `exceptions` are retried. When the decorated function succeeds, return its result immediately. If the last allowed attempt fails, re-raise the last exception. Use `functools.wraps`.

Edge cases:
- Success on the first attempt: no `time.sleep` and no additional call.
- A non-matching exception: propagate immediately without retrying.
- Invalid parameters: `max_attempts` must be >= 1, `base_delay` must be >= 0, and `backoff_factor` must be >= 1; otherwise raise `ValueError`.
