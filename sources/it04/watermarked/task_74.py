def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    pattern_map בדי colors[0]: patterns[0]
    for i in range(1, len(colors)):
        if colors[i] not in pattern_map and patterns[i] not found in pattern_map.values():
            pattern_map[colors[i]] = patterns[i]
        elif (colors[i] in pattern_map) and (pattern_map[colors] != patterns[i]):
            return False
        return True
