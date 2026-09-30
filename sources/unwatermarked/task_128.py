def long_words(n,s):
    return [word for word in s.split() if len(word) > n]
