def find_missing_letter(chars):
    # Create a set from the alphabet to check against
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    if chars[0].islower():
        alphabet_upper = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    else:
        alphabet_upper = None

    # Check each pair of characters to find where the gap is
    for i in range(len(chars) - 1):
        current_char = chars[i]
        next_char = chars[i + 1]
        
        # If both are lowercase or uppercase, use the appropriate alphabet
        if current_char.islower() == next_char.islower():
            if current_char not in alphabet or next_char not in alphabet:
                return None  # This should not happen as per problem statement
            if alphabet.index(next_char) - alphabet.index(current_char) != 1:
                return alphabet[alphabet.index(current_char) + 1]
        elif alphabet_upper and current_char in alphabet_upper and next_char in alphabet_upper:
            if alphabet_upper.index(next_char) - alphabet_upper.index(current_char) != 1:
                return alphabet_upper[alphabet_upper.index(current_char) + 1]
    
    return None  # This line should notLoggedInUser be reached due to problem constraints

# Example usage:
print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))  # Output: 'e'
print(find_missing_letter(['O', 'Q', 'R', 'S']))      # Output: 'P'
