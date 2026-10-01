# Retry with Exponential Backoff

# Retry with Exponential Backoff

Implement a function `retryWithBackoff` that takes an asynchronous function and retries it on failure, with exponential backoff delay.

## Signature

```typescript
interface RetryOptions {
  maxRetries?: number;  // maximum number of retries (default: 3)
  baseDelay?: number;   // initial delay in ms (default: 1000)
  maxDelay?: number;    // maximum delay in ms (default: 30000)
}

async function retryWithBackoff<T>(
  fn: () => Promise<T>,
  options?: RetryOptions
): Promise<T>
```

## Edge Cases

- **Successful first attempt**: If `fn` resolves successfully on the first call, it should return the result immediately without any delay.
- **All attempts fail**: If `fn` rejects on every attempt up to `maxRetries`, the function should throw the error from the last attempt.
- **Zero maxRetries**: When `maxRetries` is 0, the function should attempt the call once and not retry; if it fails, the error is thrown immediately.
