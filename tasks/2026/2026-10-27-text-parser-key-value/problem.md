# Text Parser for Key-Value Format

Implement a parser for a simple key-value text format.

Each line contains a key and a value separated by the first `=` character.
Lines starting with `#` are comments and should be ignored. Empty lines should also be ignored.
Leading and trailing whitespace around keys and values must be trimmed.
If a key appears more than once, the last value wins (i.e., later lines override earlier ones).

**Signature:**
```typescript
export function parse(text: string): Record<string, string>
```

**Edge cases to respect:**
1. Empty input string → `{}`.
2. Only comments and blank lines → `{}`.
3. Duplicate keys → the last encountered value is stored.
