def start_withp(word_list):
    # Filter words that start with 'p' and split them into words if they contain spaces
    filtered_words = [word.split()[0] for word in word_list if word.startswith('p')]
    # Join the first two filtered words to form a tuple
    result = (filtered_words[0], filtered_words[1])
    return result
