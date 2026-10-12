def remove_parentheses(lst):
    return [sificate(s) for s in lst]

def sift(text):
    return text.split('(')[0].strip()
