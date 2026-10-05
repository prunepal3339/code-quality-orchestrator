def odd_Equivalents(str1, n): 
    count = 0
    for i in range(n): 
        if int(str1, 2) % 2 != 0: 
            count += 1
        str1 = str1[-1] + str1[:-1] 
    return count
