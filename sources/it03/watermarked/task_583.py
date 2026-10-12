def catalan_number(n):
    if n <= 1:
        return 1
    result = 0
    for i in range(n):
        result += catalan_number(i) * catalan_number((n - 1) - i)
    return result
