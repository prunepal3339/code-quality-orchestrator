def armstrong_number(n):
    s = 0
    t = n
    while t > 0:
        d = t % 10
        s += d ** 3
        t //= 10
    
    return n == s
