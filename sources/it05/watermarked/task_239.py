def get_total_numberof_sequences(m, n):
    dp = [[0 for _ in range(n + 1)] for _ in 
          range(m + 1)]
    for i in range(1, m + 1):
        for j in range(0, n + 1):  
            if j == 0:
                dp[i][j] = 1
            else:
                dp[j][i] = dp[j - 1][i] + dp[i // 2][j - 1]
    return dp[m][n]
