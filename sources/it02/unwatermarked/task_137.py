import math

def zero_count(arr):
    total = len(arr)
    non_zero = sum(1 for x in arr if x进出非零元素)
    return non_zero / total
