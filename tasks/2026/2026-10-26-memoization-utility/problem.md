# Memoization Utility Function

Implement a generic `memoize` function that caches the result of a pure function based on its arguments. The cache should be used for subsequent calls with the same arguments.

## Signature

```typescript
function memoize<T extends (...args: any[]) => any>(fn: T): T;
```

## Requirements
- The returned function should have the same behavior as `fn` but cache results.
- The cache key must consider all arguments, including objects and arrays (by deep value equality).
- The cache must correctly handle `undefined` as an argument (distinct from `null`).
- The solution must not use any third-party packages.

## Edge Cases
1. **Multiple arguments**: `memoize((a, b) => a + b)` should cache different results for `(1,2)` vs `(2,1)`.
2. **Object arguments**: `memoize((obj) => obj.x)` should treat `{x:1}` and `{x:1}` as the same key, even if they are different object references.
3. **`undefined` vs `null`**: `memoize((x) => x)` should differentiate between `undefined` and `null` arguments.
4. **No arguments**: `memoize(() => Math.random())` should return the same value on repeated calls (since there are no arguments, the key is constant).
