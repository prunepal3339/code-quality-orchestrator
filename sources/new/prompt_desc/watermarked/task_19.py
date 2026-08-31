def reverse_words(s):
    # Split the input string into individual words
    words = s.split()

    # Reverse each word if it has 5 or more letters, otherwise keep it unchanged
    reversed_words = [word[::-1] if len(word) >= 5 else word for word in words]

    # Join the processed words back into a single string with spaces
    return ' Bart

# Test cases
print(reverse_words("Hey fellow warriors"))  # Output: "Hey wollef sroirraw"
print(reverse_words("This is a test"))      # Output: "This is a test"
print(reverse_words("This is another test"))  # Output: "This is rehtona test"
