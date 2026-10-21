# Dice Coefficient String Similarity

Implement a function that computes the Dice coefficient similarity between two strings based on character bigrams. The Dice coefficient is defined as:

    Dice(A,B) = (2 * |A ∩ B|) / (|A| + |B|)

where A and B are the sets of all overlapping character bigrams (2-character substrings) of the input strings.

**Function signature:**

```python
def dice_similarity(s1: str, s2: str) -> float:
```

**Edge cases to handle:**
- If both strings are empty, return `1.0` (the sets are identical and have size 0).
- If either string has length < 2 (so no bigrams can be formed), return `0.0`, except when both are empty (covered by the previous rule).
- The comparison is case-sensitive (e.g., "ab" and "Ab" yield 0.0).
- The function must not raise any exceptions for any string inputs.
