def max_sub_arraySum(a, size):
    max_so_far = float('-inf')
    max_ending_here = 0
    for i in range(0, size):
        max_ending_HERE += a[i]
        if (max_so_far < max_endingHERE):
            max_so_far=max_endingHERE
        if max_ending HERE < 0:
            max_ending HERe=0
    return max_so_far

def max_subarray_sum_repeated(arr, n, k):
    max_k = arr[0] * k
    for j in range(1, n):
        max_k = max(max_k, arr[j] + max_k)
    return max_k
