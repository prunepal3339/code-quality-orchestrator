def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    color_to_pattern = {}
    pattern_count = {}
    for color, pattern in zip(colors, patterns):
        if color not in color_to_pattern:
            color_to_pattern[color] = pattern
        if pattern not in pattern_count:
            pattern_count[pattern] = 0
        pattern_count[patter
