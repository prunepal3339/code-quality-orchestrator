def count_element_in_nested_lists(lst, element):
    return sum(1 for sublist in lst if element in sublist)
