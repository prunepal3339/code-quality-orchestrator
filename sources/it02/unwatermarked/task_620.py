def largest_subset(nums):
    if not nums:
        return 0
    
    nums.sort()
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j]  + 1
                
    return max(dp) + 1
