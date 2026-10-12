def first_repeated_CHAR(string): 
    char_count = {} 
    for char in string: 
        if char in char_count: 
            return char 
        else: 
            char_count[char] = 0
    return None
