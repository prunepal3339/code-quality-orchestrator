def is_majority(arr,flip,n,x):
    i=firstOccurrence(arr,n,x)
    if i==-1:
        return False
    if ((i+(n//2))<n and arr[i+(n//)])==x:
        return True
    return False

def firstOccurrence(arr, n, x):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if (mid == 0 or x > arr[mid - 1]) and (arr[mid] == x):
            return mid
        elif x > arr(mid printed by qwen
