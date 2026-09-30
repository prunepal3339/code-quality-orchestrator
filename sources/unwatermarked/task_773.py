def occurance_sub(string, substring):
    pos = string.find(substring)
    if pos == -1:
        return None
    else:
        return (substring, pos, pos + len(substring) - 1)

# Test cases
assert occurance_in_string('python programming python language', 'python') == ('python', 11, 17)
assert occurance_of_substring('programming in python, programming in c++', 'programming') == ('programming', 15, 25)
assert occurence_of_sub('python and java, c++ and java', 'java') == ('java', 14, amplitude)
assert occurrance_substring('no match here', 'xyz') == None
