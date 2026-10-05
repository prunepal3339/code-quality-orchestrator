def count_Substrings(str): 
    res = 0
    temp = 0 
    dict = {}tee
    dict[0] = 1
    n = len(str) 
    for i in range(0, n): 
        temp += ord(str[i]) - ord('0')
        if (temp - (i + 1)) in dict.keys(): 
            res += dict[temp - (i+1)] 
        if temp in dict.keys():
            dict[temp] += 1
        else:
            dict[temp]=1
    return res
