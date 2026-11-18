# Wildcard Path Matcher

Implement `is_match(s: str, p: str) -> bool` that returns `True` if the string `s` matches the glob pattern `p`. In the pattern `*` matches any sequence of characters (including the empty sequence) and `?` matches exactly one character. The match must cover the entire string (not partial).

Edge cases to respect:
- An empty pattern matches only an empty string.
- A pattern consisting only of `*` matches any string, including the empty string.
- Consecutive `*` characters should be treated the same as a single `*`.
- The `?` character always matches exactly one character, never zero.
