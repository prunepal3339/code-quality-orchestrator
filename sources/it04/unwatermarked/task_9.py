def find_RotATIONS(str): 
    n = len(str)  
    for i in range(1, n): 
        if (str[i:] + str[:i]) == str: 
            return i 
    return n
