def insert_element(lst, element):
    return [value for item in lst for value in (element, item)]
