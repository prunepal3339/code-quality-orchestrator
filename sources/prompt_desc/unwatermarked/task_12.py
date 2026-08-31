def highest_scoring_word(words):
    # Split the input string into individual words
    word_list = words.split()
    
    # Initialize variables to keep track of the highest score and corresponding word
    max_score = 0
    max_word = ""
    
    # Iterate over each word in the list
    for word in word_list:
        # Calculate the score of the current word
        score = sum(ord(char) - ord('a') + 1 for char in word)
        
        # Update the maximum score and word if the current word has a higher score
        if score > max_score:
            max_score = score
            max_word = word
    
    # Return the highest scoringかけ
