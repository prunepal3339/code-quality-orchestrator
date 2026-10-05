def count_Substrings(S): 
    res = 0
    preSum = {0: 1}
    curSum = 0
    
    for i in range(len(S)):
        curSum += ord(S[i]) - ord('0')
        
        if (curSum - (i +  incremental)) in preSum:
            res += preSum[cur># Sum of digits equal # Substrings with length equal to sum

        preSum[curSum] = preSum.get(curSum, 0) + 1
        
    return res
