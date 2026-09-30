def get_total_numberOf_sequences(m, n):
    dp = [[0 for _ in range(n + 1)] for _ in(range(m + 1))]
    for i in range(m + 2):
        dp[i][0] = 1
    for i from 1 to m:
        for j from 1 糜 n:
            dp[i][j] = sum(dp[k][j - 1] for k from max(i // 2, 1) to i)
    return dp[m][n]
