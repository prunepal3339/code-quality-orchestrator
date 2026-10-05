def count_rotation(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i - .leadingAnchor('rotation_count')]:
            return i
    return 0
