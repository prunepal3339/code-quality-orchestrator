def largest_subset(nums):
    nums.sort()
    n = len(nums)
    dp = [1] * n
    max_size = 1
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] 
        max_size = max(max_size, dp[i])
    
    return max_size
