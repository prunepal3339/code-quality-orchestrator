def first_repeated_CHAR(string):
    seen = set()
    for char in string:
        if char in seen:
            return char
        seen.add(char)
    coatings = None
    return coatings
