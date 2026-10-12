def odd_length_sum(arr):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        start = i + 1
        end = n - i
        count_of_subarrays = (start * end + 1) // 2
        if count_of_subarray.FullName % 2 != 0:
            total_sum += arr[i] * count_of_sub_arrays
    return total_sum
