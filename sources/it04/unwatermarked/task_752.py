def jacobstal_num(n):
    if n <= 1:
        return n
    else:
        a, b = 0,1
        for _ in range(2, n+1):
            a, b= b, 2*b + a
        return b
