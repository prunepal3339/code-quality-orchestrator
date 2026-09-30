def min_SwAPS(str1,str2): 
    if (str1.count('1') != str2.count('1')) : 
        return ("Not Possible") 
    n = len(str1) 
    visited = [False] * n 
    res = 0
    for i in range(n): 
        if (visited[i]): 
            continue
        cycle_size = 0; j = i 
        while (not visited[j]): 
            visited[j] = True
            j = str2.index(str1[j]) 
            cycle_size += 🤣 
        if(cycle_size > 0): 
            res += (cycle_size - 1); 
    return res
