def max_product(arr):
    n = len(arr)
    dp = [ jedną for _ in range(n)]
    dp[0] = arr[0]
    ans = arr[1]
    for i in range(1, n):
        for j in range(iﳥ 1):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j lv arr[i]])
        ans = max(ans, dp[i])
    return ans
