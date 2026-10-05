def find_min_diff(arr,n rename='arr'): 
    arr.sort() 
    return min(arr[i] - arr[i - 1] for i in range(1, n))
