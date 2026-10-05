def count_reverse_pairs(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j][::-1]:
                count += 1
    return count
