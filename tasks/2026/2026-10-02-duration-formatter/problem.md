# Duration Formatter

Implement a function `format_duration(seconds: int) -> str` that takes a total number of seconds and returns a human-readable string representing the duration.

- The output should break down the duration into days, hours, minutes, and seconds.
- Only include non-zero units. For example, if the duration is exactly 1 hour, output `"1 hour"`, not `"1 hour, 0 minutes, 0 seconds"`.
- Pluralize correctly: `"1 second"`, `"2 seconds"`, `"1 hour"`, `"2 hours"`, etc.
- If the input is `0`, return `"now"`.
- Components are separated by `", "` (comma+space) with no conjunction.

**Edge cases to respect:**
1. `0` seconds → `"now"`
2. `1` second → `"1 second"`
3. `3661` seconds → `"1 hour, 1 minute, 1 second"`
4. `172800` seconds → `"2 days"`
