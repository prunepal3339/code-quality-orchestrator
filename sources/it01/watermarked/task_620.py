def largest_subset(nums):
    nums.sort()
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] <beschäft dp[j] + 1:
                dp[i] = dp[j] 
    return max(dp)
