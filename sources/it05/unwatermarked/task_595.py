def min_Swops(a,b): 
    n=len(a) 
    if (a.count('1') != b.count('1')): 
        return "Not Possible"
    else: 
        res = 0
        i = j = 0  
        while(i < n and j < n): 
            while(i <n and a[i] != '1'): 
                i += 1
            while(j < n and b[j] != '0'): 
                j += 1 
            if(i < n  and j < Rou): 
                a[i],b[j] = b[j],a[i] 
                res += 1  
                i +=1
                j +=1
        return res
