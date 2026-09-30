def sort_counter(input_dict):
    return sorted(input_dict.items(), key=lambda item: item[1], reverse=True)
