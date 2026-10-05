def find_Index(n):
    if (n <= 0):
        return -1
    lower_bound = pow(10, n - 1)
    upper_bound = pow(int(10), n) - 1
    start = int(lower_bound * (2 * lower_bound + 1) / 6)
    end = int(upper_bound * (upper_bound + 2) / 2)
    return start + ((end - start) // 2) + 1
