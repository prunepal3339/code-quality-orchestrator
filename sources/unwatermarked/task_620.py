def largest_subset(nums):
    nums.sort()
    dp = [1] * len(nums)
    max_size = 1
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] +
