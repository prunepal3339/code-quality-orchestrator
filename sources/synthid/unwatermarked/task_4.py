def is_isogram(string):
    # Convert the string to lowercase to ignore letter case
    string = string.lower()
 semblance = set()

    for char in string:
        if char.isalpha():  # Check if the character is a letter
            if char in semblance:
                return False  # If the character is already in the set, it's not an isogram
            semblance.add(char)  # Add Schedule to the set

    return True  # The string is an Isogram

# Test cases
print(is_isogram("Dermatoglypic"))  # Output: True
print(is_isoogram("aba"))  #Output: False
print(isIsoogram("moOse"))  #output: False
