# String Dice Coefficient

Implement a function that computes the Sørensen–Dice coefficient between two strings. The coefficient measures similarity based on character bigrams (overlapping pairs of adjacent characters).

**Signature:** `def dice_coefficient(s1: str, s2: str) -> float`

**Details:**
- Return a float between 0.0 (no similarity) and 1.0 (identical).
- For strings with fewer than 2 characters, define:
  - If both are empty, return 1.0.
  - If both have length 1, return 1.0 if they are equal, else 0.0.
  - If exactly one string has length <2 and the other has length >=2, return 0.0.
- Otherwise, compute: `2 * |bigrams(s1) ∩ bigrams(s2)| / (|bigrams(s1)| + |bigrams(s2)|)`.

**Edge cases to handle:**
1. Empty strings: `dice_coefficient('', '')` → 1.0
2. Single‑character strings: `dice_coefficient('a', 'b')` → 0.0
3. No common bigrams: `dice_coefficient('ab', 'cd')` → 0.0
