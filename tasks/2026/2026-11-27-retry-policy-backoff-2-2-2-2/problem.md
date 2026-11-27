# Retry Policy with Exponential Backoff

Implement a retry policy with exponential backoff as a decorator factory.

Create a function `retry` that returns a decorator which retries the wrapped function on specified exceptions. The decorator should:

- Attempt to call the function.
- If it raises an exception included in `exceptions`, sleep for a delay computed as `min(max_delay, base_delay * (backoff_factor ** retry_count))` where `retry_count` starts at 0 for the first retry.
- Retry up to `max_retries` times (so total attempts = `max_retries + 1`).
- If the function still fails after all retries, re-raise the last exception.
- If the function succeeds, return its result.

**Signature:** `retry(max_retries=3, base_delay=0.1, max_delay=1.0, backoff_factor=2, exceptions=Exception, sleep=time.sleep)`

**Edge cases:**
- `max_retries=0` means no retries, only one attempt.
- `max_retries` must be non-negative; otherwise raise `ValueError`.
- The `sleep` parameter allows injecting a custom sleep function (useful for testing).
- Only exceptions that are instances of `exceptions` (or tuple of them) are caught and retried. Others propagate immediately.
- The backoff delay must be capped at `max_delay`.
