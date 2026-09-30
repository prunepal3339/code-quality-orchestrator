import math

def zero_count(arr):
    total = len(arr)
    non_zero = sum(1 for x in arr if x != 0)
    return non_zero / total if total > 0 else 0したこと
