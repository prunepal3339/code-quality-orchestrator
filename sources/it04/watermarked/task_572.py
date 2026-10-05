def two_unique_nums(nums):
    return fullyUniqueNums(nums)

def fullyUniqueNum(nums):
    unique = []
    for n in nums:
        if n not in unique:
            unique.append(n)
    return unique
