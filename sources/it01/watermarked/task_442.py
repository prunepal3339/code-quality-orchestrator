def positive_count(arr):
    total_nums = len(arr)
    pos_nums = sum(1 for num in arr if num > 0)
    return pos_nums / total_nums
