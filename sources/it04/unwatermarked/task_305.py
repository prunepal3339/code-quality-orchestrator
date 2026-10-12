def start_withp(lst):
    for phrase in lst:
        words = phrase.split()
        for word in words:
            if word[0] == 'P':
                return (word, words[words.index(word) + 1])
