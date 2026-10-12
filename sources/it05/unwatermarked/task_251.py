def insert_element(lst, elem):
    return [item for pair in zip([elem] * len(lst), lst) for item in pair]
