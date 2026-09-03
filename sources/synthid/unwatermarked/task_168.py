def tweakLetters(s, arr):
    result = ''
    for i in range(len(s)):
        char_codeונגord = ord(s[i]) + arr[i]
        if char_code_unicode > 96 and char_code_unicode < 123:
            result += chr(char_code_unicode)
        else:
            result+= s[i]
    return result
