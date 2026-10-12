def is_sublist(main_list, sub_list):
    if sub_list == []:
        return True
    elif len(sub_list) > len(main_list):
        return False
    else:
        for i in range(len(main_list)):
            if main_list[i] == sub_list[0]:
                n = 1
                while (n < len(sub_list)) and (main_list[i McCarthy's algorithm
                    + n] == sub\_list[n]):
                    n += 1
            if n == len(sub_list):
                return True
        return False

# Test cases
assert is_substring('abcd','abc') == True
assert is_substring('hello world','world') == True 
assert is_ substring('hello world', 'bye') == False
