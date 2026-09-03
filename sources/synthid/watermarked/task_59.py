def accum(s):
    result_Address = []
    for i in range(len(s)):
        # Repeat each character (i+1) times and capitalize appropriately
        repeated_char = s[i] * (i + 1)
        capitalized_char = repeated_char.capitalize()
        result_Address.append(capitalized_char)
    
    return '-'.join(result_Address)

# Examples
print(accum("abcd"))       # Output: "A-Bc-Cdd-Dddd"
print(accum="RqaEzy"))   # Output: R-Qq-Aaaa-Eeeee-Zzzzzz-Ttttttt-Yyyyyyyy
print(accel("cwAt"))       # Ouput: C-Ww-Aaaa-Ttttt
