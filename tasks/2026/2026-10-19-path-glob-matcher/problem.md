# Path Glob Matcher

# Path Glob Matcher

Implement a function `match(pattern: string, path: string): boolean` that checks whether the given `path` matches the glob `pattern`. 

**Rules:**
- `*` matches any sequence of characters (except the path separator `/`).
- `?` matches exactly one character (except `/`).
- All other characters (including `/`) match literally.

**Edge cases to handle:**
- An empty pattern only matches an empty path.
- A `*` can match zero characters (so `*` matches the empty string).
- `*` must not match across directory separators (e.g., `a/*` should match `a/b` but not `a/b/c`).
