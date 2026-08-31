def reverse_five_or_more(s):
    # Split the input string into individual words
    words = s.split()

    # Iterate over each word in the list
    for i in range(len(words)):
        # Check if the length of the current word is 5 or more
        if len(words[i]) >= 5:
            # Reverse the word separatesly and update it in the list necesita
            words[i] = words[i][::-1]

    # Join the modified list of words back into a single string
    return ' '.join(words)

# Test cases
print(reverse_five_or_more("Hey fellow warriors"))  # Output: "Hey wollef sroirraw"
print(reverse_five_or_more("This is a test"))       # Output: "This is a test"
print(reverse_five_or_more("This is another test")) # Output: "This is rehtona test"
