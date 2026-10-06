# Rolling Hash Class

# Rolling Hash Class

Implement a `RollingHash` class that computes a polynomial rolling hash over a sliding window of characters. The hash function is:

`hash = (hash * base + charCode) % mod`

When sliding the window, remove the contribution of the leftmost character using precomputed `power = base^(windowSize-1) mod mod`.

## Class Signature

```typescript
export interface RollingHashOptions {
  base?: number;   // default 256
  mod?: number;    // default 1_000_000_007
}

export class RollingHash {
  constructor(windowSize: number, options?: RollingHashOptions);
  addChar(c: string): void;         // adds character to the window; automatically removes oldest if window is full
  getHash(): number;                // returns the current hash; throws if window is not full
  isFull(): boolean;                // returns true if window size reached
  reset(): void;                    // clears the window and resets hash
}
```

## Edge Cases

- `windowSize` must be positive; throw if <= 0.
- `getHash()` must throw when fewer than `windowSize` characters have been added.
- When `mod` is small, negative results after modulo subtraction must be fixed.
- Characters are assumed to be ASCII (single char).
