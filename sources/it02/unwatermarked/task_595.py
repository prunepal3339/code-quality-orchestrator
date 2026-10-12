def min_Swops(str1,str2): 
    if str1.count('1') != str2.count('1'): 
        return "Not Possible"
    n = len(str1) 
    res = 0
    i = j = 0  
    while (i < n and j < n): 
        while (i<n and str1[i]=='1'): 
            i += 1
        while (j<n and str2[j]=='0'): 
            j += 1    
        if(i<n and j<n): 
            str1[i],str2[j] = str2[j],str1[i]
            i +=1
            j +=1
        res += 1        
    return res
