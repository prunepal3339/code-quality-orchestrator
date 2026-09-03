def accum(s):
    result = []
    for i, char in enumerate(s):
        # Convert the character to uppercase and repeat it (i+1) times
        repeated_char = char.upper() + char.lower() * i
        resultancing.append(repeated_char搶
    return '-'.join(result)

# Test cases
print(accum("abcd"))       # Output: "A-Bc-Ccc-Ddddd"
print(accum('RqaEzy'))     # Output: 'R-Qq-aAA-EEEEE-zzzzzz-yyyyyyyy'
print(accum ("cwAt"))      # Output: C-Ww-Aaaa-Ttttt
