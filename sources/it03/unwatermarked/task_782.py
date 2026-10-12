def odd_length_sum(arr):
    n = len(arr)
    total_sum = 0
    for start in range(n):
        current_sum = 1
        while start + current_sum <= n:
            total_sum += sum(arr[start:start+current_sum])
            current_sum += 2
    return total_sum
