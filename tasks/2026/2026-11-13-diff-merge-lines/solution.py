from typing import List, Tuple

Operation = Tuple[str, str]


def diff_lines(old: List[str], new: List[str]) -> List[Operation]:
    """Compute a line-based diff between two lists of strings.

    Returns a list of ('equal', line), ('delete', line), or ('insert', line)
    operations that, when applied in order to `old`, produce `new`.
    Uses an LCS-based dynamic programming approach.
    """
    m, n = len(old), len(new)
    # dp[i][j] = length of LCS of old[i:] and new[j:]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if old[i] == new[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    ops = []
    i = j = 0
    while i < m and j < n:
        if old[i] == new[j]:
            ops.append(('equal', old[i]))
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            ops.append(('delete', old[i]))
            i += 1
        else:
            ops.append(('insert', new[j]))
            j += 1

    # Append remaining
    while i < m:
        ops.append(('delete', old[i]))
        i += 1
    while j < n:
        ops.append(('insert', new[j]))
        j += 1

    return ops


def apply_patch(base: List[str], patch: List[Operation]) -> List[str]:
    """Apply a patch (list of operations) to a base list of lines.

    Returns a new list of lines. The patch must be a valid output from
    `diff_lines`. For each op:
      'equal' -> keep the line (it must match the next line in base)
      'delete' -> skip the line (it must match the next line in base)
      'insert' -> add the new line to the result
    """
    result = []
    base_iter = iter(base)
    for op, line in patch:
        if op == 'equal':
            result.append(next(base_iter))  # should equal line
        elif op == 'delete':
            next(base_iter)  # skip
        elif op == 'insert':
            result.append(line)
        else:
            raise ValueError(f"Unknown op: {op}")
    # After a valid patch, the rest of base should be empty.
    # We don't check to keep it simple.
    return result
