def sort_counter(input_dict):
    sorted_items = sorted(input_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_items
