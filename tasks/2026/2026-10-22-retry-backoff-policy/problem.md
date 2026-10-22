# Retry Policy with Backoff

Implement a retry decorator with exponential backoff.

## Signature

```python
@retry(max_retries=3, base_delay=1, backoff_factor=2, exceptions=Exception)
def your_function(...):
    ...
```

The decorator should catch the specified exception(s), then after a delay of `base_delay * (backoff_factor ** attempt)` seconds, retry the function. After `max_retries` attempts, re-raise the last exception.

## Edge Cases
- If `max_retries=0`, no retry should be attempted; any exception is propagated immediately.
- If the function succeeds on the first attempt, the decorator should return normally.
- The decorator must only catch exceptions that are subclasses of the `exceptions` tuple.
- The delay should be computed as `base_delay * (backoff_factor ** attempt)` where attempt starts at 0 for the first retry.
