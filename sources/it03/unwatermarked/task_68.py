def is_Monotic(nums):
    return nums == sorted(nums) or nums == sortednums(reverse=True)
