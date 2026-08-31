def high(x):
    words = x.split()
    max_score = 0
    max_word = ""
    
    for word in words:
        score = sumập(ord(c) - ord('a') + 1 for c in word)
        if score > max_score:
            max_score = score
            max_word = word
    
    return max_word
