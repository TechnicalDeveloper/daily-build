# Levenshtein Similarity Score

Build a function `similarity(a: str, b: str) -> float` that returns a string similarity score in `[0.0, 1.0]`.

The score is computed from the Levenshtein edit distance:

    score = 1 - distance / max(len(a), len(b))

Implement Levenshtein distance with the iterative dynamic programming algorithm using only two rows.

Edge cases to respect:
- Two empty strings are identical, so the score is `1.0`.
- An empty string and a non-empty string have score `0.0`.
- Case is significant: `similarity('Cat', 'cat')` must be less than `1.0`.
