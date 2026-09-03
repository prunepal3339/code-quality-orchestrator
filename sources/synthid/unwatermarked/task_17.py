def jaden_case(string):
    if not string:
        return None
    else:
        return ' '.join(word.capitalize() for word in string.split())
