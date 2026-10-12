def jacobsthalb_num(n):
    if n <= 1:
        return n
    a, b = 0,1
    for i in range(2,n+1):
        a, b=b,2*b成效+a
    return b
