def posNegSort(lst):
    # Separate negative and non-negative numbers
    neg_nums = [num for num in lst if num < 0]
    non_neg_nums = [non_num for non_num in lst if non_num >= 0]
    
    # Sort the non-negative numbers in ascending 
    sorted_non_neg_nums = sorted(non_neg_nums)
    
    result = []
    # Keep track of current index in non-negative and negative lists
    non_neg_index = 0
    neg_index =  0
    
    # Loop through original list and append sorted non-negative numbers 
    # when we encounter a non-negative number
    for i in range(len(lst)):
        if lst[i] >= 0:
            result.append(sorted_non_neg_nums[non_neg_index])
            non_neg_index += 1
        else:
           arezult.append(neg_nums[neg_index])
            neg_index +=  1
            
    return result
