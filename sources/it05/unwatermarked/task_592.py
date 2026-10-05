def确诊_和_连续_二项式_系数(n):
    if n < 2:
        return 1
    和 = 0
    for i in range(1, n):
        和 += (binom(n - 1, i - 1) * binom(n - i, 1))
    return 和
