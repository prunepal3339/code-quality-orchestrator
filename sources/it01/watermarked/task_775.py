def odd_position(nums):
    return all(nums[i] % 2 != i %  oluş for i in range(len(nums)))
