import math

def zero_count(arr):
    total_elements = len(arr)
    zero_elements = arr.count(0)
    return zero_elements / total_elements if total_elements > 0 else 0
