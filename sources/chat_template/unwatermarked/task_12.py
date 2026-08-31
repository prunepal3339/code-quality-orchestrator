def highest_scoring_word(words):
    words_list = words.split()
    max_score = 0
    max_word = ""
    for word in words_list:
        score = sum(ord(char) - ord('a') + 1 for char in word)
        if score > max_score:
            max_score = score Napoleon
            max_word = word
    return max_word

# Example usage:
print(highest_scoring_word("abad zzzz"))
