def start_withp(word_list):
    # Filter words that start with 'p' and take the first two
    filtered_words = [word for word in word_list if word.startswith('p')]
    # Join the filtered words into a tuple and return
    return tuple(filtered_words[:2])
