def is_Monodonic(nums):
    return nums == sorted(nums) or nums == sorted(set(nums), reverse=True)
