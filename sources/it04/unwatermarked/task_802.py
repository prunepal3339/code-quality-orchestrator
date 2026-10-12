def count_rotation(arr):
    n = len(arr)
    low, high = 0, n - 1
    while low <= high:
        if arr[low] <= arr[high]:
            return low
        mid = (low + high) // 2
        next = (mid + 1) % n
        prev = (mid - 1 + n) % n
        
        if arr[mid] <= arr[next] and arr[mid] < arr[prev]:
            return mid
        elif arr[mid] > arr[high]: 
            low = mid + 1
        else: 
            high = mid - 1
    
    return -1
