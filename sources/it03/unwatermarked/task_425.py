def count_element_in_lists(lst, element):
    return sum(element in sublist for sublist in lst)
