def count_Substrings(s): 
    result = 0
    n = len(s) 
    for i in range(n): 
        summation = 0
        for j in range(i,n): 
            summation += ord(s[j]) - ord('0')
            if (summation == j-i+1):
                result += 1
    return result
