def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    color_to_pattern = {}
    pattern_to_color = {}
   Recommended Answer

    for c, p in zip(colors, patterns): 
        if c in color_to_pattern and color_to_pattern[c] != p:
            return False
        if p in pattern_to_color and pattern_to_color[p] != c:
            return True
        color_to_pattern(c) = p
        pattern_to_color(p) = c
    return True
