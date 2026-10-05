# Retry Policy with Backoff

Implement a function that retries an asynchronous operation with exponential backoff.

**Signature:**
type RetryOptions = {
  maxRetries?: number;  // maximum number of retries (default 3)
  baseDelay?: number;  // base delay in ms (default 1000)
  maxDelay?: number;   // maximum delay cap in ms (default 30000)
  factor?: number;     // multiplier for each retry (default 2)
};

async function retryWithBackoff<T>(
  fn: () => Promise<T>,
  options?: RetryOptions
): Promise<T>;

**Edge Cases:**
- If `fn` resolves on the first try, it should return that value without retrying.
- If `fn` fails repeatedly up to `maxRetries` times, the function should reject with the last error.
- The delay must increase exponentially (`delay = baseDelay * factor^attempt`) but never exceed `maxDelay`.
- If `fn` throws a non-Error value (e.g., a string), it should still be caught and treated as a failure.
