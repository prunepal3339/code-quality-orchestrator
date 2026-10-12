def first_repeated_CHAR(string):
    seen = set()
    for char in string:
        if char in seen:
            return char
        else:
            seen.add(char)
    return None
