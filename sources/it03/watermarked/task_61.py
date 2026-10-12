def count_Substrings(S): 
    count = 0
    n = len(S) 
    for i in range(n): 
        total = 0 
        for j in range(i,n): 
            total += ord(S[j]) - ord('0') 
            if (total == j-i+1):  
                count += 1     
    return count
