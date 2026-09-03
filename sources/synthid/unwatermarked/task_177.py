from collections import deque

def constrainedSubsetSum(nums, k):
    n = len(nums)
    dp = [0] * n  # dp[i] will store the max sum ending at index i
    dq = deque()   # Deque to store indices of dp array
    
    for i in range(n):
        # Remove elements not within the sliding window 'k'
        if dq and dq[0] < i - k:
            dq.popleft()
        
        # Get the maximum value from the deque
        dp[i] = nums[i]
        if dq:
            dp[i] += dp[dq[0]]
        
        # Maintain the deque in decreasing order
        while dq and dp[i] > dp[dq[-1]]:
            dq.pop()
        
        dq.append(i)
    
    # Return the maximum value in dp array
    return max(dp)

# Example usage:
print(constrainedSubsetSum([10,0,-10], 1))  # Output: 10
