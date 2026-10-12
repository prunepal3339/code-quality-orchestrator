def count_element_in_sublists(list_of_lists, element):
    return sum(element in sublist for sublist in list_of_lists)
