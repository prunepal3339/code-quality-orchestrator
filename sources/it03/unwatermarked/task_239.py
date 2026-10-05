def get_total_numberOf_sequences(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        dp[i][1] = i
    for i from 2 to n:
        for j from 1 to m:
            dp[j][i] = sum(dp[k][i - 1] for k in range(j // 2, j + 1))
    return dp[m][n]
