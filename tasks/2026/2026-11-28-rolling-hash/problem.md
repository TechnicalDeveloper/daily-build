# Rolling Hash (Rabin-Karp)

Implement a rolling hash class that supports adding a value to the right and removing a value from the left, maintaining a hash of the current window in O(1) per operation.

## Signature

```typescript
export class RollingHash {
  constructor(base: number, mod: number);
  add(value: number): void;      // append value to the right
  removeLeft(): void;            // remove the leftmost value (throws if empty)
  getHash(): number;             // current hash modulo mod, always in [0, mod)
  readonly size: number;         // current window length
}
```

## Requirements

- `base` and `mod` must be positive, coprime, with `mod > base` (recommended).
- Hash is computed as: `(a₀·base^(k-1) + a₁·base^(k-2) + ... + aₖ₋₁) mod mod`, where `k` is the window length.
- `add` and `removeLeft` must update the hash in O(1).
- All numbers are JavaScript integers (safe up to 2^53).

## Edge Cases

- Removing from an empty window must throw an error.
- The hash must always be non‑negative (i.e., normalized to `[0, mod)`).
- The constructor must throw if `base` and `mod` are not coprime or if either is not positive.
