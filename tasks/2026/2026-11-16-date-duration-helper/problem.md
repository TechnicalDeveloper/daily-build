# Date and Duration Helper

## Date and Duration Helper

Implement three functions for working with durations and dates.

### `parseDuration(input: string): number`
Parses a human-readable duration string like `"1d2h3m4s"` and returns the total number of milliseconds. The string may contain days (`d`), hours (`h`), minutes (`m`), and seconds (`s`) in any order, with optional spaces. Throw an `Error` on empty input, unknown tokens, or leftover characters.

### `formatDuration(ms: number): string`
Converts a non-negative number of milliseconds into a compact human-readable string, e.g. `86400000` → `"1d"`. Use the units `d`, `h`, `m`, `s`, and `ms`. For zero, return `"0ms"`. Throw an `Error` on negative input.

### `addDuration(date: Date, duration: string): Date`
Returns a new `Date` by adding the given duration string to `date` (does not mutate the input). Uses `parseDuration` internally.

### Edge cases to respect
- `parseDuration` should accept `"1d 2h 3m 4s"` (spaces) and lowercase only.
- `parseDuration` should reject empty strings, strings with unrecognized characters (e.g. `"2h3x"`), and strings without any valid pattern (e.g. `"abc"`).
- `formatDuration` must handle `0` and large values (e.g., `9000000` → `"2h 30m"`).
