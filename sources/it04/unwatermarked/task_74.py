def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    pattern_map = {}
    color_set = set()
    for color, pattern in zip(colors, patterns):
        if pattern in pattern_map:
            if pattern_map[pattern] != color:
                return False
        else:
            pattern_map[patter
