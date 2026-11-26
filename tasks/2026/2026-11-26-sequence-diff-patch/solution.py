def diff(a, b):
    '''Return a patch that turns sequence a into sequence b.'''
    a = list(a)
    b = list(b)
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    ops = []
    i, j = n, m
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            ops.append(('equal', a[i - 1]))
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            ops.append(('delete', a[i - 1]))
            i -= 1
        else:
            ops.append(('insert', b[j - 1]))
            j -= 1
    while i > 0:
        ops.append(('delete', a[i - 1]))
        i -= 1
    while j > 0:
        ops.append(('insert', b[j - 1]))
        j -= 1
    ops.reverse()
    return ops


def apply_patch(seq, patch):
    '''Apply a patch to seq and return the resulting list.'''
    seq = list(seq)
    result = []
    idx = 0
    for op, item in patch:
        if op == 'equal':
            if idx >= len(seq) or seq[idx] != item:
                raise ValueError('Patch does not match sequence')
            result.append(seq[idx])
            idx += 1
        elif op == 'delete':
            if idx >= len(seq) or seq[idx] != item:
                raise ValueError('Patch does not match sequence')
            idx += 1
        elif op == 'insert':
            result.append(item)
        else:
            raise ValueError('Unknown operation: {0!r}'.format(op))
    if idx != len(seq):
        raise ValueError('Patch did not consume entire sequence')
    return result
