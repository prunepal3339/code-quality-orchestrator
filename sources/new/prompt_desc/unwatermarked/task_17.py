def jaden_case(sentence):
    ifcrm = sentence.split(' ')
    result = []

    for i in ifcrm:
        if i != '':
            result.append(i[0].upper() + i[1:])

    return ' '.join(result)

# Test the function
sentence = "how can mirrors be real if our eyes aren't real"
print(jaden_case(sentence))  # Output: "How Can Mirrors Be Real If Our Eyes Aren't Real"
