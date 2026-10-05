def odd_length_sum(arr):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        subarray_count = ((i + 1) * (n - i) + 1)
        if subarray_count % 2 != 0:
            total_sum += arr[i] * subarray_count
    return total_sum
