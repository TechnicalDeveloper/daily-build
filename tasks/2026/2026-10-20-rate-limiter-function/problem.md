# Rate Limiter

Implement a rate limiter that restricts the number of function calls within a sliding time window.

## Signature
```typescript
interface RateLimiter {
  call: () => boolean;
}

function createRateLimiter(maxCalls: number, windowMs: number): RateLimiter;
```

## Behavior
- `call()` returns `true` if the call is allowed (within the limit) and `false` otherwise.
- The rate limiter uses a sliding window: timestamps older than `windowMs` milliseconds are ignored.
- The window starts with the first call.

## Edge Cases
1. `maxCalls <= 0` or `windowMs <= 0` should throw an error with a descriptive message.
2. After the window expires, calls should be allowed again, resetting the count.
3. Multiple windows in sequence must be handled correctly.
