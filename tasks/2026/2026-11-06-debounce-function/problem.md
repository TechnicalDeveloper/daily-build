# Implement a Debounce Function

Build a generic `debounce` function that delays invocation of a callback until after `wait` milliseconds have elapsed since the last invocation. The returned function must also have a `cancel` method that aborts any pending invocation.

**Signature:**
```typescript
function debounce<T extends (...args: any[]) => any>(
  fn: T,
  wait: number,
  options?: { leading?: boolean; trailing?: boolean }
): {
  (...args: Parameters<T>): void;
  cancel: () => void;
}
```

**Edge cases to respect:**
- If `leading` is `true`, the function is invoked on the first call, then subsequent calls are debounced as usual.
- `this` context must be preserved in the debounced callback.
- Calling `cancel` must prevent any pending invocation from occurring, and subsequent calls after cancel must continue to work.
