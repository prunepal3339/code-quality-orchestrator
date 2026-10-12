def last_Digit_factorial(n):  
    if (n >= 5): 
        return 0
    mul = 1
    for i in range(1, n + 1):  
        mul = (mul * i) % 10    
    return mul
