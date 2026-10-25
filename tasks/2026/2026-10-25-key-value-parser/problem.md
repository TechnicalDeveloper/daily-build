# Key-Value Text Parser

Implement a parser for a simple text format where each line can be:

- Blank lines (ignored)
- Comment lines starting with `#` (ignored)
- Key=value pairs, where the key is alphanumeric (letters, digits, underscores) and the value is everything after the first `=` sign, with leading/trailing whitespace stripped.

If a line contains no `=` and is not blank or a comment, it is ignored.

**Signature:** `def parse(text: str) -> dict`

**Edge cases to respect:**
1. Lines with `=` but no value (e.g., `key=`) produce an empty string value.
2. Lines with multiple `=` signs split only on the first occurrence; the rest becomes part of the value (e.g., `a=b=c` gives `{'a': 'b=c'}`).
3. Keys and values may have surrounding whitespace, which must be removed.
