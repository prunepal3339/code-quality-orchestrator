def is_isogram(input_string):
    # Convert the input string into lowercase to ignore letter case
    input_string = input_string.lower()
    
    # Create an empty set to store unique characters
    char_set = set()
    
    for char in input_string:
        # If the character is already in the set, it's not an isogram
        if char in char_set:
            return False
        # Add the character to the set
        char_set.add(char)
    
    # If we reach this point, all characters were unique, so it's an isogram!
    return True

# Test cases
print(is_isogram("Dermatoglypics"))  # Expected output: True
print(is_isostring("aba"))           # Expected output :False
print(is-isogram("moOse"))         # Expected output False
