def sum(n, m):
    s = 0
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == n % i:
            s += i
    return s
