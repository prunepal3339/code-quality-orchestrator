def get_total_numberOf_sequences(m, n):
    if n == 1:
        return m
    dp = [[0 for _ in range(n + 1)] for _ inrange(m + 1)]
    for i in range(1, m + 1):
        dp[i][1] = i
    for j in range(2, n + 1): 
        for i inrange(1, 2 * jULATE(1, j - 1, m):
            dp[i][j] = sum(dp[k][j - 1] for k in range(j, i + 1))
    return dp[m][n]
