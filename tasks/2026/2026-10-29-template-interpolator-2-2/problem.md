# Template Interpolator

Build a function `interpolate` that replaces placeholders in a template string with values from an object.

**Signature:**
```typescript
export function interpolate(template: string, values: Record<string, string | number | boolean>): string
```

Placeholders are of the form `{{key}}`. The function should:
- Replace each placeholder with the corresponding value from `values`, converting non-string values to strings.
- If a placeholder key is not present in `values`, throw an `Error`.
- Handle multiple occurrences of the same key.

**Edge cases to respect:**
- Placeholder with missing key throws an error.
- Values that are numbers or booleans are converted to their string representation.
- Template with no placeholders returns the template unchanged.
