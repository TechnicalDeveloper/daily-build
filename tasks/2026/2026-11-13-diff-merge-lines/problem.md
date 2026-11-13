# Line-based Diff and Merge

Implement two functions for line-based diff and merge.

`diff_lines(old: list[str], new: list[str]) -> list[tuple[str, str]]`
  - Takes two lists of strings (lines of text).
  - Returns a list of operations that transforms `old` into `new`.
  - Each operation is a tuple: `('equal', line)`, `('delete', line)`, or `('insert', line)`.
  - The operations are in order and, when applied to `old`, produce `new`.

`apply_patch(base: list[str], patch: list[tuple[str, str]]) -> list[str]`
  - Takes a base list of lines and a patch as produced by `diff_lines`.
  - Returns a new list that results from applying the patch to `base`.
  - The resulting list should equal the `new` list used to create the patch, given the original `old`.

Edge cases to respect:
- Empty input lists.
- Lines can appear multiple times; the diff must be consistent with the order.
- If the patch is invalid (e.g., tries to delete a line that isn't there), behavior is undefined, but your implementation should not crash; we only test valid patches.
- The diff algorithm should produce a minimal diff (use LCS).
