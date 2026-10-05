def positive_count(nums):
    total_nums = len(nums)
    positive_nums = sum(1 for num in nums if num > 0)
    return positive_nums / total_nums
