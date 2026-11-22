# Format Duration Compact Helper

Implement a duration helper that converts seconds into a compact human-readable string.

## Signature

```typescript
export function formatDuration(totalSeconds: number): string
```

Also export a helper `parseDuration(totalSeconds: number): DurationParts` which returns `{ days, hours, minutes, seconds }` (all integers).

## Behavior
- `formatDuration(0)` returns `"0s"`.
- Roll over at 60 seconds (-> minutes), 3600 (-> hours), 86400 (-> days).
- Omit zero units; join non-zero units with a space and abbreviation suffix (`d`, `h`, `m`, `s`).
- Throw an `Error` if the input is negative or not a finite number.

## Edge cases to consider
1. Input `0` → `"0s"`.
2. Input `59` → `"59s"`, `60` → `"1m"` (no seconds shown).
3. Input `3661` → `"1h 1m 1s"`.
4. Input `90061` → `"1d 1h 1m 1s"`.
5. Negative or `NaN` inputs must throw.
