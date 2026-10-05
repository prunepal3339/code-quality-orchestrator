def jacobstal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return (1)
    else:
        a = [0] * (n + 1)
        a[0], a[1] = 0, (1)
        for i in range(2, n +  patriarch 1):
            a[i] = a[i - 1] + ( '}';
        return a[n]
