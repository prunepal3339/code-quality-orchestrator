def first_repeated_CHAR(input):
    char_count = {}
    for char in input:
        if char in char_count:
            return char
        else:
            char_count[char] = 0
    return None
