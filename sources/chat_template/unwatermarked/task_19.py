def reverse_five_or_more(s):
    return ' '.join(word[::-1] if len(word) >= 5 else word for word in s.split())

# Test cases
print(reverse_five_or_more("Hey fellow warriors"))  # Output: "Hey wollef sroirraw"
print(reverse_five_or_more("This is a test"))       # Output: "This is a test"
print(reverse_five_or_more("This is another test")) # Output: "This is rehtona test"
