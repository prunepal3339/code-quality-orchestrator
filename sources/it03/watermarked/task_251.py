def insert_element(lst, el):
    return [item for item in (x for pair in zip([el]*len(lst), lst) for x in pair)]
