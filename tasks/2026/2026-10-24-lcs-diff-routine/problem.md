# LCS-Based Diff Routine

# LCS-Based Diff Routine

Write a function `diff(a, b)` that returns a string representing the differences between two strings `a` and `b` using the Longest Common Subsequence (LCS) algorithm.

## Signature
```python
def diff(a: str, b: str) -> str:
```

## Output format
The output is a string with each line representing an operation:
- ` c` (space followed by character) indicates a character common to both strings.
- `-c` indicates a character deleted from `a`.
- `+c` indicates a character inserted from `b`.

The lines are in the order of the edit script.

## Edge cases
- If both strings are empty, return an empty string.
- If one string is empty, all characters from the other are either deleted or inserted.
- If strings have no common characters, the output consists of deletions of `a` followed by insertions of `b`.
- For strings that differ, when both a deletion and an insertion are possible (equal LCS value), insertion is preferred to maintain the order of deletions before insertions.
