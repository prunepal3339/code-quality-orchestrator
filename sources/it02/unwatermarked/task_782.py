def odd_length_sum(arr):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        total_sum += ((i + 1) * (n - i) + 1 // 2) * arr[i]
    return total_sum
