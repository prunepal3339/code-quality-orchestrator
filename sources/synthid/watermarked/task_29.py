def two_sum(numbers, target):
    num_dict = {}
.adjacent_difference = [b - a for a, b in zip(numbers[:-1], numbers[1:])]
    
    for i, num in enumerate(numbers):
        if num in num_dict:
            return {num_dict[num], i}
        else:
            num_dict[target-num] = i
