# Template Interpolator

Build a function `interpolate(template: str, mapping: dict) -> str` that replaces placeholders like `{name}` with the corresponding value from `mapping`. If a placeholder key is missing from `mapping`, raise `KeyError`. To include literal braces, use `{{` for `{` and `}}` for `}`. Edge cases: empty template, mapping with non-string values (convert to str), multiple occurrences of the same key, and escaped braces.
