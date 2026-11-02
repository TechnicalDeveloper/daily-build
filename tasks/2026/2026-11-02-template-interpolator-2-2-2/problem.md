# Template Interpolator

Build a template interpolator function that replaces placeholders in a string.

**Signature**: `interpolate(template: string, values: Record<string, string | number | boolean | null | undefined>): string`

- Placeholders are of the form `{{key}}`. The key inside the braces may have optional whitespace around it.
- If a key exists in `values`, replace the placeholder with its string representation.
- If a key does not exist, replace the placeholder with an empty string.
- Values that are not strings (numbers, booleans) should be converted to strings. `null` and `undefined` are treated as missing (empty string).

**Edge cases to respect**:
1. Missing keys should result in an empty string.
2. Values that are numbers should be converted to their string representation.
3. Whitespace inside the braces (`{{ key }}`) should be ignored, matching the same key.
