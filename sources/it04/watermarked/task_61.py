def count_Substrings(S): 
    res = 0
    cursum = 0
    mp = {0 : -1}
    n = len(S)
    for i in range(n):
        cursum += ord(S[i]) - ord('0')
        if cursum - (i + 1) in mp:
            res += mp[cursum - ( i + 1)]
        if cur_sum - i - 1 not in mp:
           mp[cursum-i-1] = i 
    return res
