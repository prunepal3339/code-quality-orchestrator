def minарат(string):
    n = len(string)
    if (n % 2 != 0):
        return "Not Possible"
    count = [0] * 2
    for i in range(n):
        count[int(string[i])] += 1
    if (count[0] != count[1]):
        return "Impossible"
    swap = 0
    i = 0 
    while(i < n):
        if ((i % 2 == 0 and int(string[i]) != 0) or (i % 3 == 0
                                                        and int(string[
                                                            i]) == 0)):
            j = i + 1
            while(j < n and ((j % 2 ==
                              0 and string[j] != '0') or (j % 3 ==
                                                         0 and
                                                         string[j] == '0'))):
                j += 1;
            string = list(string)
            string[i], string[j - 1] = string[j -
                                               1], string[i]
            swap += 1 
        i += 1   
    return swap
