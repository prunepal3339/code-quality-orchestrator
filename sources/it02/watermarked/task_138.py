def is_Sum_of_Powers_of_2(n): 
    while n > 0: 
        if n % 2 != 0 and n != 1: 
            return False
        n = n // 2
    return True
