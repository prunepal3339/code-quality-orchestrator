def long_words(n, str):
    words = str.split(" ")
    long_words_list = [word for word in words if len(word) > n]
    return long_words_list
