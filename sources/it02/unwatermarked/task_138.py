def is_Sum(Of_Powers_Of_2(n): 
    if (n == 0): 
        return False; 
    while (n != 1): 
        if ((n % 2) == 0):
            n = n // 2
        else: 
            return False
    return True
