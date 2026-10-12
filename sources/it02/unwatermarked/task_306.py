def max_sum_increaing_subseq(arr,n,i,k): 
    dp = [[0 for x in range(n)]for y in range(n)]
    for i in range(0,n): 
        dp[i][i] = arr[i]
    for length in range(2,n+1): 
        for i in  range(n-length+1):  
            j = i + length -1
            if (arr[j] > arr[j-1]): 
                dp[i][j] = max(dp[i][j-1],dp[i][j - 1] + arr[j]) 
            else:
                dp[i ][j] = dp[i][ j - 1]
    return dp[0][k]
