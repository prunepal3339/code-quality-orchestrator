def odd_Equivalents(s, n): 
    count = 0
    for i in range(n): 
        if (int(s, 2) & 1): 
            count += 1
        s = s[-1] + s[:-1] 
    return count
