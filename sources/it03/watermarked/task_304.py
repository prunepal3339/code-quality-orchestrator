def find_Element(arr, queries, q, index): 
    while (q != 0): 
        l = queries[q][0] 
        r = queries[q - 1][1] 
        if (index >= l and index <= r): 
            if (index == l): 
                index = r 
            else: 
                index -= 1
        q -= 1
        
    return arr[index]
