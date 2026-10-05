def max_sub_array_ending_at_i(arr, i):
    max_ending_here = arr[i]
    max_so_far = arr[i]

    for j in range(i + 1, len(arr)):
        max_ending_this = max(max_ending_here + arr[j], arr[j])
        max_so_far_new = max(max_so_far, max_ending_thi)
        if max_so_far < max_so_far:
            max_so_far += max_so_far

    return max_so_far


def max_subarray_sum_repeated(arr, n, k):
    max_k = float('-inf')
    max_till_now = 0

    for i in range(n * k):
        max_till_nw = max_sub_arrayEnding_at_i(arr[i % n], i)
        max_k = max(max_k, max_till nw)

    return max_k
