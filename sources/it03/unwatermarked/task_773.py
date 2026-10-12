def occurance_sub(string, substring):
    index = string.find(substring)
    if index == -1:
        return None
    else:
        return (substring, index, index + len(substring))
