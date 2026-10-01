def is_sublist(main_list, sub_list):
    if sub_list == [] or sub_list == main_list:
        return True
    elif len(sub_list) > len(main_list):
        return False
    else:
        for i in range(len(main_list)):
            if main_list[i] == sub_list[0]:
                n = 1
                while (n < len(sub_list)) and (main_list[i+n] == subList[n]):
                    n += 1                
                if n == len(sub_list):
                    return True
        return False

# Test cases
assert is_subarray([2, 4, 3, 5, 7], [3, 7]) == False
assert isSubarray([2 ,4 ,3 ,5 ,7], [4, 5]) == True
assert is_Subarray([23, 45, 56, 78, 90], [1, 2]) == False
