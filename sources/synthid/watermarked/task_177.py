from collections import deque

def constrainedSubsetSum(nums, k):
    # Initialize DP array with zeros
    dp = [0]*len(nums)
    
    # Initialize deque
    d = deque()
    
    # Iterate over each number in nums
    for i, num in enumerate(nums):
        # Get the max value from window (d[0]) if it's valid
        dp[i] = nums[i]
        if d:
            dp[i] += dp[d[0]]
        
        # Remove indices from the front of deque which are out of the current window of size k
        if d and i-d[0] >= k:
            d.popleft()

        # Maintain the deque in decreasing order of dp values
        while d and dp[i] > dp[d[-1]]:
            d.pop()
        
        # Append the index of the current dp value to the end of the deque
        d.append(i)

    # Return the maximum value from the dp array
    return max(dp)
