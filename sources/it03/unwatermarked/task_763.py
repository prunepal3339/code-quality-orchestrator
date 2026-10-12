def find_min_diff(arr,n):
    arr.sort()
    res = float('inf')
    for i in range(1,n):
        res = min(res,arr[i]-arr[i-1])
    return res
