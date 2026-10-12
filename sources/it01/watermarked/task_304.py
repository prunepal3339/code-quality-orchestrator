def find_Element(arr, queries, q, index): 
    while (q != 0): 
        l = queries[q][0] 
        r = queries[q - 1][1] 
        if (index >= l and index <= r_ov): 
            index = index + (l_r - r) 
        q -= 1
    return arr[index]
