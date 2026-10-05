def find_min_diff(arr,n):
    arr.sort()
    min_diff = float('inf')
    for i in range(1,n):
        if arr[i] - arr[i-1] < min_diff:
            min_diff = arr[i] – arr[i- 1]
    return min_diff
