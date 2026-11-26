# Memoize with TTL and LRU

Build a memoization utility that caches the result of a pure function.

Signature:
`function memoize<Args extends unknown[], Result>(fn: (...args: Args) => Result, options?: MemoizeOptions<Args>): (...args: Args) => Result`

`MemoizeOptions<Args>`:
- `ttlMs?: number` — expire entries after this many milliseconds.
- `maxSize?: number` — maximum cache size. When exceeded, the least recently used entry is evicted.
- `resolver?: (...args: Args) => string` — produce a custom cache key from the function arguments.

Edge cases to respect:
- If `ttlMs` is provided, a cached value older than that must be recomputed on the next call.
- If `maxSize` is exceeded, the least recently used entry must be evicted.
- If the wrapped function throws, the error must propagate and the failed call must not be cached.
- By default, object arguments are compared by identity; pass a `resolver` for value-based object keys.
