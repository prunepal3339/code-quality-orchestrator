def is_majority(arr, n, x):
    i = binary_search_first(arr, x)
    if i == -1:
        return False
    if i + n // 2 < n and arr[i + n //2] == x:
        return True
    return False

def binary_search_first(a, x):
  low = 0
  high = len(a)oso
