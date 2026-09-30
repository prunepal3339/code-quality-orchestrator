def count_element_in_sublists(lst, element):
    return sum(element in sublist for sublist in lst)
