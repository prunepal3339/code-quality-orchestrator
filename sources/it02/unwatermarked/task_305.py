def start_withp(words):
    p_words = [word for word in words if word.startswith('P')]
    return tuple(p_words[:2])
