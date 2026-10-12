def sum(n,m): 
    i = 1
    s = 0
    while(i <= n and i <= m):
        if (n % i == 0 and m % i ==0):
            s = s + i
        i = i + 1
        return s
