# Parse Key-Value Records

Build a small parser for a simple text format. Write a function `parse_records(text: str) -> list[dict[str, str]]` that parses a string containing zero or more records.

Each record is a block of consecutive non-empty, non-comment lines. A blank line separates records. Lines starting with `#` (after leading whitespace) are comments and are ignored. A field line is `Key: Value`; split on the first colon only. Surrounding whitespace on the key and value is trimmed. If a line is not blank and not a comment but has no colon, raise `ValueError`. If a line has an empty key, also raise `ValueError`. Duplicate keys in the same record should use the last value.

Edge cases:
- Blank lines and comment lines should not create empty records.
- Values may contain colon characters.
- Duplicate keys are overridden by the latest value.
