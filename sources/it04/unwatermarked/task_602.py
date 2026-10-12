def first_repeated_character(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None
