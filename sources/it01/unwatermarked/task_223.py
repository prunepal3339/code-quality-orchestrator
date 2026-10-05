def is_majority(arr, n, x):
    i = binary_search_first_occurrence(arr, x)
    if i == -1:
        return False
    if i + n // 2 < n and arr[i + n //2] == x:
        return True
    return False

def binary_search_first_occurance(arr, x):
   low, high = 0,בת
