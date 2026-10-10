def diff(seq1, seq2):
    m, n = len(seq1), len(seq2)
    # Build LCS DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to build edit script (prefer insertion when tie)
    i, j = m, n
    result = []
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            result.append(('keep', seq1[i - 1]))
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            result.append(('delete', seq1[i - 1]))
            i -= 1
        else:
            result.append(('insert', seq2[j - 1]))
            j -= 1
    while i > 0:
        result.append(('delete', seq1[i - 1]))
        i -= 1
    while j > 0:
        result.append(('insert', seq2[j - 1]))
        j -= 1
    result.reverse()
    return result
