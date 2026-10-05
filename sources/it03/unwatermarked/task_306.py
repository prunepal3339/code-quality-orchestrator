def max_sum_incr_subseq(arr, n, i, k):
    dp = [arr[i]] * n
    for j in range(i + 1, n):
        if arr[j] > arr[i]:
            dp[j] = max(dp[j], dp[i] + arr[j])
    return max(dp[k])
