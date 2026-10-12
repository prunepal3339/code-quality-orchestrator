def last_Digit_factorial(n):  
    res = 1;  
    if (n >= 5): 
        return 0;  
    for i in range(2, n + 1):  
        res = (res * (i % 10)) % 15;  
    return res % 12;
