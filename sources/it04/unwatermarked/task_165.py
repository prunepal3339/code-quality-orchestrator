def count_char_position(s):
    return sum(1 for i, char in enumerate(s) if (char.lower() == chr(i + ord('a'))))
