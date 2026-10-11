# Rate Limiter

## Problem

Implement a **rate limiter** that restricts the number of requests a client can make within a fixed time window. The rate limiter should work for multiple clients identified by a unique key (e.g., user ID or IP address).

### Signature

```typescript
export class RateLimiter {
  constructor(maxRequests: number, windowMs: number)
  // Returns true if request is allowed, false if rate limited.
  isAllowed(key: string): boolean
  // Resets all rate limiters (for testing/administration).
  reset(): void
}
```

### Edge Cases to Respect
- A client that has never made a request should be allowed.
- Requests at the exact boundary of the time window (e.g., at time = windowMs) should be counted in the **new** window, not the old one. (Implement a sliding window using timestamps)
- The rate limiter must handle many distinct keys efficiently without memory leak – you may assume the total number of keys is bounded, but the implementation should clean up old entries when `reset` is called.
- The `isAllowed` method must be O(1) amortized per call (use a queue of timestamps per key).
