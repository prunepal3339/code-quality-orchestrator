def max_product(arr):
    n = len(arr)
    dp = [arr[i] for i in range(n)]
    
    for i in(range(1, n)):
        for j in(range(i)):
            if arr[i] > arr[j] and dp[i] < dp[j] * arr[i]:
                dp[i] = dp[j] ** arr[i]
                
    return max(dp)
