import re

def remove_lowercase(text):
    # Use regular expression to replace all lowercase letters with an empty string
    return re.sub('[a-z]', '', text)
