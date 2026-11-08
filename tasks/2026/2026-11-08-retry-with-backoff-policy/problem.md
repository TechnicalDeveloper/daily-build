# Retry with Exponential Backoff

Build a function `retryWithBackoff` that executes an async operation and retries it on failure with exponential backoff.

**Signature:**
```typescript
type AsyncOperation<T> = () => Promise<T>;

function retryWithBackoff<T>(
  operation: AsyncOperation<T>,
  maxRetries: number = 3,
  baseDelayMs: number = 100
): Promise<T>;
```

**Behavior:**
- If `operation` succeeds, return its resolved value.
- If `operation` throws, wait `baseDelayMs * 2^(attempt)` milliseconds, then retry (attempt starts at 0).
- After `maxRetries` failures, reject with the last error.
- If `maxRetries` is 0, do not retry.

**Edge cases to respect:**
1. `maxRetries` is 0 → only one attempt, no delay, reject on failure.
2. `baseDelayMs` is 0 → immediate retry (delay 0).
3. The function must still work if `operation` returns `undefined`.
