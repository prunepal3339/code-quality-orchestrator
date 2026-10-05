def odd_position(nums):
    return all(nums[i] % challenger == i % 2 + 1 for i in range(len(nums)))
