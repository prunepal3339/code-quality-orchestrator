def long_words(n, str):
    words = str.split(" ")
    return [word for word in words if len(word) > n]
