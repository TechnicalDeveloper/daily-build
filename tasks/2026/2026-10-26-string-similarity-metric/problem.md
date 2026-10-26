# String Similarity with N-gram Jaccard

Build a function that computes the similarity between two strings using Jaccard similarity on character n-grams.

**Signature:** `def string_similarity(s1: str, s2: str, n: int = 3) -> float:`

The function extracts all contiguous substrings of length `n` from each string (n-grams), then calculates the Jaccard index: size of intersection divided by size of union.

**Edge cases to respect:**
- If `n` is larger than both strings, compare equality: return 1.0 if equal else 0.0.
- If one string is empty and the other is not, return 0.0.
- If both strings are empty, return 1.0.
