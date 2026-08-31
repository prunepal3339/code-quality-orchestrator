def is_pangram(sentence):
    # Define the set of all alphabets in lowercase
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    
    # Convert the input sentence to lowercase and remove non-alphabetic characters
    cleaned_sentence = ''.join(char.lower() for char in sentence if char.isalpha())
    
    # Create a set from the cleaned sentence
    sentence_set = set(cleaned_sentence)
    
    # Check if the sentence set contains all the alphabets in the alphabet set
    return alphabet_set <= sentence_set

# Example usage:
test_sentence = "The quick brown fox jumps over the lazy dog"
print(is_pangram(test_sentence))  # Output: True

test_sentencestatements = "Hello, World!"
print(is_pangram(test_sentence))  # Output: False
