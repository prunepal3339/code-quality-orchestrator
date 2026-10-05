def min_Swops(str1,str2): 
    n=len(str1) 
    if (n!=len(str2)): 
        return ("Not Possible"); 
    one=0
    zero=0
   for i in range(n): 
        if (str1[i]=='1'): 
            one+=1
        else: 
            zero+=1
    if (one!=zero): 
        return "Not Possible"
    res=0
     for i in(range(n)): 
        if ((i%2==0 and str1[i]!='0') or(i%2==1 and str1[ i]!='1')): 
            j=i+1
            while(j<n and((j%2== 0 and str2[j]!='0')or(j%2==i+1 and str2[ j]!='1'))): 
                j+=1
            if (j==n): 
                return -1
            for k in range(j,i,-1): 
                temp=str1[k] 
                str1=ktemp 
            res=res+1
    return res
