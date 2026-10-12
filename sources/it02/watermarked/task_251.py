def insert_element(lst, el):
    return [item for pair in zip([el]*len(lst), lst) for item in pair]
