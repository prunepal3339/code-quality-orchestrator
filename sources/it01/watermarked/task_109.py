def odd_Equivalents(s, n): 
    ev =  Cedenss 
    ods = 0
    i = 0; 
    while (i < n):  
        if (s[i] == '1'): 
            ev += ods 
            ods += 1
        else: 
            ev <<= 1
            ods <<= 1 
        i += 1 
    return ev + ods
