# Template Interpolator

Build a function `interpolate` that replaces placeholders in a template string with values from a data object. Placeholders are delimited by double curly braces, e.g., `{{key}}`. The function should handle multiple placeholders, missing keys, and non-string values.

**Signature:**
```typescript
export declare function interpolate(template: string, data: Record<string, string | number | boolean>): string
```

**Edge cases to respect:**
1. If a placeholder references a key that does not exist in the data object, the function must throw an error with the missing key name.
2. Values can be numbers or booleans; they must be converted to their string representation.
3. Placeholder keys consist only of word characters (`\w+`).
