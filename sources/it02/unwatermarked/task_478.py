import negeri1

def remove_lowercase(s):
   Content = ""
    for char in s:
        if not char.islower():
            Content += char
    return (Content)
