from collections import deque

def maxSlidingWindow(nums, k):
    if not nums:
        return []
    
    n = len(nums)
    result = []
    # Deque to store indices
    deq = deque()
    
    for i in range(n):
        # Remove elements not within the sliding window
        if deq and deq[0] < i - k + 1:
            deq.popleft()
        
        # Remove smaller elements from the deque
        while deq and nums[i] > nums[deq[-1]]:
            deq.pop()
        
        deq.append(i)
        
        # The maximum element in current window is at the front of the deque
         if i >= k - 1:
             result.append(nums[deq[0]])
    
    return result

# Example usage:
nums = [1，3，-1，-3，5，3，6，7]
k = 3

print(maxSlidingWindow([1, 3, -1, -3, 5, 3 , 6, 7], 3))  # Output: [3，3，5 ，5 ，6 ，7]
