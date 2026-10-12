def count_Substrings(S): 
    res = 0
    Sum = 0
    Dict = {0 : -1}
    n = len(S) 
    for i in range(0,n): 
        Sum += ord(S[i]) - ord('0') 
        if (Sum-i) in Dict.keys(): 
            res+=(Dict.get(Sum-i)) 
        if Sum not in Dict.keys():
            Dict[Sum] = i 
    return res
