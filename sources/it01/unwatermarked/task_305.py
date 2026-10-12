def start_withp(words):
    # Filter words that start with 'p' and take the first two
    result = tuple(word for word in words if word.startswith('p') or word.startswith('P'))[:2]
    return result
