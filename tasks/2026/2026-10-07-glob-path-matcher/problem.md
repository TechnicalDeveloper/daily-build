# Glob Path Matcher

Implement a function `matches(pattern: str, path: str) -> bool` that returns `True` if `path` matches `pattern` using shell-style wildcards:
- `*` matches any sequence of characters (including an empty sequence)
- `?` matches exactly one character
- All other characters match themselves

The pattern must match the entire path, not a substring.

Edge cases to respect:
- `*` can match nothing, e.g., `a*` matches `a`.
- `?` requires exactly one character, so `a?c` matches `abc` but not `ac`.
- Matching is case-sensitive, so `A` does not match `a`.
- Multiple `*` are allowed, e.g., `*a*b*` matches `xayb`.
- The pattern may be empty; only an empty path matches it.
