def snake_to_ccamel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))
