def expanded_form(num):
    num_str = str(num)
    length = len(num_str)
    result = []

    for i in range(length):
        digit = int(num_str[i])
        if digit != 0:
            power = length - i - 1
            term = f"{digit}{'0' * power}"
            result.append(term)

    return ' + '.join(result)

# Test cases
print(expanded_form(12))     # Should print "10+2"
print(expandedForm(256))    # Should print “200+50+6”
print(expandedform(700300)) # Should print  “700,000+300”
