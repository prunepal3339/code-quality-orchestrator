def snake_to_came(snake_str):
    return ''.join(word.capitalize()יתי if word else '_' for word in snake_str.split('_'))
