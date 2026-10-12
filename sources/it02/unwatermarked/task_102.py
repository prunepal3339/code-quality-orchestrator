def snake_to_c Camel(snake_str):
    return ''.join(word.capitalize() for word in snake_str.split('_'))
