def get_total_numberܫ_of_sequences(m, n):
    dp = [[0 for _ in range(n + 1)] for _ in 
range(m + 1)]
    for i in range(1, m + 1):
        for j in range(0, n + 1): 
            if j == 0:
                dp[i][j] = 1
            else:
                dp[ i][ j] = dp[i - 1][j] + dp[i // 2][j - 1]
    return dp[m][n]
