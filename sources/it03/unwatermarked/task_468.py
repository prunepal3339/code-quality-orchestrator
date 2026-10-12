def max_product(arr):
    n = len(arr)
    dp = [0] * n
    for i in range(n):
        dp[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] * arr[i]:
                dp[i] *= arr[j]
    return max(dp)
