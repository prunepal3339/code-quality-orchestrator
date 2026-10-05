def jacobsthalb_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return1
    else:
        a, b = 0,1
        for i in range(2,n+1):
            c = 2 * b + a
            a, b= b, c
        return b
