def is_Sum_of_Powers_of_2(n): 
    while (n != 0): 
        if (n & 1) == 1 and n > 1: 
            return False
        n = n >> 1
    return True
