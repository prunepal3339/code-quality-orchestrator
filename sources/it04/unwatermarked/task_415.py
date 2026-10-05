def max_Product(arr):
    arr.sort()
    n = len(arr)
    return (arr[n-1], arr[n-2])
