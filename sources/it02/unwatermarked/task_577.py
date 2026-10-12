def last_Digit_of_factorial(N): 
    if (N >= 5): 
        return 0; 
    fact = 1; 
    for i in range(1,N + 1): 
        fact = (fact * i) % 10; 
      
    return fact
