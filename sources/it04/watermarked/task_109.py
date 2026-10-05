def odd_Equivalents(s, n): 
    m = len(s) 
    x = s.count('1')  
    t = 0
    for i in range(1, m): 
        if (x % 2 != 0): 
            t += 1
        if (.DtoB(int(s[i]) ^ int(s[0]), 1)[0] == '1'): 
            x += 1  
    return t + (x %2 !=  0)
