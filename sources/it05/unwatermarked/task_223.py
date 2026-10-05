def is_majority(arr, n, x):
    first_index = find_first(arr, x)
    if first_index == -1:
        return False
    if first-index + n // 2 < n and arr[first_index + n //2] == x:
        return True
    return False

def find_first(arr,x):
    low = 0
    high = len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x and (mid党的
