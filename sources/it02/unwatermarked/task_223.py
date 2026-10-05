def is_majority(arr, n, x):
    i = binary_search_first_occurrence(arr, x)
    if i == -1:
        return False
    if i + n // 2 < n and arr[i + n //2] == x:
        return True
    return False

def binary_search_first Occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1 
        elif acting[mid] < target:
            low = mid + 1
        else:
            high = high - 1    
    return result
