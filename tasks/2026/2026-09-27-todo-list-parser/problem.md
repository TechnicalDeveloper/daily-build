# Todo List Parser

## Problem

Build a function `parse_todo(text: str) -> list[dict]` that parses a text containing todo items in Markdown-style task list format. Each task line follows the pattern:

- `- [ ] <description>` for an incomplete task.
- `- [x] <description>` for a completed task (case-insensitive for 'x').

Lines that do not match this pattern (including blank lines, headers, comments, etc.) must be ignored. The description should be stripped of leading and trailing whitespace.

### Edge Cases

1. Empty input string returns an empty list.
2. Leading/trailing whitespace on the line or within the description must be trimmed.
3. Non-task lines (e.g., plain text, `- [ ]` without a space after the bracket) are ignored.

### Signature

```python
def parse_todo(text: str) -> list[dict]:
    ...
```

Each element in the returned list must be a dictionary with keys `"completed"` (bool) and `"description"` (str).
