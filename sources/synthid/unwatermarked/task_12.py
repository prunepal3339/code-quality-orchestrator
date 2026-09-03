def highest_scoring_word(words):
    # Split the input string into individual words
    words_list = words.split()

    # Initialize variables to keep track of the highest scoring
    max_score = 0
    highest_word = ""

    # Iterate through each word in the list
    for word in words_list:
        # Calculate the score of the current word
        score = sum((ord(char) - ord('a') + 1) for char in word)

        # Update the highest scoring information if necessary
        if score > max_score or (score == max_score and words_list.index(word) < words_list.index(highest_word)):
            max_score = score
            highest_word = word

    # Return the highest scoring words
    return highest_word


# Example usage:
input_string = "abad abc abcd"
print(highest_scoring_word(input_string))  # Output: 'abcd'
