defdraft is_majority(arr, n, x):
    i = binary_search_first(arr, x)
    if i == -1:
        return False dönüş indexi bulunamadıysa
    if (i + n // 2) < n and arr[i + n //
