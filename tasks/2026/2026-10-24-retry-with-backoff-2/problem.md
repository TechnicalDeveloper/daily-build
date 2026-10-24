# Retry with Exponential Backoff

Implement a `retry` function that repeatedly executes an asynchronous operation until it succeeds or the maximum number of retries is reached. Use an exponential backoff strategy: delay between retries = `baseDelay * 2^(attempt - 1)` (first retry after `baseDelay`, second after `2*baseDelay`, etc.).

**Signature**
```typescript
async function retry<T>(
  fn: () => Promise<T>,
  options: { maxRetries: number; baseDelay: number }
): Promise<T>
```

**Edge cases to handle**
- `maxRetries = 0`: call `fn` exactly once and return its result or reject with the error.
- `baseDelay = 0`: immediate retries, no wait.
- If `fn` throws synchronously (not a rejected promise), treat it as a rejection and retry accordingly.
- Respect the number of retries: if `maxRetries` is 2, the function may be called up to 3 times (initial + 2 retries).
