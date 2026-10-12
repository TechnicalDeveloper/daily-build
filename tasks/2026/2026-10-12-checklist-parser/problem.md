# Checklist Parser

## Build a parser for markdown-style checklist text.

Write a function `parseChecklist(input: string): Task[]` that parses text lines in the format:
- `- [ ] task description` (unchecked)
- `- [x] task description` (checked)

### Signature
```typescript
export interface Task {
  description: string;
  completed: boolean;
}

export function parseChecklist(input: string): Task[];
```

### Edge cases to respect
1. Lines with leading/trailing whitespace are trimmed appropriately; only the checklist format is matched.
2. Lines that do not match the pattern exactly (e.g., `-[ ]` missing space, `- [ ] no space after brackets) are ignored.
3. Empty input or lines with no valid tasks return an empty array.
