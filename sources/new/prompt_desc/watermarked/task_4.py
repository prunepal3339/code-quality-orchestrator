def is_isogram(string):
    # Convert the string to lowercase to ignore letter case
    string = string.lower()
    
    # Use a set to keep track of seen characters
    seen_chars = set()
    
    for char in string:
        if char.isalpha():  # Check if the character is a letter
            if char in seen_chars:
                return False
            seen_chars.add(char)
    
    return True

# Test cases
print(is_isogram("Dermatoglyphics"))  # Output: True
print(is_isogram("aba"))              # Output: False
print(is_isogram("moOse"))            # Output: False
