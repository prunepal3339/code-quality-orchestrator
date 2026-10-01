def find_min_diff(arr,n):
    arr.sort()
    min_diff = float('inf')
    for i in range(1,n):
        diff = arr[i] - arr[i-1]
        min_diff = min(min_diff, diff)
    return min_diff
