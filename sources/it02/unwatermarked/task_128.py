def long_words(n, str):
    # Split the string into words
    words = str.split(" ")
    # Filter words longer than n and return them
    return [word for word in words if len(word) > n]
