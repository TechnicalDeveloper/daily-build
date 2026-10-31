# Path Glob Matcher

Implement a function `glob_match(pattern: str, path: str) -> bool` that checks whether a `path` matches a simple glob `pattern`.

Rules:
- `*` matches any sequence of characters (including the empty string) except the path separator `/`.
- `?` matches exactly one character, except `/`.
- All other characters match literally.
- The pattern must match the **entire** path (not a substring).

Edge cases to respect:
1. Empty pattern and empty path: should return `True`.
2. Pattern with only `*` should match any path without `/`.
3. A `?` cannot match `/`; for example, pattern `a?b` should not match `a/b`.
