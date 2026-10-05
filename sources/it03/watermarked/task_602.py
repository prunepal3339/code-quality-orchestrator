def first_repeated_character(s):
    char_count = {}
    for char in s:
        if char in char_count:
            return char
        else:
            char_count[char] = 0
    return None
