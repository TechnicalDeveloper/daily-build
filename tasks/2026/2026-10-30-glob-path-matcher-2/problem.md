# Glob Path Matcher

Implement a function `match_path(pattern: str, path: str) -> bool` that determines whether a given path matches a glob pattern. The glob syntax supports:
- `*` matches any sequence of characters (including empty) except the path separator `/`.
- `?` matches exactly one character except `/`.
- `**` matches any sequence of characters including `/` (i.e., zero or more path segments).
- Other characters match themselves literally.

The pattern and path are both strings. The match is case-sensitive. The function returns `True` if the entire path matches the pattern, `False` otherwise.

Edge cases to respect:
- `**` must be used as a whole path segment (i.e., it must be surrounded by `/` or at the start/end of the pattern). For example, `a**b` is invalid and should raise `ValueError`.
- The path may or may not start with a leading `/`; the pattern should match exactly as given (no implicit leading slash normalization).
- `**` can match zero segments. For example, pattern `a/**/b` should match `a/b` as well as `a/x/y/b`.

Signature: `def match_path(pattern: str, path: str) -> bool:`
