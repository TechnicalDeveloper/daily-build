# Duration Format Helper

Write a function `format_duration(start: str, end: str) -> str` that takes two ISO 8601 datetime strings (e.g., "2024-01-01T12:00:00") and returns a human-readable string describing the time difference between them. 

- The result should include only non-zero components: days, hours, minutes. Components are separated by `", "`. 
- If the difference is zero, return `"0 minutes"`. 
- Use singular for 1 (e.g., "1 day", "1 hour", "1 minute") and plural otherwise. 
- If `end` is earlier than `start`, raise a `ValueError`.

Edge cases to respect:
1. Same datetime → `"0 minutes"`
2. Exactly 1 day apart → `"1 day"`
3. `end` before `start` → raise `ValueError`
