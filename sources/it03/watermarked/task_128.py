def long_words(n,s): 
    lst = s.split(" ") 
    return [word for word in lst if len(word) > n]
