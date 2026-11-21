# Human-readable duration

Build a function `format_duration(seconds: int) -> str` that converts a duration in seconds into a human-readable string. The output should use units: years (365 days), days, hours, minutes, seconds. Only include non-zero units, separated by commas and "and" before the last unit. Pluralize unit names when the value is not 1. For zero seconds, return "now". Negative seconds should be treated as their absolute value.

Edge cases:
- `format_duration(0)` returns `"now"`.
- `format_duration(62)` returns `"1 minute and 2 seconds"`.
- Negative inputs should behave as if the absolute value is passed.
- Large values must correctly use all available units.
