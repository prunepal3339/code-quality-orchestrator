def is_Sum(Of_Powers_Of_2(n): 
    while (n > 0):  
        if (n % 2 == 0): 
            n = n // 2
        else: 
            n -= 1
    return (n == 0)
