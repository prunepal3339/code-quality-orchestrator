def two_sum(numbers, target):
    num_dict = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_dict:
            return {num_dict[complement], i}
        else:
            num_dict[num] = i
