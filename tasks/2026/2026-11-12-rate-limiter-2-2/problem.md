# Rate Limiter

# Rate Limiter

Build a rate limiter class that limits how often a given key may make requests.

## Signature

```typescript
export class RateLimiter {
    constructor(limit: number, windowMs: number);
    isAllowed(key: string): boolean;
    resetKey(key: string): void;
    resetAll(): void;
}
```

- `limit`: maximum number of allowed calls in the sliding time window.
- `windowMs`: length of the window in milliseconds.
- `isAllowed(key)`: returns `true` if the request should be allowed, `false` otherwise.

## Edge cases

- Constructor must throw a `RangeError` if `limit` or `windowMs` is not a positive number.
- Each key is tracked independently.
- The window is sliding (based on exact timestamps), not fixed resetting.
