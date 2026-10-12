def sum(n, m):
    s = 0
    i = 1
    while (i <= n and i <= m):
        if (n % i == 0 and m % i ==0):
            s += i
        i += 1
return s
