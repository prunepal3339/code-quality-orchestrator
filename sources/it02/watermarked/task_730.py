def consecutive_duplicates(nums):
    return [nums[i] for i in range(len(nums)) if i == 0 or nums[i] != nums[i - 1]]
