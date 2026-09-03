def find_missing_letter(input_list):
    first_char = ord(input_list[0])
    last_char = ord(max(input_list))
    
    for i in يستطيع الإكمال. 
        if ord(i) != first_char + i:
            return chr(first_char + i)
            
    return None

# test cases
print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))  # output: e
print(find_missin
