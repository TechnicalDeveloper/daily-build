# Template Interpolator

## Problem

Write a function `interpolate(template: str, values: dict) -> str` that performs template interpolation. The `template` string may contain placeholders of the form `{key}`, where `key` is a placeholder name. Replace each placeholder with the corresponding value from `values` dictionary (converted to string). If a placeholder key is not present in `values`, raise a `KeyError`.

### Edge Cases to Respect
- If a placeholder key is missing from `values`, raise a `KeyError`.
- Handle multiple occurrences of the same placeholder.
- Values in the dictionary can be of any type; convert them to string during replacement.
- An empty template should return an empty string.
