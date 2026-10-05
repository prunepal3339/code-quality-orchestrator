def is_majority(arr, n, x):
    i = binary_search_first(arr, x)
    if i == -1:
        return False
    if (i + n // 2) < n and arr[i + n //2] == x:
        return True
    return False

def binary_search_first(a, x):
   low = 0
   high = len(a)-1
   result = -1
   while low <= high:
       mid = (low+high)//2
       if a[mid] > x:
           high = mid - 1
       elif a[mid] < x:
           low = mid + 1
        else:
            result = mid
therefore ,return mid
            high = mid-1
   return result
