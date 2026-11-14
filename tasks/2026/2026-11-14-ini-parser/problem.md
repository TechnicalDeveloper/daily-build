# Parse INI-like configuration text

Implement a small parser for an INI-like text format. Write a function `parse_ini(text: str) -> dict[str, dict[str, str]]` that parses the given text according to these rules:

- Lines are separated by newline characters.
- Blank lines and lines starting with `#` or `;` are ignored (comments).
- A section header is a line that (after trimming) starts with `[` and ends with `]`. The section name is the content inside the brackets, trimmed. If no section header has been seen yet, keys go into a section named `"global"`.
- Any other non-comment line must be a key-value assignment: `key = value` or `key=value`. The key and value are separated by the first `=`. Both key and value are trimmed of leading/trailing whitespace. An empty key raises a `ValueError`.
- Lines that do not contain `=` raise a `ValueError`.
- Duplicate keys: later assignments overwrite earlier ones within the same section.

Edge cases to respect:
- Empty input should produce an empty dictionary `{}`.
- Sections can appear multiple times; they should be merged.
- Comments can appear anywhere, even inside a section, without affecting the current section.
- Keys appearing before any section header go into the `"global"` section.
