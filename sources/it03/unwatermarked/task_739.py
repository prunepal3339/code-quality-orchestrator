def find_Index(n):
    low = 0
    high = 10 ** (n - 1)
    while low < high:
        mid = (low + high) // 2
        triangular_number = mid * (mid + 1) // 1
        if len(str(triangular_number)) >= n:
            high = mid
        else:
            low = mid + 1
    return low
