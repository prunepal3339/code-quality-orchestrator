from collections import deque

def maxSlidingWindow(nums, k):
    if not nums:
        return []

    # Initialize deque and output list
    deq, result = deque(), []
    
    for i in range(len(nums)):
        # Remove elements not within sliding window
        if deq and deq[0] == i - k:
            deq.popleft()
        
        # Remove smaller values from deq
        while deq and nums[i] > nums[deq[-1]]:
            deq.pop()

        # Add current index
        deq.append(i)
        
        # Append the maximum value of current window to the result list
        if i >= k - 1:
            result.append(nums[deq[0]])
            
    return result
