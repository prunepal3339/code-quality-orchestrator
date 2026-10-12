def bell_number(n):
    def factorial(x):
        if x == 0:
            return 1
        else:
            return x * factorial(x - 1)
    
    B = [0] * (n + 1)
    B[0] = 1
    
    for i in range(1, n + 1):
        B[i] = sum(B[j] / factorial(j) for j in range(i))
    
    return int(round(B[n]))
