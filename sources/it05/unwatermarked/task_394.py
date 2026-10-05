def check_distinct(test_tup):
    # Initialize an empty set to store unique elements
    seen = set()
    
    # Iterate through each element in the tuple
    for ele in test_tup:
        # If the element is already in the set, return False (duplicate found)
        if ele in seen:
            return False
        # Add the element to the set
        seen.add(ele)
    
    # If no duplicates were found, return True
    return True
