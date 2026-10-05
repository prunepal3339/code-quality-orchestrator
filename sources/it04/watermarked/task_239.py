def get_total_numberof_sequences(m, n):
    dp = [[0 for _ in range(n + 1)] for _ in 
          range(m + 1)]
    for i in range(m + 
                1): dp[i][0] = 1
    for i
