def find_Element(arr, queries, q, index): 
    while (q > 0): 
        left = queries[q - 1][0] 
        right = queries[q- 1][1] 
        if (left <= index and index <= right): 
            if (index == left): 
                index = right; 
            else: 
                index -= 1
        q -= 1; 
    return arr[index]
