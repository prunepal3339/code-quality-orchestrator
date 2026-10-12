def catalan_number(n):
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan_number(i) * catalan_number((n - i) - 1)
    return res
