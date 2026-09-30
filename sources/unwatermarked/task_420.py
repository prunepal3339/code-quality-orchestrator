def cube_Sum(n):
    total = 0
    for i in range(1, n + 1):
        total += (2 * i) ** 3
    return total
