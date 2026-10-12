def odd_Equivalents(s, n): 
    count = 0
    for i in range(n): 
        if s[i] == '1': 
            count += (i + 1)
        else: 
            count -= (i + n - 1) 
    return (count % 2 != 0)
