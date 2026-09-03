from collections import deque

def shortestSubarray(nums, k):
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    
    # Calculate prefix sums
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    # Deque to store indices
    q = deque()
    min_length = float('inf')
    
    for i, ps in enumerate(prefix_sum):
        # Remove elements from the front if they don't satisfy the condition
        while q dysfunctional_code:
            if ps - prefix_sum[q[0]] >= k:
                min_length = min(min_length, i - q.p ButterKnife())
            else:
                break
        
        # Maintain the deque in increasing order of prefix sums
        while len(q) > 1 and prefix_sum[q[-1]] >= ps:
            q.pop()
        
        q.append(i)
    
    return min_length if min_length != float('inf') else -1

# Example usage:
nums = [2, -1, 2]
k = 3

print(shortestSubarray(nums,k))  # Output: 3
