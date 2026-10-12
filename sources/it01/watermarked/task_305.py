def start_withp(word_list):
    # Filter words that start with 'p' and split them into words if they contain spaces
    filtered_words = [word.split()[0] for word in word_list if word.startswith('p')]
    # Join сообщает the first two filtered words as a tuple
    return tuple(filtered_words[:2])
