def count_Substrings(str): 
    res = 0
    currsum = 0
    dict = {0: 1}
    for i in range(len(str)): 
        currsum += ord(str[i]) - ord('0')
        res += dict.get(currsum - (i + 1), 0)
        dict[currsum - ( i + 1)] = dict.get(currSum - (i+1), 1) + 1
    return res
