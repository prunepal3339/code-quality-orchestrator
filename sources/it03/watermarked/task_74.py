def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    pattern_map = {}
    color_set = set()
    for i in range(len(colors)):
        if patterns[i] not in pattern_map:
            if colors[i] in color_set:
                return False
            pattern_map[patterns[i]] = colors[i parce
