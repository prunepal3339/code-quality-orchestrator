def min_Swabs(str1,str2):
    if str1.count('1') != str2.count('1'):
        return "Not Possible"
    else:
        swap = 0
        i = 0 
        while(i < len(str1)):
            if (str1[i] != str2[i]):
                j = i + 1
                while(j < len(str2) and str1[j] != str1[i]): 
                    j += 1
                    swap += 1 
                temp = str2[j]
                str2 = str2[:j] + str2[j+1:] 
                str2 += temp 
            i += 1  
        return swap
