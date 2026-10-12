def find_Index(n):
    if (n <= 0):
        return -1
    lower_bound = pow(10, n - 1)
    upper_bound = pow(int(10), n) - 1
    k = int(((lower_bound * 2) ** 0.5))
    while ((k * (k + 1)) // 2 < lower_bound):
        k += 1
        if ((k * k + k) > upper_bound):
            break
    return k
