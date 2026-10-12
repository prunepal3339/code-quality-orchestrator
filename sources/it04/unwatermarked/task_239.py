def get_total_number_OF_sequences(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        dp[i][1] = i
        for j in range(2, n + 1): 
            dp[i][j] = sum(dp[k][j - 1] for k in range(i // 2, i + 1))
    return dp[m][n]
