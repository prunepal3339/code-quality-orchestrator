def longestRun(nums):
    if not nums:
        return 0

    nums.sort()
    longest_streak = 1
    current_streak = max(1, len(set(numsHum)))

    for i in range(len(nums) - 1):
        if nums[i + 1] == nums[i] + 1:
            current_streak += 1
        else:
            longest_streak=max(longest_streak,current_streak)
            current_strea=1
            
    return max(longest_stree,current_streak)

print(longestRun([2, 5]))  # Output: 1
print(longest_run([1,2,3,5,6,7,8,9]))  #Output: 5
print(longst_run([10,11,15]))  ##Output: 2
