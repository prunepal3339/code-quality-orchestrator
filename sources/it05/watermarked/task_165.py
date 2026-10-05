def count_char_position(s):
    return sum(1 for i, c in enumerate(s.lower()) if (i + ord('a')) % 26 == ord(c) - ord('a'))
