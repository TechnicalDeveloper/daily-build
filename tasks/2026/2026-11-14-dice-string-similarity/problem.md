# Dice Coefficient String Similarity

Implement a function `diceCoefficient(a: string, b: string): number` that returns a similarity score between 0 and 1.

The score is computed using the Dice coefficient on character bigrams (adjacent character pairs). For strings shorter than 2 characters, treat the entire string as a single token.

Edge cases:
- Both strings empty → returns 1.
- Exactly one string empty → returns 0.
- Identical non-empty strings → returns 1.
- The metric is case-sensitive: "abc" and "Abc" are not identical.
