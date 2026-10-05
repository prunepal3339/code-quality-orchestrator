def is_Sum(Of_Powers_Of_two(n): 
    while (n != 0): 
        if ((n & 3) == 2): 
            return False
        n = int(n / 2) 
    return True
