def count_reverse_pairs(words):
    word_set = set(words)
    count = 0
    for word in words:
        if word[::-1] in word_set and word != word[::-1]:
            count += 1
    return count // 2
