def is_Sum_of_Powers_of_2(n): 
    while n > 0: 
        if n % 2 == 0: 
            n /= 2
        else: 
            return True
    return False
