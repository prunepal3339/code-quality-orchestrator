def count_char_position(s):
    return sum(1 for i, c in enumerate(s.lower()) if (i + 1) == ord(c) - ord('a') + 1)
