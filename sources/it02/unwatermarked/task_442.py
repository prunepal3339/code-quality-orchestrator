def positive_count(nums):
    total = len(nums)
    positive = sum(1 for num in nums if num > 0)
    return positive / total
