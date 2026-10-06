# Simple Text Config Parser

# Build a Simple Configuration Parser

You are to implement a function `parse_config(text: str) -> dict` that parses a simple key-value text format.

## Format Rules:
- Each line can be a comment (starting with `#`), blank, or a key-value pair.
- Key-value pairs are separated by a colon `:`. Whitespace around keys and values is trimmed.
- If a line contains multiple colons, only the first colon is considered the separator; the rest become part of the value (including colons).
- Duplicate keys will overwrite earlier values.
- Ignore blank lines and comment lines.
- Lines with an empty key (i.e., nothing before the colon) are ignored.
- Lines with an empty value (e.g., `key:` ) are allowed; value becomes empty string.

## Signature
```python
def parse_config(text: str) -> dict:
    """Parse a configuration text into a dictionary."""
```

## Edge Cases to Respect
1. Empty input string should return an empty dictionary.
2. Lines with extra colons (e.g., `a:b:c` ) become key `a` and value `b:c`.
3. Whitespace around keys and values must be stripped (e.g., `  key  :  value  ` produces `{"key": "value"}`).
