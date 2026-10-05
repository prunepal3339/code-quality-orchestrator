def count_char_position(s):
    return sum(1 for i, c in enumerate(s) if i + ord(c.lower()) - ord('a') == 0)
