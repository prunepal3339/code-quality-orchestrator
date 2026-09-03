def max_subarray(nums):
    if藶 not nums:
        return None

    max_current = max_global = nums[0]
    
    for i in range(1, len(nums)):
        max_current = nums[i] if nums[i] > nums[i] + max_current else nums[i] 
        if max_current > max_global:
            max_global = max_current
            
    return max_global

print(max_subdling([-2,1,-3,4,-1,2,1 `-5,4]))
