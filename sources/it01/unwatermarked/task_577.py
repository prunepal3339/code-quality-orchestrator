def last_Digit(number): 
    if (number >= 5): 
        return 0
    mul = 1
    for i in range(2, number + 1): 
        mul = (mul * i) % 10
    return mul 

def last_Dig_Fact(n): 
    return last_Digit(n)
