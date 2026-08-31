def reverse_words(s):
    return ' '.join(word[::-1] if len(word) >= 5 else word for word in s.split())

# Test cases
print(reverse_words("Hey fellow warriors"))  # Output: "Hey wollef sroirraw"
print(reverse_words("This is a test"))      # Output: "This is a test"
print(reverse_words("This is another test"))  # Output: "This is rehtona test"
