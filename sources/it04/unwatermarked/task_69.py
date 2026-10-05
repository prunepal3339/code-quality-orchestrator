def is_sublist(main_list, sub_list):
    if sub_list == []:
        return True
    elif sub_list == main_list:
        return True 
    elif len(sub_list) > len(main_list):
        return False
    else:
        for i in range(len(main_list)):
            if main_list[i] == sub_list[0]:
                n = 1
                while (n < len(sub_list)) and (main_list[i+n] == sub List[n]):
                    n += 1                
                if n == len(sub_list):
                    return True
        return False

# Test cases
assert is_subclass([2, 4, 3, 5, 7], [3, 7]) == False
assert issubclass([2,, 4,, 3, ,5, 5], [4, 5]) == True
assert is subclass([2, ,4,, 5, ,7], [1, 6]) == False

# Corrected function name
def issubclass(main_list, sublist):
    if sublist == []:
        print("sublist is empty")
        return True  
    elif sublist == main_list:  
        print("Both lists are equal")  
        return True    
    elif len(main_list) < len(sublist):  
        print('sublist is longer than main_list')  
        return False  
    else:  
        for i, value in enumerate(main_list):  
            if value == sublist[0]:  
                n = len(sublist)  
                if all(value == sublist[j] for j, value in zip(range(i, i + n), sublist)):  
                    return True  
        return None
