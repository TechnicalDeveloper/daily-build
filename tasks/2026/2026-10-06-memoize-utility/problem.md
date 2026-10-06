# Memoization Utility Function

Implement a generic memoization function `memoize` that caches the return value of a given function based on its arguments.

## Signature
```typescript
function memoize<Args extends any[], Return>(
  fn: (...args: Args) => Return,
  keyFn?: (...args: Args) => string
): (...args: Args) => Return;
```

## Requirements
- The returned memoized function should call `fn` only once for a given set of arguments, and return the cached value on subsequent calls with the same arguments (as determined by `keyFn`).
- If no `keyFn` is provided, use `JSON.stringify(args)` as the default key function.
- If `fn` throws an error, the error should propagate and **not** be cached – subsequent calls with the same arguments must re-execute `fn`.

## Edge Cases to Respect
1. **Arguments that are not serializable by `JSON.stringify`** (e.g., `undefined`, functions, circular references) – the default key function will fail. The user must supply a custom `keyFn` that can produce a stable string representation.
2. **Equal but distinct objects** – `JSON.stringify` produces the same string for deeply equal objects (assuming consistent property order), so the default key works for that case. However, property order is not guaranteed; a custom key function can force a deterministic order.
3. **No arguments** – the function is called once and the result is cached.
4. **Error handling** – errors must not be cached; each call that previously threw must re-invoke `fn`.
