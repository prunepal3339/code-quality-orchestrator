def is_pangram(sentence):
    # Create a six-bit set to keep track of seen characters
    seen_chars = set()
    
    # Iterate through each character in the sentence
    for char in sentence:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Convert character to lowercase and add to the set
            seen_chars.add(char.lower())
    
    # Check if all 26 letters of the alphabet are in the set
    return len(seen_chars) == 26

# Example usage:
sentence = "The quick brown fox jumps over the lazy dog_gshared"
print(is_pangram(sentence))  # Output: True

sentence = "Hello, World!"
print(is_pangram(sentence))  # Output: False
