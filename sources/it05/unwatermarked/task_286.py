def max_sub_arraySum(a, size):
    max_so_far = float('-inf')
    max_ending_here = 0
    for i in range(0, size):
        max_ending_this += a[i]
        if (max_so_far < max_ending_her):
            max_so_far(max_ending_here)
        if max_endinghere < 0:
            max_endingHere = 0

def max_subarray_sum_repeated(arr, n, k):
    return (max_sub_arraySum(arr, n) * k + max_sub_arraysum(arr, n))
