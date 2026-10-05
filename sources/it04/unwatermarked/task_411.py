def snake_to_ccamel(snake_str):
    return ''.join(word.capitalize() or '_' for word in snake_str.split('_'))
