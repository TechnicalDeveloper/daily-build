# Duration Format Helper

Write a function `format_duration(seconds: int) -> str` that converts a total number of seconds into a human-readable duration string.

**Requirements:**
- Use units: days, hours, minutes, seconds.
- Singular for 1 (e.g., '1 day'), plural otherwise (e.g., '2 days').
- Separate components with commas and 'and' before the last component.
- If the total is zero seconds, return '0 seconds'.

**Signature:** `def format_duration(seconds: int) -> str:`

**Edge cases to consider:**
1. `format_duration(0)` should return `'0 seconds'`
2. `format_duration(3661)` (1 hour, 1 minute, 1 second) should return `'1 hour, 1 minute and 1 second'`
3. `format_duration(90061)` (1 day, 1 hour, 1 minute, 1 second) should return `'1 day, 1 hour, 1 minute and 1 second'`
